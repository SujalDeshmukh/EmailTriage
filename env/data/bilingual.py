# env/data/bilingual.py
# Hindi + English code-switching — realistic Indian corporate workplace emails

BILINGUAL_EMAILS = [

    {
        "id": "b001",
        "sender": "manager.sharma@company.com",
        "subject": "Aaj ki meeting postpone ho gayi — please note",
        "body": (
            "Hi team, aaj 3 baje wali standup meeting postpone ho rahi hai. "
            "New time: kal subah 10 AM. "
            "Please apna daily update Slack pe post kar do. "
            "Koi bhi questions ho toh ping karo."
        ),
        "timestamp": "2024-01-15T14:00:00",
        "sla_minutes": None,
        "labels": ["info", "medium_priority", "meeting"]
    },
    {
        "id": "b002",
        "sender": "hr@company.com",
        "subject": "Leave policy update — please dhyan se padhe",
        "body": (
            "Dear all, hum apni leave policy update kar rahe hain effective February 1 se. "
            "Key changes: Casual leave 12 se badh ke 15 days ho gayi. "
            "Sick leave ab carry forward hogi (max 10 days). "
            "Earned leave encashment policy bhi change hui hai — details attached PDF mein hain. "
            "Koi bhi doubt ho toh hr@company.com pe mail karo."
        ),
        "timestamp": "2024-01-15T10:00:00",
        "sla_minutes": None,
        "labels": ["info", "medium_priority", "hr"]
    },
    {
        "id": "b003",
        "sender": "cto@company.com",
        "subject": "URGENT: Server neeche aa gaya — sabhi on-call engineers respond karo",
        "body": (
            "Yaar ye kya ho raha hai — production server phir se crash ho gaya. "
            "Ye aaj raat ka teesra crash hai. "
            "On-call team please abhi Zoom join karo: zoom.us/j/12345678. "
            "Baki sabh please apna kaam band karo aur stand by raho."
        ),
        "timestamp": "2024-01-15T02:30:00",
        "sla_minutes": 15,
        "labels": ["urgent", "action_required", "high_priority", "it_support"]
    },
    {
        "id": "b004",
        "sender": "employee.ravi@company.com",
        "subject": "Mujhe aaj half day chahiye — family emergency",
        "body": (
            "Hi, meri mummy ki tabiyat thodi kharab hai. "
            "Kya main aaj 2 baje ke baad half day le sakta hoon? "
            "Meri koi important meetings nahi hain aaj afternoon. "
            "Please bata do jaldi — abhi hospital le jaana hai."
        ),
        "timestamp": "2024-01-15T11:00:00",
        "sla_minutes": 60,
        "labels": ["action_required", "medium_priority", "hr"]
    },
    {
        "id": "b005",
        "sender": "finance@company.com",
        "subject": "Q3 expenses exceed ho gayi — explanation chahiye",
        "body": (
            "Hi, Q3 mein travel aur entertainment budget ₹8.2 lakhs tha "
            "lekin actual spend ₹11.7 lakhs raha — 43% over budget. "
            "CFO ne breakdown maanga hai. "
            "Please department-wise breakdown kal subah tak bhejo. "
            "Yeh CFO review ke liye urgent hai."
        ),
        "timestamp": "2024-01-15T09:00:00",
        "sla_minutes": 1440,
        "labels": ["action_required", "medium_priority", "finance"]
    },
    {
        "id": "b006",
        "sender": "angry.customer.hindi@gmail.com",
        "subject": "Aapki service bahut bekar hai — refund do abhi",
        "body": (
            "Main 2 hafte se apni problem solve karane ki koshish kar raha hoon. "
            "Aapka support team koi reply nahi kar raha. "
            "Maine ₹15,000 pay kiye hain is software ke liye aur yeh kaam hi nahi kar raha. "
            "Agar aaj tak refund nahi mila toh main consumer forum mein complaint karunga."
        ),
        "timestamp": "2024-01-15T11:30:00",
        "sla_minutes": 120,
        "labels": ["urgent", "action_required", "high_priority"]
    },
    {
        "id": "b007",
        "sender": "office.admin@company.com",
        "subject": "Diwali party planning — suggestions maange hain",
        "body": (
            "Hi everyone! Is saal ki Diwali party ke liye planning shuru ho rahi hai. "
            "Date: November 1, Venue: Office terrace. "
            "Kya kya activities chahiye? Food preferences kya hain (veg/non-veg ratio)? "
            "Please is Google Form ko fill karo by October 20: forms.google.com/..."
        ),
        "timestamp": "2024-01-15T12:00:00",
        "sla_minutes": None,
        "labels": ["info", "low_priority"]
    },
    {
        "id": "b008",
        "sender": "security.alert@company.com",
        "subject": "Aapke account mein suspicious login — turant action lo",
        "body": (
            "Aapke company account mein ek suspicious login detect hua hai. "
            "Location: Hyderabad (aapka usual location: Lucknow). "
            "Time: 11:45 PM IST. Device: Unknown Android device. "
            "Agar yeh aap nahi the, toh abhi apna password change karo: sso.company.com. "
            "Security team ko bhi inform karo: security@company.com."
        ),
        "timestamp": "2024-01-15T23:50:00",
        "sla_minutes": 30,
        "labels": ["urgent", "action_required", "high_priority", "security"]
    },
    {
        "id": "b009",
        "sender": "manager.priya@company.com",
        "subject": "Good work on the release — well done team!",
        "body": (
            "Hi all, bahut achha kaam kiya is sprint mein! "
            "The v2.4 release went smoothly — zero critical bugs post-deployment. "
            "Special shoutout to Aakash aur Divya for staying late on Thursday. "
            "Celebrate karo — free lunch on Friday! "
        ),
        "timestamp": "2024-01-15T10:00:00",
        "sla_minutes": None,
        "labels": ["info", "low_priority"]
    },
    {
        "id": "b010",
        "sender": "compliance@company.com",
        "subject": "DPDP Act training mandatory hai — Jan 25 tak complete karo",
        "body": (
            "Sabhi employees ke liye Digital Personal Data Protection Act 2023 training mandatory hai. "
            "LMS pe 45-minute module available hai: lms.company.com/dpdp-training. "
            "Deadline: January 25. "
            "Jo complete nahi karenge unhe HR notice milega. "
            "Koi confusion ho toh compliance@company.com pe mail karo."
        ),
        "timestamp": "2024-01-15T09:30:00",
        "sla_minutes": None,
        "labels": ["action_required", "medium_priority", "compliance", "hr"]
    },
    {
        "id": "b011",
        "sender": "vendor.ramesh@supplier.in",
        "subject": "Payment pending hai — please jaldi process karo",
        "body": (
            "Respected Sir/Ma'am, hamare October aur November ke invoices — "
            "Inv#1089 (₹85,000) aur Inv#1102 (₹92,000) — "
            "abhi tak payment nahi aayi. "
            "Yeh 60 days se zyada ho gaye hain. "
            "Please is week process kar dijiye warna hum service rok denge."
        ),
        "timestamp": "2024-01-15T10:00:00",
        "sla_minutes": 1440,
        "labels": ["action_required", "medium_priority", "finance"]
    },
    {
        "id": "b012",
        "sender": "intern.ankita@company.com",
        "subject": "Project guidance chahiye — kab time milega?",
        "body": (
            "Hi, main final year intern hoon aur mera internship project next week submit hai. "
            "Mujhe API integration waale part mein kuch doubts hain. "
            "Kya aap 20-30 minutes nikal sakte ho is week? "
            "Main aapke schedule ke hisaab se available hoon. Thanks!"
        ),
        "timestamp": "2024-01-15T14:00:00",
        "sla_minutes": 2880,
        "labels": ["action_required", "low_priority"]
    },
    {
        "id": "b013",
        "sender": "it@company.com",
        "subject": "VPN nahi chal raha — kya aap bhi face kar rahe ho?",
        "body": (
            "Hi all, kuch employees report kar rahe hain ki company VPN se connect nahi ho raha. "
            "Hum investigate kar rahe hain. ETA for fix: 2 hours. "
            "Temporary workaround: Hotspot se try karo ya office aa jao. "
            "Updates milte rahenge is thread pe."
        ),
        "timestamp": "2024-01-15T09:00:00",
        "sla_minutes": None,
        "labels": ["info", "medium_priority", "it_support"]
    },
    {
        "id": "b014",
        "sender": "ceo@company.com",
        "subject": "Company town hall — next Friday 4 PM — must attend",
        "body": (
            "Dear team, hum quarterly town hall rakh rahe hain next Friday 4 PM. "
            "Main Q3 results share karunga, 2024 ke goals discuss karenge, "
            "aur kuch exciting announcements bhi hain. "
            "In-person aur Zoom dono available hai. "
            "Please apni calendar block karo — attendance mandatory hai."
        ),
        "timestamp": "2024-01-15T11:00:00",
        "sla_minutes": None,
        "labels": ["info", "high_priority", "meeting"]
    },
    {
        "id": "b015",
        "sender": "accounts@company.com",
        "subject": "TDS certificate chahiye — Form 16 ke liye",
        "body": (
            "Dear employee, income tax filing season aa rahi hai. "
            "Aapka Form 16 (Part A aur Part B) process ho raha hai. "
            "Please apni investment declarations submit karo payroll portal pe by January 31 "
            "taaki accurate TDS calculation ho sake. "
            "Late submission se excess TDS cut ho sakta hai."
        ),
        "timestamp": "2024-01-15T10:00:00",
        "sla_minutes": None,
        "labels": ["action_required", "medium_priority", "finance", "hr"]
    },
]