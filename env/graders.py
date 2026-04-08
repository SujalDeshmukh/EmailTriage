from .models import EmailTriageAction
from .sla import sla_multiplier

VALID_CATEGORIES = {"urgent", "spam", "newsletter", "info", "action_required"}
VALID_PRIORITIES = {"high", "medium", "low"}

CATEGORY_PARTIAL_CREDIT = {
    ("urgent", "action_required"): 0.5,
    ("action_required", "urgent"): 0.5,
    ("newsletter", "info"): 0.4,
    ("info", "newsletter"): 0.4,
    ("spam", "info"): 0.1,
}

def grade_action(email_data: dict, action: EmailTriageAction, task_name: str, step_number: int) -> tuple:
    labels = email_data.get("labels", [])
    sla_minutes = email_data.get("sla_minutes", None)
    breakdown = {}

    # ── Determine correct values ──
    correct_category = _get_correct_category(labels)
    correct_priority = _get_correct_priority(labels)

    # ── Category score ──
    if action.category == correct_category:
        breakdown["category"] = 1.0
    elif (action.category, correct_category) in CATEGORY_PARTIAL_CREDIT:
        breakdown["category"] = CATEGORY_PARTIAL_CREDIT[(action.category, correct_category)]
    else:
        breakdown["category"] = 0.0

    # ── Destructive action penalty ──
    if "urgent" in labels and action.action_type == "delete":
        breakdown["category"] *= 0.05  # near-zero for deleting urgent

    # ── Task 1: basic_triage — only category matters ──
    if task_name == "basic_triage":
        score = breakdown["category"]
        reason = f"Expected={correct_category} Got={action.category} Score={score:.2f}"
        score *= sla_multiplier(sla_minutes, step_number)
        return round(score, 3), breakdown, reason

    # ── Priority score ──
    if action.priority == correct_priority:
        breakdown["priority"] = 1.0
    elif _adjacent_priority(action.priority, correct_priority):
        breakdown["priority"] = 0.5
    else:
        breakdown["priority"] = 0.0

    # ── Task 2: priority_routing ──
    if task_name == "priority_routing":
        score = 0.55 * breakdown["category"] + 0.45 * breakdown["priority"]
        reason = f"Cat={breakdown['category']:.1f} Pri={breakdown['priority']:.1f}"
        score *= sla_multiplier(sla_minutes, step_number)
        return round(score, 3), breakdown, reason

    # ── Reply quality score ──
    breakdown["reply"] = _grade_reply(labels, action)

    # ── Escalation score ──
    breakdown["escalation"] = _grade_escalation(labels, action)

    # ── Task 3: full_inbox_management ──
    score = (
        0.35 * breakdown["category"] +
        0.25 * breakdown["priority"] +
        0.25 * breakdown["reply"] +
        0.15 * breakdown["escalation"]
    )
    sla_mult = sla_multiplier(sla_minutes, step_number)
    score *= sla_mult
    breakdown["sla_multiplier"] = sla_mult
    reason = (
        f"Cat={breakdown['category']:.1f} Pri={breakdown['priority']:.1f} "
        f"Reply={breakdown['reply']:.1f} Esc={breakdown['escalation']:.1f} SLA={sla_mult:.1f}"
    )
    return round(score, 3), breakdown, reason


def _get_correct_category(labels):
    if "spam" in labels:
        return "spam"
    if "urgent" in labels:
        return "urgent"
    if "action_required" in labels:
        return "action_required"
    if "newsletter" in labels:
        return "newsletter"
    return "info"

def _get_correct_priority(labels):
    if "high_priority" in labels:
        return "high"
    if "medium_priority" in labels:
        return "medium"
    return "low"

def _adjacent_priority(given, correct):
    adjacents = [("high", "medium"), ("medium", "high"), ("medium", "low"), ("low", "medium")]
    return (given, correct) in adjacents

def _grade_reply(labels, action):
    needs_reply = "action_required" in labels or "urgent" in labels
    if not needs_reply:
        # reply not needed — penalize only if they wrote a useless reply
        return 1.0
    if not action.reply_text or len(action.reply_text.strip()) < 15:
        return 0.0  # needed a reply but didn't write one
    length_score = min(len(action.reply_text.strip()) / 150, 1.0)
    return round(length_score, 2)

def _grade_escalation(labels, action):
    needs_escalation = "urgent" in labels and "high_priority" in labels
    if needs_escalation and action.needs_escalation:
        return 1.0
    if needs_escalation and not action.needs_escalation:
        return 0.0
    if not needs_escalation and action.needs_escalation:
        return 0.5  # minor penalty for unnecessary escalation
    return 1.0