# env/data/emails.py
# 50 synthetic corporate workplace emails
# Categories: urgent, action_required, info, newsletter, spam, meeting, hr, finance, legal, it_support

EMAILS = [

    # ══════════════════════════════════════════
    # URGENT (10 emails)
    # ══════════════════════════════════════════
    {
        "id": "e001",
        "sender": "cto@company.com",
        "subject": "URGENT: Production API returning 500 errors",
        "body": (
            "All API endpoints have been returning 500 errors for the last 15 minutes. "
            "Our monitoring shows 3,000 failed requests per minute. "
            "Customer-facing features are completely broken. "
            "On-call engineer please respond immediately. "
            "This is a P0 — all hands on deck."
        ),
        "timestamp": "2024-01-15T03:12:00",
        "sla_minutes": 15,
        "labels": ["urgent", "action_required", "high_priority", "it_support"]
    },
    {
        "id": "e002",
        "sender": "legal@bigclient.com",
        "subject": "Formal breach of contract notice — 24 hour response window",
        "body": (
            "We are formally notifying you of a breach of Section 4.2 of our MSA dated Feb 2023. "
            "Your platform has failed to meet the 99.9% uptime SLA for three consecutive months: "
            "October (98.1%), November (97.8%), December (98.4%). "
            "We require a written remediation plan within 24 hours. "
            "Failure to respond will result in contract termination and legal action."
        ),
        "timestamp": "2024-01-15T09:00:00",
        "sla_minutes": 60,
        "labels": ["urgent", "action_required", "high_priority", "legal"]
    },
    {
        "id": "e003",
        "sender": "security@company.com",
        "subject": "CRITICAL: Potential data breach detected",
        "body": (
            "Our SIEM has flagged unusual data exfiltration patterns from the employee-data S3 bucket. "
            "Approximately 50,000 records may have been accessed by an unauthorized IP (45.33.32.156). "
            "The incident started at 01:30 UTC. We have isolated the bucket. "
            "CISO and legal team must be looped in within the next 30 minutes. "
            "Do not discuss this over Slack — use encrypted email only."
        ),
        "timestamp": "2024-01-15T02:00:00",
        "sla_minutes": 30,
        "labels": ["urgent", "action_required", "high_priority", "security"]
    },
    {
        "id": "e004",
        "sender": "ops@company.com",
        "subject": "Office flooded — all staff must evacuate by 9 AM",
        "body": (
            "A pipe burst overnight on the 3rd floor. Floors 3 and 4 are flooded. "
            "Building management has issued a mandatory evacuation for those floors by 9 AM today. "
            "IT is setting up a temporary workspace at WeWork Connaught Place. "
            "Please acknowledge receipt of this email immediately."
        ),
        "timestamp": "2024-01-15T07:00:00",
        "sla_minutes": 30,
        "labels": ["urgent", "action_required", "high_priority"]
    },
    {
        "id": "e005",
        "sender": "payroll@company.com",
        "subject": "URGENT: Bank account verification needed before 2 PM today",
        "body": (
            "We are processing this month's salaries today. "
            "Our records show your bank account details have not been verified after the recent portal migration. "
            "If you do not submit your verified bank details by 2 PM today, "
            "your salary will be delayed by 5–7 business days. "
            "Please log in to hr.company.com and verify under 'Payment Settings'."
        ),
        "timestamp": "2024-01-15T10:00:00",
        "sla_minutes": 120,
        "labels": ["urgent", "action_required", "high_priority", "hr", "finance"]
    },
    {
        "id": "e006",
        "sender": "angry.enterprise@client.com",
        "subject": "Your service has been down for 2 hours — escalating to CEO",
        "body": (
            "This is completely unacceptable. Our entire team of 200 people has been unable to access "
            "your platform since 8 AM. We pay $50,000 per year for this service. "
            "I have already left 3 voicemails. No one has called back. "
            "I am escalating this directly to your CEO. "
            "I expect a call from a senior engineer within 30 minutes."
        ),
        "timestamp": "2024-01-15T10:05:00",
        "sla_minutes": 30,
        "labels": ["urgent", "action_required", "high_priority"]
    },
    {
        "id": "e007",
        "sender": "noreply@paypal.com",
        "subject": "You sent $1,200 to an unknown recipient",
        "body": (
            "A payment of $1,200.00 was sent from your PayPal account to quickpay@unknown.net "
            "on Jan 15, 2024 at 04:22 AM IST. Transaction ID: 9K22LQ8. "
            "If you did not authorize this transaction, please call PayPal immediately at 1800-102-3344 "
            "or log in and open a dispute within 24 hours."
        ),
        "timestamp": "2024-01-15T04:25:00",
        "sla_minutes": 60,
        "labels": ["urgent", "action_required", "high_priority", "finance"]
    },
    {
        "id": "e008",
        "sender": "devops@company.com",
        "subject": "Disk usage at 97% on prod-db-01 — immediate action needed",
        "body": (
            "prod-db-01 is at 97% disk usage. At current write rate, the disk will be full in ~2 hours. "
            "A full disk will cause all database writes to fail and bring down the application. "
            "DBA team needs to archive old logs or expand the volume immediately. "
            "Paging on-call DBA now."
        ),
        "timestamp": "2024-01-15T05:30:00",
        "sla_minutes": 45,
        "labels": ["urgent", "action_required", "high_priority", "it_support"]
    },
    {
        "id": "e009",
        "sender": "compliance@regulator.gov.in",
        "subject": "Non-compliance notice: DPDP Act filing overdue",
        "body": (
            "Your organization was required to file its annual data processing report under the "
            "Digital Personal Data Protection Act 2023 by December 31, 2023. "
            "Our records show this filing has not been received. "
            "You have 7 days from the date of this notice to submit or face a penalty of up to ₹2 crore. "
            "Contact compliance@regulator.gov.in with your filing reference number."
        ),
        "timestamp": "2024-01-15T11:00:00",
        "sla_minutes": 480,
        "labels": ["urgent", "action_required", "high_priority", "legal", "compliance"]
    },
    {
        "id": "e010",
        "sender": "cfo@company.com",
        "subject": "Wire transfer approval needed in next 2 hours",
        "body": (
            "We have a vendor payment of ₹45 lakhs due today. "
            "The finance team needs your digital signature on the payment authorization form. "
            "This is time-sensitive — the bank's RTGS cutoff is 4:30 PM. "
            "Please approve via the finance portal under 'Pending Approvals' ASAP."
        ),
        "timestamp": "2024-01-15T13:00:00",
        "sla_minutes": 90,
        "labels": ["urgent", "action_required", "high_priority", "finance"]
    },

    # ══════════════════════════════════════════
    # ACTION REQUIRED — MEDIUM PRIORITY (12 emails)
    # ══════════════════════════════════════════
    {
        "id": "e011",
        "sender": "hr@company.com",
        "subject": "Submit your Q4 self-appraisal by January 20",
        "body": (
            "The Q4 performance review cycle is now open. "
            "Please log in to the HRMS portal and complete your self-appraisal by January 20. "
            "Your manager's review will begin on January 22. "
            "Ratings will factor into the February increment cycle."
        ),
        "timestamp": "2024-01-15T09:00:00",
        "sla_minutes": 7200,
        "labels": ["action_required", "medium_priority", "hr"]
    },
    {
        "id": "e012",
        "sender": "sarah.jones@partner.org",
        "subject": "Can we schedule a call to discuss Q1 roadmap alignment?",
        "body": (
            "Hi, hope you're doing well. I wanted to connect before the board meeting next week "
            "to align on the Q1 product roadmap. "
            "I'm available Tuesday 2–4 PM or Thursday after 12 PM. "
            "Would either of those slots work? Happy to send a calendar invite once confirmed."
        ),
        "timestamp": "2024-01-15T09:15:00",
        "sla_minutes": 1440,
        "labels": ["action_required", "medium_priority", "meeting"]
    },
    {
        "id": "e013",
        "sender": "finance@company.com",
        "subject": "Invoice #4521 from TechSupplies Ltd is pending your approval",
        "body": (
            "Invoice #4521 for ₹1,85,000 from TechSupplies Ltd (laptops for new joiners) "
            "is awaiting your approval in the procurement portal. "
            "The vendor has a Net-30 payment term and the invoice date is Jan 3. "
            "Please approve or reject by January 18 to avoid late payment charges."
        ),
        "timestamp": "2024-01-15T10:00:00",
        "sla_minutes": 4320,
        "labels": ["action_required", "medium_priority", "finance"]
    },
    {
        "id": "e014",
        "sender": "it@company.com",
        "subject": "Your laptop is due for OS update — schedule a maintenance window",
        "body": (
            "Your laptop (Asset ID: LT-2291) is running an outdated OS version (Windows 10 21H1). "
            "As per IT policy, all devices must be updated to Windows 11 22H2 by February 1. "
            "Please schedule a 2-hour maintenance window by clicking the link below. "
            "The update will require a restart. Save your work before the scheduled time."
        ),
        "timestamp": "2024-01-15T11:00:00",
        "sla_minutes": 14400,
        "labels": ["action_required", "medium_priority", "it_support"]
    },
    {
        "id": "e015",
        "sender": "travel@company.com",
        "subject": "Confirm your travel dates for the Bangalore offsite",
        "body": (
            "The engineering offsite in Bangalore is confirmed for Feb 12–14. "
            "Please confirm your attendance and travel preferences by January 19. "
            "We are booking flights in bulk — late confirmations will need self-booking and reimbursement. "
            "Hotel is Marriott Whitefield. Reply with: attending yes/no, departure city, seat preference."
        ),
        "timestamp": "2024-01-15T12:00:00",
        "sla_minutes": 5760,
        "labels": ["action_required", "medium_priority"]
    },
    {
        "id": "e016",
        "sender": "recruiter@company.com",
        "subject": "Interview panel request: Backend Engineer candidate on Jan 18",
        "body": (
            "We have a strong Backend Engineer candidate, Rohan Mehta, interviewing on January 18 at 3 PM. "
            "You've been requested as the technical interviewer for the system design round (45 mins). "
            "Please confirm your availability by EOD today. "
            "Interview brief and resume attached."
        ),
        "timestamp": "2024-01-15T10:30:00",
        "sla_minutes": 480,
        "labels": ["action_required", "medium_priority", "hr"]
    },
    {
        "id": "e017",
        "sender": "contracts@vendor.com",
        "subject": "Renewal reminder: Software license expires in 14 days",
        "body": (
            "Your enterprise license for DataViz Pro (25 seats) expires on January 29, 2024. "
            "To avoid service interruption, please initiate the renewal process. "
            "Our renewal team can be reached at renew@vendor.com or +91-80-4567-8901. "
            "Early renewal before Jan 22 gets a 10% discount."
        ),
        "timestamp": "2024-01-15T08:00:00",
        "sla_minutes": 2880,
        "labels": ["action_required", "medium_priority", "finance"]
    },
    {
        "id": "e018",
        "sender": "user456@gmail.com",
        "subject": "Question about upgrading to Pro plan",
        "body": (
            "Hi team, I've been using the free plan for about 3 months and I'm considering upgrading. "
            "I have a few questions: Does Pro include API access? How many team members can I add? "
            "Is there annual billing with a discount? "
            "Also, can I get a 14-day trial before committing? Thanks!"
        ),
        "timestamp": "2024-01-15T14:00:00",
        "sla_minutes": 1440,
        "labels": ["action_required", "medium_priority"]
    },
    {
        "id": "e019",
        "sender": "manager@company.com",
        "subject": "Please review and merge PR #342 before EOD",
        "body": (
            "Hey, PR #342 (auth token refresh fix) has been open for 2 days. "
            "It's blocking the QA team from starting regression testing. "
            "Can you review and merge it today? "
            "It's a small change — about 80 lines. I've already approved it."
        ),
        "timestamp": "2024-01-15T11:30:00",
        "sla_minutes": 480,
        "labels": ["action_required", "medium_priority"]
    },
    {
        "id": "e020",
        "sender": "admin@company.com",
        "subject": "Mandatory: Update emergency contact details in HRMS by Jan 31",
        "body": (
            "As part of our annual HR data audit, all employees must verify and update "
            "their emergency contact details in the HRMS portal by January 31. "
            "This is mandatory per company policy. "
            "Log in at hrms.company.com → Profile → Emergency Contacts."
        ),
        "timestamp": "2024-01-15T09:30:00",
        "sla_minutes": 23040,
        "labels": ["action_required", "medium_priority", "hr"]
    },
    {
        "id": "e021",
        "sender": "accounts@gstportal.gov.in",
        "subject": "GSTR-1 filing due in 3 days",
        "body": (
            "This is a reminder that your GSTR-1 return for December 2023 is due on January 11. "
            "Please ensure all outward supply invoices are uploaded before the deadline. "
            "Late filing attracts a penalty of ₹50 per day. "
            "Log in at gst.gov.in to file."
        ),
        "timestamp": "2024-01-08T10:00:00",
        "sla_minutes": 4320,
        "labels": ["action_required", "medium_priority", "finance", "compliance"]
    },
    {
        "id": "e022",
        "sender": "boss@company.com",
        "subject": "Quick question",
        "body": (
            "Hey, got a minute tomorrow morning? "
            "Nothing urgent — just wanted to catch up on a few things. "
            "Let me know what time works."
        ),
        "timestamp": "2024-01-15T17:30:00",
        "sla_minutes": 1440,
        "labels": ["action_required", "medium_priority"]
        # Tricky: vague boss email — agent must not ignore it
    },

    # ══════════════════════════════════════════
    # INFORMATIONAL (10 emails)
    # ══════════════════════════════════════════
    {
        "id": "e023",
        "sender": "noreply@github.com",
        "subject": "Your repo crossed 1,000 stars ⭐",
        "body": (
            "Congratulations! Your repository 'fast-api-boilerplate' just reached 1,000 stars. "
            "Thank you to the open source community for your support!"
        ),
        "timestamp": "2024-01-15T12:00:00",
        "sla_minutes": None,
        "labels": ["info", "low_priority"]
    },
    {
        "id": "e024",
        "sender": "noreply@aws.amazon.com",
        "subject": "Your AWS bill for December 2023: ₹12,430",
        "body": (
            "Your AWS bill for December 2023 is ₹12,430. "
            "Auto-pay is scheduled for January 20 from your registered payment method. "
            "Top services by cost: EC2 (₹7,200), RDS (₹3,100), S3 (₹1,130). "
            "Log in to Cost Explorer for a full breakdown."
        ),
        "timestamp": "2024-01-15T08:00:00",
        "sla_minutes": None,
        "labels": ["info", "medium_priority", "finance"]
    },
    {
        "id": "e025",
        "sender": "calendar@company.com",
        "subject": "Reminder: All-hands meeting tomorrow at 10 AM",
        "body": (
            "This is a reminder for tomorrow's company all-hands at 10 AM in Conference Room A. "
            "Agenda: Q4 results, 2024 OKRs, team announcements, and open Q&A. "
            "Zoom link for remote attendees: zoom.us/j/98234756."
        ),
        "timestamp": "2024-01-15T08:00:00",
        "sla_minutes": None,
        "labels": ["info", "medium_priority", "meeting"]
    },
    {
        "id": "e026",
        "sender": "devops@company.com",
        "subject": "Scheduled maintenance tonight 11 PM–2 AM IST",
        "body": (
            "We are performing database index optimization and load balancer config updates tonight "
            "from 11 PM to 2 AM IST. The platform may be intermittently slow. "
            "No user action required. Post-maintenance report will be sent by 3 AM."
        ),
        "timestamp": "2024-01-15T15:00:00",
        "sla_minutes": None,
        "labels": ["info", "medium_priority", "it_support"]
    },
    {
        "id": "e027",
        "sender": "notifications@linkedin.com",
        "subject": "You appeared in 47 searches this week",
        "body": (
            "Your LinkedIn profile appeared in 47 searches this week — up 31% from last week. "
            "Viewers include people from Google, Razorpay, and Zepto. "
            "Update your profile to improve visibility."
        ),
        "timestamp": "2024-01-15T09:00:00",
        "sla_minutes": None,
        "labels": ["info", "low_priority"]
    },
    {
        "id": "e028",
        "sender": "noreply@jira.atlassian.com",
        "subject": "Sprint 24 ended — 8 of 12 story points completed",
        "body": (
            "Sprint 24 has ended. Your team completed 8 of 12 planned story points (67%). "
            "Incomplete: PROJ-441 (API rate limiting), PROJ-445 (dark mode toggle). "
            "Sprint 25 planning is scheduled for Jan 16 at 11 AM."
        ),
        "timestamp": "2024-01-15T00:00:00",
        "sla_minutes": None,
        "labels": ["info", "low_priority"]
    },
    {
        "id": "e029",
        "sender": "team@figma.com",
        "subject": "New Figma features — January 2024 release notes",
        "body": (
            "What's new in Figma this month: AI layout suggestions in auto-layout, "
            "improved variable inspector, faster prototype rendering on mobile preview. "
            "Full changelog at figma.com/releases."
        ),
        "timestamp": "2024-01-15T10:00:00",
        "sla_minutes": None,
        "labels": ["info", "low_priority"]
    },
    {
        "id": "e030",
        "sender": "feedback@typeform.com",
        "subject": "New response on 'Product Feedback Survey'",
        "body": (
            "A user submitted your Product Feedback Survey. Rating: 4/5. "
            "Comment: 'Love the product but mobile UX needs improvement — buttons are hard to tap.' "
            "View full response in your Typeform dashboard."
        ),
        "timestamp": "2024-01-15T13:00:00",
        "sla_minutes": None,
        "labels": ["info", "low_priority"]
    },
    {
        "id": "e031",
        "sender": "hr@company.com",
        "subject": "Welcome Priya Nair — joining as Product Designer on Jan 17",
        "body": (
            "Please join us in welcoming Priya Nair who is joining as a Senior Product Designer "
            "on January 17. Priya comes from Swiggy and will be working on the growth team. "
            "Her onboarding buddy is Arjun Sharma. Please make her feel welcome!"
        ),
        "timestamp": "2024-01-15T10:00:00",
        "sla_minutes": None,
        "labels": ["info", "low_priority", "hr"]
    },
    {
        "id": "e032",
        "sender": "noreply@statuspage.io",
        "subject": "Resolved: Payment gateway latency incident",
        "body": (
            "The payment gateway latency incident that began at 14:32 IST has been resolved at 15:47 IST. "
            "Root cause: misconfigured nginx upstream timeout. "
            "All transactions during the window have been reprocessed. "
            "Post-mortem will be published within 48 hours."
        ),
        "timestamp": "2024-01-15T16:00:00",
        "sla_minutes": None,
        "labels": ["info", "medium_priority", "it_support"]
    },

    # ══════════════════════════════════════════
    # NEWSLETTERS (8 emails)
    # ══════════════════════════════════════════
    {
        "id": "e033",
        "sender": "digest@hackernewsletter.com",
        "subject": "Hacker Newsletter #651 — Top stories this week",
        "body": (
            "This week: Mistral releases new 7B model, "
            "GitHub Copilot adds multi-file context, "
            "a deep dive on how Notion rebuilt their sync engine. "
            "Read more at hackernewsletter.com"
        ),
        "timestamp": "2024-01-15T08:00:00",
        "sla_minutes": None,
        "labels": ["newsletter", "low_priority"]
    },
    {
        "id": "e034",
        "sender": "weekly@morningbrew.com",
        "subject": "Morning Brew ☕ Jan 15 — Markets, Tech & Business",
        "body": (
            "Sensex up 312 points. Zomato reports first quarterly profit. "
            "RBI keeps repo rate unchanged at 6.5%. "
            "Paytm in regulatory trouble again. Full stories inside."
        ),
        "timestamp": "2024-01-15T06:00:00",
        "sla_minutes": None,
        "labels": ["newsletter", "low_priority"]
    },
    {
        "id": "e035",
        "sender": "updates@medium.com",
        "subject": "Top stories for you this week on Medium",
        "body": (
            "Recommended reads: '10 things I wish I knew before becoming an engineering manager', "
            "'Why I moved from React to htmx', "
            "'The silent crisis in Indian tech hiring'. "
            "Happy reading!"
        ),
        "timestamp": "2024-01-15T07:00:00",
        "sla_minutes": None,
        "labels": ["newsletter", "low_priority"]
    },
    {
        "id": "e036",
        "sender": "noreply@substack.com",
        "subject": "New post from Lenny's Newsletter: 'The product trio'",
        "body": (
            "Lenny Rachitsky just published: 'The Product Trio: How the best teams align PM, Design, and Eng.' "
            "Read it at lennysnewsletter.substack.com"
        ),
        "timestamp": "2024-01-15T14:00:00",
        "sla_minutes": None,
        "labels": ["newsletter", "low_priority"]
    },
    {
        "id": "e037",
        "sender": "digest@tldr.tech",
        "subject": "TLDR: AI makes code, humans make bugs | Jan 15 2024",
        "body": (
            "Today in tech: Anthropic releases Claude 3, "
            "Stack Overflow traffic down 35% YoY (blame Copilot), "
            "Databricks acquires MosaicML for $1.3B. "
            "5-minute read at tldr.tech."
        ),
        "timestamp": "2024-01-15T08:30:00",
        "sla_minutes": None,
        "labels": ["newsletter", "low_priority"]
    },
    {
        "id": "e038",
        "sender": "noreply@producthunt.com",
        "subject": "Today's top products — Jan 15, 2024",
        "body": (
            "🥇 #1: Replit AI Agent — build full apps with one prompt. "
            "🥈 #2: Linear AI — auto-generated issue summaries. "
            "🥉 #3: Fathom 2.0 — AI meeting notes with CRM sync. "
            "Explore at producthunt.com."
        ),
        "timestamp": "2024-01-15T09:00:00",
        "sla_minutes": None,
        "labels": ["newsletter", "low_priority"]
    },
    {
        "id": "e039",
        "sender": "weekly@economictimes.com",
        "subject": "ET Tech Weekly: India's AI startup boom",
        "body": (
            "This week's deep dive: How Indian AI startups raised $2.1B in 2023, "
            "why Bangalore is becoming the LLM capital of Asia, "
            "and what the DPDP Act means for your data team. "
            "Read the full edition at et.com/tech."
        ),
        "timestamp": "2024-01-15T07:30:00",
        "sla_minutes": None,
        "labels": ["newsletter", "low_priority"]
    },
    {
        "id": "e040",
        "sender": "noreply@bytebytego.com",
        "subject": "System Design Newsletter #89: How Uber scales real-time location",
        "body": (
            "This week Alex covers how Uber's location service handles 1M GPS pings per second, "
            "the role of geohashing, and why they moved from MongoDB to a custom solution. "
            "Read at blog.bytebytego.com."
        ),
        "timestamp": "2024-01-15T08:00:00",
        "sla_minutes": None,
        "labels": ["newsletter", "low_priority"]
    },

    # ══════════════════════════════════════════
    # SPAM (10 emails)
    # ══════════════════════════════════════════
    {
        "id": "e041",
        "sender": "deals@megapromo99.biz",
        "subject": "YOU WON ₹50,000!! Claim before midnight!!",
        "body": (
            "CONGRATULATIONS! You were randomly selected as today's lucky winner. "
            "Claim your ₹50,000 prize by clicking: bit.ly/claimnow9923. "
            "Offer expires at midnight. Act NOW!"
        ),
        "timestamp": "2024-01-15T07:00:00",
        "sla_minutes": None,
        "labels": ["spam", "low_priority"]
    },
    {
        "id": "e042",
        "sender": "invest@crypto-10x.io",
        "subject": "Make ₹1 lakh from ₹5000 in 30 days — GUARANTEED",
        "body": (
            "Our AI trading bot has generated 2000% returns in 2023. "
            "Invest just ₹5,000 today and watch it grow to ₹1 lakh in 30 days. "
            "Limited spots available. WhatsApp us at +91-99XXXXXXXX."
        ),
        "timestamp": "2024-01-15T06:00:00",
        "sla_minutes": None,
        "labels": ["spam", "low_priority"]
    },
    {
        "id": "e043",
        "sender": "hr.hiring2024@gmail.com",
        "subject": "Work from home job — earn ₹80,000/month doing simple tasks",
        "body": (
            "We are hiring part-time data entry workers. No experience needed. "
            "Work 2 hours a day and earn ₹80,000 per month. "
            "Registration fee: ₹500 only (refundable). "
            "Reply with your name and phone number to apply."
        ),
        "timestamp": "2024-01-15T08:00:00",
        "sla_minutes": None,
        "labels": ["spam", "low_priority"]
    },
    {
        "id": "e044",
        "sender": "prince.ibrahim@transfer-bureau.org",
        "subject": "Confidential: $6.5 million transfer assistance needed",
        "body": (
            "Dear Friend, I am Prince Ibrahim Al-Rashid, son of a late Nigerian diplomat. "
            "I need a trusted foreign partner to help transfer $6.5 million. "
            "Your commission: 25%. Reply with full name, address, and phone number."
        ),
        "timestamp": "2024-01-15T05:00:00",
        "sla_minutes": None,
        "labels": ["spam", "low_priority"]
    },
    {
        "id": "e045",
        "sender": "noreply@iphonewin2024.com",
        "subject": "Your iPhone 15 Pro is ready for dispatch — confirm address",
        "body": (
            "You've been selected to receive a FREE iPhone 15 Pro (256GB). "
            "Just pay ₹299 shipping. Confirm your address at: iphone-win2024.com/confirm. "
            "Valid for 12 hours only."
        ),
        "timestamp": "2024-01-15T09:00:00",
        "sla_minutes": None,
        "labels": ["spam", "low_priority"]
    },
    {
        "id": "e046",
        "sender": "seo@rank1google.biz",
        "subject": "Rank #1 on Google in 7 days — guaranteed SEO service",
        "body": (
            "We guarantee your website will rank on Page 1 of Google within 7 days or full refund. "
            "Our black-hat... I mean, cutting-edge SEO techniques have worked for 500+ clients. "
            "Starting at just $99. Reply to get started."
        ),
        "timestamp": "2024-01-15T10:00:00",
        "sla_minutes": None,
        "labels": ["spam", "low_priority"]
    },
    {
        "id": "e047",
        "sender": "alert@sbi-kyc-update.net",
        "subject": "SBI Alert: Your account will be blocked in 24 hours",
        "body": (
            "Dear SBI Customer, your account KYC is pending. "
            "Your account will be BLOCKED within 24 hours if not updated. "
            "Update now at: sbi-kyc-update.net/verify (NOT the official SBI site). "
            "Enter Aadhaar, PAN, and OTP to verify."
        ),
        "timestamp": "2024-01-15T11:00:00",
        "sla_minutes": None,
        "labels": ["spam", "low_priority"]
        # Classic phishing — agent should recognize fake domain
    },
    {
        "id": "e048",
        "sender": "lotteryboard@uk-lottery-intl.com",
        "subject": "You've won £850,000 in the UK National Lottery",
        "body": (
            "We are pleased to inform you that your email address has won £850,000 "
            "in the UK National Lottery International Draw. "
            "To claim, contact our agent Mr. David Cole at davidcole_agent@gmail.com "
            "with your full name and address."
        ),
        "timestamp": "2024-01-15T07:00:00",
        "sla_minutes": None,
        "labels": ["spam", "low_priority"]
    },
    {
        "id": "e049",
        "sender": "bulk@medicalsupplements.shop",
        "subject": "Lose 10kg in 10 days with our Ayurvedic formula — Doctor approved!",
        "body": (
            "Our 100% natural Ayurvedic weight loss formula is clinically proven to burn 1kg per day. "
            "No diet, no exercise needed. Just ₹999 for a 30-day supply. "
            "Order now at medicalsupplements.shop. Limited stock!"
        ),
        "timestamp": "2024-01-15T08:00:00",
        "sla_minutes": None,
        "labels": ["spam", "low_priority"]
    },
    {
        "id": "e050",
        "sender": "free.recharge@jio-offer2024.com",
        "subject": "Jio Free Recharge 2024 — Get ₹999 recharge for free",
        "body": (
            "Jio is giving away free ₹999 recharges to celebrate 8 years. "
            "Click here to claim: jio-offer2024.com/free-recharge. "
            "Share with 5 friends to unlock. Expires today!"
        ),
        "timestamp": "2024-01-15T09:00:00",
        "sla_minutes": None,
        "labels": ["spam", "low_priority"]
    },
]