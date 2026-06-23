"""Call center vertical — staffing-agency phone screen eval records."""

from __future__ import annotations

CALL_CENTER_RECORDS: list[dict] = [
    {
        "id": "cc-001",
        "vertical": "call_center",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": "Three years inbound utilities support, Salesforce daily use, QA 90%+, confirmed rotating weekend availability and on-site training start date.",
        "resume": "Daniela Ruiz\nCustomer Service Representative | 3 years call center\n\nCenterPoint Energy — Inbound CSR (2022–2025)\n- Handled billing, outage, and payment arrangement calls\n- AHT 4:45 avg on 200+ call monthly reviews\n- QA scores 91–94% last four quarters\n- Salesforce Service Cloud case notes and disposition codes\n\nH-E-B — Courtesy clerk (2020–2022)\n\nSkills: Salesforce, de-escalation, bilingual English/Spanish\nTyping: 72 WPM | Schedule: open to rotating weekends",
        "job_description": "Inbound Customer Service — Utilities Campaign\n\nResponsibilities:\n- Answer inbound calls for billing, service start/stop, and outage status\n- Document interactions in Salesforce with accurate disposition codes\n- Meet AHT target of 5:30 and monthly QA minimum of 85%\n\nRequirements:\n- 2+ years inbound call center (utilities or telecom preferred)\n- Salesforce or comparable CRM experience\n- Rotating weekends required after 4-week on-site training\n- Professional phone manner, typing 45+ WPM\n\nLocation: Houston TX — hybrid training then WFH | Pay: $17.50–19/hr",
        "transcript": (
            "Recruiter: Hi Daniela, this is Sarah with Apex Staffing. I'm screening for an inbound utilities customer service role. Can you walk me through your call center background?\n"
            "Candidate: Sure. I've been at CenterPoint Energy for almost three years on inbound billing and outage lines. We use Salesforce for every call — cases, notes, disposition codes.\n"
            "Recruiter: What are your handle time and QA numbers?\n"
            "Candidate: My AHT runs about four forty-five. QA has been between ninety-one and ninety-four the last four quarters.\n"
            "Recruiter: This client requires rotating weekends after a four-week on-site training block. Any conflicts?\n"
            "Candidate: No — my husband works weekdays so I already cover every other weekend. I can start training March third if selected."
        ),
    },
    {
        "id": "cc-002",
        "vertical": "call_center",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": "Two years third-party collections with FDCPA training, stable QA above 88%, comfortable with dialer workflows and Saturday rotation.",
        "resume": "Marcus Webb\nCollections Representative\n\nNationwide Credit Services — Collections Agent (2023–2025)\n- Outbound and inbound collections on medical and utility portfolios\n- FDCPA and state mini-Miranda compliance training (annual)\n- QA 88–91%, RPC rate top quartile on team\n- Experian dialer, Salesforce collections module\n\nWalmart — Customer service desk (2021–2023)\n\nEducation: Associate degree, Business Administration\nAvailable: Saturdays required — no conflict",
        "job_description": "Collections Agent — Third-Party Agency\n\nRequirements:\n- 1+ years collections call center experience\n- FDCPA familiarity and compliant call scripting\n- Comfortable with outbound dialer and inbound callback queues\n- Saturday rotation mandatory\n- QA minimum 85%, attendance policy strict\n\nMetrics: RPC and promise-to-pay tracked weekly\nCRM: Salesforce Collections Cloud\nShift: Mon–Fri plus 2 Saturdays/month | On-site Nashville TN",
        "transcript": (
            "Thanks for taking my call Marcus this is Apex Staffing screening for a collections role with a third party agency.\n\n"
            "I've been at Nationwide Credit Services about two years outbound and inbound on medical and utility debt. We do FDCPA training every year and I follow the mini-Miranda script every call.\n\n"
            "What kind of QA are you running? Usually eighty-eight to ninety-one percent on my scorecards. I'm on Experian dialer and we log everything in Salesforce collections.\n\n"
            "Saturdays are required two per month. That works for me my kids are with their mom every other weekend so I'm actually looking for Saturday hours.\n\n"
            "When could you start? I can do a face to face Wednesday and start the following Monday."
        ),
    },
    {
        "id": "cc-003",
        "vertical": "call_center",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": "Eighteen months tier 1 tech support with Zendesk and Salesforce, AHT under target, confirmed rotating schedule and headset/WFH setup after training.",
        "resume": "Aisha Patel\nTechnical Support Representative — Tier 1\n\nTP — ISP Support Tier 1 (2024–2025)\n- Troubleshoot modem, router, and Wi-Fi connectivity issues\n- AHT 7:20 vs 8:00 team target\n- QA 89% average, first-call resolution 78%\n- Zendesk tickets, Salesforce customer history lookup\n\nBest Buy — Geek Squad agent (2022–2024)\n\nHome office: wired ethernet, noise-canceling headset, backup LTE hotspot",
        "job_description": "Tech Support Tier 1 — Internet Service Provider\n\nRequirements:\n- 1+ years phone-based technical support\n- Tier 1 troubleshooting: connectivity, modem reset, account verification\n- CRM: Salesforce; ticketing familiarity required\n- AHT target 8:00, QA minimum 85%\n- Rotating evenings and every third weekend\n- Four weeks on-site training, then WFH with company VPN\n\nMust pass background check and equipment audit",
        "transcript": (
            "um hi this is Sarah from Apex Staffing calling about the tier one tech support opening you applied for.\n\n"
            "yeah I've been at TP about eighteen months on tier one ISP support modems routers Wi-Fi stuff. we use Zendesk for tickets and Salesforce for customer history.\n\n"
            "what's your average handle time? uh around seven twenty team target is eight minutes. QA I'm usually like eighty-nine percent first call resolution high seventies.\n\n"
            "schedule is rotating evenings and every third weekend. that's fine I did swing at Best Buy before this.\n\n"
            "training is four weeks on site then work from home. I've got wired ethernet a good headset backup hotspot ready for the equipment check."
        ),
    },
    {
        "id": "cc-004",
        "vertical": "call_center",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": "Four years tier 2 escalation experience, strong Salesforce case ownership, meets weekend rotation and can mentor tier 1 agents during ramp.",
        "resume": "Robert Kim\nTechnical Support — Tier 2\n\nAT&T — Tier 2 Broadband Support (2021–2025)\n- Escalations from tier 1: provisioning, outage triage, CPE replacement\n- AHT 11:30, QA 93% trailing twelve months\n- Salesforce case owner through resolution, coached 4 new hires\n- Weekend on-call rotation every third week\n\nU.S. Army — IT specialist (2017–2021)\n\nCertifications: CompTIA Network+, ITIL Foundation",
        "job_description": "Tech Support Tier 2 — Telecom Client\n\nRequirements:\n- 3+ years tier 2 phone support (broadband or mobile)\n- Salesforce advanced case management\n- Escalation documentation and root-cause notes\n- Weekend rotation every third week\n- QA minimum 90%, AHT target 12:00\n\nPreferred: mentoring experience, Network+ or equivalent\nOn-site: Plano TX | Pay: $24–27/hr",
        "transcript": (
            "Sarah: Robert, thanks for picking up. This is tier two broadband support for our telecom client. Tell me about your escalation experience.\n"
            "Candidate: Four years at AT&T tier two — provisioning failures, outage triage, CPE swaps. I own cases end to end in Salesforce until resolution.\n"
            "Sarah: Metrics and schedule?\n"
            "Candidate: AHT around eleven thirty, QA ninety-three percent last twelve months. I'm on weekend rotation every third week already — no issue continuing that.\n"
            "Sarah: Any mentoring?\n"
            "Candidate: I coached four tier one hires last year on documentation standards. Happy to help during ramp if you need it."
        ),
    },
    {
        "id": "cc-005",
        "vertical": "call_center",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": "Two years inbound utilities campaign, no sales baggage, CRM experience, partner covers opposite weekends for childcare — schedule fit confirmed.",
        "resume": "James Okonkwo\nCustomer Service Representative\n\nComcast — Tier 2 Support (2021–2023)\n- 88–92% QA scores\n- AHT 6:10 avg\n- Handled 60+ calls/day peak\n\nRetail — Best Buy mobile (2019–2021)\n\nSkills: CRM (Salesforce), de-escalation, typing 65 WPM\nSchedule: rotating weekends — childcare covered",
        "job_description": "Inbound Customer Service — Utilities Campaign\n\nRequirements:\n- 2+ years call center experience\n- CRM familiarity (Salesforce preferred)\n- Rotating weekends required\n- Empathy and clear communication\n- No sales quota — support only\n\nShift: Tue–Sat rotating | WFH after 6-week training\nAHT target: 6:00 | QA minimum: 85%",
        "transcript": (
            "Hi James this is Apex Staffing screening for an inbound utilities customer service campaign.\n\n"
            "I did two years at Comcast handling billing and tech support tiers one and two. AHT around six ten QA usually eighty-eight to ninety-two.\n\n"
            "This campaign is inbound only no sales. Comfortable with that? Yes I prefer support over hard sales honestly.\n\n"
            "Schedule is rotating weekends. OK? I have childcare covered every other weekend my partner works opposite weekends so we're good.\n\n"
            "CRM experience? Salesforce at Comcast for customer history and case notes. I can start after giving two weeks notice so roughly the eighteenth."
        ),
    },
    {
        "id": "cc-006",
        "vertical": "call_center",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": "Prior WFH call center role with documented QA, secure home office passes client checklist, available for two-week on-site training then remote.",
        "resume": "Nicole Foster\nRemote Customer Service Agent\n\nLiveOps — WFH Customer Support (2023–2025)\n- Inbound order status and warranty calls for retail client\n- QA 90–92%, AHT 5:15 on 100% remote queue\n- Salesforce Lightning, dual monitors, wired connection\n\nVerizon — Retail sales (2021–2023)\n\nHome office: dedicated room, door lock, 100 Mbps fiber, UPS backup",
        "job_description": "WFH Inbound Customer Service — After Training\n\nRequirements:\n- 1+ years phone customer service\n- Prior WFH call center experience strongly preferred\n- Home office: private room, wired internet 50+ Mbps, company VPN compatible\n- Two-week on-site training in Phoenix AZ (travel stipend provided)\n- Salesforce proficiency\n- Rotating weekends once remote\n\nQA minimum 85% | AHT target 5:30",
        "transcript": (
            "hi Nicole Sarah with Apex Staffing about the work from home customer service role.\n\n"
            "I spent two years at LiveOps fully remote inbound order status and warranty calls. QA was ninety to ninety-two AHT about five fifteen.\n\n"
            "client needs two weeks on site training in Phoenix then remote. can you do that? yeah I did on boarding in person at LiveOps too no problem.\n\n"
            "home office setup? dedicated room with a door hundred meg fiber wired not Wi-Fi dual monitors UPS backup passed their equipment audit before.\n\n"
            "weekends once you're remote? rotating weekends work I've done that schedule remote already."
        ),
    },
    {
        "id": "cc-007",
        "vertical": "call_center",
        "decision": "select",
        "difficulty": "borderline",
        "ingest_format": "labeled",
        "reason": "QA dipped to 82% last quarter after system migration but strong de-escalation references and bilingual skills; recruiter advancing for client interview given utilities Spanish call volume.",
        "resume": "Elena Morales\nBilingual Customer Service Representative\n\nCity Public Utilities — CSR (2023–2025)\n- Billing and payment plan calls English and Spanish\n- QA 82–88% (dip during CRM migration Q3 2024)\n- AHT 5:50, customer satisfaction 4.6/5 on post-call surveys\n- Salesforce Service Cloud\n\nGap explanation: CRM migration training period — scores recovered to 88% Q4",
        "job_description": "Inbound Customer Service — Municipal Utilities\n\nRequirements:\n- 1+ years call center customer service\n- Bilingual Spanish strongly preferred\n- Salesforce experience\n- QA minimum 85% (flex for strong bilingual pipeline)\n- Weekend rotation 1 in 4\n\nAHT target: 6:00 | On-site San Antonio TX",
        "transcript": (
            "Recruiter: Elena, I'm Sarah with Apex. This utilities client wants bilingual CSRs. Walk me through your background.\n"
            "Candidate: Two years at City Public Utilities billing and payment plans in English and Spanish. Salesforce every call.\n"
            "Recruiter: QA scores?\n"
            "Candidate: Honestly they dipped to eighty-two during our CRM migration last summer but I finished Q4 at eighty-eight. Surveys stayed at four six out of five.\n"
            "Recruiter: Weekend rotation one in four weeks.\n"
            "Candidate: That works — my mother watches my daughter on weekends when I'm scheduled."
        ),
    },
    {
        "id": "cc-008",
        "vertical": "call_center",
        "decision": "select",
        "difficulty": "borderline",
        "ingest_format": "asr_paragraph",
        "reason": "Only eleven months formal collections but six months high-volume inbound billing at utility company; FDCPA course completed, coachable tone — client agreed to consider for junior collector track.",
        "resume": "Tyrone Jackson\nCustomer Service / Collections Trainee\n\nRegional Water Authority — Billing CSR (2024–2025)\n- Inbound shutoff prevention and payment arrangement calls\n- Soft collections scripting, no formal dialer yet\n- QA 86%, AHT 6:30\n\nCoursera — FDCPA Compliance Certificate (2024)\n\nPrior: Target — electronics associate (2022–2024)",
        "job_description": "Junior Collections Agent — Utility Portfolios\n\nRequirements:\n- 6+ months call center OR collections exposure\n- FDCPA awareness training (course acceptable if no agency tenure)\n- Willingness to transition to outbound dialer after 90 days\n- Saturday rotation\n- QA minimum 85%\n\nCRM: Salesforce | Training provided on Experian dialer",
        "transcript": (
            "Tyrone thanks for calling back this is Apex Staffing on the junior collections opening.\n\n"
            "I don't have a full year at a collections agency yet. I've been eleven months at Regional Water Authority on inbound billing and shutoff prevention calls payment arrangements that kind of soft collections.\n\n"
            "FDCPA training? I completed a Coursera FDCPA compliance course and we follow scripts at the water authority for past due accounts.\n\n"
            "This role moves to outbound dialer after ninety days. I'm open to that I want to grow into real collections work.\n\n"
            "Saturdays? Yes I can do the rotation. QA at the authority is eighty-six percent."
        ),
    },
    {
        "id": "cc-009",
        "vertical": "call_center",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": "Tier 1 ISP support with AHT and QA above target, Salesforce daily, clean attendance — straightforward fit for campaign start.",
        "resume": "Christopher Nguyen\nTechnical Support Representative\n\nSpectrum — Tier 1 Support (2023–2025)\n- Modem provisioning, outage tickets, account verification\n- AHT 6:45 vs 7:30 target\n- QA 91% trailing six months\n- Salesforce and Remedy ticket integration\n\nSchedule: available rotating weekends and one evening shift weekly",
        "job_description": "Tech Support Tier 1 — Cable/Internet Client\n\nRequirements:\n- 1+ years tier 1 phone technical support\n- Salesforce case documentation\n- AHT target 7:30, QA minimum 85%\n- Rotating weekends and one weeknight shift\n- On-site Charlotte NC — no WFH for first year\n\nBackground check required",
        "transcript": (
            "Christopher hi this is Sarah Apex Staffing tier one tech support screening.\n\n"
            "two years Spectrum tier one modems outages account verification. Salesforce and Remedy for tickets.\n\n"
            "handle time and QA? AHT six forty-five target is seven thirty. QA ninety-one percent last six months.\n\n"
            "this is on site Charlotte no remote first year. that's actually what I want I'm tired of WFH isolation.\n\n"
            "weekends and a weeknight? rotating weekends plus one evening shift works fine no attendance issues ever."
        ),
    },
    {
        "id": "cc-010",
        "vertical": "call_center",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": "Utilities inbound veteran with Salesforce, meets AHT/QA bars, confirmed WFH setup post six-week training and rotating Sat schedule.",
        "resume": "Angela Brooks\nUtilities Customer Service Specialist\n\nDuke Energy — Inbound CSR (2020–2025)\n- High-bill investigations, payment extensions, service transfers\n- AHT 5:20, QA 92–95%\n- Salesforce Service Cloud power user\n- Trained new hires on disposition codes\n\nHome office certified for prior storm overflow WFH pilot",
        "job_description": "Utilities Campaign — Inbound CSR (WFH After Training)\n\nRequirements:\n- 2+ years utilities or telecom inbound experience\n- Salesforce required\n- AHT 5:45 max, QA 88% minimum\n- Six-week on-site training Raleigh NC then WFH\n- Rotating Saturdays once remote\n\nEquipment stipend after hire",
        "transcript": (
            "Sarah: Angela, Apex Staffing calling about the Duke-area utilities campaign — WFH after training.\n"
            "Candidate: I've been five years at Duke Energy inbound — high bills, extensions, transfers. Salesforce is my daily tool.\n"
            "Sarah: Numbers?\n"
            "Candidate: AHT five twenty, QA ninety-two to ninety-five. I helped train new hires on disposition codes last year.\n"
            "Sarah: Six weeks on-site in Raleigh then remote with rotating Saturdays.\n"
            "Candidate: I did their storm overflow WFH pilot — home office already certified. I can start training April seventh."
        ),
    },
    {
        "id": "cc-011",
        "vertical": "call_center",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": "No call center experience — only fast food and retail floor work; cannot meet 2+ years inbound requirement or CRM familiarity.",
        "resume": "Brandon Lewis\nFood Service / Retail\n\nChick-fil-A — Team member (2023–2025)\n- Drive-thru headset, cash handling\n- No phone queue or CRM experience\n\nWalmart — Stock associate (2021–2023)\n\nEducation: High school diploma\nSeeking first office job",
        "job_description": "Inbound Customer Service — Utilities Campaign\n\nRequirements:\n- 2+ years call center experience (mandatory)\n- CRM familiarity — Salesforce preferred\n- Rotating weekends required\n- AHT and QA metrics track record\n\nNo retail-only floor experience substitute",
        "transcript": (
            "Hi Brandon this is Apex Staffing about the inbound utilities customer service role you applied for.\n\n"
            "I've mostly worked fast food and stocking at Walmart. Chick-fil-A drive-thru I wore a headset but it's not the same as a call queue.\n\n"
            "Any formal call center or CRM? Not really. I've never used Salesforce. I type okay maybe forty words a minute.\n\n"
            "The client needs two plus years inbound call center. I don't have that but I'm a fast learner and people say I'm friendly.\n\n"
            "Rotating weekends? I could do weekends yeah. But I get you need the experience first."
        ),
    },
    {
        "id": "cc-012",
        "vertical": "call_center",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": "Inbound retail order status only — no collections, FDCPA, or dialer experience; cannot place on regulated collections floor day one.",
        "resume": "Kayla Simmons\nCustomer Service Representative\n\nZappos — Inbound Order Support (2023–2025)\n- Order tracking, returns, exchange processing\n- QA 90%, AHT 4:30\n- Zendesk — no collections or Salesforce\n\nNo FDCPA training or outbound dialer exposure",
        "job_description": "Collections Agent — Third-Party Agency\n\nRequirements:\n- 1+ years collections call center (mandatory)\n- FDCPA compliance and mini-Miranda scripting\n- Outbound dialer experience\n- Saturday rotation\n- Salesforce Collections Cloud\n\nRetail order support does not qualify",
        "transcript": (
            "Kayla hi Sarah Apex Staffing collections agent screening.\n\n"
            "I've been at Zappos two years inbound orders returns exchanges. QA ninety percent AHT four thirty.\n\n"
            "collections or outbound dialer experience? um no it's all customer service happy to help stuff not debt collection.\n\n"
            "FDCPA training? I've never heard of that honestly.\n\n"
            "I could probably pick it up quick though I mean I'm good on the phone. client needs real collections experience day one so I understand if that's a no."
        ),
    },
    {
        "id": "cc-013",
        "vertical": "call_center",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": "Retail mobile sales only — no tier 2 escalation, no Salesforce case ownership, failed to describe troubleshooting beyond reboot; does not meet tier 2 bar.",
        "resume": "Devon Price\nMobile Sales Consultant\n\nT-Mobile — Retail store (2022–2025)\n- In-store activations and upsells\n- Occasional customer troubleshooting at genius bar level\n- No phone queue metrics or tier 2 escalation path\n\nNo Salesforce, no ticketing system experience",
        "job_description": "Tech Support Tier 2 — Telecom Client\n\nRequirements:\n- 3+ years tier 2 phone support\n- Salesforce case ownership through resolution\n- Escalation documentation, AHT target 12:00, QA 90%+\n- Weekend rotation every third week\n\nRetail floor sales does not substitute for tier 2 phone support",
        "transcript": (
            "Recruiter: Devon, Sarah with Apex Staffing — tier two telecom support. What's your phone support background?\n"
            "Candidate: I've been T-Mobile retail three years. I troubleshoot phones in the store sometimes — restart, check settings.\n"
            "Recruiter: Tier two escalations on a phone queue? Salesforce cases?\n"
            "Candidate: No it's all walk-in. We don't use Salesforce. I haven't worked a call queue with handle time targets.\n"
            "Recruiter: This role needs three years tier two phone support with case ownership.\n"
            "Candidate: I could transfer to a call center maybe but I don't have that yet."
        ),
    },
    {
        "id": "cc-014",
        "vertical": "call_center",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": "Strong metrics but cannot work Saturdays due to religious observance with no alternate coverage — hard schedule requirement for utilities campaign.",
        "resume": "Hannah Cohen\nCustomer Service Representative\n\nVerizon — Inbound Wireless Support (2022–2025)\n- AHT 6:00, QA 93%\n- Salesforce Service Cloud\n- Top performer Q2 2024\n\nSchedule constraint: unavailable Saturdays (religious observance)",
        "job_description": "Inbound Customer Service — Utilities Campaign\n\nRequirements:\n- 2+ years call center experience\n- Salesforce proficiency\n- Rotating weekends mandatory — no exceptions\n- Tue–Sat rotating shift pattern\n\nSchedule flexibility on weekends is non-negotiable for client",
        "transcript": (
            "Hannah thanks for speaking with Apex Staffing about the utilities inbound campaign.\n\n"
            "I have three years Verizon inbound wireless support. AHT six minutes QA ninety-three percent Salesforce every day.\n\n"
            "This role is Tuesday through Saturday rotating including Saturdays every other week. Any issue?\n\n"
            "I observe Shabbat so I cannot work Fridays after sundown or Saturdays at all. I could do Sunday through Thursday if they had that.\n\n"
            "Unfortunately the client schedule is fixed rotating Saturdays no alternate shift. I understand that's a dealbreaker."
        ),
    },
    {
        "id": "cc-015",
        "vertical": "call_center",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": "WFH role requires private quiet workspace — candidate shares studio apartment with roommates and unreliable Wi-Fi; fails client home office audit criteria.",
        "resume": "Jordan Blake\nCustomer Service Representative\n\nAlorica — On-site CSR (2023–2024)\n- Inbound insurance verification calls\n- QA 87%, AHT 5:45\n- On-site only — no WFH experience\n\nHome situation: studio apartment, two roommates, shared Wi-Fi 25 Mbps",
        "job_description": "WFH Inbound Customer Service — After Training\n\nRequirements:\n- 1+ years call center experience\n- Private home office with door, no background noise\n- Wired internet 50+ Mbps dedicated line\n- Prior WFH experience preferred\n- Two-week on-site training then permanent remote\n\nCompany conducts home office video audit before WFH start",
        "transcript": (
            "Jordan hi Sarah Apex Staffing work from home customer service role.\n\n"
            "I did about a year at Alorica on site insurance verification QA eighty-seven. never worked from home for a call center.\n\n"
            "client does a home office audit private room wired fifty meg internet. what's your setup?\n\n"
            "uh I have a studio with two roommates. I'd take calls from the couch or kitchen honestly. Wi-Fi is like twenty-five meg shared.\n\n"
            "could you get a dedicated space? not really lease is up in six months can't afford an office setup right now.\n\n"
            "yeah I figured that wouldn't pass their audit."
        ),
    },
    {
        "id": "cc-016",
        "vertical": "call_center",
        "decision": "reject",
        "difficulty": "borderline",
        "ingest_format": "labeled",
        "reason": "Only three months call center tenure after long employment gap — below 2-year minimum; good attitude but client will not waive experience bar for utilities queue.",
        "resume": "Maria Santos\nCustomer Service Representative\n\nConvergys — Inbound CSR (2024–2025)\n- Three months utilities campaign training quit due to relocation\n- QA 84% in short tenure\n- Prior gap 2020–2024 caregiving for parent\n\nSalesforce exposure during training only",
        "job_description": "Inbound Customer Service — Utilities Campaign\n\nRequirements:\n- 2+ years call center experience (strict)\n- Salesforce proficiency\n- Rotating weekends\n- QA minimum 85%, AHT target 5:45\n\nShort training-only tenure does not count toward 2-year requirement",
        "transcript": (
            "Recruiter: Maria, Apex Staffing — utilities inbound role. Tell me about your call center time.\n"
            "Candidate: I was at Convergys three months on a utilities campaign before I had to relocate for family. QA was eighty-four.\n"
            "Recruiter: Anything before that gap?\n"
            "Candidate: I cared for my dad from 2020 to 2024. Before that I did hotel front desk but not phone queues.\n"
            "Recruiter: Client requires two full years call center. We're at three months.\n"
            "Candidate: I know it's short but the training stuck — I remember Salesforce dispositions. I'd work hard."
        ),
    },
    {
        "id": "cc-017",
        "vertical": "call_center",
        "decision": "reject",
        "difficulty": "borderline",
        "ingest_format": "asr_paragraph",
        "reason": "Collections background present but two attendance write-ups and recruiter concern about adversarial tone when describing debtor interactions — client rejected for compliance risk.",
        "resume": "Derek Walsh\nCollections Representative\n\nMidland Credit — Collections Agent (2023–2025)\n- Outbound medical collections, Experian dialer\n- QA 86%, RPC above team average\n- Two attendance write-ups 2024 (tardiness)\n- Salesforce collections module\n\nNote: left after final warning on punctuality",
        "job_description": "Collections Agent — Third-Party Agency\n\nRequirements:\n- 1+ years collections experience\n- FDCPA compliance — professional tone mandatory\n- Clean attendance last 12 months\n- Saturday rotation\n- QA minimum 85%\n\nAttendance policy: three tardies equals termination",
        "transcript": (
            "Derek this is Apex Staffing following up on the collections opening.\n\n"
            "I've got about two years at Midland Credit outbound medical collections Experian dialer Salesforce. QA eighty-six RPC was strong.\n\n"
            "Attendance history? I had two write-ups last year for being late mornings are rough with my kid's school drop-off.\n\n"
            "How do you handle debtors who push back? look if they owe they owe I don't sugarcoat it I tell them what happens if they don't pay.\n\n"
            "The agency needs compliant professional tone and spotless attendance going forward. I get why that's a concern."
        ),
    },
    {
        "id": "cc-018",
        "vertical": "call_center",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": "QA below 75% three consecutive months and AHT double team target on tier 1 role — metrics disqualify despite tenure.",
        "resume": "Ryan O'Connell\nTechnical Support Representative\n\nFrontier — Tier 1 Support (2023–2025)\n- QA 72–74% last three quarters\n- AHT 14:30 vs 7:00 team target\n- Multiple coaching plans on file\n- Salesforce case notes often incomplete per QA audits",
        "job_description": "Tech Support Tier 1 — ISP Client\n\nRequirements:\n- 1+ years tier 1 phone support\n- QA minimum 85%, AHT target 7:30\n- Salesforce documentation standards\n- Rotating weekends\n\nPerformance must meet client metrics at time of placement",
        "transcript": (
            "Ryan Apex Staffing tier one tech support screening.\n\n"
            "I've been Frontier tier one about two years modems billing basic troubleshooting Salesforce.\n\n"
            "what are your QA and AHT numbers lately? uh QA's been low seventies last three quarters. AHT like fourteen thirty target is seven.\n\n"
            "coaching plans? yeah a couple I'm working on it documentation is where I lose points.\n\n"
            "client needs eighty-five QA minimum at placement. I'm not there yet I know."
        ),
    },
    {
        "id": "cc-019",
        "vertical": "call_center",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": "Disclosed failed pre-employment drug screen at prior BPO within last 12 months — client requires clean screen for utilities contract; cannot submit.",
        "resume": "Kevin Hartley\nCustomer Service Representative\n\nTeleperformance — Utilities CSR (2024)\n- Terminated during onboarding after failed drug screen\n- Prior: Starbucks shift supervisor (2021–2024)\n\nNo completed call center tenure",
        "job_description": "Inbound Customer Service — Utilities Campaign\n\nRequirements:\n- 2+ years call center experience\n- Pass background check and drug screen (client contract mandate)\n- Salesforce proficiency\n- Rotating weekends\n\nFailed drug screen within 12 months is automatic disqualification per client",
        "transcript": (
            "Sarah: Kevin, Apex Staffing — utilities inbound screening. What's your call center experience?\n"
            "Candidate: I was hired at Teleperformance last year for a utilities campaign but didn't finish onboarding.\n"
            "Sarah: What happened?\n"
            "Candidate: I failed the drug screen. It was marijuana — legal in my state but they still pulled the offer.\n"
            "Sarah: This client runs the same panel. Any call center time after that?\n"
            "Candidate: No just Starbucks since. I'd pass now but I get you can't send me if it's within twelve months."
        ),
    },
    {
        "id": "cc-020",
        "vertical": "call_center",
        "decision": "reject",
        "difficulty": "borderline",
        "ingest_format": "asr_paragraph",
        "reason": "Strong tier 1 metrics but cannot attend mandatory six-week on-site training in another state — WFH role still requires training residency; no remote training waiver available.",
        "resume": "Samantha Reed\nTechnical Support — Tier 1\n\nCox Communications — Tier 1 Support (2022–2025)\n- AHT 7:10, QA 90%\n- Salesforce and internal ticketing\n- Cannot travel for six-week training — sole caregiver locally\n\nLocated: Portland OR | Training site: Atlanta GA",
        "job_description": "Tech Support Tier 1 — WFH After Training\n\nRequirements:\n- 1+ years tier 1 phone support\n- Six-week mandatory on-site training Atlanta GA (no virtual option)\n- Housing not provided — candidate must self-fund stay\n- After training: WFH with rotating weekends\n- QA 85%+, AHT target 8:00",
        "transcript": (
            "Samantha Apex Staffing about the tier one work from home role after training.\n\n"
            "Three years Cox tier one support AHT seven ten QA ninety percent Salesforce daily.\n\n"
            "Training is six weeks on site in Atlanta no virtual option. Can you do that?\n\n"
            "I'm sole caregiver for my mom in Portland after her surgery. I can't leave for six weeks and I can't afford Atlanta housing on top of that.\n\n"
            "Any flexibility? Could I do partial remote training? Client said no waiver last time we asked.\n\n"
            "Then I guess I'm out even though the remote job itself would be perfect."
        ),
    },
]

assert len(CALL_CENTER_RECORDS) == 20
assert sum(1 for r in CALL_CENTER_RECORDS if r["decision"] == "select") == 10
assert sum(1 for r in CALL_CENTER_RECORDS if r["decision"] == "reject") == 10
