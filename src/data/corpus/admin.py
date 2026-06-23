"""Curated admin/office staffing-agency phone screen records."""

from __future__ import annotations

ADMIN_RECORDS: list[dict] = [
    {
        "id": "ad-001",
        "vertical": "admin",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Seven years EA experience with C-suite support, advanced Office suite, "
            "and 72 WPM typing. Confirmed temp-to-perm interest and on-site availability."
        ),
        "resume": (
            "Danielle Foster\nExecutive Assistant | 7 years\n\n"
            "Meridian Capital Partners — Executive Assistant to CFO (2020–2024)\n"
            "- Managed complex calendars for 3 executives in Outlook\n"
            "- Prepared board decks in PowerPoint; expense reports in Excel\n"
            "- Screened calls on 12-line Avaya system; coordinated travel\n\n"
            "Hartwell Law Group — Legal Secretary (2017–2020)\n\n"
            "Skills: Outlook, Word, Excel, PowerPoint, Teams, Concur\n"
            "Typing: 72 WPM | Certifications: Notary (active)"
        ),
        "job_description": (
            "Executive Assistant — Temp-to-Perm (90 days)\n\n"
            "Client: Regional financial services firm, downtown Hartford\n\n"
            "Responsibilities:\n"
            "- Calendar management and meeting coordination for VP Finance\n"
            "- Travel booking, expense reconciliation, board materials\n"
            "- Multi-line phone coverage and visitor reception\n\n"
            "Requirements:\n"
            "- 3+ years executive assistant experience\n"
            "- Advanced Microsoft Office (Outlook, Excel, PowerPoint)\n"
            "- 65+ WPM typing with accuracy\n"
            "- Professional phone manner; on-site 5 days\n"
            "- Temp-to-perm through Apex Staffing\n\n"
            "Pay: $28–32/hr temp | Benefits after conversion"
        ),
        "transcript": (
            "Recruiter: Hi Danielle, this is Sarah from Apex Staffing. I'm screening for an "
            "executive assistant temp-to-perm at a financial services client in Hartford. "
            "Can you walk me through your EA background?\n"
            "Candidate: Sure. I've supported C-suite executives for seven years, most recently "
            "the CFO at Meridian Capital. Heavy Outlook calendaring, board decks in PowerPoint, "
            "and I handled a twelve-line phone system daily.\n"
            "Recruiter: What's your typing speed and Office comfort level?\n"
            "Candidate: Seventy-two words per minute on a recent skills test. I'm advanced in "
            "Word, Excel, Outlook, and PowerPoint — I built pivot tables for budget tracking.\n"
            "Recruiter: This starts as a ninety-day temp with conversion potential. On-site five "
            "days — does that work?\n"
            "Candidate: Yes, I'm looking for stability after a layoff. I can start next Monday "
            "and I'm very interested in the perm path."
        ),
    },
    {
        "id": "ad-002",
        "vertical": "admin",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": (
            "Strong front-desk background with multi-line phone and Office skills. "
            "Typing 68 WPM exceeds requirement; available for temp-to-perm schedule."
        ),
        "resume": (
            "Maria Santos\nReceptionist / Front Desk | 4 years\n\n"
            "Brookline Medical Associates — Receptionist (2021–2024)\n"
            "- Answered 80+ daily calls on 8-line Cisco phone system\n"
            "- Scheduled appointments; checked patients in via Office calendar\n"
            "- Maintained lobby, coordinated vendor deliveries\n\n"
            "Temp — Corporate reception, Waltham (2020)\n\n"
            "Skills: Microsoft Office, multi-line phones, data entry\n"
            "Typing: 68 WPM"
        ),
        "job_description": (
            "Receptionist — Temp-to-Perm\n\n"
            "Client: Professional services office, Waltham MA\n\n"
            "Duties:\n"
            "- Greet visitors; manage 6-line phone system\n"
            "- Mail, supplies, conference room scheduling\n"
            "- Light data entry in Excel\n\n"
            "Requirements:\n"
            "- 2+ years reception or front desk experience\n"
            "- 60+ WPM typing\n"
            "- Microsoft Office proficiency\n"
            "- Professional appearance; reliable attendance\n"
            "- 90-day temp-to-perm via Kelly Services\n\n"
            "Schedule: Mon–Fri 8:30–5:00 on-site"
        ),
        "transcript": (
            "thanks for taking my call maria this is recruiter james with kelly services "
            "screening for a receptionist temp to perm in waltham tell me about your front "
            "desk experience candidate i was receptionist at brookline medical for three "
            "years answered about eighty calls a day on an eight line cisco system scheduled "
            "in outlook and did light excel tracking for supply orders recruiter typing speed "
            "and office skills candidate sixty eight wpm on our last test comfortable with "
            "word excel and outlook recruiter client wants someone on site monday through "
            "friday temp for ninety days with perm conversion candidate that works i live "
            "twelve minutes away and i am actively looking for a long term role"
        ),
    },
    {
        "id": "ad-003",
        "vertical": "admin",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": (
            "Meets data entry requirements: 9,500 KPH with 99.1% accuracy, Excel experience, "
            "and prior temp assignments. Confirmed full-time availability for temp-to-perm."
        ),
        "resume": (
            "Kevin Tran\nData Entry Clerk | 3 years\n\n"
            "DataForce Solutions — Data Entry Specialist (2022–2024)\n"
            "- Entered 400+ records daily in custom CRM and Excel\n"
            "- 9,500 KPH / 99.1% accuracy on quality audits\n"
            "- Verified invoice data against source documents\n\n"
            "Apex Staffing temp — Insurance indexing (2021)\n\n"
            "Skills: Excel, 10-key, OCR workflows, attention to detail\n"
            "Typing: 85 WPM | 10-key: 9,500 KPH"
        ),
        "job_description": (
            "Data Entry Clerk — Temp-to-Perm (90 days)\n\n"
            "Client: Insurance back-office, remote-first with 2 days on-site\n\n"
            "Responsibilities:\n"
            "- High-volume policy and claims data entry\n"
            "- Excel spreadsheets, duplicate detection, QA checks\n"
            "- Meet 9,000+ KPH accuracy standards\n\n"
            "Requirements:\n"
            "- 1+ years data entry or clerical experience\n"
            "- 8,500+ KPH ten-key; 55+ WPM typing\n"
            "- Microsoft Excel — filters, basic formulas\n"
            "- Reliable attendance; temp-to-perm path\n\n"
            "Pay: $19–21/hr | Apex Staffing placement"
        ),
        "transcript": (
            "Recruiter: Hi Kevin, um, Apex Staffing calling about the data entry temp role. "
            "What's your like data entry background?\n"
            "Candidate: Uh I did three years at DataForce, four hundred records a day, "
            "ninety nine point one percent accuracy on audits. Ten key around ninety five "
            "hundred KPH.\n"
            "Recruiter: Excel experience?\n"
            "Candidate: Yeah filters V lookups basic formulas I used excel for invoice "
            "verification daily.\n"
            "Recruiter: This is temp to perm ninety days two days on site in framingham. "
            "Full time okay?\n"
            "Candidate: Yes I'm between contracts I can start uh this thursday."
        ),
    },
    {
        "id": "ad-004",
        "vertical": "admin",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Office coordinator experience matches: facilities coordination, vendor management, "
            "Office suite, and multi-department scheduling. Strong temp-to-perm fit."
        ),
        "resume": (
            "Jennifer Walsh\nOffice Coordinator | 5 years\n\n"
            "Pinnacle Property Management — Office Coordinator (2019–2024)\n"
            "- Coordinated moves, supplies, and vendor contracts for 3 buildings\n"
            "- Managed shared Outlook calendars for 40-person staff\n"
            "- Processed AP invoices under $5K; tracked POs in Excel\n\n"
            "Skills: Office 365, SharePoint, multi-line phones, facilities\n"
            "Typing: 70 WPM"
        ),
        "job_description": (
            "Office Coordinator — Temp-to-Perm\n\n"
            "Client: Commercial real estate firm, Boston\n\n"
            "Responsibilities:\n"
            "- Office operations: supplies, mail, conference rooms\n"
            "- Vendor coordination and light AP processing\n"
            "- Support 50-person floor; 4-line phone backup\n\n"
            "Requirements:\n"
            "- 2+ years office coordinator or admin experience\n"
            "- Microsoft Office 365; Excel tracking\n"
            "- 60+ WPM; professional communication\n"
            "- On-site; 90-day temp-to-perm\n\n"
            "Pay: $24–27/hr"
        ),
        "transcript": (
            "Sarah (Recruiter): Jennifer, thanks for applying through Apex. This office "
            "coordinator role is temp-to-perm at a real estate client. What's your background?\n"
            "Candidate: I've coordinated office operations for five years at Pinnacle — "
            "vendor management, supply ordering, shared calendars for forty people, and "
            "light AP under five thousand dollars.\n"
            "Sarah (Recruiter): How are you with Excel and phones?\n"
            "Candidate: Excel for PO tracking and budgets. I cover a four-line system when "
            "reception is at lunch — seventy WPM typing.\n"
            "Sarah (Recruiter): Ninety-day temp then conversion. On-site in Boston Financial "
            "District. Start date?\n"
            "Candidate: Two weeks notice to my current employer, so the fifteenth works."
        ),
    },
    {
        "id": "ad-005",
        "vertical": "admin",
        "decision": "select",
        "difficulty": "borderline",
        "ingest_format": "asr_paragraph",
        "reason": (
            "AP experience is solid and QuickBooks matches client stack, but only 58 WPM "
            "typing is below the 60 WPM JD target. Recruiter advances given strong invoice "
            "volume history and temp-to-perm urgency."
        ),
        "resume": (
            "Robert Kim\nAccounts Payable Clerk | 4 years\n\n"
            "Summit Manufacturing — AP Clerk (2020–2024)\n"
            "- Processed 150+ invoices weekly in QuickBooks and Excel\n"
            "- Three-way match PO/receipt/invoice; vendor statement reconciliation\n"
            "- 58 WPM typing; 10-key 8,200 KPH\n\n"
            "Temp — AR clerk, construction firm (2019)\n\n"
            "Skills: QuickBooks, Excel, vendor relations"
        ),
        "job_description": (
            "AP/AR Clerk — Temp-to-Perm (90 days)\n\n"
            "Client: Mid-size manufacturer, Lowell MA\n\n"
            "Duties:\n"
            "- Accounts payable processing in QuickBooks\n"
            "- Invoice coding, check runs, vendor inquiries\n"
            "- Backup AR aging reports\n\n"
            "Requirements:\n"
            "- 2+ years AP or AR experience\n"
            "- QuickBooks Desktop; Excel\n"
            "- 60+ WPM typing preferred\n"
            "- On-site 5 days; temp-to-perm\n\n"
            "Pay: $22–25/hr"
        ),
        "transcript": (
            "recruiter hi robert calling from kelly about the ap clerk temp to perm in lowell "
            "walk me through your ap experience candidate four years at summit manufacturing "
            "processed about one fifty invoices a week in quickbooks three way matching vendor "
            "reconciliations recruiter typing and ten key candidate typing is fifty eight wpm "
            "ten key around eighty two hundred kph recruiter jd asks sixty wpm how do you "
            "feel about that candidate i am accurate on invoices rarely need corrections i can "
            "retest if needed recruiter client needs someone monday for ninety day temp with "
            "conversion candidate i can start monday i did a temp ar assignment through kelly "
            "before and i want perm this time"
        ),
    },
    {
        "id": "ad-006",
        "vertical": "admin",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": (
            "EA background with C-suite travel coordination, 70 WPM, and advanced Office. "
            "Bilingual Spanish is a plus for this client."
        ),
        "resume": (
            "Carmen Reyes\nExecutive Assistant | 6 years\n\n"
            "Vista Hospitality Group — EA to CEO (2018–2024)\n"
            "- International travel coordination; Concur expense reports\n"
            "- Board meeting logistics; PowerPoint presentations\n"
            "- Bilingual English/Spanish — translated correspondence\n\n"
            "Typing: 70 WPM | Skills: Office 365, Concur, Teams"
        ),
        "job_description": (
            "Executive Assistant — Temp-to-Perm\n\n"
            "Client: Hospitality management company, Miami\n\n"
            "Requirements:\n"
            "- 4+ years EA experience supporting senior leadership\n"
            "- Advanced Office; travel and expense systems\n"
            "- 65+ WPM; multi-line phone etiquette\n"
            "- Bilingual Spanish preferred\n"
            "- 90-day temp-to-perm; on-site\n\n"
            "Pay: $26–30/hr"
        ),
        "transcript": (
            "Recruiter: Carmen, Apex Staffing here. Executive assistant temp to perm in Miami. "
            "Tell me about supporting executives.\n"
            "Candidate: Six years EA to the CEO at Vista Hospitality. Travel on concur, board "
            "meetings, power point decks. I am bilingual english spanish.\n"
            "Recruiter: Typing in office?\n"
            "Candidate: Seventy WPM. Outlook excel word power point daily. I handled a ten "
            "line phone when admin was out.\n"
            "Recruiter: Ninety day temp then perm. On site five days.\n"
            "Candidate: Perfect I'm relocating to Miami anyway can start in ten days."
        ),
    },
    {
        "id": "ad-007",
        "vertical": "admin",
        "decision": "select",
        "difficulty": "borderline",
        "ingest_format": "labeled",
        "reason": (
            "Only 14 months reception experience vs 2-year ask, but high call volume and "
            "65 WPM typing are strong. Client agreed to interview given temp-to-perm pipeline."
        ),
        "resume": (
            "Ashley Nguyen\nReceptionist | 14 months\n\n"
            "Clearview Dental — Front Desk Receptionist (2023–2024)\n"
            "- 60+ daily calls on 4-line phone; patient scheduling\n"
            "- Insurance verification; Excel appointment reports\n"
            "- Typing: 65 WPM\n\n"
            "Part-time — Campus library desk (2021–2023)"
        ),
        "job_description": (
            "Receptionist — Temp-to-Perm\n\n"
            "Client: Law firm, suburban office\n\n"
            "Requirements:\n"
            "- 2+ years reception experience\n"
            "- Multi-line phone; Microsoft Office\n"
            "- 60+ WPM typing\n"
            "- Professional demeanor; client-facing\n"
            "- 90-day temp-to-perm\n\n"
            "Pay: $20–23/hr"
        ),
        "transcript": (
            "Recruiter: Ashley, I'm screening for a law firm receptionist temp-to-perm. "
            "Reception experience?\n"
            "Candidate: About fourteen months at Clearview Dental — sixty calls a day on a "
            "four-line system, scheduling, insurance checks. Before that part-time library desk.\n"
            "Recruiter: JD asks two years. Concern?\n"
            "Candidate: The dental office was high volume and professional. I type sixty-five "
            "WPM and I'm comfortable in Word and Excel for reports.\n"
            "Recruiter: Client is strict on phone manner. Comfortable with attorneys and clients?\n"
            "Candidate: Yes — I dealt with anxious patients daily. I stay calm and professional.\n"
            "Recruiter: I'll present you — ninety-day temp. Available?\n"
            "Candidate: Yes, I can start immediately."
        ),
    },
    {
        "id": "ad-008",
        "vertical": "admin",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": (
            "Exceeds data entry benchmarks: 10,200 KPH, Excel macros for QA, and prior "
            "temp-to-perm conversion through Apex."
        ),
        "resume": (
            "Lisa Park\nData Entry Clerk | 5 years\n\n"
            "National Benefits Admin — Senior Data Entry (2019–2024)\n"
            "- 10,200 KPH with 99.4% accuracy\n"
            "- Built Excel macros for duplicate flagging\n"
            "- Apex Staffing temp converted to perm in 2020\n\n"
            "Typing: 90 WPM | 10-key: 10,200 KPH"
        ),
        "job_description": (
            "Data Entry Clerk — Temp-to-Perm\n\n"
            "Client: Benefits administrator, hybrid 3 days on-site\n\n"
            "Requirements:\n"
            "- 2+ years high-volume data entry\n"
            "- 9,000+ KPH; 55+ WPM\n"
            "- Excel — formulas, basic automation a plus\n"
            "- Temp-to-perm 90 days\n\n"
            "Pay: $20–23/hr"
        ),
        "transcript": (
            "recruiter lisa this is apex staffing about the benefits data entry role you "
            "applied for tell me your volume and accuracy candidate five years at national "
            "benefits admin ten thousand two hundred kph ninety nine point four percent "
            "accuracy i built excel macros for duplicate checks recruiter you did a temp "
            "to perm with us before candidate yes in twenty twenty converted after ninety "
            "days recruiter this is similar hybrid three days on site temp ninety days "
            "candidate i know the workflow i can start next monday"
        ),
    },
    {
        "id": "ad-009",
        "vertical": "admin",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": (
            "Office coordinator with SharePoint, facilities, and AP backup. 68 WPM and "
            "confirmed on-site temp-to-perm availability."
        ),
        "resume": (
            "Thomas Greene\nOffice Coordinator | 4 years\n\n"
            "Harbor Tech Park — Office Coordinator (2020–2024)\n"
            "- SharePoint document libraries; room booking across 2 floors\n"
            "- Facilities tickets; vendor escort; safety drill coordination\n"
            "- AP backup: coded invoices in QuickBooks\n\n"
            "Typing: 68 WPM | Office 365, SharePoint"
        ),
        "job_description": (
            "Office Coordinator — Temp-to-Perm\n\n"
            "Client: Tech campus, Cambridge\n\n"
            "Duties:\n"
            "- Floor operations, SharePoint, meeting support\n"
            "- Light AP; supply budgets in Excel\n"
            "- Phone backup on 6-line system\n\n"
            "Requirements:\n"
            "- 2+ years office coordinator experience\n"
            "- Office 365 / SharePoint\n"
            "- 60+ WPM; on-site; 90-day temp-to-perm\n\n"
            "Pay: $25–28/hr"
        ),
        "transcript": (
            "Recruiter: Thomas, um, Kelly Services, office coordinator temp to perm cambridge. "
            "Your coordinator background?\n"
            "Candidate: Four years at harbor tech park sharepoint room booking facilities "
            "vendor escort ap backup in quickbooks.\n"
            "Recruiter: Typing?\n"
            "Candidate: Sixty eight WPM excel for supply budgets.\n"
            "Recruiter: On site five days ninety day temp.\n"
            "Candidate: Yes I am leaving due to relocation within cambridge so timing is good."
        ),
    },
    {
        "id": "ad-010",
        "vertical": "admin",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Strong AR/AP hybrid: collections experience, QuickBooks, 62 WPM, and clean "
            "attendance. Matches manufacturer client needs."
        ),
        "resume": (
            "Patricia Olson\nAP/AR Clerk | 6 years\n\n"
            "Northline Distributors — AR Specialist (2018–2024)\n"
            "- Managed aging reports; collection calls on past-due accounts\n"
            "- AP backup: 100+ weekly invoices in QuickBooks\n"
            "- Excel pivot tables for cash application\n\n"
            "Typing: 62 WPM | QuickBooks Desktop, Excel"
        ),
        "job_description": (
            "AP/AR Clerk — Temp-to-Perm (90 days)\n\n"
            "Client: Wholesale distributor, Nashua NH\n\n"
            "Requirements:\n"
            "- 3+ years AP or AR experience\n"
            "- QuickBooks; Excel pivot tables\n"
            "- 55+ WPM; phone follow-up on AR\n"
            "- On-site; temp-to-perm\n\n"
            "Pay: $23–26/hr"
        ),
        "transcript": (
            "Recruiter: Patricia, Apex Staffing — AP/AR temp-to-perm in Nashua. Walk me "
            "through AR and AP.\n"
            "Candidate: Six years at Northline — primary AR aging, collection calls, cash "
            "application in Excel pivots. AP backup, hundred invoices a week in QuickBooks.\n"
            "Recruiter: Typing and phone work on collections?\n"
            "Candidate: Sixty-two WPM. I'm professional on collection calls — firm but "
            "respectful. Multi-line phone at the office.\n"
            "Recruiter: Ninety-day temp, on-site. Start?\n"
            "Candidate: I can start in one week. Looking for perm after a successful temp."
        ),
    },
    {
        "id": "ad-011",
        "vertical": "admin",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": (
            "Executive assistant applicant lacks calendar management depth and advanced Excel. "
            "45 WPM typing is well below 65 WPM requirement. No multi-line phone experience."
        ),
        "resume": (
            "Gregory Mills\nAdministrative Assistant | 1 year\n\n"
            "Small retail office — Admin Assistant (2023–2024)\n"
            "- Filed papers; occasional Word letters\n"
            "- Single-line phone only\n"
            "- Typing: 45 WPM\n\n"
            "No executive support or travel coordination listed"
        ),
        "job_description": (
            "Executive Assistant — Temp-to-Perm\n\n"
            "Client: Private equity firm\n\n"
            "Requirements:\n"
            "- 3+ years EA experience with C-suite support\n"
            "- Advanced Outlook calendaring; Excel, PowerPoint\n"
            "- 65+ WPM typing\n"
            "- Multi-line phone; on-site; 90-day temp-to-perm\n\n"
            "Pay: $30–35/hr"
        ),
        "transcript": (
            "recruiter gregory kelly services screening executive assistant temp to perm "
            "tell me about supporting executives candidate i was admin assistant at a small "
            "retail office for a year filed papers typed letters in word single phone line "
            "recruiter calendar management travel excel candidate not really travel was "
            "handled by the owner i did basic filing recruiter typing speed candidate forty "
            "five wpm recruiter role needs sixty five plus and multi line experience "
            "candidate i could learn recruiter client needs day one readiness thanks for your "
            "time we will not move forward"
        ),
    },
    {
        "id": "ad-012",
        "vertical": "admin",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": (
            "Receptionist candidate has no multi-line phone experience and 48 WPM typing "
            "fails 60 WPM minimum. Schedule conflict: can only work afternoons."
        ),
        "resume": (
            "Samantha Cole\nReceptionist (seeking)\n\n"
            "Coffee shop — Barista (2022–2024)\n"
            "- Customer service; cash register\n"
            "- No office or phone system experience\n\n"
            "Typing: 48 WPM (self-reported)"
        ),
        "job_description": (
            "Receptionist — Temp-to-Perm\n\n"
            "Client: Accounting firm\n\n"
            "Requirements:\n"
            "- 2+ years reception experience\n"
            "- Multi-line phone system required\n"
            "- 60+ WPM; Microsoft Office\n"
            "- Full-day on-site coverage 8:30–5:00\n"
            "- 90-day temp-to-perm\n\n"
            "Pay: $19–22/hr"
        ),
        "transcript": (
            "Recruiter: Samantha, Apex, receptionist temp to perm. Office experience?\n"
            "Candidate: Um I was a barista for two years great with customers but no office "
            "yet.\n"
            "Recruiter: Multi line phone?\n"
            "Candidate: No just cafe register.\n"
            "Recruiter: Typing WPM?\n"
            "Candidate: Like forty eight I think.\n"
            "Recruiter: Full day eight thirty to five on site?\n"
            "Candidate: I can only do afternoons I have morning classes.\n"
            "Recruiter: Client needs full coverage. We'll pass for now."
        ),
    },
    {
        "id": "ad-013",
        "vertical": "admin",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Data entry applicant's 6,200 KPH is far below 8,500 KPH requirement. Accuracy "
            "issues cited at last role (96.2%). No Excel beyond basic entry."
        ),
        "resume": (
            "Brian Hutchins\nData Entry | 8 months\n\n"
            "QuickTemp Agency — Data Entry (2023–2024)\n"
            "- Manual entry in proprietary system\n"
            "- 6,200 KPH; 96.2% accuracy on review\n"
            "- Minimal Excel use\n\n"
            "Typing: 42 WPM"
        ),
        "job_description": (
            "Data Entry Clerk — Temp-to-Perm\n\n"
            "Client: Healthcare claims processor\n\n"
            "Requirements:\n"
            "- 1+ years data entry\n"
            "- 8,500+ KPH ten-key; 55+ WPM\n"
            "- Excel filters and formulas\n"
            "- 99%+ accuracy standard\n"
            "- Temp-to-perm 90 days\n\n"
            "Pay: $18–20/hr"
        ),
        "transcript": (
            "Recruiter: Brian, screening for data entry temp-to-perm. Volume and accuracy?\n"
            "Candidate: Eight months through QuickTemp. About 6,200 KPH. Accuracy was 96.2% "
            "on my last audit — they said I needed to improve.\n"
            "Recruiter: Excel?\n"
            "Candidate: Basic typing into cells. I don't know formulas.\n"
            "Recruiter: This client requires 8,500 KPH and 99% accuracy day one.\n"
            "Candidate: I could try to get faster.\n"
            "Recruiter: We need someone who already meets the benchmark. I'll keep your "
            "profile for lighter-volume roles."
        ),
    },
    {
        "id": "ad-014",
        "vertical": "admin",
        "decision": "reject",
        "difficulty": "borderline",
        "ingest_format": "asr_paragraph",
        "reason": (
            "Office coordinator has relevant title but frequent job changes (4 roles in 3 years) "
            "and attendance write-ups at last assignment. Client requires stable tenure for "
            "temp-to-perm conversion."
        ),
        "resume": (
            "Nicole Bradshaw\nOffice Coordinator | 3 years (4 employers)\n\n"
            "Various — Office Coordinator temps (2021–2024)\n"
            "- Short assignments: 3–8 months each\n"
            "- Last role ended after attendance warning\n"
            "- Skills: Office, phones, data entry\n"
            "- Typing: 64 WPM"
        ),
        "job_description": (
            "Office Coordinator — Temp-to-Perm\n\n"
            "Client: Stable corporate HQ\n\n"
            "Requirements:\n"
            "- 2+ years office coordinator experience\n"
            "- Microsoft Office; reliable attendance\n"
            "- 60+ WPM; multi-line phone backup\n"
            "- 90-day temp-to-perm with conversion focus\n\n"
            "Pay: $23–26/hr"
        ),
        "transcript": (
            "recruiter nicole apex staffing office coordinator temp to perm you have several "
            "short assignments why candidate offices downsized or contract ended last one i "
            "had an attendance warning three tardies in six weeks recruiter this client "
            "converts temps who show stability ninety days solid attendance candidate i "
            "understand i had car trouble recruiter skills wise office and typing candidate "
            "sixty four wpm excel outlook four line phone backup at the last site recruiter "
            "i am concerned about the pattern and attendance we will not submit for this "
            "conversion focused role"
        ),
    },
    {
        "id": "ad-015",
        "vertical": "admin",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": (
            "AP clerk has only retail cash-handling, no QuickBooks or invoice processing. "
            "Cannot describe three-way match. Not qualified for AP temp-to-perm."
        ),
        "resume": (
            "Derek Lawson\nRetail Associate\n\n"
            "BigBox Store — Cashier / Floor (2020–2024)\n"
            "- Cash handling; customer service\n"
            "- No AP, AR, or accounting software\n\n"
            "Typing: 50 WPM"
        ),
        "job_description": (
            "AP/AR Clerk — Temp-to-Perm\n\n"
            "Client: Manufacturing AP department\n\n"
            "Requirements:\n"
            "- 2+ years AP experience\n"
            "- QuickBooks Desktop; three-way match\n"
            "- 55+ WPM; vendor communication\n"
            "- On-site; 90-day temp-to-perm\n\n"
            "Pay: $22–25/hr"
        ),
        "transcript": (
            "Recruiter: Derek, Kelly, AP clerk temp to perm. AP background?\n"
            "Candidate: I was cashier at bigbox four years good with money counts.\n"
            "Recruiter: Quick books invoices three way match?\n"
            "Candidate: Uh what is three way match? I never used quickbooks.\n"
            "Recruiter: Vendor statements excel coding?\n"
            "Candidate: No office accounting just register.\n"
            "Recruiter: This is not an entry level role. We will not proceed."
        ),
    },
    {
        "id": "ad-016",
        "vertical": "admin",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "EA applicant requires fully remote work; client mandates on-site 5 days for "
            "temp-to-perm. Also lacks PowerPoint and board-meeting support experience."
        ),
        "resume": (
            "Helen Cho\nVirtual Assistant | 2 years\n\n"
            "Freelance — Remote VA (2022–2024)\n"
            "- Email management; social media scheduling\n"
            "- Remote only; no in-office executive support\n"
            "- Typing: 60 WPM\n\n"
            "No PowerPoint or board logistics listed"
        ),
        "job_description": (
            "Executive Assistant — Temp-to-Perm\n\n"
            "Client: Investment office, on-site required\n\n"
            "Requirements:\n"
            "- 3+ years in-office EA experience\n"
            "- Outlook, Excel, PowerPoint; board materials\n"
            "- Multi-line phone; visitor reception\n"
            "- On-site 5 days; 90-day temp-to-perm\n\n"
            "Pay: $28–32/hr"
        ),
        "transcript": (
            "Recruiter: Helen, Apex Staffing — executive assistant temp-to-perm in Boston. "
            "Your EA experience?\n"
            "Candidate: I've been a freelance virtual assistant two years — email, scheduling, "
            "social posts. All remote.\n"
            "Recruiter: In-office support? Board decks, PowerPoint, greeting visitors?\n"
            "Candidate: I haven't done board meetings or PowerPoint. I prefer remote only.\n"
            "Recruiter: This client is five days on-site with conversion after ninety days.\n"
            "Candidate: I can't commute daily. Remote is a must for me.\n"
            "Recruiter: That's a hard mismatch. We won't submit your profile."
        ),
    },
    {
        "id": "ad-017",
        "vertical": "admin",
        "decision": "reject",
        "difficulty": "borderline",
        "ingest_format": "asr_paragraph",
        "reason": (
            "Receptionist meets typing (61 WPM) but has two no-call no-shows in last role. "
            "Law firm client has zero tolerance for attendance risk on temp-to-perm front desk."
        ),
        "resume": (
            "Rachel Dunn\nReceptionist | 2 years\n\n"
            "Westside Insurance — Receptionist (2022–2024)\n"
            "- 6-line phone; Outlook scheduling\n"
            "- Left after NCNS incidents (2) during final month\n"
            "- Typing: 61 WPM\n\n"
            "Skills: Office, multi-line phones"
        ),
        "job_description": (
            "Receptionist — Temp-to-Perm\n\n"
            "Client: Law firm, front desk\n\n"
            "Requirements:\n"
            "- 2+ years reception\n"
            "- Multi-line phone; 60+ WPM\n"
            "- Impeccable attendance — client converts temps at 90 days\n"
            "- Microsoft Office\n\n"
            "Pay: $21–24/hr"
        ),
        "transcript": (
            "recruiter rachel kelly services law firm receptionist temp to perm experience "
            "candidate two years westside insurance six line phone outlook sixty one wpm "
            "recruiter why did you leave candidate there were two no call no shows in my last "
            "month family emergency and a miscommunication recruiter client converts only temps "
            "with perfect attendance ninety days candidate i am reliable now recruiter law "
            "firm front desk cannot risk coverage gaps i cannot submit given the ncns history"
        ),
    },
    {
        "id": "ad-018",
        "vertical": "admin",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": (
            "Data entry candidate refuses on-site days required for temp-to-perm. WPM and KPH "
            "meet standards but hybrid policy is non-negotiable for client."
        ),
        "resume": (
            "Amanda Price\nData Entry Specialist | 3 years\n\n"
            "Remote Data Services — Data Entry (2021–2024)\n"
            "- 9,800 KPH; 99% accuracy; fully remote\n"
            "- Excel VLOOKUP, filters\n"
            "- Typing: 78 WPM\n\n"
            "No on-site office experience"
        ),
        "job_description": (
            "Data Entry Clerk — Temp-to-Perm\n\n"
            "Client: Insurance processor — 3 days on-site required\n\n"
            "Requirements:\n"
            "- 2+ years data entry\n"
            "- 9,000+ KPH; Excel\n"
            "- Must work 3 days on-site (Framingham)\n"
            "- 90-day temp-to-perm\n\n"
            "Pay: $20–22/hr"
        ),
        "transcript": (
            "Recruiter: Amanda, Apex, data entry temp to perm. Your stats?\n"
            "Candidate: Ninety eight hundred KPH ninety nine percent accuracy seventy eight "
            "WPM all remote last three years.\n"
            "Recruiter: Client needs three days on site framingham for ninety day temp.\n"
            "Candidate: I only work from home I won't do on site.\n"
            "Recruiter: That's required for security and training.\n"
            "Candidate: Then it's not for me.\n"
            "Recruiter: Agreed we will not move forward."
        ),
    },
    {
        "id": "ad-019",
        "vertical": "admin",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Office coordinator lacks SharePoint and Excel budget tracking required by client. "
            "Only word processing experience from home office setup."
        ),
        "resume": (
            "Janet Fowler\nHome Office Assistant | 1 year\n\n"
            "Self-employed — Home office (2023–2024)\n"
            "- Personal Word documents and printing\n"
            "- No SharePoint, facilities, or vendor coordination\n"
            "- Typing: 55 WPM\n\n"
            "No corporate office coordinator experience"
        ),
        "job_description": (
            "Office Coordinator — Temp-to-Perm\n\n"
            "Client: 80-person corporate floor\n\n"
            "Requirements:\n"
            "- 2+ years office coordinator in corporate setting\n"
            "- SharePoint, Excel budget tracking\n"
            "- Vendor and facilities coordination\n"
            "- 60+ WPM; 90-day temp-to-perm\n\n"
            "Pay: $24–27/hr"
        ),
        "transcript": (
            "Recruiter: Janet, screening office coordinator temp-to-perm. Corporate coordinator "
            "background?\n"
            "Candidate: I ran a home office for a year — Word documents, organizing files, "
            "printing labels.\n"
            "Recruiter: SharePoint, vendor management, Excel budgets?\n"
            "Candidate: I haven't used SharePoint or managed vendors. Basic Word only.\n"
            "Recruiter: Typing?\n"
            "Candidate: Fifty-five WPM.\n"
            "Recruiter: We need corporate floor experience and sixty-plus WPM. I'll pass "
            "on this submission."
        ),
    },
    {
        "id": "ad-020",
        "vertical": "admin",
        "decision": "reject",
        "difficulty": "borderline",
        "ingest_format": "asr_noisy",
        "reason": (
            "AP clerk has QuickBooks exposure but only 11 months AP and 52 WPM. Borderline "
            "skills; rejected because client requires 2+ years AP for temp-to-perm conversion "
            "and candidate cannot start for six weeks."
        ),
        "resume": (
            "Victor Ramos\nAP Clerk | 11 months\n\n"
            "Local HVAC contractor — AP Clerk (2023–2024)\n"
            "- QuickBooks invoice entry ~40/week\n"
            "- 52 WPM; learning three-way match\n"
            "- Gaps in employment before this role\n\n"
            "Skills: QuickBooks (basic), Excel entry"
        ),
        "job_description": (
            "AP/AR Clerk — Temp-to-Perm (90 days)\n\n"
            "Client: Distributor AP team\n\n"
            "Requirements:\n"
            "- 2+ years AP experience\n"
            "- QuickBooks; three-way match proficient\n"
            "- 55+ WPM; start within 2 weeks\n"
            "- On-site; temp-to-perm\n\n"
            "Pay: $22–25/hr"
        ),
        "transcript": (
            "Recruiter: Victor, Kelly, AP temp to perm. How much AP experience?\n"
            "Candidate: Eleven months at hvac contractor quickbooks maybe forty invoices a "
            "week still learning three way match.\n"
            "Recruiter: Two years required for this conversion track. Typing?\n"
            "Candidate: Fifty two wpm.\n"
            "Recruiter: Start date client wants within two weeks?\n"
            "Candidate: I need six weeks notice at my job uh side gig.\n"
            "Recruiter: Experience and timing don't fit. We will not submit."
        ),
    },
]

assert len(ADMIN_RECORDS) == 20
assert sum(1 for r in ADMIN_RECORDS if r["decision"] == "select") == 10
assert sum(1 for r in ADMIN_RECORDS if r["decision"] == "reject") == 10
