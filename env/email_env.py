from .models import *
from .graders import grade_action
from .data.emails import EMAILS
from .data.threads import THREADS
from .data.bilingual import BILINGUAL_EMAILS

TASK_EMAIL_IDS = {
    "basic_triage": [
        "e001", "e006", "e009", "e003", "e023",    # very clear: urgent, spam, newsletter, action, info
    ],
    "priority_routing": [
        "e001", "e002", "e005", "e006", "e009",
        "e013", "e016", "e018", "e024", "e032",     # mixed, priorities matter
    ],
    "full_inbox_management": None  # uses ALL emails + threads + bilingual
}

class EmailTriageEnv:
    def __init__(self, task_name: str = "basic_triage"):
        self.task_name = task_name
        self.items = []       # list of raw dicts (emails, threads, bilingual)
        self.current_index = 0
        self.history = []
        self.done = False
        self.sla_breaches = 0

    def reset(self) -> EmailTriageObservation:
        self.items = self._load_items()
        self.current_index = 0
        self.history = []
        self.done = False
        self.sla_breaches = 0
        return self._make_observation()

    def step(self, action: EmailTriageAction):
        if self.done:
            raise ValueError("Episode done. Call reset() first.")

        item = self.items[self.current_index]
        reward_value, breakdown, reason = grade_action(
            item, action, self.task_name, self.current_index
        )

        if breakdown.get("sla_multiplier", 1.0) < 1.0:
            self.sla_breaches += 1

        self.history.append({
            "item_id": item.get("id") or item.get("thread_id"),
            "action": action.dict(),
            "reward": reward_value,
            "reason": reason
        })

        self.current_index += 1
        self.done = self.current_index >= len(self.items)
        obs = self._make_observation(previous_result=reason)
        reward = EmailTriageReward(value=reward_value, breakdown=breakdown, reason=reason)
        return obs, reward, self.done, {"history": self.history}

    def state(self) -> EmailTriageState:
        correct = sum(1 for h in self.history if h["reward"] >= 0.7)
        score = sum(h["reward"] for h in self.history) / max(len(self.history), 1)
        return EmailTriageState(
            task_name=self.task_name,
            emails_processed=self.current_index,
            total_emails=len(self.items),
            correct_actions=correct,
            score_so_far=round(score, 3),
            sla_breaches=self.sla_breaches,
            done=self.done
        )

    def _make_observation(self, previous_result=None) -> EmailTriageObservation:
        if self.done:
            item = self.items[-1]
        else:
            item = self.items[self.current_index]

        is_thread = "thread_id" in item
        is_bilingual = item.get("id", "").startswith("b")

        if is_thread:
            messages = item["messages"]
            latest = messages[-1]
            thread_context = [
                {"from": m["from"], "timestamp": m["timestamp"], "body": m["body"]}
                for m in messages[:-1]
            ]
            return EmailTriageObservation(
                email_id=item["thread_id"],
                sender=latest["from"],
                subject=item["subject"],
                body=latest["body"],
                thread_context=thread_context,
                inbox_remaining=len(self.items) - self.current_index,
                step_number=self.current_index,
                previous_action_result=previous_result,
                is_thread=True,
                is_bilingual=False
            )

        return EmailTriageObservation(
            email_id=item["id"],
            sender=item["sender"],
            subject=item["subject"],
            body=item["body"],
            thread_context=None,
            inbox_remaining=len(self.items) - self.current_index,
            step_number=self.current_index,
            previous_action_result=previous_result,
            is_thread=False,
            is_bilingual=is_bilingual
        )

    def _load_items(self):
        email_map = {e["id"]: e for e in EMAILS}

        if self.task_name == "basic_triage":
            ids = TASK_EMAIL_IDS["basic_triage"]
            return [email_map[i] for i in ids]

        elif self.task_name == "priority_routing":
            ids = TASK_EMAIL_IDS["priority_routing"]
            return [email_map[i] for i in ids]

        else:  # full_inbox_management
            all_items = list(EMAILS) + list(THREADS) + list(BILINGUAL_EMAILS)
            return all_items