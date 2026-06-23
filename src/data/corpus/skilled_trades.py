"""Skilled trades vertical — staffing-agency phone screen eval records."""

from __future__ import annotations

SKILLED_TRADES_RECORDS: list[dict] = [
    {
        "id": "st-001",
        "vertical": "skilled_trades",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Four years commercial HVAC service, current EPA 608 Universal, and strong "
            "troubleshooting examples. Confirmed swing-shift availability and clean safety record."
        ),
        "resume": (
            "Derek Holloway\nCommercial HVAC Technician | 4 years\n\n"
            "Comfort Systems USA — Service Tech (2021–2025)\n"
            "- Diagnosed and repaired rooftop units, VAV systems, and refrigeration circuits\n"
            "- EPA 608 Universal certified (renewed Jan 2025)\n"
            "- OSHA 10 completed; zero recordable incidents\n"
            "- Responded to 8–12 service calls per shift during peak season\n\n"
            "Apprentice — Residential install helper, Atlanta (2019–2021)\n\n"
            "Certifications: EPA 608 Universal, OSHA 10, NATE Ready-to-Work\n"
            "Tools: manifold gauges, leak detectors, brazing, multimeter\n"
            "Education: HVAC diploma, Lincoln Tech (2019)"
        ),
        "job_description": (
            "Commercial HVAC Service Technician — Swing Shift\n\n"
            "Responsibilities:\n"
            "- Service and repair commercial RTUs, split systems, and refrigeration equipment\n"
            "- Perform preventive maintenance per client PM schedules\n"
            "- Complete work orders, parts usage, and safety documentation\n\n"
            "Requirements:\n"
            "- 3+ years commercial HVAC service experience\n"
            "- EPA 608 Universal certification (current)\n"
            "- Valid driver's license; able to lift 75 lbs and work on rooftops\n"
            "- Swing shift: 2pm–10pm, Mon–Fri\n\n"
            "Preferred: NATE certification, brazing experience\n"
            "Location: Charlotte NC | Pay: $28–34/hr"
        ),
        "transcript": (
            "Interviewer: Thanks for taking my call, Derek. This is a commercial HVAC service "
            "role on swing shift. Walk me through your relevant experience.\n"
            "Candidate: I've been with Comfort Systems for four years doing commercial service — "
            "rooftop units, VAV boxes, some walk-in cooler work. Before that I did residential "
            "install as an apprentice.\n"
            "Interviewer: Do you hold EPA 608? Which type?\n"
            "Candidate: Universal — renewed it this January. I handle recovery and charging on "
            "R-410A and R-22 systems regularly.\n"
            "Interviewer: Any safety incidents or attendance issues we should know about?\n"
            "Candidate: No recordables, no write-ups. I had perfect attendance last year except "
            "two PTO days.\n"
            "Interviewer: This is swing shift, 2 to 10, Monday through Friday. Does that work?\n"
            "Candidate: Yes, that's actually what I prefer. My wife works days so childcare "
            "lines up.\n"
            "Interviewer: Can you start within two weeks if we move forward?\n"
            "Candidate: Yes, I can give two weeks' notice and start the following Monday."
        ),
    },
    {
        "id": "st-002",
        "vertical": "skilled_trades",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Strong EPA 608 Type II and install background on commercial RTUs. OSHA 10 current, "
            "confirmed day-shift availability and reliable transportation to job sites."
        ),
        "resume": (
            "Maria Santos\nHVAC Installer | 3 years commercial\n\n"
            "Trane Commercial — Install Technician (2022–2025)\n"
            "- Installed and commissioned rooftop units up to 25 tons\n"
            "- Brazed line sets, set curbs, ran control wiring\n"
            "- EPA 608 Type II certified (2023, current)\n"
            "- OSHA 10 card (2024)\n\n"
            "Helper — Light commercial retrofit crew (2021–2022)\n\n"
            "Certifications: EPA 608 Type II, OSHA 10\n"
            "Licenses: Valid driver's license, clean MVR\n"
            "Education: Trade school HVAC fundamentals certificate"
        ),
        "job_description": (
            "HVAC Installer — Commercial New Construction\n\n"
            "Responsibilities:\n"
            "- Install rooftop units, ductwork, refrigerant lines, and controls\n"
            "- Assist with startup and commissioning\n"
            "- Follow job-site safety and QC checklists\n\n"
            "Requirements:\n"
            "- 2+ years commercial HVAC install experience\n"
            "- EPA 608 Type II or Universal (mandatory)\n"
            "- OSHA 10 preferred\n"
            "- Day shift, travel to sites within 60-mile radius\n"
            "- Able to work at heights with fall protection\n\n"
            "Location: Phoenix AZ | Pay: $24–30/hr"
        ),
        "transcript": (
            "Interviewer: Hi Maria, I'm screening for a commercial HVAC installer role. Tell me "
            "about your install background.\n"
            "Candidate: I've been with Trane Commercial almost three years. Mostly rooftop "
            "installs — setting curbs, rigging units, brazing lines, pulling wire for controls.\n"
            "Interviewer: EPA certification status?\n"
            "Candidate: Type II, got it in 2023, still current. I don't do much recovery on "
            "install but I'm certified for it.\n"
            "Interviewer: OSHA 10?\n"
            "Candidate: Yes, completed last year. I wear harness on every rooftop job.\n"
            "Interviewer: This is day shift with some travel around the valley. Transportation?\n"
            "Candidate: I have my own truck and tools. I'm fine driving up to an hour each way.\n"
            "Interviewer: Any gaps in employment or job hopping concerns?\n"
            "Candidate: No gaps. I've been with Trane the whole time since trade school."
        ),
    },
    {
        "id": "st-003",
        "vertical": "skilled_trades",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Two years electrician helper experience on commercial sites with current OSHA 10. "
            "Demonstrated conduit bending and panel work; available for required day shift."
        ),
        "resume": (
            "Jordan Ellis\nElectrician Helper | 2 years\n\n"
            "Miller Electric — Commercial Helper (2023–2025)\n"
            "- Pulled wire, bent EMT and rigid conduit, assisted panel terminations\n"
            "- Supported rough-in on office and retail TI projects\n"
            "- OSHA 10 certified (2023)\n"
            "- Maintained clean job-site safety compliance\n\n"
            "Laborer — General construction (2022–2023)\n\n"
            "Certifications: OSHA 10\n"
            "Skills: EMT bending, wire pulling, blueprint reading basics\n"
            "Education: High school diploma"
        ),
        "job_description": (
            "Electrician Helper — Commercial Construction\n\n"
            "Responsibilities:\n"
            "- Assist journeyman electricians with rough-in and trim-out\n"
            "- Pull wire, bend conduit, mount boxes and panels\n"
            "- Maintain tools, materials, and site cleanliness\n\n"
            "Requirements:\n"
            "- 1+ years helper or apprentice experience on commercial jobs\n"
            "- OSHA 10 (required before site access)\n"
            "- Ability to read basic electrical drawings\n"
            "- Day shift Mon–Fri, occasional Saturday OT\n"
            "- Pass background check and drug screen\n\n"
            "Location: Dallas TX | Pay: $18–22/hr"
        ),
        "transcript": (
            "Interviewer: Jordan, thanks for applying to the electrician helper role. What's your "
            "commercial experience?\n"
            "Candidate: Two years with Miller Electric on commercial TI work — office buildings, "
            "a couple retail fit-outs. I pull wire, bend EMT, help with panel terminations.\n"
            "Interviewer: Do you have OSHA 10?\n"
            "Candidate: Yes, got it when I started in 2023. I renew my awareness training through "
            "the company yearly.\n"
            "Interviewer: Have you worked off drawings or mostly direction from the journeyman?\n"
            "Candidate: Both. I can follow one-lines and floor plans for box layout and conduit "
            "runs. I ask when something's not clear.\n"
            "Interviewer: Day shift with some Saturdays during crunch. Any scheduling limits?\n"
            "Candidate: Days and OT are fine. I don't have night restrictions.\n"
            "Interviewer: Why leave Miller?\n"
            "Candidate: Project winding down and layoffs on our crew. Looking for steady work."
        ),
    },
    {
        "id": "st-004",
        "vertical": "skilled_trades",
        "decision": "select",
        "difficulty": "borderline",
        "ingest_format": "labeled",
        "reason": (
            "OSHA 30 and three years helper experience outweigh lighter commercial exposure. "
            "Strong safety mindset and motor control experience; good fit for industrial electrical helper."
        ),
        "resume": (
            "Andre Williams\nElectrical Helper | 3 years\n\n"
            "Baldor Industrial — Electrical Helper (2022–2025)\n"
            "- Assisted with motor terminations, conduit runs, and control panel wiring\n"
            "- Supported PM shutdowns in food-processing plant\n"
            "- OSHA 30 certified (2024)\n\n"
            "Residential wireman helper — Small contractor (2021–2022)\n\n"
            "Certifications: OSHA 30, forklift awareness training\n"
            "Skills: Conduit, tray cable, VFD wiring assist, lockout/tagout\n"
            "Education: Associate coursework — industrial technology (in progress)"
        ),
        "job_description": (
            "Electrical Helper — Industrial Maintenance Contractor\n\n"
            "Responsibilities:\n"
            "- Support electricians during plant shutdowns and capital projects\n"
            "- Pull cable tray, terminate controls, assist motor swaps\n"
            "- Follow LOTO and site-specific safety rules\n\n"
            "Requirements:\n"
            "- 2+ years electrical helper or apprentice experience\n"
            "- OSHA 10 minimum; OSHA 30 preferred for industrial sites\n"
            "- Comfortable in active manufacturing environments\n"
            "- Flexible schedule for shutdown windows (some nights/weekends)\n\n"
            "Location: Memphis TN | Pay: $20–25/hr"
        ),
        "transcript": (
            "Interviewer: Andre, this helper role supports industrial shutdown work. Tell me about "
            "your background.\n"
            "Candidate: Three years total — two at Baldor on a food plant account, one year "
            "residential before that. Motor terminations, conduit, some VFD panels.\n"
            "Interviewer: OSHA level?\n"
            "Candidate: OSHA 30, finished last year. I'm strict about lockout-tagout — no shortcuts.\n"
            "Interviewer: Most of your work industrial or residential?\n"
            "Candidate: Last two years mostly industrial. Residential was smaller service calls — "
            "receptacles, panels, basics.\n"
            "Interviewer: Shutdowns can run nights and weekends for two weeks straight. OK?\n"
            "Candidate: Yes, I've done two shutdowns already. I plan childcare when weekends hit.\n"
            "Interviewer: Any concerns from past employers?\n"
            "Candidate: No terminations. Baldor is cutting contract headcount, not performance."
        ),
    },
    {
        "id": "st-005",
        "vertical": "skilled_trades",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Residential-only background with no EPA 608 certification. Role requires commercial "
            "service and current EPA Universal — mandatory day-one credential not met."
        ),
        "resume": (
            "Kevin Tran\nHVAC Helper | 14 months residential\n\n"
            "Cool Breeze Home Services — Install Helper (2024–2025)\n"
            "- Assisted residential split system and furnace changeouts\n"
            "- Duct sealing, line set flush, startup assist\n"
            "- No EPA certification\n"
            "- No commercial or rooftop experience\n\n"
            "Retail — Hardware store (2023–2024)\n\n"
            "Education: High school diploma\n"
            "Certifications: None"
        ),
        "job_description": (
            "Commercial HVAC Service Technician\n\n"
            "Requirements:\n"
            "- 2+ years commercial HVAC service (not residential-only)\n"
            "- EPA 608 Universal certification — required before first dispatch\n"
            "- Experience on rooftop units and commercial refrigeration\n"
            "- Valid driver's license and clean background\n"
            "- Day shift with on-call rotation\n\n"
            "Location: Tampa FL | Pay: $26–32/hr"
        ),
        "transcript": (
            "Interviewer: Kevin, this is commercial HVAC service. What's your experience?\n"
            "Candidate: About fourteen months with Cool Breeze doing residential installs — "
            "changeouts, furnaces, mini-splits sometimes.\n"
            "Interviewer: Any commercial rooftops or EPA 608?\n"
            "Candidate: Not really commercial. I haven't taken the EPA test yet — my boss said "
            "he'd sponsor me when things slow down.\n"
            "Interviewer: This role requires Universal EPA before you can go on a truck. "
            "Would you have that at start?\n"
            "Candidate: Probably not for a month or two. I could study and test on my own though.\n"
            "Interviewer: Unfortunately the client won't wait. Any other certifications?\n"
            "Candidate: Just driver's license. I'm a fast learner on the tools side."
        ),
    },
    {
        "id": "st-006",
        "vertical": "skilled_trades",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": (
            "EPA 608 expired over a year ago and only six months paid HVAC experience. Below "
            "minimum tenure and cannot legally handle refrigerant on day one."
        ),
        "resume": (
            "Lisa Morales\nHVAC Technician | 6 months\n\n"
            "QuickCool HVAC — Junior Tech (2024–2025)\n"
            "- Residential service calls under senior tech supervision\n"
            "- EPA 608 Type I — expired 2023\n"
            "- Basic charging and leak check assist\n\n"
            "Server — Restaurant (2022–2024)\n\n"
            "Certifications: EPA 608 Type I (expired)\n"
            "Education: Community college — 1 semester HVAC intro"
        ),
        "job_description": (
            "HVAC Service Technician — Light Commercial\n\n"
            "Requirements:\n"
            "- 2+ years HVAC service experience\n"
            "- Current EPA 608 Type II or Universal\n"
            "- Own basic hand tools\n"
            "- Clean driving record\n\n"
            "Location: Denver CO | Pay: $25–29/hr"
        ),
        "transcript": (
            "Interviewer: Hi Lisa, um, tell me about your HVAC service background.\n"
            "Candidate: I've been with QuickCool about six months, mostly residential service, "
            "you know, like under a senior tech.\n"
            "Interviewer: EPA cert status?\n"
            "Candidate: I had Type I from a class in 2022 but uh I think it expired last year. "
            "I haven't renewed yet.\n"
            "Interviewer: This job needs current Type II or Universal and two years experience. "
            "How do you compare?\n"
            "Candidate: I'm probably short on years. I learn quick though — definately willing "
            "to retest for EPA.\n"
            "Interviewer: Experience on commercial units?\n"
            "Candidate: Not really, mostly houses and some small storefront units once or twice."
        ),
    },
    {
        "id": "st-007",
        "vertical": "skilled_trades",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "No OSHA 10 and no prior commercial electrical site experience. Client mandates "
            "OSHA 10 before badge access; candidate cannot start on required timeline."
        ),
        "resume": (
            "Chris Dalton\nConstruction Laborer | 1 year\n\n"
            "Various day-labor — Demolition and cleanup (2024–2025)\n"
            "- General labor, material staging, site cleanup\n"
            "- No electrical helper work\n"
            "- No OSHA 10\n\n"
            "Warehouse — Amazon FC (2023–2024)\n\n"
            "Education: GED (2023)\n"
            "Certifications: None"
        ),
        "job_description": (
            "Electrician Helper — Commercial TI\n\n"
            "Requirements:\n"
            "- 1+ years electrical helper experience on commercial jobsites\n"
            "- OSHA 10 card required before first day (no exceptions)\n"
            "- Basic hand tools\n"
            "- Day shift, Dallas metro\n\n"
            "Location: Dallas TX | Pay: $18–21/hr"
        ),
        "transcript": (
            "Interviewer: Chris, what electrical helper experience do you have?\n"
            "Candidate: I haven't worked on electrical crews. Mostly demolition labor and "
            "warehouse before that.\n"
            "Interviewer: Any OSHA 10?\n"
            "Candidate: No, I was going to take it online if I got hired.\n"
            "Interviewer: The GC won't badge anyone without OSHA 10 already in hand. Timeline?\n"
            "Candidate: I could probably finish a course in a week if I pay for it.\n"
            "Interviewer: They need someone Monday. Any wire pulling or conduit at all?\n"
            "Candidate: Not on a job. I helped a buddy run wire in his garage once."
        ),
    },
    {
        "id": "st-008",
        "vertical": "skilled_trades",
        "decision": "reject",
        "difficulty": "borderline",
        "ingest_format": "labeled",
        "reason": (
            "Helper experience is adequate but candidate is nights-only while role requires "
            "day shift with mandatory Saturday overtime during project closeout."
        ),
        "resume": (
            "Ramon Vega\nElectrician Helper | 18 months\n\n"
            "Spark Electric — Helper (2023–2025)\n"
            "- Commercial rough-in, wire pulls, box mounting\n"
            "- OSHA 10 (2023)\n"
            "- Strong attendance\n\n"
            "Availability: Nights only — attends community college days\n\n"
            "Certifications: OSHA 10"
        ),
        "job_description": (
            "Electrician Helper — Commercial Day Shift\n\n"
            "Requirements:\n"
            "- 1+ years commercial helper experience\n"
            "- OSHA 10\n"
            "- Day shift 6am–2:30pm Mon–Fri\n"
            "- Mandatory Saturdays during final 6 weeks of project\n"
            "- No schedule exceptions\n\n"
            "Location: Houston TX | Pay: $19–23/hr"
        ),
        "transcript": (
            "Interviewer: Ramon, tell me about your helper experience.\n"
            "Candidate: Eighteen months with Spark on commercial rough-in. OSHA 10, good "
            "attendance, no issues.\n"
            "Interviewer: This is strict day shift, 6 AM start, plus Saturdays for six weeks. "
            "Any conflicts?\n"
            "Candidate: I take college classes mornings until noon — I really need nights only, "
            "like 4 PM or later start.\n"
            "Interviewer: The GC won't flex. Could you adjust your class schedule?\n"
            "Candidate: Not this semester. I could do days in August when the semester ends.\n"
            "Interviewer: They need someone in two weeks on days. Anything else?\n"
            "Candidate: Experience-wise I'm ready. It's just the schedule."
        ),
    },
    {
        "id": "st-009",
        "vertical": "skilled_trades",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Registered second-year plumbing apprentice with valid state card and relevant "
            "commercial rough-in experience. Confirmed tools, transportation, and day-shift availability."
        ),
        "resume": (
            "Ethan Brooks\nPlumbing Apprentice — 2nd year\n\n"
            "Summit Mechanical — Apprentice Plumber (2023–2025)\n"
            "- Commercial rough-in: copper, PVC, cast iron, ProPress\n"
            "- Underground storm and sanitary on TI projects\n"
            "- Registered apprentice #PL-48291 (State of Ohio, current)\n"
            "- OSHA 10 (2023)\n\n"
            "Helper — Residential service (2022–2023)\n\n"
            "Certifications: OSHA 10, apprentice registration current\n"
            "Tools: Own pro press tool, threaders, basic hand tools"
        ),
        "job_description": (
            "Plumber Apprentice — Commercial Construction\n\n"
            "Responsibilities:\n"
            "- Rough-in and top-out under journeyman supervision\n"
            "- Install underground and above-ground piping systems\n"
            "- Maintain apprentice log hours for licensure\n\n"
            "Requirements:\n"
            "- Registered plumbing apprentice in good standing\n"
            "- 1+ years commercial plumbing experience\n"
            "- OSHA 10\n"
            "- Own basic tools and reliable transportation\n"
            "- Day shift, Columbus metro\n\n"
            "Location: Columbus OH | Pay: $19–24/hr"
        ),
        "transcript": (
            "Interviewer: Ethan, this is a commercial plumber apprentice role. What's your status?\n"
            "Candidate: Second-year registered apprentice in Ohio, card's current. Two years "
            "with Summit doing commercial rough-in — copper, PVC, some cast iron.\n"
            "Interviewer: Apprentice registration number valid?\n"
            "Candidate: Yes, PL-48291, renewed in March. My hours are logged through the union "
            "book and company.\n"
            "Interviewer: OSHA 10?\n"
            "Candidate: Got it in 2023. I have my own press tool and basic hand tools.\n"
            "Interviewer: Day shift travel around Columbus. Any restrictions?\n"
            "Candidate: None. I have a truck and can start in ten days."
        ),
    },
    {
        "id": "st-010",
        "vertical": "skilled_trades",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": (
            "First-year apprentice with pipefitting exposure on industrial plumbing and current "
            "registration. Meets minimum experience for apprentice-tier commercial role."
        ),
        "resume": (
            "Nina Kowalski\nPlumbing Apprentice — 1st year\n\n"
            "Great Lakes Pipe — Apprentice (2024–2025)\n"
            "- Assisted with industrial pipefitting and plumbing on plant expansion\n"
            "- Threaded black iron, grooved pipe, PVC chemical waste lines\n"
            "- Registered apprentice #WI-11802 (current)\n\n"
            "Welder helper — Fabrication shop (2023–2024)\n\n"
            "Certifications: Apprentice registration, OSHA 10 (2024)\n"
            "Education: Trade center plumbing pre-apprenticeship"
        ),
        "job_description": (
            "Plumber Apprentice — Industrial Projects\n\n"
            "Requirements:\n"
            "- Registered apprentice or eligible for registration\n"
            "- 6+ months commercial or industrial plumbing/pipe experience\n"
            "- OSHA 10\n"
            "- Ability to read isometric sketches (training provided)\n"
            "- Day shift, some travel within Wisconsin\n\n"
            "Location: Milwaukee WI | Pay: $18–22/hr"
        ),
        "transcript": (
            "Thanks for taking the call. I'm screening for an industrial plumber apprentice on "
            "the Great Lakes corridor.\n\n"
            "I'm first year registered in Wisconsin, WI-11802. I've been with Great Lakes Pipe "
            "about a year on a plant expansion — threaded black iron, grooved systems, PVC for "
            "chemical waste.\n\n"
            "Before that I was a welder helper so I'm comfortable on industrial sites. OSHA 10 "
            "done last year.\n\n"
            "I can read basic isometrics with journeyman check. I have a car and can travel "
            "within a couple hours of Milwaukee.\n\n"
            "Looking to stay on commercial-industrial path for my hours. I can start two weeks "
            "out."
        ),
    },
    {
        "id": "st-011",
        "vertical": "skilled_trades",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Not a registered plumbing apprentice and only informal residential helper work. "
            "Client requires active apprentice card for insurance and journeyman ratio compliance."
        ),
        "resume": (
            "Tommy Reed\nPlumbing Helper | 8 months informal\n\n"
            "Uncle's side jobs — Residential repairs (2024–2025)\n"
            "- Assisted with fixture swaps and drain cleaning\n"
            "- No registered apprenticeship\n"
            "- No commercial experience\n\n"
            "Landscaping labor (2023–2024)\n\n"
            "Education: High school diploma\n"
            "Certifications: None"
        ),
        "job_description": (
            "Plumber Apprentice — Registered Required\n\n"
            "Requirements:\n"
            "- Active state plumbing apprentice registration (mandatory)\n"
            "- 6+ months commercial plumbing experience\n"
            "- OSHA 10 within 30 days of hire\n"
            "- Day shift\n\n"
            "Location: Nashville TN | Pay: $17–21/hr"
        ),
        "transcript": (
            "Interviewer: Tommy, tell me about your plumbing background.\n"
            "Candidate: I've helped my uncle on weekends — toilets, faucets, drain snakes, "
            "mostly houses.\n"
            "Interviewer: Are you a registered apprentice?\n"
            "Candidate: No, we never set that up. It's been cash side work while I figure out "
            "the trade.\n"
            "Interviewer: This GC requires an active apprentice card for insurance. Any commercial?\n"
            "Candidate: Not on a real jobsite. I'd register if the company sponsors me.\n"
            "Interviewer: They won't sponsor unregistered helpers for this slot. OSHA 10?\n"
            "Candidate: Don't have it yet."
        ),
    },
    {
        "id": "st-012",
        "vertical": "skilled_trades",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Candidate disclosed recent failed pre-employment drug screen at prior employer. "
            "Client facility requires strict drug-free policy with no exceptions for plumbing apprentice role."
        ),
        "resume": (
            "Jason Pike\nPlumbing Apprentice — 1st year\n\n"
            "Blue River Plumbing — Apprentice (2024–2025)\n"
            "- Commercial rough-in experience 10 months\n"
            "- Registered apprentice #TN-33017\n"
            "- Terminated after failed drug screen (disclosed)\n\n"
            "Certifications: Apprentice registration, OSHA 10"
        ),
        "job_description": (
            "Plumber Apprentice — Commercial\n\n"
            "Requirements:\n"
            "- Registered apprentice in good standing\n"
            "- 6+ months commercial plumbing\n"
            "- Pass background and drug screen\n"
            "- OSHA 10\n"
            "- Zero tolerance drug policy on client site\n\n"
            "Location: Nashville TN | Pay: $18–22/hr"
        ),
        "transcript": (
            "Interviewer: Jason, walk me through your apprentice background.\n"
            "Candidate: First-year registered, about ten months commercial rough-in with Blue River.\n"
            "Interviewer: Why did you leave?\n"
            "Candidate: I failed a random drug screen last month. They let me go. I'm being "
            "straight about it — I want a clean start.\n"
            "Interviewer: This client does hair follicle testing and won't hire anyone with a "
            "failed screen in the last twelve months.\n"
            "Candidate: I haven't used since then. I'm in NA meetings now.\n"
            "Interviewer: I appreciate the honesty, but their policy is automatic disqualification. "
            "Anything else I should know?\n"
            "Candidate: No, that was the only issue. Skills-wise I was doing fine on the crew."
        ),
    },
    {
        "id": "st-013",
        "vertical": "skilled_trades",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Five years industrial maintenance with strong mechanical troubleshooting, current OSHA "
            "10, and experience on pumps, conveyors, and PM programs. Good fit for plant mechanic role."
        ),
        "resume": (
            "Robert Gaines\nIndustrial Maintenance Mechanic | 5 years\n\n"
            "PackRight Foods — Maintenance Mechanic II (2020–2025)\n"
            "- Repaired packaging lines, pneumatic systems, and conveyor drives\n"
            "- Performed preventive maintenance on pumps and gearboxes\n"
            "- OSHA 10 and forklift certified\n"
            "- Responded to breakdowns with avg downtime reduction 15% YoY\n\n"
            "Machine operator — Automotive supplier (2018–2020)\n\n"
            "Certifications: OSHA 10, forklift, lockout/tagout authorized\n"
            "Skills: Bearings, belts, alignment, basic welding, CMMS (Maximo)"
        ),
        "job_description": (
            "Maintenance Mechanic — Food Manufacturing\n\n"
            "Responsibilities:\n"
            "- Troubleshoot and repair production equipment\n"
            "- Execute PM schedules and document work in CMMS\n"
            "- Support sanitation windows and emergency breakdowns\n\n"
            "Requirements:\n"
            "- 3+ years industrial maintenance mechanic experience\n"
            "- Experience with conveyors, pumps, and pneumatic systems\n"
            "- OSHA 10 and LOTO training\n"
            "- 2nd or 3rd shift rotation\n"
            "- Food manufacturing experience preferred\n\n"
            "Location: Omaha NE | Pay: $27–33/hr"
        ),
        "transcript": (
            "Interviewer: Robert, this maintenance mechanic role is in a food plant on rotating "
            "shifts. Tell me about your experience.\n"
            "Candidate: Five years at PackRight on packaging lines — conveyors, fillers, "
            "pneumatics, pumps. I run PMs in Maximo and handle breakdowns on second shift.\n"
            "Interviewer: OSHA and LOTO?\n"
            "Candidate: OSHA 10, LOTO authorized, forklift cert current. No safety write-ups.\n"
            "Interviewer: Shift rotation 2nd and 3rd every eight weeks. Workable?\n"
            "Candidate: Yes, I've rotated shifts there for two years. I prefer 2nd but can do 3rd.\n"
            "Interviewer: Why leave?\n"
            "Candidate: Plant closure announced — last day is end of next month."
        ),
    },
    {
        "id": "st-014",
        "vertical": "skilled_trades",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Multi-trade building maintenance background with HVAC, plumbing, and electrical "
            "basics. OSHA 10 current; strong fit for facilities mechanic supporting commercial portfolio."
        ),
        "resume": (
            "Angela Ruiz\nBuilding Maintenance Mechanic | 4 years\n\n"
            "Crown Property Management — Facilities Tech (2021–2025)\n"
            "- Maintained HVAC, plumbing, and electrical in 12-building office portfolio\n"
            "- Completed work orders, vendor coordination, after-hours emergencies\n"
            "- OSHA 10 (2022, current)\n"
            "- EPA 608 Type I for small appliance charging\n\n"
            "Apartment maintenance — Turn tech (2019–2021)\n\n"
            "Certifications: OSHA 10, EPA 608 Type I\n"
            "Skills: BAS troubleshooting basics, door hardware, minor electrical, plumbing repairs"
        ),
        "job_description": (
            "Maintenance Mechanic — Commercial Facilities\n\n"
            "Responsibilities:\n"
            "- Respond to tenant work orders across office portfolio\n"
            "- Perform HVAC filter changes, minor plumbing/electrical repairs\n"
            "- Coordinate with vendors on major repairs\n\n"
            "Requirements:\n"
            "- 3+ years building maintenance or facilities mechanic experience\n"
            "- OSHA 10\n"
            "- Valid driver's license; company van provided\n"
            "- On-call rotation one week per month\n"
            "- Day shift with occasional after-hours emergencies\n\n"
            "Location: Atlanta GA | Pay: $22–27/hr"
        ),
        "transcript": (
            "Interviewer: Angela, this is a facilities maintenance mechanic for an office "
            "portfolio. What's your background?\n"
            "Candidate: Four years with Crown Property — twelve office buildings. HVAC PMs, "
            "plumbing clogs, ballasts, door hardware, after-hours leaks.\n"
            "Interviewer: OSHA 10?\n"
            "Candidate: Yes, current since 2022. I also have EPA Type I for small splits in "
            "server rooms.\n"
            "Interviewer: On-call one week a month including weekends. OK?\n"
            "Candidate: I've done on-call there for two years. My phone is always on during rotation.\n"
            "Interviewer: Driver's license clean?\n"
            "Candidate: Clean MVR. They gave me a company van at Crown."
        ),
    },
    {
        "id": "st-015",
        "vertical": "skilled_trades",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Janitorial and light custodial background only — no mechanical repair experience "
            "on production equipment. Does not meet industrial maintenance mechanic requirements."
        ),
        "resume": (
            "Marcus Lee\nJanitor / Custodian | 3 years\n\n"
            "CleanPro Services — Janitor (2022–2025)\n"
            "- Floor care, restroom cleaning, trash removal\n"
            "- Changed HVAC filters when requested (no repairs)\n"
            "- No conveyor, pump, or machine repair experience\n\n"
            "Fast food crew member (2020–2022)\n\n"
            "Education: High school diploma\n"
            "Certifications: None"
        ),
        "job_description": (
            "Industrial Maintenance Mechanic\n\n"
            "Requirements:\n"
            "- 2+ years industrial maintenance or machine repair experience\n"
            "- Troubleshoot mechanical drives, bearings, pneumatics\n"
            "- OSHA 10\n"
            "- 2nd shift manufacturing environment\n\n"
            "Location: Detroit MI | Pay: $26–31/hr"
        ),
        "transcript": (
            "Interviewer: Marcus, tell me about your maintenance mechanic experience.\n"
            "Candidate: I've been janitorial at a factory — mopping, trash, cleaning production "
            "floors after shift.\n"
            "Interviewer: Any machine repairs or PM work?\n"
            "Candidate: Sometimes I change air filters if maintenance is busy. I don't fix "
            "conveyors or pumps.\n"
            "Interviewer: This role is mechanic-level — bearings, alignments, breakdown response.\n"
            "Candidate: I want to move into that but I haven't gotten the chance.\n"
            "Interviewer: OSHA 10?\n"
            "Candidate: No. I watch the safety videos when they make us."
        ),
    },
    {
        "id": "st-016",
        "vertical": "skilled_trades",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": (
            "Mechanical experience is relevant but candidate cannot work at heights due to "
            "medical restriction. Role requires rooftop HVAC and elevated conveyor work — safety disqualifier."
        ),
        "resume": (
            "Paul Henning\nMaintenance Mechanic | 3 years\n\n"
            "Metro Manufacturing — Mechanic (2022–2025)\n"
            "- Repaired assembly line equipment at ground level\n"
            "- OSHA 10 (2022)\n"
            "- Medical restriction: no work above 6 feet (doctor note on file)\n\n"
            "Machine repair helper (2020–2022)\n\n"
            "Certifications: OSHA 10"
        ),
        "job_description": (
            "Maintenance Mechanic — Multi-Site Manufacturing\n\n"
            "Requirements:\n"
            "- 2+ years industrial maintenance experience\n"
            "- Comfortable working at heights on mezzanines and rooftop units\n"
            "- OSHA 10, fall protection training\n"
            "- 1st shift with travel between two plants\n\n"
            "Location: Indianapolis IN | Pay: $25–30/hr"
        ),
        "transcript": (
            "Screening for maintenance mechanic covering two plants with mezzanine lines and "
            "rooftop HVAC.\n\n"
            "Three years at Metro on assembly equipment — motors, belts, pneumatics at floor level. "
            "OSHA 10 from 2022.\n\n"
            "I need to be upfront — I have a vertigo issue after a concussion. My doctor gave a "
            "note saying no work above six feet. Metro accommodated me on ground-level jobs only.\n\n"
            "This posting mentions rooftop units and mezzanine conveyors regularly. I don't think "
            "I can safely do the height parts even with a harness.\n\n"
            "Mechanically I'm solid on the floor stuff but I understand if that's a dealbreaker."
        ),
    },
    {
        "id": "st-017",
        "vertical": "skilled_trades",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Six years diesel fleet experience with current CDL Class A and ASE T2/T4 certifications. "
            "Strong PM and DOT inspection background; available for early-shift fleet shop role."
        ),
        "resume": (
            "Samuel Ortiz\nDiesel Mechanic | 6 years\n\n"
            "FleetCo Logistics — Lead Diesel Tech (2019–2025)\n"
            "- Maintained Class 8 fleet: engines, aftertreatment, brakes, air systems\n"
            "- ASE T2 Diesel Engines, T4 Brakes (current)\n"
            "- CDL Class A with clean MVR\n"
            "- DOT annual inspection certified\n"
            "- OSHA 10 (2021)\n\n"
            "Diesel apprentice — Truck dealership (2017–2019)\n\n"
            "Certifications: ASE T2, T4, CDL Class A, DOT inspector\n"
            "Tools: Own diagnostics laptop (JPRO), pneumatic tools"
        ),
        "job_description": (
            "Diesel Mechanic — Fleet Maintenance Shop\n\n"
            "Responsibilities:\n"
            "- Diagnose and repair Class 7–8 trucks and trailers\n"
            "- Perform PM services and DOT inspections\n"
            "- Document repairs in fleet management system\n\n"
            "Requirements:\n"
            "- 4+ years diesel mechanic experience on heavy trucks\n"
            "- CDL Class A or B (required for road tests)\n"
            "- ASE certification preferred (T2 minimum)\n"
            "- Early shift 5am–1:30pm Mon–Sat rotation\n"
            "- Pass background and motor vehicle check\n\n"
            "Location: San Antonio TX | Pay: $30–38/hr"
        ),
        "transcript": (
            "Interviewer: Samuel, this is a fleet diesel shop role. Walk me through your background.\n"
            "Candidate: Six years at FleetCo on Class 8 trucks — Cummins, Detroit, aftertreatment, "
            "brakes, PMs, DOT inspections.\n"
            "Interviewer: CDL and ASE status?\n"
            "Candidate: CDL Class A, clean MVR. ASE T2 and T4 renewed last fall.\n"
            "Interviewer: Early shift starts 5 AM, some Saturdays. OK?\n"
            "Candidate: That's my current schedule. No problem.\n"
            "Interviewer: Road test drives required occasionally. Any license issues?\n"
            "Candidate: None. I do road tests weekly for comeback verification."
        ),
    },
    {
        "id": "st-018",
        "vertical": "skilled_trades",
        "decision": "select",
        "difficulty": "borderline",
        "ingest_format": "labeled",
        "reason": (
            "Four years municipal fleet diesel experience with CDL Class B and OSHA 10. Lacks ASE "
            "but strong hydraulic and brake work; client accepts equivalent experience for journeyman slot."
        ),
        "resume": (
            "Diane Foster\nDiesel Mechanic | 4 years\n\n"
            "City of Riverside — Fleet Mechanic (2021–2025)\n"
            "- Maintained fire apparatus, dump trucks, and transit buses\n"
            "- Hydraulic systems, air brakes, exhaust aftertreatment\n"
            "- CDL Class B (current)\n"
            "- OSHA 10 (2023)\n"
            "- No ASE certs (city paid for internal training only)\n\n"
            "Auto tech — Quick lube and brakes (2019–2021)\n\n"
            "Certifications: CDL Class B, OSHA 10\n"
            "Training: Allison transmission course, hydraulic troubleshooting"
        ),
        "job_description": (
            "Diesel Mechanic — Municipal Fleet Contractor\n\n"
            "Requirements:\n"
            "- 3+ years heavy diesel mechanic experience\n"
            "- CDL Class B minimum\n"
            "- Experience on air brakes and hydraulic systems\n"
            "- ASE preferred but not mandatory with equivalent experience\n"
            "- Day shift, government background check\n\n"
            "Location: Riverside CA | Pay: $32–36/hr"
        ),
        "transcript": (
            "Interviewer: Diane, tell me about your diesel experience.\n"
            "Candidate: Four years with Riverside city fleet — fire trucks, dumps, buses. Air "
            "brakes, hydraulics, DEF systems.\n"
            "Interviewer: ASE certifications?\n"
            "Candidate: Not yet. The city used in-house training. I've done Allison trans course "
            "and hydraulic troubleshooting workshops.\n"
            "Interviewer: CDL?\n"
            "Candidate: Class B, current, clean record. I road-test buses after brake jobs.\n"
            "Interviewer: This client prefers ASE but allows proven experience. Any gov clearance issues?\n"
            "Candidate: No. I pass city background every year. OSHA 10 done in 2023.\n"
            "Interviewer: Start timeline?\n"
            "Candidate: Two weeks notice to the city, then available."
        ),
    },
    {
        "id": "st-019",
        "vertical": "skilled_trades",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": (
            "Auto/light-duty mechanic background only with no heavy diesel or Class 7–8 experience. "
            "No CDL; role requires road-testing fleet trucks after repair."
        ),
        "resume": (
            "Greg Walsh\nAutomotive Technician | 5 years light-duty\n\n"
            "Express Auto Care — Technician (2020–2025)\n"
            "- Passenger car brakes, tires, oil changes, light diagnostics\n"
            "- No Class 7–8 truck work\n"
            "- No CDL\n"
            "- ASE A1, A4 (automobile only)\n\n"
            "Tire shop — Technician (2018–2020)\n\n"
            "Certifications: ASE A1, A4\n"
            "Education: Automotive technology certificate"
        ),
        "job_description": (
            "Diesel Mechanic — Heavy Fleet\n\n"
            "Requirements:\n"
            "- 3+ years diesel mechanic on Class 7–8 trucks\n"
            "- CDL Class A or B required for road tests\n"
            "- Air brake and aftertreatment experience\n"
            "- ASE T-series preferred\n\n"
            "Location: El Paso TX | Pay: $28–34/hr"
        ),
        "transcript": (
            "Interviewer: Greg, this role is heavy diesel fleet. What's your truck experience?\n"
            "Candidate: I've been at Express Auto five years — cars and small SUVs, brakes, "
            "suspension, diagnostics.\n"
            "Interviewer: Any Class 8 or diesel truck work?\n"
            "Candidate: Not really. Maybe a Sprinter van once. Mostly Hondas, Fords, that kind.\n"
            "Interviewer: CDL?\n"
            "Candidate: No. I don't drive trucks for work.\n"
            "Interviewer: We need road tests on repaired semis. ASE diesel?\n"
            "Candidate: I have A1 and A4 for automobiles. I'd need training on the big stuff."
        ),
    },
    {
        "id": "st-020",
        "vertical": "skilled_trades",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": (
            "CDL Class A suspended due to DUI — cannot perform required road tests. Diesel "
            "experience is otherwise adequate but license disqualification is non-negotiable for fleet role."
        ),
        "resume": (
            "Miguel Torres\nDiesel Mechanic | 4 years\n\n"
            "TransWest Truck Center — Diesel Tech (2021–2025)\n"
            "- Class 8 engine and brake repairs\n"
            "- CDL Class A — SUSPENDED (DUI, eligible reinstatement in 8 months)\n"
            "- ASE T2 (expired 2024)\n\n"
            "Diesel helper — Independent shop (2019–2021)\n\n"
            "Certifications: ASE T2 (expired), CDL Class A (suspended)"
        ),
        "job_description": (
            "Diesel Mechanic — Dealership Fleet Account\n\n"
            "Requirements:\n"
            "- 3+ years Class 8 diesel repair experience\n"
            "- Active CDL Class A or B — required for road tests and moving units\n"
            "- Clean MVR per client insurance\n"
            "- Current ASE T2 preferred\n\n"
            "Location: Albuquerque NM | Pay: $29–35/hr"
        ),
        "transcript": (
            "Interviewer: Miguel, tell me about your diesel background for this fleet account.\n"
            "Candidate: Four years at TransWest on Class 8 — engines, brakes, aftertreatment, "
            "the whole thing.\n"
            "Interviewer: CDL status?\n"
            "Candidate: I had Class A but it's uh suspended right now. DUI last year. I can get it "
            "back in like eight months.\n"
            "Interviewer: This client requires active CDL for road tests — insurance won't budge.\n"
            "Candidate: Mechanically I'm strong. I just can't legally drive on the road till "
            "reinstatement.\n"
            "Interviewer: ASE T2 current?\n"
            "Candidate: It expired 2024. I was gonna renew when the license thing got sorted."
        ),
    },
]

assert len(SKILLED_TRADES_RECORDS) == 20
assert sum(1 for r in SKILLED_TRADES_RECORDS if r["decision"] == "select") == 10
assert sum(1 for r in SKILLED_TRADES_RECORDS if r["decision"] == "reject") == 10
