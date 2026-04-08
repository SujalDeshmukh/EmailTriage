from pydantic import BaseModel
from typing import Optional, List, Dict

class Email(BaseModel):
    id: str
    sender: str
    subject: str
    body: str
    timestamp: str
    sla_minutes: Optional[int] = None
    labels: List[str] = []

class ThreadMessage(BaseModel):
    sender: str
    timestamp: str
    body: str

class EmailThread(BaseModel):
    thread_id: str
    subject: str
    labels: List[str]
    sla_minutes: Optional[int]
    messages: List[ThreadMessage]

class EmailTriageObservation(BaseModel):
    email_id: str
    sender: str
    subject: str
    body: str
    thread_context: Optional[List[Dict]] = None  # prior messages if thread
    inbox_remaining: int
    step_number: int
    previous_action_result: Optional[str] = None
    is_thread: bool = False
    is_bilingual: bool = False

class EmailTriageAction(BaseModel):
    action_type: str        # categorize, reply, escalate, archive, delete, flag
    category: Optional[str] = None     # urgent, spam, newsletter, info, action_required
    priority: Optional[str] = None     # high, medium, low
    reply_text: Optional[str] = None
    needs_escalation: Optional[bool] = False

class EmailTriageReward(BaseModel):
    value: float
    breakdown: Dict[str, float]
    reason: str

class EmailTriageState(BaseModel):
    task_name: str
    emails_processed: int
    total_emails: int
    correct_actions: int
    score_so_far: float
    sla_breaches: int
    done: bool