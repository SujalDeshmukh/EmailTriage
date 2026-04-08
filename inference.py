import os
import json
from openai import OpenAI
from env.email_env import EmailTriageEnv
from env.models import EmailTriageAction

# Mandatory Variables - The validator injects API_BASE_URL and API_KEY
# We prioritize these, then fall back to your local environment names
FINAL_BASE_URL = os.environ.get("API_BASE_URL", "https://router.huggingface.co/v1")
FINAL_API_KEY = os.environ.get("API_KEY") or os.environ.get("HF_TOKEN") or os.environ.get("OPENAI_API_KEY")
MODEL_NAME = os.environ.get("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")

# Verification: Ensure we actually have a key before initializing
if not FINAL_API_KEY:
    raise ValueError("No API Key found. Please set API_KEY or HF_TOKEN environment variable.")

client = OpenAI(base_url=FINAL_BASE_URL, api_key=FINAL_API_KEY)

# Rest of your code (SYSTEM_PROMPT, get_llm_action, etc.) follows...

SYSTEM_PROMPT = """You are an expert email triage assistant for a corporate workplace inbox.

Given an email (and thread history if available), respond with ONLY a valid JSON object — no explanation, no markdown, no extra text.

JSON format:
{
  "action_type": "categorize | reply | escalate | archive | delete | flag",
  "category": "urgent | spam | newsletter | info | action_required",
  "priority": "high | medium | low",
  "reply_text": "your reply here if action_required or urgent, else null",
  "needs_escalation": true or false
}

Rules:
- urgent = production issues, legal threats, security breaches, payment fraud, angry enterprise customers
- action_required = needs a response or decision but not emergency (leave requests, invoice approvals, meeting requests)
- spam = promotional, phishing, prize scams, crypto schemes, fake job offers
- newsletter = digest emails, product updates, weekly roundups
- info = FYI emails, notifications, resolved incidents, welcome emails
- high priority = SLA < 2 hours or serious business impact
- medium priority = needs response within 24-48 hours
- low priority = no time pressure
- needs_escalation = true ONLY for urgent + high_priority emails
- reply_text = write a professional reply ONLY for urgent or action_required, else null
- For Hindi+English emails: understand both languages and triage correctly"""


def get_llm_action(obs) -> EmailTriageAction:
    """Call the LLM to decide action for current email."""

    # Build context string
    thread_str = ""
    if obs.thread_context:
        thread_str = "\n\nTHREAD HISTORY (oldest first):\n"
        for msg in obs.thread_context:
            thread_str += f"From: {msg.get('from', msg.get('sender',''))}\n"
            thread_str += f"Message: {msg.get('body', '')}\n---\n"

    bilingual_note = ""
    if obs.is_bilingual:
        bilingual_note = "\n[Note: This email contains Hindi+English mixed language content]"

    user_prompt = f"""Triage this email:

From: {obs.sender}
Subject: {obs.subject}
Body: {obs.body}{thread_str}{bilingual_note}

Inbox remaining: {obs.inbox_remaining}
Step: {obs.step_number}

Respond with ONLY the JSON object."""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=300,
            temperature=0.1,  # low temp for consistent triage decisions
        )
        raw = response.choices[0].message.content.strip()

        # Clean up if model wraps in markdown
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        raw = raw.strip()

        data = json.loads(raw)

        return EmailTriageAction(
            action_type=data.get("action_type", "categorize"),
            category=data.get("category", "info"),
            priority=data.get("priority", "low"),
            reply_text=data.get("reply_text", None),
            needs_escalation=bool(data.get("needs_escalation", False))
        )

    except Exception as e:
        # Fallback if LLM fails or returns bad JSON
        print(f"[DEBUG] LLM error: {e}", flush=True)
        return EmailTriageAction(
            action_type="categorize",
            category="info",
            priority="low",
            reply_text=None,
            needs_escalation=False
        )


def run_task(task_name: str, max_steps: int) -> float:
    """Run one full task episode and return final score."""

    env = EmailTriageEnv(task_name=task_name)
    obs = env.reset()

    rewards = []
    steps_taken = 0
    done = False

    print(f"[START] task={task_name} env=email-triage model={MODEL_NAME}", flush=True)

    for step in range(1, max_steps + 1):
        if done:
            break

        # LLM decides the action
        action = get_llm_action(obs)

        # Step the environment
        obs, reward_obj, done, info = env.step(action)
        current_reward = float(reward_obj.value)
        rewards.append(current_reward)
        steps_taken = step

        print(
            f"[STEP] step={step} action={action.action_type} "
            f"reward={current_reward:.2f} done={str(done).lower()} error=null",
            flush=True
        )

    score = sum(rewards) / len(rewards) if rewards else 0.0
    score = round(min(max(score, 0.0), 1.0), 3)
    success = score >= 0.5
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    print(
        f"[END] success={str(success).lower()} steps={steps_taken} "
        f"score={score:.3f} rewards={rewards_str}",
        flush=True
    )

    return score


if __name__ == "__main__":
    # Run all 3 tasks as required by the spec
    results = {}

    results["basic_triage"] = run_task("basic_triage", max_steps=5)
    results["priority_routing"] = run_task("priority_routing", max_steps=10)
    results["full_inbox_management"] = run_task("full_inbox_management", max_steps=90)

    print("\n[SUMMARY]", flush=True)
    for task, score in results.items():
        print(f"  {task}: {score:.3f}", flush=True)
