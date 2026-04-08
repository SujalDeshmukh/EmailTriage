from .models import EmailTriageAction
from .sla import sla_multiplier

# Constants for scoring
VALID_CATEGORIES = {"urgent", "spam", "newsletter", "info", "action_required"}
VALID_PRIORITIES = {"high", "medium", "low"}

# Partial credit for "close" misclassifications
CATEGORY_PARTIAL_CREDIT = {
    ("urgent", "action_required"): 0.6,
    ("action_required", "urgent"): 0.6,
    ("newsletter", "info"): 0.4,
    ("info", "newsletter"): 0.4,
    ("spam", "info"): 0.1,
}

def grade_action(email_data: dict, action: EmailTriageAction, task_name: str, step_number: int) -> tuple:
    labels = email_data.get("labels", [])
    sla_minutes = email_data.get("sla_minutes", None)
    breakdown = {}

    # 1. Determine ground truth from data
    correct_category = _get_correct_category(labels)
    correct_priority = _get_correct_priority(labels)

    # 2. Category Scoring (Logic Consistency)
    if action.category == correct_category:
        cat_score = 0.99  # Nudged from 1.0
    else:
        cat_score = CATEGORY_PARTIAL_CREDIT.get((action.category, correct_category), 0.01)
    
    # Penalty: If user labels as SPAM but tries to REPLY
    if action.category == "spam" and action.action_type == "reply":
        cat_score *= 0.2

    breakdown["category"] = cat_score

    # 3. Priority Scoring
    if action.priority == correct_priority:
        breakdown["priority"] = 0.99  # Nudged from 1.0
    elif _adjacent_priority(action.priority, correct_priority):
        breakdown["priority"] = 0.5
    else:
        breakdown["priority"] = 0.01

    # 4. Reply Quality
    breakdown["reply"] = _grade_reply_sophisticated(labels, action)

    # 5. Escalation Management
    breakdown["escalation"] = _grade_escalation(labels, action)

    # 6. Task-Specific Weighting
    if task_name == "basic_triage":
        score = breakdown["category"]
    elif task_name == "priority_routing":
        score = (0.5 * breakdown["category"]) + (0.5 * breakdown["priority"])
    else:  # full_inbox_management
        score = (
            0.30 * breakdown["category"] +
            0.20 * breakdown["priority"] +
            0.35 * breakdown["reply"] +
            0.15 * breakdown["escalation"]
        )

    # 7. Apply SLA Decay
    sla_mult = sla_multiplier(sla_minutes, step_number)
    score *= sla_mult
    breakdown["sla_multiplier"] = sla_mult

    # 8. Destructive Action Guardrail
    if "urgent" in labels and action.action_type in ["delete", "archive"] and cat_score < 0.99:
        score *= 0.1 

    reason = (
        f"Cat:{breakdown['category']:.2f} | Pri:{breakdown['priority']:.1f} | "
        f"Reply:{breakdown['reply']:.2f} | SLA:{sla_mult:.2f}"
    )
    
    # Final Clamp strictly between 0.001 and 0.999
    final_score = round(min(max(score, 0.001), 0.999), 3)
    
    return final_score, breakdown, reason


def _get_correct_category(labels):
    if "spam" in labels: return "spam"
    if "urgent" in labels: return "urgent"
    if "action_required" in labels: return "action_required"
    if "newsletter" in labels: return "newsletter"
    return "info"


def _get_correct_priority(labels):
    if "high_priority" in labels: return "high"
    if "medium_priority" in labels: return "medium"
    return "low"


def _adjacent_priority(given, correct):
    adj = [("high", "medium"), ("medium", "high"), ("medium", "low"), ("low", "medium")]
    return (given, correct) in adj


def _grade_reply_sophisticated(labels, action):
    needs_reply = any(l in labels for l in ["action_required", "urgent"])
    
    if not needs_reply:
        return 0.99 if not action.reply_text else 0.5

    if not action.reply_text or len(action.reply_text.strip()) < 10:
        return 0.01

    text = action.reply_text.lower()
    professional_tokens = ["sincerely", "thanks", "regards", "best", "confirm", "meeting", "scheduled"]
    token_hits = sum(1 for t in professional_tokens if t in text)
    
    length_bonus = min(len(text) / 200, 1.0)
    tone_score = min(token_hits / 2, 1.0)
    
    reply_val = (0.4 * length_bonus) + (0.6 * tone_score)
    return round(min(max(reply_val, 0.01), 0.99), 2)


def _grade_escalation(labels, action):
    should_escalate = "urgent" in labels and "high_priority" in labels
    
    if should_escalate:
        # Nudged boundaries
        return 0.99 if action.needs_escalation else 0.01
    else:
        # Nudged boundaries
        return 0.7 if action.needs_escalation else 0.99
