# env/data/threads.py
# Each thread is a chain of 2–4 emails on the same topic
# Agent sees the full thread and must triage the LATEST email in context

THREADS = [

    {
        "thread_id": "t001",
        "subject": "Re: Production API outage — status update",
        "labels": ["urgent", "action_required", "high_priority"],
        "sla_minutes": 15,
        "messages": [
            {
                "from": "monitoring@company.com",
                "timestamp": "2024-01-15T03:00:00",
                "body": "ALERT: API error rate crossed 50% threshold. Auto-paging on-call team."
            },
            {
                "from": "oncall@company.com",
                "timestamp": "2024-01-15T03:05:00",
                "body": "Acknowledged. Investigating. Looks like a bad deployment — rolling back now."
            },
            {
                "from": "cto@company.com",
                "timestamp": "2024-01-15T03:12:00",
                "body": (
                    "Rollback failed. Error persists. I need the DB team and networking team "
                    "on a call right now. This has been 12 minutes — customers are tweeting about it."
                )
            }
        ]
    },
    {
        "thread_id": "t002",
        "subject": "Re: Q1 roadmap alignment — follow up",
        "labels": ["action_required", "medium_priority", "meeting"],
        "sla_minutes": 1440,
        "messages": [
            {
                "from": "sarah.jones@partner.org",
                "timestamp": "2024-01-10T09:00:00",
                "body": "Hi, wanted to connect on Q1 roadmap. Are you free this week?"
            },
            {
                "from": "you@company.com",
                "timestamp": "2024-01-11T10:00:00",
                "body": "Hi Sarah, yes happy to connect. I'm free Thursday after 2 PM."
            },
            {
                "from": "sarah.jones@partner.org",
                "timestamp": "2024-01-15T09:00:00",
                "body": (
                    "Great! Thursday 2 PM works. Should I send the invite or will you? "
                    "Also, can you share the draft roadmap doc before the call so I can prep?"
                )
            }
        ]
    },
    {
        "thread_id": "t003",
        "subject": "Re: Invoice #4521 — approval status",
        "labels": ["action_required", "medium_priority", "finance"],
        "sla_minutes": 2880,
        "messages": [
            {
                "from": "finance@company.com",
                "timestamp": "2024-01-12T10:00:00",
                "body": "Invoice #4521 from TechSupplies Ltd for ₹1,85,000 needs your approval."
            },
            {
                "from": "you@company.com",
                "timestamp": "2024-01-13T11:00:00",
                "body": "I need the PO number attached before I can approve. Can you add it?"
            },
            {
                "from": "finance@company.com",
                "timestamp": "2024-01-15T09:00:00",
                "body": (
                    "PO number added: PO-2024-0089. Please approve now — "
                    "vendor is following up and we risk late payment charges."
                )
            }
        ]
    },
    {
        "thread_id": "t004",
        "subject": "Re: Data breach investigation update",
        "labels": ["urgent", "action_required", "high_priority", "security"],
        "sla_minutes": 30,
        "messages": [
            {
                "from": "security@company.com",
                "timestamp": "2024-01-15T02:00:00",
                "body": "Potential breach detected in S3 bucket. Isolating now. CISO looped in."
            },
            {
                "from": "ciso@company.com",
                "timestamp": "2024-01-15T02:15:00",
                "body": "Confirmed unauthorized access. Legal team must be briefed immediately."
            },
            {
                "from": "legal@company.com",
                "timestamp": "2024-01-15T02:30:00",
                "body": (
                    "Legal briefed. Under DPDP Act, we have 72 hours to notify affected users "
                    "if PII was compromised. Need confirmation from security team: was PII accessed?"
                )
            }
        ]
    },
    {
        "thread_id": "t005",
        "subject": "Re: Salary not received — escalation",
        "labels": ["urgent", "action_required", "high_priority", "hr", "finance"],
        "sla_minutes": 120,
        "messages": [
            {
                "from": "employee.raj@company.com",
                "timestamp": "2024-01-05T10:00:00",
                "body": "Hi HR, my salary for December hasn't been credited yet. Please check."
            },
            {
                "from": "hr@company.com",
                "timestamp": "2024-01-06T09:00:00",
                "body": "Checking with finance. Will revert by EOD."
            },
            {
                "from": "employee.raj@company.com",
                "timestamp": "2024-01-10T10:00:00",
                "body": "It's been 4 more days. Still no update. This is very stressful."
            },
            {
                "from": "employee.raj@company.com",
                "timestamp": "2024-01-15T09:00:00",
                "body": (
                    "It has now been 15 days since I raised this. No salary, no resolution. "
                    "I am escalating to the CEO and filing a complaint with the Labour Commissioner "
                    "if this is not resolved by today."
                )
            }
        ]
    },
    {
        "thread_id": "t006",
        "subject": "Re: Refund request for order #ORD-8821",
        "labels": ["action_required", "medium_priority"],
        "sla_minutes": 1440,
        "messages": [
            {
                "from": "customer.priya@gmail.com",
                "timestamp": "2024-01-10T14:00:00",
                "body": "Hi, I received a damaged product in order #ORD-8821. I want a refund."
            },
            {
                "from": "support@company.com",
                "timestamp": "2024-01-11T10:00:00",
                "body": "Sorry to hear that! Please share a photo of the damage and we'll process it."
            },
            {
                "from": "customer.priya@gmail.com",
                "timestamp": "2024-01-15T11:00:00",
                "body": (
                    "Photos sent 3 days ago. No update. "
                    "How long does a refund take? Please resolve this today."
                )
            }
        ]
    },
    {
        "thread_id": "t007",
        "subject": "Re: Performance improvement plan — check-in",
        "labels": ["action_required", "high_priority", "hr"],
        "sla_minutes": 480,
        "messages": [
            {
                "from": "hr@company.com",
                "timestamp": "2024-01-08T10:00:00",
                "body": "Sharing the PIP document for Amit Kumar (SDE-2). Manager review needed."
            },
            {
                "from": "manager.vikram@company.com",
                "timestamp": "2024-01-10T11:00:00",
                "body": "Reviewed. I've added my comments. Please schedule the meeting with Amit."
            },
            {
                "from": "hr@company.com",
                "timestamp": "2024-01-15T09:00:00",
                "body": (
                    "Meeting is scheduled for Jan 17 at 3 PM. "
                    "Please confirm you and the manager are available "
                    "and review the final PIP document before then."
                )
            }
        ]
    },
    {
        "thread_id": "t008",
        "subject": "Re: AWS cost spike — investigation",
        "labels": ["action_required", "medium_priority", "finance", "it_support"],
        "sla_minutes": 1440,
        "messages": [
            {
                "from": "finance@company.com",
                "timestamp": "2024-01-12T10:00:00",
                "body": "AWS bill this month is ₹2.4 lakhs vs ₹80k last month. What happened?"
            },
            {
                "from": "devops@company.com",
                "timestamp": "2024-01-13T11:00:00",
                "body": "Investigating. Initial look: someone left 12 large EC2 instances running."
            },
            {
                "from": "finance@company.com",
                "timestamp": "2024-01-15T10:00:00",
                "body": (
                    "Those instances have been terminated. Bill is now projected at ₹95k. "
                    "Please prepare a cost analysis report for the CFO by Thursday."
                )
            }
        ]
    },
    {
        "thread_id": "t009",
        "subject": "Re: Vendor contract renewal — final terms",
        "labels": ["action_required", "medium_priority", "legal", "finance"],
        "sla_minutes": 2880,
        "messages": [
            {
                "from": "vendor@saassupplier.com",
                "timestamp": "2024-01-10T10:00:00",
                "body": "Sending revised contract for 2024. Key change: 15% price increase."
            },
            {
                "from": "procurement@company.com",
                "timestamp": "2024-01-12T11:00:00",
                "body": "We can accept 8% max. Sent counter-proposal."
            },
            {
                "from": "vendor@saassupplier.com",
                "timestamp": "2024-01-15T09:00:00",
                "body": (
                    "We can meet at 10%. Final offer. "
                    "Contract must be signed by Jan 20 or current pricing expires "
                    "and new rates take effect immediately."
                )
            }
        ]
    },
    {
        "thread_id": "t010",
        "subject": "Re: Server migration — go/no-go decision",
        "labels": ["action_required", "high_priority", "it_support"],
        "sla_minutes": 240,
        "messages": [
            {
                "from": "devops@company.com",
                "timestamp": "2024-01-14T15:00:00",
                "body": "Migration to new data center is planned for tonight 11 PM. Team is ready."
            },
            {
                "from": "cto@company.com",
                "timestamp": "2024-01-14T16:00:00",
                "body": "Hold — I need a rollback plan documented before we proceed."
            },
            {
                "from": "devops@company.com",
                "timestamp": "2024-01-15T09:00:00",
                "body": (
                    "Rollback plan is documented and shared in Confluence. "
                    "Migration window is tonight. Need go/no-go decision by 3 PM today."
                )
            }
        ]
    },

    # ── 5 more shorter/simpler threads for easy task ──

    {
        "thread_id": "t011",
        "subject": "Re: Team lunch on Friday",
        "labels": ["info", "low_priority"],
        "sla_minutes": None,
        "messages": [
            {
                "from": "manager@company.com",
                "timestamp": "2024-01-13T12:00:00",
                "body": "Hey team, planning a lunch this Friday at 1 PM. Barbeque Nation, Gomtinagar. Interested?"
            },
            {
                "from": "you@company.com",
                "timestamp": "2024-01-14T10:00:00",
                "body": "Count me in!"
            },
            {
                "from": "manager@company.com",
                "timestamp": "2024-01-15T10:00:00",
                "body": "Great! 8 confirmed so far. Booking for 10. See you Friday!"
            }
        ]
    },
    {
        "thread_id": "t012",
        "subject": "Re: Leave approval request",
        "labels": ["action_required", "medium_priority", "hr"],
        "sla_minutes": 1440,
        "messages": [
            {
                "from": "employee.neha@company.com",
                "timestamp": "2024-01-14T11:00:00",
                "body": "Hi, requesting 3 days leave Jan 22–24 for family function. Please approve."
            },
            {
                "from": "you@company.com",
                "timestamp": "2024-01-15T10:00:00",
                "body": "Hi Neha, let me check the sprint calendar before approving."
            },
            {
                "from": "employee.neha@company.com",
                "timestamp": "2024-01-15T14:00:00",
                "body": "Sure, please let me know today if possible so I can book travel. Thanks!"
            }
        ]
    },
    {
        "thread_id": "t013",
        "subject": "Re: Blog post review request",
        "labels": ["action_required", "low_priority"],
        "sla_minutes": 2880,
        "messages": [
            {
                "from": "marketing@company.com",
                "timestamp": "2024-01-13T10:00:00",
                "body": "Hi, can you review our technical blog post before we publish? Link: docs.google.com/..."
            },
            {
                "from": "you@company.com",
                "timestamp": "2024-01-14T11:00:00",
                "body": "Sure, I'll look at it today."
            },
            {
                "from": "marketing@company.com",
                "timestamp": "2024-01-15T10:00:00",
                "body": "Hi, just following up — we want to publish by Thursday. Any feedback yet?"
            }
        ]
    },
    {
        "thread_id": "t014",
        "subject": "Re: Expense reimbursement — ₹12,500",
        "labels": ["action_required", "medium_priority", "finance"],
        "sla_minutes": 2880,
        "messages": [
            {
                "from": "employee.arjun@company.com",
                "timestamp": "2024-01-10T10:00:00",
                "body": "Submitted expense report for client dinner + travel: ₹12,500. Receipts attached."
            },
            {
                "from": "finance@company.com",
                "timestamp": "2024-01-12T11:00:00",
                "body": "Approved by finance. Waiting for manager sign-off before processing."
            },
            {
                "from": "finance@company.com",
                "timestamp": "2024-01-15T10:00:00",
                "body": "Manager sign-off still pending. Please approve in the expense portal ASAP."
            }
        ]
    },
    {
        "thread_id": "t015",
        "subject": "Re: Laptop not working — IT support ticket #IT-4421",
        "labels": ["action_required", "medium_priority", "it_support"],
        "sla_minutes": 480,
        "messages": [
            {
                "from": "employee.sunita@company.com",
                "timestamp": "2024-01-14T09:00:00",
                "body": "My laptop won't turn on since this morning. Have a presentation at 2 PM today."
            },
            {
                "from": "it@company.com",
                "timestamp": "2024-01-14T10:00:00",
                "body": "Ticket raised. Tech will visit your desk within 2 hours."
            },
            {
                "from": "employee.sunita@company.com",
                "timestamp": "2024-01-15T09:00:00",
                "body": (
                    "Issue still not resolved. I used a colleague's laptop for the presentation. "
                    "But I still need my laptop fixed today — all my work files are on it."
                )
            }
        ]
    },

    # ── 10 more threads for hard task ──
    {
        "thread_id": "t016",
        "subject": "Re: Whistleblower complaint — confidential",
        "labels": ["urgent", "action_required", "high_priority", "legal", "hr"],
        "sla_minutes": 240,
        "messages": [
            {
                "from": "anonymous@protonmail.com",
                "timestamp": "2024-01-14T22:00:00",
                "body": (
                    "I am reporting financial misconduct by a senior manager. "
                    "Expenses are being inflated and approved by a related party. "
                    "I fear retaliation. Please keep this confidential."
                )
            },
            {
                "from": "hr@company.com",
                "timestamp": "2024-01-15T08:00:00",
                "body": "Acknowledged. We take this seriously. Looping in Legal and Compliance."
            },
            {
                "from": "legal@company.com",
                "timestamp": "2024-01-15T09:00:00",
                "body": (
                    "This triggers our POSH/Whistleblower policy. "
                    "An internal investigation committee must be constituted within 24 hours. "
                    "All communications on this must be privileged. "
                    "Please confirm who will lead the investigation."
                )
            }
        ]
    },
    {
        "thread_id": "t017",
        "subject": "Re: Key employee resignation — notice period negotiation",
        "labels": ["urgent", "action_required", "high_priority", "hr"],
        "sla_minutes": 480,
        "messages": [
            {
                "from": "lead.dev@company.com",
                "timestamp": "2024-01-13T11:00:00",
                "body": "I am resigning from my position. My notice period is 3 months per contract."
            },
            {
                "from": "hr@company.com",
                "timestamp": "2024-01-14T10:00:00",
                "body": "Received. Can we schedule a retention conversation before accepting the resignation?"
            },
            {
                "from": "lead.dev@company.com",
                "timestamp": "2024-01-15T09:00:00",
                "body": (
                    "I've already accepted an offer elsewhere. I'm willing to serve 6 weeks instead of 12 "
                    "for a smoother transition. Please revert with a decision today — "
                    "my new employer needs a joining date."
                )
            }
        ]
    },
    {
        "thread_id": "t018",
        "subject": "Re: Press inquiry — response needed before 4 PM",
        "labels": ["urgent", "action_required", "high_priority"],
        "sla_minutes": 180,
        "messages": [
            {
                "from": "journalist@techcrunch.com",
                "timestamp": "2024-01-15T10:00:00",
                "body": (
                    "Hi, I'm writing a piece on the recent outage affecting your customers. "
                    "Can you provide a statement by 4 PM today? "
                    "We'll be publishing with or without your comment."
                )
            },
            {
                "from": "pr@company.com",
                "timestamp": "2024-01-15T10:30:00",
                "body": "Forwarding to CEO and Communications team. We need an approved statement ASAP."
            },
            {
                "from": "ceo@company.com",
                "timestamp": "2024-01-15T11:00:00",
                "body": (
                    "Draft statement ready. Needs legal review before sending. "
                    "Legal team please review and approve by 2 PM — "
                    "PR needs 1 hour to coordinate the response."
                )
            }
        ]
    },
    {
        "thread_id": "t019",
        "subject": "Re: Acquisition offer — NDA and initial discussion",
        "labels": ["urgent", "action_required", "high_priority", "legal"],
        "sla_minutes": 1440,
        "messages": [
            {
                "from": "bd@bigcorp.com",
                "timestamp": "2024-01-13T14:00:00",
                "body": "We are interested in exploring an acquisition of your company. Would you be open to a call?"
            },
            {
                "from": "ceo@company.com",
                "timestamp": "2024-01-14T10:00:00",
                "body": "Open to a conversation. Please send an NDA and we can schedule a call."
            },
            {
                "from": "legal@bigcorp.com",
                "timestamp": "2024-01-15T09:00:00",
                "body": (
                    "NDA attached. Please have your legal team review and sign. "
                    "Our CEO is available for a call this Friday or next Monday. "
                    "This is time-sensitive — we are in conversations with two other targets."
                )
            }
        ]
    },
    {
        "thread_id": "t020",
        "subject": "Re: Workplace harassment complaint",
        "labels": ["urgent", "action_required", "high_priority", "hr", "legal"],
        "sla_minutes": 240,
        "messages": [
            {
                "from": "employee.meera@company.com",
                "timestamp": "2024-01-14T18:00:00",
                "body": (
                    "I am filing a formal complaint against my team lead for creating a hostile work environment. "
                    "Incidents on Jan 8, Jan 10, and Jan 14 are documented. I can share details."
                )
            },
            {
                "from": "hr@company.com",
                "timestamp": "2024-01-15T08:00:00",
                "body": "We take this seriously. POSH committee has been notified. Will contact you today."
            },
            {
                "from": "posh@company.com",
                "timestamp": "2024-01-15T09:30:00",
                "body": (
                    "POSH committee convened. Formal inquiry initiated per Sexual Harassment Act 2013. "
                    "The respondent (team lead) must be temporarily separated from the complainant's team "
                    "pending investigation. HR and manager approval needed immediately."
                )
            }
        ]
    },
    {
        "thread_id": "t021",
        "subject": "Re: Customer churn risk — enterprise account",
        "labels": ["urgent", "action_required", "high_priority"],
        "sla_minutes": 240,
        "messages": [
            {
                "from": "csm@company.com",
                "timestamp": "2024-01-14T15:00:00",
                "body": "RetailCorp (₹60L ARR) has flagged dissatisfaction in their QBR. High churn risk."
            },
            {
                "from": "vp.sales@company.com",
                "timestamp": "2024-01-14T16:00:00",
                "body": "What are their main complaints? Can we get on a call with their CTO this week?"
            },
            {
                "from": "csm@company.com",
                "timestamp": "2024-01-15T09:00:00",
                "body": (
                    "Main issues: API reliability and lack of enterprise SSO (they've asked 3 times). "
                    "Their contract renewal is February 1. "
                    "CTO is available Jan 17 or Jan 18. "
                    "We need to bring an engineering lead and a concrete SSO timeline to the call."
                )
            }
        ]
    },
    {
        "thread_id": "t022",
        "subject": "Re: Tax audit notice from Income Tax Department",
        "labels": ["urgent", "action_required", "high_priority", "legal", "finance", "compliance"],
        "sla_minutes": 2880,
        "messages": [
            {
                "from": "accounts@company.com",
                "timestamp": "2024-01-12T11:00:00",
                "body": "Received a scrutiny notice from Income Tax Dept for FY 2021-22. Documents needed."
            },
            {
                "from": "ca@taxfirm.com",
                "timestamp": "2024-01-13T10:00:00",
                "body": "Reviewed the notice. We need P&L, balance sheet, bank statements, and TDS returns."
            },
            {
                "from": "accounts@company.com",
                "timestamp": "2024-01-15T09:00:00",
                "body": (
                    "All documents ready except TDS returns for Q3 FY22 — these are missing. "
                    "The deadline to respond to IT Dept is January 20. "
                    "CA needs TDS returns by Jan 17 to prepare the response. "
                    "Please check if the payroll team has these."
                )
            }
        ]
    },
    {
        "thread_id": "t023",
        "subject": "Re: Office lease renewal — landlord negotiation",
        "labels": ["action_required", "medium_priority", "finance", "legal"],
        "sla_minutes": 4320,
        "messages": [
            {
                "from": "landlord@realestate.in",
                "timestamp": "2024-01-10T11:00:00",
                "body": "Your 3-year lease expires March 31. We propose renewal at 20% rent increase."
            },
            {
                "from": "admin@company.com",
                "timestamp": "2024-01-12T10:00:00",
                "body": "20% is too high. We can offer 8%. Would you consider a 5-year lock-in for a better rate?"
            },
            {
                "from": "landlord@realestate.in",
                "timestamp": "2024-01-15T10:00:00",
                "body": (
                    "We can do 12% for a 5-year lease, with no increase for first 2 years. "
                    "If not renewed by Feb 1, we'll need to show the property to other tenants."
                )
            }
        ]
    },
    {
        "thread_id": "t024",
        "subject": "Re: New joiner background verification failed",
        "labels": ["urgent", "action_required", "high_priority", "hr", "legal"],
        "sla_minutes": 480,
        "messages": [
            {
                "from": "bgv@verifyfast.com",
                "timestamp": "2024-01-14T16:00:00",
                "body": "BGV for Rahul Gupta (joining Jan 17) has returned a discrepancy in employment history."
            },
            {
                "from": "hr@company.com",
                "timestamp": "2024-01-14T17:00:00",
                "body": "What kind of discrepancy? Is it a gap or falsification?"
            },
            {
                "from": "bgv@verifyfast.com",
                "timestamp": "2024-01-15T09:00:00",
                "body": (
                    "Candidate claimed 2 years at PreviousCorp but our check shows only 8 months. "
                    "This appears to be intentional falsification. "
                    "Joining is in 2 days — do you want to proceed, hold, or rescind the offer?"
                )
            }
        ]
    },
    {
        "thread_id": "t025",
        "subject": "Re: Board meeting materials — final review",
        "labels": ["urgent", "action_required", "high_priority"],
        "sla_minutes": 360,
        "messages": [
            {
                "from": "ceo@company.com",
                "timestamp": "2024-01-14T18:00:00",
                "body": "Board meeting is tomorrow 10 AM. Please finalize the board deck and financials tonight."
            },
            {
                "from": "finance@company.com",
                "timestamp": "2024-01-14T21:00:00",
                "body": "Financials done. Sent to CEO. Waiting for product slides from the product team."
            },
            {
                "from": "ceo@company.com",
                "timestamp": "2024-01-15T08:00:00",
                "body": (
                    "Still missing product slides and Q1 forecast. "
                    "Board meeting is in 2 hours. "
                    "Product team please send your slides to ea@company.com immediately."
                )
            }
        ]
    },
]