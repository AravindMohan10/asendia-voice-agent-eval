"""Curated healthcare staffing-agency phone screen records."""

from __future__ import annotations

HEALTHCARE_RECORDS: list[dict] = [
    {
        "id": "hc-001",
        "vertical": "healthcare",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Three years orthopedic front desk with Epic Cadence and Prelude. "
            "Confirms hybrid schedule, insurance verification experience, and clean attendance."
        ),
        "resume": (
            "Danielle Brooks\nMedical Front Desk | Epic Cadence\n\n"
            "Summit Orthopedics — Front Desk Receptionist (2021–2024)\n"
            "- 50+ daily check-ins; Epic scheduling, registration, copay collection\n"
            "- Verified eligibility via Availity and payer portals; obtained prior auth referrals\n"
            "- HIPAA annual training current (2024)\n\n"
            "Temp — Athena check-in, urgent care float (2020)\n\n"
            "Certifications: Epic Cadence/Prelude Proficiency, HIPAA (2024)\n"
            "Education: Medical Office Administration certificate, Hennepin Tech"
        ),
        "job_description": (
            "Medical Front Desk — Orthopedic Clinic\n\n"
            "Responsibilities:\n"
            "- Patient check-in/out, appointment scheduling, phone triage\n"
            "- Insurance verification and copay collection\n"
            "- Epic Cadence/Prelude daily use\n"
            "- Maintain HIPAA compliance in all patient interactions\n\n"
            "Requirements:\n"
            "- 2+ years medical front desk in specialty or primary care\n"
            "- Epic or comparable EMR; insurance verification required\n"
            "- Professional demeanor with anxious or post-surgical patients\n"
            "- Hybrid schedule: 3 days on-site (Mon/Wed/Fri), 2 remote\n\n"
            "Location: Edina MN | Pay: $19–22/hr"
        ),
        "transcript": (
            "Recruiter: Hi Danielle, this is Megan from Apex Staffing. I'm screening for a "
            "medical front desk role at an orthopedic clinic. Can you walk me through your "
            "recent experience?\n"
            "Candidate: Sure. I've been at Summit Orthopedics for three years on the front "
            "desk. I use Epic Cadence and Prelude every day — scheduling, registration, "
            "copays, the whole check-in flow.\n"
            "Recruiter: How comfortable are you with insurance verification?\n"
            "Candidate: Very. I verify eligibility in Availity and payer portals before "
            "appointments, and I flag prior auth needs for surgical cases.\n"
            "Recruiter: This is hybrid — three days on-site. Does that work?\n"
            "Candidate: Yes, I live twelve minutes away. I've done hybrid since 2022 and "
            "I'm fine with it.\n"
            "Recruiter: Any attendance or HIPAA issues?\n"
            "Candidate: No write-ups. HIPAA training is current through this year."
        ),
    },
    {
        "id": "hc-002",
        "vertical": "healthcare",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": (
            "Strong patient coordinator background with Athena and referral workflows. "
            "Confirmed on-site availability and experience closing care gaps."
        ),
        "resume": (
            "Rosa Mendez\nPatient Care Coordinator\n\n"
            "Lakeside Primary Care — Patient Coordinator (2022–2024)\n"
            "- Coordinated referrals to cardiology, ortho, and imaging; tracked auth status\n"
            "- Athena EMR scheduling, messaging, and care gap outreach\n"
            "- Bilingual English/Spanish; managed 30+ referral cases weekly\n\n"
            "Community Health Center — Medical Receptionist (2020–2022)\n\n"
            "Certifications: HIPAA, CPR/AED\n"
            "Education: Associate degree, Health Sciences"
        ),
        "job_description": (
            "Patient Coordinator — Multi-Specialty Clinic\n\n"
            "Responsibilities:\n"
            "- Manage inbound referrals and prior authorization tracking\n"
            "- Schedule follow-ups and coordinate with specialist offices\n"
            "- Patient outreach for care gaps and annual wellness visits\n"
            "- Document all interactions in Athena EMR\n\n"
            "Requirements:\n"
            "- 2+ years patient coordination or care navigation\n"
            "- Athena or Epic experience required\n"
            "- Strong phone skills; insurance basics required\n"
            "- On-site Mon–Fri, 8am–5pm (no remote)\n\n"
            "Preferred: bilingual Spanish\n"
            "Location: Austin TX | Pay: $20–24/hr"
        ),
        "transcript": (
            "Thanks for taking my call Rosa. This patient coordinator role is at a "
            "multi-specialty clinic using Athena. What's your background?\n\n"
            "I've been patient coordinator at Lakeside Primary Care for two years. I "
            "handle referrals to cardiology and ortho, track prior auths, and close care "
            "gaps — annual wellness, mammography reminders, that kind of outreach.\n\n"
            "Are you on Athena day to day?\n\n"
            "Yes, scheduling, messaging, referral queues — all in Athena. I also did Epic "
            "at my previous clinic but Athena is my main system now.\n\n"
            "This is fully on-site, eight to five. Any schedule conflicts?\n\n"
            "No, I'm available full time on-site. I don't need remote.\n\n"
            "How do you handle a patient whose referral auth is denied?\n\n"
            "I review the denial reason, contact the payer if it's a coding issue, loop in "
            "the provider for clinical notes, and keep the patient updated so they're not "
            "left wondering."
        ),
    },
    {
        "id": "hc-003",
        "vertical": "healthcare",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Active CNA certification, two years LTC experience, BLS current. "
            "Day shift matches client need; willing to float units."
        ),
        "resume": (
            "Terrence Walsh\nCertified Nursing Assistant\n\n"
            "Sunrise Senior Living — CNA (2022–2024)\n"
            "- Assisted 12–14 residents per shift; ADLs, vitals, glucose checks\n"
            "- Documented in PointClickCare; reported changes to charge nurse\n"
            "- Zero safety incidents; employee of the quarter Q2 2023\n\n"
            "Volunteer — hospital transport aide (2021)\n\n"
            "Certifications: CNA (MN #CNA-448291, expires 2026), BLS (AHA, 2024)\n"
            "Education: CNA program, Minneapolis Community & Technical College"
        ),
        "job_description": (
            "CNA — Long-Term Care Facility\n\n"
            "Responsibilities:\n"
            "- ADL support, vitals, repositioning, meal assistance\n"
            "- Accurate charting in PointClickCare\n"
            "- Report changes in condition to nursing staff promptly\n"
            "- Maintain HIPAA and infection control standards\n\n"
            "Requirements:\n"
            "- Active state CNA certification (mandatory)\n"
            "- 1+ years LTC or acute care CNA experience\n"
            "- BLS certification\n"
            "- Day shift 6am–2pm; may float between memory care and rehab\n\n"
            "Location: St. Paul MN | Pay: $18–21/hr"
        ),
        "transcript": (
            "Sarah: Hi Terrence, thanks for applying to the CNA role. Tell me about your "
            "certification status.\n"
            "Candidate: My Minnesota CNA is active through 2026. BLS is current — renewed "
            "last fall through AHA.\n"
            "Sarah: Where have you been working?\n"
            "Candidate: Sunrise Senior Living for two years. I run a hall of twelve to "
            "fourteen residents, ADLs, vitals, glucose checks. I chart in PointClickCare.\n"
            "Sarah: This is day shift, six to two, and you may float to memory care.\n"
            "Candidate: That's fine. I've floated before. I prefer days — I'm off by "
            "afternoon.\n"
            "Sarah: Any attendance or safety concerns?\n"
            "Candidate: No write-ups. I was employee of the quarter in 2023. No incidents "
            "on my record."
        ),
    },
    {
        "id": "hc-004",
        "vertical": "healthcare",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": (
            "CPT-1 certified with outpatient draw volume. Confirmed on-site availability "
            "and experience with difficult sticks and Epic Beaker orders."
        ),
        "resume": (
            "Kim Nguyen\nPhlebotomist | CPT-1\n\n"
            "Quest Diagnostics — Phlebotomy Technician (2021–2024)\n"
            "- 40–55 venipunctures daily; pediatric and geriatric draws\n"
            "- Order entry and label verification in Epic Beaker\n"
            "- Maintained 98% first-stick success on tracked QA samples\n\n"
            "LabCorp — Floater phlebotomist (2019–2021)\n\n"
            "Certifications: CPT-1 (CA), HIPAA (2024)\n"
            "Education: Phlebotomy certificate, Contra Costa College"
        ),
        "job_description": (
            "Phlebotomist — Outpatient Lab\n\n"
            "Responsibilities:\n"
            "- Venipuncture and capillary collections per physician orders\n"
            "- Verify orders in Epic Beaker; label and process specimens\n"
            "- Patient identification per HIPAA two-identifier protocol\n"
            "- Handle difficult draws with calm, professional manner\n\n"
            "Requirements:\n"
            "- Active CPT-1 or equivalent national certification\n"
            "- 2+ years outpatient phlebotomy (not volunteer only)\n"
            "- Epic Beaker or comparable LIS experience\n"
            "- On-site Mon–Sat mornings; no remote\n\n"
            "Location: Oakland CA | Pay: $22–26/hr"
        ),
        "transcript": (
            "so Kim this is for an outpatient lab phlebotomy role um walk me through your "
            "certification\n\n"
            "yeah I've got active CPT one through the state board renewed um last year I've "
            "been at Quest three years doing forty to fifty five sticks a day\n\n"
            "are you on epic beaker or another LIS\n\n"
            "beaker mostly at Quest I verify orders print labels two identifier check "
            "before every draw per HIPAA protocol\n\n"
            "schedule is on site mornings including Saturday rotation okay\n\n"
            "yes I'm good with that I did Saturday rotation at Quest already no problem\n\n"
            "any incidents with mislabeled specimens or patient ID errors\n\n"
            "no I've never had a patient ID sentinel event I follow the two identifier "
            "rule every time"
        ),
    },
    {
        "id": "hc-005",
        "vertical": "healthcare",
        "decision": "select",
        "difficulty": "borderline",
        "ingest_format": "asr_paragraph",
        "reason": (
            "Only eight months dedicated billing but strong Epic Resolute exposure and "
            "accurate coding on 837 claims. Recruiter advanced due to cert progress and "
            "manager reference."
        ),
        "resume": (
            "Ashley Tran\nMedical Billing Specialist\n\n"
            "Northview Health System — Billing Specialist (2024–present)\n"
            "- Post charges and submit 837P claims in Epic Resolute\n"
            "- Work denials for coding edits, timely filing, and COB issues\n"
            "- Verify eligibility pre-visit; ~200 claims/week\n\n"
            "Medical Records Clerk — same system (2023–2024)\n"
            "- Released records per HIPAA; familiar with chart structure\n\n"
            "Certifications: CPC exam scheduled June 2025\n"
            "Education: Medical Billing & Coding diploma, UMA"
        ),
        "job_description": (
            "Medical Billing Specialist — Physician Group\n\n"
            "Responsibilities:\n"
            "- Charge entry and 837 claim submission in Epic Resolute\n"
            "- Denial management and payer follow-up\n"
            "- Insurance verification and eligibility checks\n"
            "- HIPAA-compliant handling of PHI on all calls\n\n"
            "Requirements:\n"
            "- 2+ years medical billing (professional claims)\n"
            "- Epic Resolute or comparable PM/billing module\n"
            "- Understanding of CPT/ICD-10 basics\n"
            "- Hybrid: 2 days on-site for team meetings, otherwise remote\n\n"
            "Location: Chicago IL | Pay: $23–27/hr"
        ),
        "transcript": (
            "Ashley, this billing role wants two plus years. Your resume shows about eight "
            "months in billing — can you clarify?\n\n"
            "Right. I was records clerk for a year at Northview, then moved to billing last "
            "August. So eight months billing, but I've been in Epic Resolute the whole time "
            "and I'm submitting professional claims daily.\n\n"
            "What payers do you work?\n\n"
            "Mostly commercial — Blue Cross, Aetna, United — plus Medicare. I work denials "
            "for timely filing and coding edits. I'm testing for CPC in June.\n\n"
            "This is hybrid, two days on-site. OK?\n\n"
            "Yes, I can be on-site Tuesdays and Thursdays like the posting says.\n\n"
            "Your manager would vouch for you moving from records to billing?\n\n"
            "Yes, I have a reference letter from my billing supervisor. She put me on the "
            "denial queue after three months because my accuracy was high."
        ),
    },
    {
        "id": "hc-006",
        "vertical": "healthcare",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Four years clinic admin with staff scheduling, supply ordering, and Epic "
            "admin workflows. Strong fit for hybrid clinic operations lead."
        ),
        "resume": (
            "Gregory Hale\nClinic Administrator / Office Manager\n\n"
            "Westside Family Medicine — Clinic Administrator (2020–2024)\n"
            "- Managed front desk and MA team of 8; weekly scheduling and payroll input\n"
            "- Epic admin workflows: template builds, visit type maintenance\n"
            "- Oversaw OSHA and HIPAA compliance training for staff\n"
            "- Reduced supply waste 15% by negotiating vendor contracts\n\n"
            "Prior — Urgent care shift lead (2017–2020)\n\n"
            "Education: BS Healthcare Administration, UW-Milwaukee"
        ),
        "job_description": (
            "Clinic Administrator — Primary Care Practice\n\n"
            "Responsibilities:\n"
            "- Day-to-day clinic operations: scheduling, staffing, supply inventory\n"
            "- Epic template and workflow support with IT/PM liaison\n"
            "- Staff onboarding for HIPAA and clinic policies\n"
            "- Patient complaint escalation and service recovery\n\n"
            "Requirements:\n"
            "- 3+ years clinic or practice administration\n"
            "- Epic admin or practice management experience\n"
            "- Supervisory experience required\n"
            "- Hybrid: 4 days on-site, 1 remote (admin/finance day)\n\n"
            "Location: Milwaukee WI | Pay: $28–32/hr"
        ),
        "transcript": (
            "Recruiter: Gregory, I'm calling about the clinic administrator opening. What's "
            "your management background?\n"
            "Candidate: I ran Westside Family Medicine for four years — eight staff between "
            "front desk and MAs. Scheduling, payroll input, supply ordering, the daily ops.\n"
            "Recruiter: What systems have you supported?\n"
            "Candidate: Epic on the admin side — template builds, visit types. I'm not IT, "
            "but I work with our analyst on workflow fixes.\n"
            "Recruiter: HIPAA and compliance oversight?\n"
            "Candidate: I ran annual HIPAA training and tracked completion. We had a clean "
            "audit in 2023.\n"
            "Recruiter: Hybrid four days on-site. Workable?\n"
            "Candidate: Yes. I'd keep Fridays remote for admin work if that's how the "
            "practice structures it."
        ),
    },
    {
        "id": "hc-007",
        "vertical": "healthcare",
        "decision": "select",
        "difficulty": "borderline",
        "ingest_format": "asr_noisy",
        "reason": (
            "No direct clinic front desk but two years dental reception with insurance "
            "verification and scheduling. Recruiter submitted for client interview "
            "based on transferable skills and Epic training completion."
        ),
        "resume": (
            "Jasmine Ortiz\nDental Front Office / Aspiring Medical Admin\n\n"
            "Bright Smile Dental — Receptionist (2022–2024)\n"
            "- Scheduled hygiene and treatment visits; verified dental insurance benefits\n"
            "- Collected copays; managed recall campaigns\n"
            "- Dentrix software daily use\n\n"
            "Completed: Epic Fundamentals online course (2024)\n"
            "Volunteer: hospital gift shop (customer service, 2023)\n\n"
            "Education: High school diploma; medical terminology course in progress"
        ),
        "job_description": (
            "Medical Front Desk — Pediatrics Clinic\n\n"
            "Responsibilities:\n"
            "- Check-in, scheduling, immunization record requests\n"
            "- Insurance verification and Medicaid referral coordination\n"
            "- Epic welcome and checkout workflows\n"
            "- HIPAA-compliant handling of minor patient information\n\n"
            "Requirements:\n"
            "- 1+ years medical front desk (clinic or hospital)\n"
            "- Epic or Athena experience strongly preferred\n"
            "- Calm demeanor with parents and children\n"
            "- On-site Mon–Fri; occasional Saturday vaccine clinic\n\n"
            "Location: Phoenix AZ | Pay: $17–20/hr"
        ),
        "transcript": (
            "Jasmine I'm looking at your resume — it's mostly dental not medical front "
            "desk. why should we consider you\n\n"
            "um I know it's dental but I did insurance verification every day benefit "
            "breakdowns copays scheduling recall calls it's the same customer facing "
            "workflow\n\n"
            "any epic or athena\n\n"
            "not on the job but I finished epic fundamentals online last month I'm ready "
            "to learn on site fast\n\n"
            "this pediatrics clinic is on site five days sometimes Saturday vaccine "
            "clinics\n\n"
            "I can do that I don't need hybrid I have reliable childcare\n\n"
            "hipaa experience\n\n"
            "we had HIPAA training at the dental office patient privacy charts I "
            "understand you can't discuss cases in the waiting room"
        ),
    },
    {
        "id": "hc-008",
        "vertical": "healthcare",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Chronic care management coordinator with Epic and closed-loop referral "
            "tracking. Bilingual; confirmed full-time on-site schedule."
        ),
        "resume": (
            "Elena Vasquez\nPatient Coordinator — Chronic Care\n\n"
            "Valley Health Partners — Care Coordinator (2021–2024)\n"
            "- Managed CCM panel of 120 patients; outreach for A1C, BP, med adherence\n"
            "- Epic referral and orders; closed-loop tracking with cardiology and nephrology\n"
            "- Bilingual English/Spanish; interpreted during scheduling calls\n\n"
            "Medical reception — community clinic (2018–2021)\n\n"
            "Certifications: HIPAA, CCM workflow training (Epic)\n"
            "Education: Associate degree, Community Health"
        ),
        "job_description": (
            "Patient Coordinator — Chronic Care Program\n\n"
            "Responsibilities:\n"
            "- Monthly patient outreach per care plan protocols\n"
            "- Coordinate specialist referrals and track completion in Epic\n"
            "- Insurance verification for program enrollment\n"
            "- Document all touchpoints; escalate clinical concerns to RN\n\n"
            "Requirements:\n"
            "- 2+ years care coordination or patient navigation\n"
            "- Epic experience required\n"
            "- Understanding of chronic disease management basics\n"
            "- On-site full time; bilingual Spanish strongly preferred\n\n"
            "Location: San Antonio TX | Pay: $21–25/hr"
        ),
        "transcript": (
            "Sarah: Elena, tell me about your chronic care coordination experience.\n"
            "Candidate: At Valley Health I managed a CCM panel of about 120 patients. "
            "Monthly calls, med adherence, A1C and blood pressure follow-ups.\n"
            "Sarah: How do you track referrals?\n"
            "Candidate: Epic referral workqueues. I close the loop — did the patient "
            "attend cardiology, do we have notes back, reschedule if they no-showed.\n"
            "Sarah: Insurance verification for program enrollment?\n"
            "Candidate: Yes, I verify eligibility and benefits before enrolling patients "
            "in CCM or RPM.\n"
            "Sarah: Full-time on-site. Any conflicts?\n"
            "Candidate: None. I'm bilingual Spanish — I use that daily on outreach calls."
        ),
    },
    {
        "id": "hc-009",
        "vertical": "healthcare",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": (
            "Hospital CNA with acute care experience, active certification, and Epic "
            "patient list familiarity. Night-to-day shift change acceptable."
        ),
        "resume": (
            "Marcus Johnson\nCNA — Acute Care\n\n"
            "Mercy General Hospital — CNA, Med-Surg (2022–2024)\n"
            "- 6–7 patient assignment; vitals, I&O, ambulation, post-op assistance\n"
            "- Epic Rover for vitals and task documentation\n"
            "- Consistently praised for teamwork on rapid response prep\n\n"
            "Nursing home — CNA (2020–2022)\n\n"
            "Certifications: CNA (IL #12-884729, active), BLS (2024)\n"
            "Education: CNA certificate, Malcolm X College"
        ),
        "job_description": (
            "CNA — Acute Care Hospital (Med-Surg)\n\n"
            "Responsibilities:\n"
            "- Patient care under RN direction: vitals, ADLs, mobility\n"
            "- Documentation in Epic Rover\n"
            "- Maintain HIPAA standards on shared units\n"
            "- Float to step-down as needed\n\n"
            "Requirements:\n"
            "- Active CNA certification\n"
            "- 1+ years acute care preferred (hospital med-surg)\n"
            "- BLS required\n"
            "- Day/evening rotation; every third weekend\n\n"
            "Location: Chicago IL | Pay: $19–23/hr"
        ),
        "transcript": (
            "Marcus, this is a med-surg CNA role at Mercy affiliate. What's your hospital "
            "experience?\n\n"
            "I've been on med-surg at Mercy General two years. Six to seven patients, vitals, "
            "I and O, ambulation after surgery. I document in Epic Rover.\n\n"
            "Certification and BLS status?\n\n"
            "Illinois CNA is active. BLS renewed in March.\n\n"
            "Schedule is days and evenings rotating, every third weekend. You're on nights "
            "now — is that a problem?\n\n"
            "I'm leaving nights for days. I can start on the day-evening rotation they "
            "need. Weekends are fine.\n\n"
            "Any patient safety or attendance issues?\n\n"
            "No discipline. Charge nurses have me help with rapid response prep because I "
            "stay calm."
        ),
    },
    {
        "id": "hc-010",
        "vertical": "healthcare",
        "decision": "select",
        "difficulty": "borderline",
        "ingest_format": "labeled",
        "reason": (
            "CPT-1 certified only four months ago with limited draw volume, but clinical "
            "externship and lab assistant background. Client agreed to skills check interview."
        ),
        "resume": (
            "Hannah Reeves\nPhlebotomist — New Graduate\n\n"
            "Regional Medical Center — Lab Assistant (2023–2024)\n"
            "- Specimen processing and centrifuge; assisted phlebotomists on busy mornings\n"
            "- Practiced venipuncture under supervision in outpatient draw station\n\n"
            "Phlebotomy externship — 100 successful supervised draws (2024)\n\n"
            "Certifications: CPT-1 (obtained Feb 2024), HIPAA (2024)\n"
            "Education: Phlebotomy program, PIMA Medical Institute"
        ),
        "job_description": (
            "Phlebotomist — Hospital Outpatient Draw Station\n\n"
            "Responsibilities:\n"
            "- Venipuncture for outpatient lab orders\n"
            "- Order verification in Epic Beaker\n"
            "- Maintain patient comfort and HIPAA privacy in draw area\n\n"
            "Requirements:\n"
            "- Active CPT-1 certification\n"
            "- 1+ years phlebotomy experience (paid, not externship only)\n"
            "- 30+ draws per shift capability\n"
            "- On-site; flexible mornings\n\n"
            "Location: Denver CO | Pay: $20–24/hr"
        ),
        "transcript": (
            "Recruiter: Hannah, the role asks for one year paid phlebotomy. You're newer — "
            "walk me through that.\n"
            "Candidate: I got CPT-1 in February. I've been lab assistant for a year, and "
            "I did my externship with a hundred supervised draws. I pick up stick duty on "
            "busy mornings now.\n"
            "Candidate: I'm not at thirty independent draws a shift yet — more like "
            "fifteen to twenty — but my preceptor said I'm ready for outpatient.\n"
            "Recruiter: Epic Beaker exposure?\n"
            "Candidate: Yes, order lookup and labels at the draw station in Beaker.\n"
            "Recruiter: Client may want a live stick demo. Comfortable?\n"
            "Candidate: Yes, I bring my kit to interviews if they ask."
        ),
    },
    {
        "id": "hc-011",
        "vertical": "healthcare",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": (
            "No medical billing or coding experience — retail cashier background only. "
            "Cannot meet Epic Resolute or claims submission requirements."
        ),
        "resume": (
            "Chris Delaney\nRetail Cashier\n\n"
            "Target — Checkout Team Member (2022–2024)\n"
            "- POS transactions, returns, guest service\n"
            "- No healthcare or insurance experience\n\n"
            "High school diploma (2021)\n"
            "Interest: 'wants to get into medical billing because pay is better'"
        ),
        "job_description": (
            "Medical Billing Specialist — Orthopedic Practice\n\n"
            "Requirements:\n"
            "- 2+ years professional medical billing\n"
            "- Epic Resolute billing module experience\n"
            "- Denial management and payer phone follow-up\n"
            "- HIPAA training required\n"
            "- Hybrid: 3 days on-site\n\n"
            "Location: Nashville TN | Pay: $22–26/hr"
        ),
        "transcript": (
            "Chris thanks for applying to medical billing tell me about your billing "
            "experience\n\n"
            "uh I haven't done billing yet I was cashier at Target for two years I'm a "
            "fast learner though\n\n"
            "any epic or athena any insurance verification claims\n\n"
            "no I haven't used those systems I looked up what epic resolute is online "
            "though\n\n"
            "this role needs two years professional claims experience day one\n\n"
            "I could maybe take a course if you train me\n\n"
            "client won't train from zero on resolute sorry — anything else in healthcare\n\n"
            "not yet but I'm willing to start somewhere"
        ),
    },
    {
        "id": "hc-012",
        "vertical": "healthcare",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": (
            "Strong coordinator background but requires fully remote. Role is on-site "
            "four days with no work-from-home option."
        ),
        "resume": (
            "Natalie Price\nPatient Coordinator\n\n"
            "Summit Specialty Clinic — Referral Coordinator (2020–2024)\n"
            "- Athena EMR referral management and prior auth tracking\n"
            "- Insurance verification for surgical referrals\n"
            "- 95% referral closure rate per quarterly audit\n\n"
            "Certifications: HIPAA (2024)\n"
            "Education: Bachelor's, Health Communication"
        ),
        "job_description": (
            "Patient Coordinator — Surgical Specialty\n\n"
            "Requirements:\n"
            "- 2+ years referral coordination\n"
            "- Athena or Epic referral modules\n"
            "- Prior authorization workflow experience\n"
            "- On-site 4 days/week (Mon–Thu); no remote work\n"
            "- HIPAA compliance mandatory\n\n"
            "Location: Charlotte NC | Pay: $21–25/hr"
        ),
        "transcript": (
            "Natalie, your referral background looks strong. This role is four days on-site "
            "in Charlotte. Any concerns?\n\n"
            "I actually need fully remote. I moved to care for my mom in Ohio and I'm not "
            "relocating back to North Carolina.\n\n"
            "The client removed remote after a HIPAA audit — there's no work-from-home.\n\n"
            "I can't do four days on-site from Ohio. If they add remote I'd be interested.\n\n"
            "That's not on the table. Would you consider relocating?\n\n"
            "Not right now. I need to stay here for family.\n\n"
            "Understood — I'll pass for now unless the schedule changes."
        ),
    },
    {
        "id": "hc-013",
        "vertical": "healthcare",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": (
            "No medical front desk or EMR experience. Food service background does not "
            "meet insurance verification or Epic requirements."
        ),
        "resume": (
            "Ryan Cooper\nFood Service Worker\n\n"
            "Hospital cafeteria — tray line and cashier (2021–2024)\n"
            "- No patient registration or scheduling experience\n"
            "- Saw Epic kiosks in lobby but never used clinical systems\n\n"
            "Education: High school diploma"
        ),
        "job_description": (
            "Medical Front Desk — Internal Medicine\n\n"
            "Requirements:\n"
            "- 1+ years clinic front desk\n"
            "- Epic or Athena scheduling and registration\n"
            "- Insurance verification and copay collection\n"
            "- HIPAA training\n"
            "- Hybrid 3 days on-site\n\n"
            "Location: Raleigh NC | Pay: $17–20/hr"
        ),
        "transcript": (
            "Ryan this front desk role needs epic or athena experience what's yours\n\n"
            "I work in the hospital cafeteria I see the check in kiosks but I don't use "
            "epic\n\n"
            "any insurance verification scheduling phones\n\n"
            "not really I run the cash register on the tray line sometimes catering orders\n\n"
            "did you apply thinking the cafeteria qualifies as hospital experience\n\n"
            "yeah it's the same building I know the campus\n\n"
            "client needs clinic front desk with registration workflows I can't submit this "
            "profile sorry"
        ),
    },
    {
        "id": "hc-014",
        "vertical": "healthcare",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": (
            "Terminated from prior clinic admin role for HIPAA violation — accessed "
            "celebrity patient chart without authorization. Client requires clean compliance record."
        ),
        "resume": (
            "Victor Lang\nClinic Office Manager\n\n"
            "Downtown Dermatology — Office Manager (2021–2023)\n"
            "- Staff scheduling, vendor management, Epic workflow support\n"
            "- Terminated Dec 2023 (reason listed as 'policy violation' on application)\n\n"
            "Prior — medical spa front desk lead (2018–2021)\n\n"
            "Education: BS Business Administration"
        ),
        "job_description": (
            "Clinic Administrator — Dermatology Practice\n\n"
            "Requirements:\n"
            "- 3+ years clinic administration\n"
            "- Epic or ModMed experience\n"
            "- Staff supervision and HIPAA compliance oversight\n"
            "- Hybrid 3 days on-site\n"
            "- Clean compliance and employment record required\n\n"
            "Location: Miami FL | Pay: $27–31/hr"
        ),
        "transcript": (
            "Victor, I need to ask about your departure from Downtown Dermatology in late "
            "2023.\n\n"
            "I was let go. I'd rather not get into it on a screening call.\n\n"
            "The client requires disclosure of any HIPAA or compliance terminations.\n\n"
            "Fine. I accessed a patient chart I wasn't assigned to. It was a high-profile "
            "patient and I was curious. HR termed me for HIPAA violation.\n\n"
            "That role oversees HIPAA training for staff. I can't present this profile.\n\n"
            "It was one mistake. I've done admin work for years.\n\n"
            "I understand, but the client was explicit about clean compliance history."
        ),
    },
    {
        "id": "hc-015",
        "vertical": "healthcare",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": (
            "CNA certification expired six months ago with no plan to renew before start "
            "date. State requires active CNA for assignment."
        ),
        "resume": (
            "Sandra Mitchell\nFormer CNA\n\n"
            "Brookdale Assisted Living — CNA (2019–2023)\n"
            "- ADL care, vitals, dementia unit experience\n"
            "- Left role to care for family; CNA not renewed\n\n"
            "CNA (OH) — expired Sept 2024\n"
            "BLS — expired 2023"
        ),
        "job_description": (
            "CNA — Assisted Living / Memory Care\n\n"
            "Requirements:\n"
            "- Active Ohio CNA certification (required day 1)\n"
            "- 1+ years assisted living or LTC\n"
            "- BLS certification current\n"
            "- Day shift; on-site\n"
            "- HIPAA and abuse reporting training\n\n"
            "Location: Columbus OH | Pay: $17–20/hr"
        ),
        "transcript": (
            "Sandra, can you confirm your CNA status for Ohio?\n\n"
            "It expired last September. I took time off for family and didn't renew yet.\n\n"
            "This client needs active CNA on day one. Can you renew before start?\n\n"
            "I'd have to retake the class — maybe two months. I don't have the cert now.\n\n"
            "What about BLS?\n\n"
            "That's expired too. I'd need to redo it.\n\n"
            "I can't submit without active CNA. Let me know when you're renewed and we can "
            "revisit."
        ),
    },
    {
        "id": "hc-016",
        "vertical": "healthcare",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Not CPT-1 certified and stated discomfort with venipuncture. Role requires "
            "certification and independent draw volume day one."
        ),
        "resume": (
            "Paula Simmons\nMedical Assistant Student\n\n"
            "Clinical extern — mostly rooming and vitals (2024)\n"
            "- Observed phlebotomy; performed 5 supervised sticks in externship\n"
            "- No national phlebotomy certification\n\n"
            "Prior — home health aide (non-clinical, 2020–2022)\n\n"
            "Education: MA program in progress, expected completion Aug 2025"
        ),
        "job_description": (
            "Phlebotomist — Federally Qualified Health Center\n\n"
            "Requirements:\n"
            "- CPT-1 or equivalent certification (mandatory)\n"
            "- 1+ years outpatient phlebotomy\n"
            "- Epic or Centricity order verification\n"
            "- Comfortable with high-volume draws including pediatric patients\n"
            "- On-site full time\n\n"
            "Location: Fresno CA | Pay: $21–25/hr"
        ),
        "transcript": (
            "Recruiter: Paula, this is a phlebotomy-only role. Do you hold CPT-1?\n"
            "Candidate: Not yet. I'm in medical assistant school. I only did a handful of "
            "sticks during externship.\n"
            "Recruiter: The health center needs certification and independent draw volume "
            "from day one.\n"
            "Candidate: I get nervous with needles honestly. I was hoping to room patients "
            "mostly.\n"
            "Recruiter: This isn't a medical assistant role — it's fifty plus sticks a day.\n"
            "Candidate: Yeah, that's probably not for me right now."
        ),
    },
    {
        "id": "hc-017",
        "vertical": "healthcare",
        "decision": "reject",
        "difficulty": "borderline",
        "ingest_format": "asr_noisy",
        "reason": (
            "Medical records background with coding exposure but no hands-on billing or "
            "837 submission. Client rejected — needs Resolute experience, not release-of-info."
        ),
        "resume": (
            "Diane Foster\nHealth Information / Records Specialist\n\n"
            "Midstate Medical Group — ROI Specialist (2020–2024)\n"
            "- Released records per HIPAA authorization workflows\n"
            "- Read ICD-10 codes on charts; completed intro coding course (2023)\n"
            "- No charge entry or claims submission experience\n\n"
            "Certifications: HIPAA (2024), intro ICD-10 course certificate"
        ),
        "job_description": (
            "Medical Billing Specialist — Multi-Specialty Group\n\n"
            "Requirements:\n"
            "- 2+ years professional billing (837P claims)\n"
            "- Epic Resolute or Athena Collector experience\n"
            "- Denial work and payer follow-up\n"
            "- Hybrid 2 days on-site\n"
            "- HIPAA compliance\n\n"
            "Location: Indianapolis IN | Pay: $23–27/hr"
        ),
        "transcript": (
            "Diane you applied for billing your background is records release correct\n\n"
            "yes ROI mostly but I took an ICD ten intro course I know diagnosis codes on "
            "charts\n\n"
            "have you submitted professional claims in resolute or athena collector\n\n"
            "not exactly I haven't posted charges or worked denials I see codes when I "
            "pull records for attorneys\n\n"
            "client needs two years live billing um not coding literacy alone\n\n"
            "I could learn resolute fast I understand the revenue cycle conceptually\n\n"
            "they've rejected records only profiles before I'm gonna pass but keep billing "
            "certs on your radar"
        ),
    },
    {
        "id": "hc-018",
        "vertical": "healthcare",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": (
            "Available nights only due to childcare. Client needs day shift CNA with "
            "weekend rotation — schedule mismatch."
        ),
        "resume": (
            "Angela Wright\nCNA — Night Shift\n\n"
            "Greenfield Nursing Home — CNA (2021–2024)\n"
            "- Night shift 11pm–7am; dementia and rehab units\n"
            "- PointClickCare documentation\n"
            "- Active CNA (IN) and BLS current\n\n"
            "Unavailable: day shift due to school drop-off (single parent)"
        ),
        "job_description": (
            "CNA — Skilled Nursing Facility\n\n"
            "Requirements:\n"
            "- Active CNA certification\n"
            "- Day shift 7am–3pm; every other weekend\n"
            "- PointClickCare or comparable EMR\n"
            "- 1+ years SNF experience\n"
            "- On-site; HIPAA training required\n\n"
            "Location: Fort Wayne IN | Pay: $18–21/hr"
        ),
        "transcript": (
            "Angela, this SNF role is day shift seven to three with every other weekend. "
            "What's your availability?\n\n"
            "I only work nights right now. Eleven to seven at Greenfield. I can't do days "
            "because I drop my kids at school at eight.\n\n"
            "There's no night opening on this contract. Could you switch shifts?\n\n"
            "Not unless they offer on-site childcare, which they don't. I'd need nights or "
            "maybe evenings after six.\n\n"
            "Client is firm on days. I'll keep you in mind for night openings.\n\n"
            "Please do. Days won't work for me this year."
        ),
    },
    {
        "id": "hc-019",
        "vertical": "healthcare",
        "decision": "reject",
        "difficulty": "borderline",
        "ingest_format": "labeled",
        "reason": (
            "Epic-trained with solid skills but three attendance write-ups in twelve months. "
            "Client has zero-tolerance attendance policy for front desk coverage."
        ),
        "resume": (
            "Monique Taylor\nMedical Receptionist\n\n"
            "Lakeshore Clinic — Front Desk (2023–2024)\n"
            "- Epic welcome/check-out; insurance verification via Availity\n"
            "- Three attendance write-ups in 12 months (disclosed on application)\n"
            "- Terminated for attendance Oct 2024\n\n"
            "Certifications: Epic Welcome proficiency, HIPAA (2023)"
        ),
        "job_description": (
            "Medical Front Desk — Busy Primary Care\n\n"
            "Requirements:\n"
            "- 1+ years medical front desk\n"
            "- Epic scheduling and registration\n"
            "- Insurance verification\n"
            "- Reliable attendance — single coverage desk at peak hours\n"
            "- Hybrid 3 days on-site\n"
            "- HIPAA compliance\n\n"
            "Location: Atlanta GA | Pay: $18–21/hr"
        ),
        "transcript": (
            "Recruiter: Monique, your Epic skills look good. I need to ask about the "
            "attendance write-ups and your departure.\n"
            "Candidate: I had three write-ups for tardiness. Childcare broke down twice, "
            "car trouble once. They termed me in October.\n"
            "Recruiter: This clinic has one front desk person at check-in peak. They said "
            "zero tolerance on attendance.\n"
            "Candidate: I'm in a better spot now — new daycare with backup. My skills are "
            "solid: Epic, Availity, copays.\n"
            "Recruiter: I hear you, but three write-ups in a year is a hard sell for this "
            "client. I can't submit this profile.\n"
            "Candidate: Understood. I was hoping they'd weigh the skills."
        ),
    },
    {
        "id": "hc-020",
        "vertical": "healthcare",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": (
            "Hotel front desk experience only — no healthcare administration, HIPAA training, "
            "or clinic operations background."
        ),
        "resume": (
            "Brian Okafor\nHotel Front Desk Agent\n\n"
            "Marriott — Front Desk (2020–2024)\n"
            "- Guest check-in, reservations, concierge requests\n"
            "- Opera PMS hotel system\n"
            "- No healthcare or clinic experience\n\n"
            "Education: Hospitality Management certificate"
        ),
        "job_description": (
            "Clinic Administrator — Urgent Care Chain\n\n"
            "Requirements:\n"
            "- 3+ years clinic or urgent care administration\n"
            "- Staff scheduling, inventory, compliance tracking\n"
            "- Epic or eClinicalWorks experience\n"
            "- HIPAA oversight and incident reporting\n"
            "- Hybrid 4 days on-site\n\n"
            "Location: Tampa FL | Pay: $26–30/hr"
        ),
        "transcript": (
            "Brian tell me about your clinic administration background\n\n"
            "I haven't worked in a clinic I've been hotel front desk at Marriott four years "
            "managing guest check in and reservations\n\n"
            "any epic eclinicalworks hipaa compliance staff supervision\n\n"
            "no opera is the hotel system I supervised two bell staff during rush hour not "
            "medical staff\n\n"
            "this is clinic admin for an urgent care chain three plus years required\n\n"
            "I figured hospitality transfers customer service wise\n\n"
            "client wants healthcare ops experience I can't put this through"
        ),
    },
]
