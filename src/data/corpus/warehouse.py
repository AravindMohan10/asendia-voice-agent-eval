"""Warehouse and logistics vertical — staffing phone screen eval records."""

from __future__ import annotations

WAREHOUSE_RECORDS: list[dict] = [
    {
        "id": "wh-001",
        "vertical": "warehouse",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": "Active OSHA forklift certification, four years sit-down and stand-up experience, available for required 2nd shift.",
        "resume": (
            "Marcus Johnson | Forklift Operator\n"
            "742 Oak Ridge Lane, Dayton, OH 45414 | (937) 555-0182 | mjohnson47@email.com\n\n"
            "EXPERIENCE\n"
            "Forklift Operator — MidStates Distribution, Vandalia OH (2019–Present)\n"
            "• Operate sit-down and stand-up forklifts; load/unload 40+ trailers weekly\n"
            "• Maintain 99.2% inventory accuracy on cycle counts\n"
            "• OSHA Forklift Certification renewed March 2025\n\n"
            "Warehouse Associate — Premier Logistics, Springfield OH (2017–2019)\n"
            "• Pick, pack, and stage outbound orders using RF scanner\n\n"
            "CERTIFICATIONS: OSHA Powered Industrial Truck Operator (valid through 2027)"
        ),
        "job_description": (
            "Forklift Operator — Apex Staffing / Client: Regional Distribution Center, Dayton OH\n"
            "Shift: 2nd (3:00 PM – 11:30 PM), Mon–Fri, occasional Saturday OT\n"
            "Pay: $19.50/hr temp-to-perm\n\n"
            "Requirements:\n"
            "• Valid OSHA forklift certification (sit-down and stand-up)\n"
            "• Minimum 2 years warehouse forklift experience\n"
            "• Ability to lift 50 lbs and work in non-climate-controlled environment\n"
            "• Pass background check and drug screen"
        ),
        "transcript": (
            "Recruiter: Hi Marcus, this is Sarah from Apex Staffing returning your application "
            "for the forklift operator role in Dayton. Do you have a minute?\n"
            "Candidate: Yeah, sure. I put in for that last week.\n"
            "Recruiter: Great. I see you listed MidStates Distribution — are you still there?\n"
            "Candidate: Yes ma'am, still working second shift. That's actually why this caught my eye, "
            "same shift window.\n"
            "Recruiter: Perfect. Your resume shows OSHA cert — is that current?\n"
            "Candidate: Renewed it in March, good through 2027. I run sit-down and stand-up daily.\n"
            "Recruiter: And you're comfortable with the physical side — fifty-pound lifts, warehouse temps?\n"
            "Candidate: Absolutely. I've been on the dock four years. No problem there.\n"
            "Recruiter: If the client likes your profile we can get you in for orientation next week. "
            "Does that timeline work?\n"
            "Candidate: Yeah, I can start as soon as you need me."
        ),
    },
    {
        "id": "wh-002",
        "vertical": "warehouse",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": "Two years picker/packer at Amazon FC, day shift matches, confirmed Monday start date.",
        "resume": (
            "Daniela Ruiz | Picker/Packer\n"
            "118 Birch Street, Hebron, KY 41048 | (859) 555-0341 | druiz.kentucky@gmail.com\n\n"
            "EXPERIENCE\n"
            "Picker/Packer — Amazon Fulfillment Center CVG1, Hebron KY (2022–2024)\n"
            "• Pick rate averaged 320 UPH; zero safety write-ups\n"
            "• Packaged single and multi-line orders; operated conveyors and divert systems\n"
            "• Trained on stowing and problem-solve stations\n\n"
            "Retail Associate — Target, Florence KY (2020–2022)\n"
            "• Stocked backroom, pulled online pickup orders\n\n"
            "EDUCATION: Boone County High School, diploma 2020"
        ),
        "job_description": (
            "Picker/Packer — Apex Staffing / Client: E-commerce Fulfillment, Hebron KY\n"
            "Shift: 1st (6:00 AM – 2:30 PM), Mon–Fri\n"
            "Pay: $17.25/hr\n\n"
            "Requirements:\n"
            "• 6+ months pick/pack or fulfillment experience\n"
            "• Comfortable standing 8+ hours and meeting pick-rate targets\n"
            "• Day shift availability required\n"
            "• Steel-toe boots required on day one"
        ),
        "transcript": (
            "Sarah: Hi Daniela, Sarah calling from Apex Staffing about the picker packer "
            "position in Hebron. Is now okay?\n"
            "Candidate: Hi, yes, I'm off today.\n"
            "Sarah: You worked at CVG1 for about two years — what were you doing day to day?\n"
            "Candidate: Mostly pick and pack on the outbound side. I was running around three "
            "twenty units per hour most weeks.\n"
            "Sarah: This role is first shift, six AM start. Any conflicts?\n"
            "Candidate: No, that's what I want. I left Amazon because I needed days for my kid's "
            "school schedule.\n"
            "Sarah: We have a Monday orientation if your background clears. Could you make that?\n"
            "Candidate: Yes, I can start Monday. I already have steel toes."
        ),
    },
    {
        "id": "wh-003",
        "vertical": "warehouse",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": "Three years general warehouse with RF scanner and WMS experience; candidate lives locally in Riverside.",
        "resume": (
            "James Okonkwo | Warehouse Associate\n"
            "905 Magnolia Ave, Riverside, CA 92507 | (951) 555-0923 | jokonkwo.r@gmail.com\n\n"
            "EXPERIENCE\n"
            "Warehouse Associate — Inland Warehousing Solutions, Riverside CA (2021–Present)\n"
            "• Receive, put-away, and pick using Zebra RF guns and Manhattan WMOS\n"
            "• Operate electric pallet jack; assist with cycle counts\n"
            "• Cross-trained on shipping dock manifest verification\n\n"
            "Material Handler — AutoParts Direct, Ontario CA (2019–2021)\n"
            "• Staged parts for line-side delivery; maintained 5S standards\n\n"
            "SKILLS: RF scanning, WMS, pallet jack, inventory control, bilingual English/Spanish"
        ),
        "job_description": (
            "Warehouse Associate — Apex Staffing / Client: Automotive Parts DC, Riverside CA\n"
            "Shift: 1st (7:00 AM – 3:30 PM), Mon–Sat rotating\n"
            "Pay: $18.00/hr\n\n"
            "Requirements:\n"
            "• 1+ year warehouse experience with RF scanner\n"
            "• Familiarity with WMS preferred\n"
            "• Reliable transportation; site is not on public transit route\n"
            "• Bilingual Spanish a plus"
        ),
        "transcript": (
            "Thanks for applying to the warehouse associate role. I'm calling from Apex Staffing. "
            "Can you tell me about your current warehouse experience?\n\n"
            "I've been at Inland Warehousing for three years. I do receiving and picking on RF guns, "
            "mostly Manhattan. I also help on the dock when they're backed up.\n\n"
            "This is in Riverside off the 91. How far are you from that location?\n\n"
            "About ten minutes. I live on Magnolia, so it's basically local for me.\n\n"
            "The shift is first shift with some Saturday rotation. Any issues with that?\n\n"
            "No, I've been on a similar schedule. Saturdays are fine.\n\n"
            "Good. We'll run your background and if everything checks out we'll schedule a site tour."
        ),
    },
    {
        "id": "wh-004",
        "vertical": "warehouse",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": "Eighteen months outbound shipping clerk experience with UPS WorldShip; start date confirmed for next Tuesday.",
        "resume": (
            "Patricia Nguyen | Shipping Clerk\n"
            "44 Harbor View Dr, Newark, NJ 07105 | (973) 555-0617 | pnguyen.shipping@outlook.com\n\n"
            "EXPERIENCE\n"
            "Shipping Clerk — Harbor Freight Components, Newark NJ (2023–Present)\n"
            "• Process 80–120 outbound parcels daily via UPS WorldShip and FedEx Ship Manager\n"
            "• Generate BOLs for LTL freight; verify hazmat paperwork for sealed lead-acid batteries\n"
            "• Coordinate with carriers for pickup windows\n\n"
            "Office Assistant — Nguyen Family Imports, Jersey City NJ (2021–2023)\n"
            "• Data entry, invoicing, light customer service\n\n"
            "SKILLS: UPS WorldShip, FedEx Ship Manager, MS Excel, detail-oriented"
        ),
        "job_description": (
            "Shipping Clerk — Apex Staffing / Client: Industrial Supply Wholesaler, Newark NJ\n"
            "Shift: 1st (8:00 AM – 4:30 PM), Mon–Fri\n"
            "Pay: $20.00/hr\n\n"
            "Requirements:\n"
            "• 1+ year shipping clerk or outbound logistics experience\n"
            "• Proficiency with UPS WorldShip or comparable multi-carrier software\n"
            "• Accurate data entry; high volume parcel environment\n"
            "• Hazmat awareness training preferred"
        ),
        "transcript": (
            "Hi Patricia, Apex Staffing here regarding the shipping clerk opening on Frelinghuysen Avenue.\n\n"
            "Hi, yes I applied online yesterday.\n\n"
            "Walk me through your shipping experience at Harbor Freight Components.\n\n"
            "I handle outbound small parcel mostly, UPS and FedEx. I use WorldShip every day, "
            "probably a hundred labels on busy days. I also do bills of lading for pallet freight.\n\n"
            "We need someone who can jump in on WorldShip quickly. Comfortable with that?\n\n"
            "Yes, that's basically my whole job right now. I also did hazmat awareness last year "
            "for battery shipments.\n\n"
            "If background comes back clean we have orientation next Tuesday. Can you start then?\n\n"
            "Tuesday works. I'll bring my ID and direct deposit info."
        ),
    },
    {
        "id": "wh-005",
        "vertical": "warehouse",
        "decision": "select",
        "difficulty": "borderline",
        "ingest_format": "asr_paragraph",
        "reason": "Limited RF scanner tenure (six months) but strong attendance and supervisor reference; recruiter advanced to client interview.",
        "resume": (
            "Tyler Brennan | Warehouse Associate\n"
            "203 Mill Road, Lowell, MA 01852 | (978) 555-0448 | tbrennan.lowell@yahoo.com\n\n"
            "EXPERIENCE\n"
            "Warehouse Associate — New England Paper Goods, Lowell MA (2024–Present)\n"
            "• Pick and stage corrugated orders; RF scanner training completed June 2024\n"
            "• Load outbound trucks; maintain clean aisle standards\n\n"
            "General Labor — City of Lowell DPW seasonal (2022–2023)\n"
            "• Grounds maintenance, snow removal crew\n\n"
            "REFERENCES: Supervisor Mark Deluca, New England Paper Goods — available upon request"
        ),
        "job_description": (
            "Warehouse Associate — Apex Staffing / Client: Paper Products DC, Lowell MA\n"
            "Shift: 2nd (2:00 PM – 10:30 PM), Mon–Fri\n"
            "Pay: $17.75/hr\n\n"
            "Requirements:\n"
            "• 1+ year warehouse experience\n"
            "• RF scanner proficiency required\n"
            "• Consistent attendance record\n"
            "• Ability to work in dusty environment"
        ),
        "transcript": (
            "Tyler, thanks for picking up. I'm with Apex Staffing on the warehouse associate role in Lowell.\n\n"
            "Hey, yeah, I've been waiting to hear back on that one.\n\n"
            "Your resume shows about a year at New England Paper Goods. How much RF scanner work?\n\n"
            "Honestly about six months on the gun. Before that I was on the loading dock without scanners. "
            "But I've gotten pretty fast — my supervisor Mark can vouch for me.\n\n"
            "The client wants someone comfortable on RF from day one. That's a gap. What's your pick rate like now?\n\n"
            "I'm hitting their targets most days. I haven't had a attendance issue since I started.\n\n"
            "I'm going to flag the limited scanner time but send you to the client interview. "
            "They make the final call. Orientation would be Thursday if they approve.\n\n"
            "I appreciate that. I'll study their WMS videos tonight."
        ),
    },
    {
        "id": "wh-006",
        "vertical": "warehouse",
        "decision": "select",
        "difficulty": "borderline",
        "ingest_format": "asr_noisy",
        "reason": "Forklift cert expired two months ago but renewal exam scheduled Friday; six years experience; recruiter proceeding pending cert upload.",
        "resume": (
            "Robert Kowalski | Forklift Operator\n"
            "6612 45th St, Kenosha, WI 53144 | (262) 555-0771 | rkowalski.wi@gmail.com\n\n"
            "EXPERIENCE\n"
            "Forklift Operator — Great Lakes Beverage, Kenosha WI (2018–Present)\n"
            "• Operate sit-down propane forklifts in cold-storage dock\n"
            "• Load route trucks; average 35 pallets per shift\n"
            "• OSHA Forklift Certification (expired April 2025 — renewal scheduled)\n\n"
            "Dock Worker — Wisconsin Distributors, Racine WI (2016–2018)\n"
            "• Manual palletizing, hand truck operations"
        ),
        "job_description": (
            "Forklift Operator — Apex Staffing / Client: Beverage Distribution, Kenosha WI\n"
            "Shift: 3rd (10:00 PM – 6:30 AM), Sun–Thu\n"
            "Pay: $21.00/hr\n\n"
            "Requirements:\n"
            "• Current OSHA forklift certification required before start\n"
            "• 3+ years sit-down forklift in production or distribution\n"
            "• Cold-storage experience preferred\n"
            "• Third-shift availability mandatory"
        ),
        "transcript": (
            "Hi Robert, um Apex Staffing calling bout the forklift job in Kenosha. You still interested?\n\n"
            "Yeah definitely. I'm on third shift now so the hours line up.\n\n"
            "I see six years on forklifts at Great Lakes Beverage. Cert status?\n\n"
            "So mine expired in April — I slacked on renewal. I got the retest booked this Friday "
            "at the safety training center.\n\n"
            "Client won't let anyone on a lift without current OSHA card. That's a problem.\n\n"
            "I know, I know. I've been operating the whole time though, zero incidents. "
            "I can email you the appointment confirmation.\n\n"
            "If you pass Friday and send the card Monday we'll move you to orientation Wednesday. "
            "No cert, no start — fair?\n\n"
            "Fair enough. I'll get it done."
        ),
    },
    {
        "id": "wh-007",
        "vertical": "warehouse",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": "Lives twelve minutes from site, prior temp assignment at same client, confirmed 6 AM start availability.",
        "resume": (
            "Angela Morris | Picker/Packer\n"
            "312 Sycamore Ct, Florence, AL 35630 | (256) 555-0289 | amorris.florence@gmail.com\n\n"
            "EXPERIENCE\n"
            "Picker/Packer — Apex Staffing @ HomeStyle Brands DC, Florence AL (Temp, 2023)\n"
            "• Converted from temp; left for family caregiving\n"
            "• Pick-to-tote, pack station, met 98% accuracy standard\n\n"
            "Cashier — Piggly Wiggly, Florence AL (2021–2023)\n"
            "• Stocked shelves, handled freight deliveries\n\n"
            "Available for immediate start; reliable transportation"
        ),
        "job_description": (
            "Picker/Packer — Apex Staffing / Client: HomeStyle Brands DC, Florence AL\n"
            "Shift: 1st (6:00 AM – 2:00 PM), Mon–Fri\n"
            "Pay: $16.50/hr\n\n"
            "Requirements:\n"
            "• Pick/pack experience preferred; former temps at this site welcome\n"
            "• 6 AM start time non-negotiable\n"
            "• Must live within reasonable commute — attendance critical\n"
            "• Steel-toe footwear required"
        ),
        "transcript": (
            "Recruiter: Angela, hi, it's Megan from Apex Staffing. You applied for the HomeStyle "
            "picker packer role — I actually see you temped there before.\n"
            "Candidate: Yes, in twenty twenty-three. I had to leave when my mom got sick.\n"
            "Recruiter: Understood. Are you looking to go back to that same building?\n"
            "Candidate: Yes, I liked the team. I know the layout already.\n"
            "Recruiter: It's a six AM sharp start. How far are you from the DC?\n"
            "Candidate: Twelve minutes. I'm on Sycamore off Cox Creek.\n"
            "Recruiter: And your availability — any restrictions?\n"
            "Candidate: None now. Mom's in assisted living. I can start next week.\n"
            "Recruiter: Perfect. I'll push your reinstatement through since you have prior time on site."
        ),
    },
    {
        "id": "wh-008",
        "vertical": "warehouse",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": "Active OSHA forklift certification covering cherry picker and stand-up; four years distribution center experience.",
        "resume": (
            "Devon Hayes | Forklift Operator\n"
            "1900 Industrial Pkwy, Columbus, OH 43228 | (614) 555-0534 | dhayes.ops@gmail.com\n\n"
            "EXPERIENCE\n"
            "Forklift Operator — Central Ohio Fulfillment, Grove City OH (2020–Present)\n"
            "• Certified on reach truck, order picker (cherry picker), and stand-up counterbalance\n"
            "• Slot replenishment in narrow-aisle racking up to 30 feet\n"
            "• OSHA PIT Certification valid through December 2026\n\n"
            "Warehouse Associate — Target DC, West Jefferson OH (2018–2020)\n"
            "• Unload trailers, build pallets, RF scanning"
        ),
        "job_description": (
            "Forklift Operator — Apex Staffing / Client: Grocery Distribution, Grove City OH\n"
            "Shift: 2nd (3:00 PM – 11:00 PM), Tue–Sat\n"
            "Pay: $20.25/hr\n\n"
            "Requirements:\n"
            "• Current OSHA certification on reach truck and order picker\n"
            "• 2+ years narrow-aisle experience\n"
            "• Comfortable with heights up to 30 ft\n"
            "• Pass drug screen and background check"
        ),
        "transcript": (
            "Devon Hayes? Hi, Apex Staffing regarding the forklift position at the grocery DC in Grove City.\n\n"
            "Speaking. I've been expecting your call.\n\n"
            "Which equipment are you certified on?\n\n"
            "Reach truck, order picker — we call it cherry picker — and stand-up counterbalance. "
            "All on one OSHA card renewed last year, good through twenty twenty-six.\n\n"
            "How much narrow-aisle work?\n\n"
            "Four years at Central Ohio Fulfillment. Daily slotting in thirty-foot racking.\n\n"
            "Second shift Tuesday through Saturday. Any conflicts?\n\n"
            "That's my current schedule basically. I'm ready to switch employers for the pay bump.\n\n"
            "We'll need a copy of your cert before scheduling the practical test on site.\n\n"
            "I can email it tonight."
        ),
    },
    {
        "id": "wh-009",
        "vertical": "warehouse",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": "Eighteen months outbound shipping experience with current hazmat awareness training; matches first shift.",
        "resume": (
            "Christopher Vega | Shipping Clerk\n"
            "77 Depot St, Allentown, PA 18101 | (610) 555-0812 | cvega.ship@icloud.com\n\n"
            "EXPERIENCE\n"
            "Shipping Clerk — Lehigh Valley Industrial Supply, Allentown PA (2023–Present)\n"
            "• Process outbound LTL and parcel shipments; 60–90 orders per day\n"
            "• Print shipping labels via FedEx Ship Manager; schedule carrier pickups\n"
            "• Hazmat awareness certification renewed January 2025\n\n"
            "Warehouse Associate — Staples DC, Hanover PA (2022–2023)\n"
            "• Pick and stage orders; operated pallet jack"
        ),
        "job_description": (
            "Shipping Clerk — Apex Staffing / Client: MRO Parts Distributor, Allentown PA\n"
            "Shift: 1st (7:30 AM – 4:00 PM), Mon–Fri\n"
            "Pay: $19.00/hr\n\n"
            "Requirements:\n"
            "• 1+ year shipping or outbound clerk experience\n"
            "• Experience with multi-carrier shipping software\n"
            "• Hazmat awareness certification preferred\n"
            "• Accurate order verification"
        ),
        "transcript": (
            "Is this Christopher Vega? Apex Staffing, uh, calling about the shipping clerk role.\n\n"
            "Yeah this is Chris. Sorry there's noise — I'm on break in the warehouse.\n\n"
            "No worries. Tell me about your shipping background.\n\n"
            "I've been shipping clerk at Lehigh Valley Industrial about a year and a half. "
            "FedEx ship manager mostly, some LTL bills of lading. I re-upped my hazmat awareness "
            "in January.\n\n"
            "First shift seven thirty to four. Does that work?\n\n"
            "That's literally my shift right now so yeah, no issue.\n\n"
            "We're looking for someone who can verify orders before they go out. Experience with that?\n\n"
            "I double-check weight dims and counts before I print labels. We had an audit last quarter "
            "and my area passed clean.\n\n"
            "Good. I'll submit your profile to the client today."
        ),
    },
    {
        "id": "wh-010",
        "vertical": "warehouse",
        "decision": "select",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": "Night shift availability matches, two years cross-dock warehouse experience, clean background expected.",
        "resume": (
            "Kevin O'Brien | Warehouse Associate\n"
            "528 Ridgewood Ave, Memphis, TN 38111 | (901) 555-0156 | kobrien.memphis@gmail.com\n\n"
            "EXPERIENCE\n"
            "Warehouse Associate — Mid-South Crossdock, Memphis TN (2022–Present)\n"
            "• Sort and stage LTL freight for linehaul departures\n"
            "• Operate electric pallet jack and floor loader\n"
            "• Night shift lead when supervisor off-floor\n\n"
            "Loader — FedEx Ground, Memphis TN (2020–2022)\n"
            "• Load delivery vans; scan packages to routes"
        ),
        "job_description": (
            "Warehouse Associate — Apex Staffing / Client: Crossdock Facility, Memphis TN\n"
            "Shift: 3rd (11:00 PM – 7:30 AM), Sun–Thu\n"
            "Pay: $18.50/hr\n\n"
            "Requirements:\n"
            "• Cross-dock or freight sorting experience preferred\n"
            "• Third-shift availability required\n"
            "• Pallet jack experience\n"
            "• Background check — felony theft convictions disqualify"
        ),
        "transcript": (
            "Recruiter: Kevin O'Brien? Hi, this is Jordan from Apex Staffing about the warehouse "
            "associate role at the crossdock on American Way.\n"
            "Candidate: Hey Jordan. Yeah I applied Friday night.\n"
            "Recruiter: I see crossdock experience at Mid-South. Still there?\n"
            "Candidate: Yep, on nights. Looking for something closer to home and a little more pay.\n"
            "Recruiter: This is third shift, eleven PM to seven thirty. Same as now?\n"
            "Candidate: Same hours actually. I'm a night person, works for my family.\n"
            "Recruiter: Any criminal history we should know about before background check?\n"
            "Candidate: No sir. Clean driving record too.\n"
            "Recruiter: Great. Pallet jack experience?\n"
            "Candidate: Daily. Electric jack and floor loader.\n"
            "Recruiter: I'll get you on the schedule for a site walkthrough Wednesday."
        ),
    },
    {
        "id": "wh-011",
        "vertical": "warehouse",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": "No OSHA forklift certification; candidate only operated manual pallet jacks, client requires certified operator on day one.",
        "resume": (
            "Luis Ortega | Warehouse Worker\n"
            "88 Pine Street, El Paso, TX 79901 | (915) 555-0623 | lortega.elpaso@yahoo.com\n\n"
            "EXPERIENCE\n"
            "Warehouse Worker — Borderlands Supply, El Paso TX (2023–Present)\n"
            "• Move freight with manual pallet jack and hand truck\n"
            "• Load/unload containers; shrink-wrap pallets\n"
            "• Assisted forklift operators with staging\n\n"
            "Construction Laborer — Various contractors, El Paso TX (2020–2023)"
        ),
        "job_description": (
            "Forklift Operator — Apex Staffing / Client: Import/Export Warehouse, El Paso TX\n"
            "Shift: 1st (6:00 AM – 2:30 PM), Mon–Fri\n"
            "Pay: $18.75/hr\n\n"
            "Requirements:\n"
            "• Valid OSHA forklift certification mandatory\n"
            "• Minimum 1 year operating sit-down forklift\n"
            "• Bilingual English/Spanish preferred\n"
            "• Near-border site; passport or FAST card helpful"
        ),
        "transcript": (
            "Recruiter: Luis, hi, Apex Staffing calling about the forklift operator job you applied for.\n"
            "Candidate: Hi, yes. I've been around forklifts a lot at my warehouse.\n"
            "Recruiter: Do you hold a current OSHA forklift certification?\n"
            "Candidate: Not officially. I move pallets with the manual jack mostly. "
            "Sometimes the certified guys let me practice on the sit-down.\n"
            "Recruiter: This client won't allow uncertified operators on equipment. It's a hard requirement.\n"
            "Candidate: Could I get certified after I start?\n"
            "Recruiter: They need someone certified day one. I'd suggest getting your OSHA card "
            "and reapplying — we run a class monthly.\n"
            "Candidate: Okay, I understand.\n"
            "Recruiter: I'll note that and close this req for now. Good luck with the training."
        ),
    },
    {
        "id": "wh-012",
        "vertical": "warehouse",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": "Candidate requires weekends off; role mandates rotating Saturday shifts every other week.",
        "resume": (
            "Michelle Park | Picker/Packer\n"
            "1440 Westwood Blvd, Los Angeles, CA 90024 | (310) 555-0398 | mpark.la@gmail.com\n\n"
            "EXPERIENCE\n"
            "Picker/Packer — WestCoast Apparel Fulfillment, Commerce CA (2022–2024)\n"
            "• Pick-to-light system; packed apparel for DTC brands\n"
            "• Maintained 99% accuracy on quality audits\n\n"
            "Student — UCLA Extension, Business Certificate program (evenings, 2024–Present)"
        ),
        "job_description": (
            "Picker/Packer — Apex Staffing / Client: Apparel Fulfillment, Commerce CA\n"
            "Shift: 1st (7:00 AM – 3:30 PM) plus rotating Saturday (7:00 AM – 3:30 PM) every other week\n"
            "Pay: $17.50/hr\n\n"
            "Requirements:\n"
            "• Pick/pack experience in apparel or e-commerce\n"
            "• Mandatory rotating Saturday shift — no exceptions\n"
            "• Detail-oriented; careful with garment handling\n"
            "• Standing 8+ hours"
        ),
        "transcript": (
            "Sarah: Hi Michelle, Sarah from Apex Staffing about the picker packer role in Commerce.\n"
            "Candidate: Hi! I have fulfillment experience so I thought I'd be a good fit.\n"
            "Sarah: You do — WestCoast Apparel looks solid. This site runs a rotating Saturday "
            "every other week. Can you commit to that?\n"
            "Candidate: Oh, I didn't realize Saturdays were required. I take classes Sunday prep "
            "and I really can't work Saturdays.\n"
            "Sarah: Unfortunately the client doesn't offer weekend waivers. It's in the contract.\n"
            "Candidate: Is there any flexibility — maybe swap with someone?\n"
            "Sarah: Not for this account. I'd hate to place you and have attendance issues.\n"
            "Candidate: Yeah, I wouldn't be reliable on that schedule.\n"
            "Sarah: I'll keep your resume for weekday-only openings if something comes up."
        ),
    },
    {
        "id": "wh-013",
        "vertical": "warehouse",
        "decision": "reject",
        "difficulty": "borderline",
        "ingest_format": "asr_paragraph",
        "reason": "Sit-down forklift certified but client requires reach truck certification on day one; candidate willing to train but client declined wait.",
        "resume": (
            "Andre Williams | Forklift Operator\n"
            "2201 Peachtree Rd NE, Atlanta, GA 30309 | (404) 555-0714 | awilliams.atl@proton.me\n\n"
            "EXPERIENCE\n"
            "Forklift Operator — Peach State Logistics, Atlanta GA (2020–Present)\n"
            "• Operate sit-down counterbalance forklifts; load outbound trailers\n"
            "• OSHA sit-down certification valid through August 2025\n"
            "• No reach truck or order picker experience\n\n"
            "Material Handler — Coca-Cola Bottling, Atlanta GA (2018–2020)"
        ),
        "job_description": (
            "Forklift Operator — Apex Staffing / Client: Narrow-Aisle Parts DC, Atlanta GA\n"
            "Shift: 2nd (4:00 PM – 12:30 AM), Mon–Fri\n"
            "Pay: $21.50/hr\n\n"
            "Requirements:\n"
            "• Reach truck certification required — sit-down only does not qualify\n"
            "• 2+ years operating reach truck in racking 20 ft+\n"
            "• Cannot accommodate on-the-job reach truck training\n"
            "• Drug screen required"
        ),
        "transcript": (
            "Andre Williams? Apex Staffing following up on the forklift role at the parts DC.\n\n"
            "Yes sir. I've got four years on forklifts, OSHA cert is current.\n\n"
            "The equipment there is primarily reach trucks in twenty-foot racking. Have you operated reach?\n\n"
            "Not yet. My cert is sit-down counterbalance. I've watched the reach guys — "
            "I'm confident I could learn fast.\n\n"
            "I appreciate that, but this client specifically said no training period. "
            "They've been burned before.\n\n"
            "What if I took reach training on my own this week?\n\n"
            "Lead time is two weeks minimum and they need someone Monday. "
            "I'd recommend getting reach certified and we'll resubmit you.\n\n"
            "All right. Disappointing but I get it."
        ),
    },
    {
        "id": "wh-014",
        "vertical": "warehouse",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": "Agency records show three no-call/no-show incidents on last warehouse assignment in past six months.",
        "resume": (
            "Jasmine Cole | Warehouse Associate\n"
            "409 Elm Street, Gary, IN 46402 | (219) 555-0267 | jcole.gary@gmail.com\n\n"
            "EXPERIENCE\n"
            "Warehouse Associate — Apex Staffing @ Steel City Logistics (Temp, 2024)\n"
            "• Pick and pack automotive fasteners\n"
            "• Assignment ended after attendance issues\n\n"
            "Fast Food Crew — McDonald's, Gary IN (2022–2024)\n"
            "• Cashier and grill; reliable until warehouse placement"
        ),
        "job_description": (
            "Warehouse Associate — Apex Staffing / Client: Automotive Fasteners, Gary IN\n"
            "Shift: 1st (6:00 AM – 2:30 PM), Mon–Fri\n"
            "Pay: $16.75/hr\n\n"
            "Requirements:\n"
            "• Prior warehouse experience preferred\n"
            "• Strict attendance policy — three NCNS incidents result in termination\n"
            "• Steel-toe boots required\n"
            "• Rehire of former temps subject to agency record review"
        ),
        "transcript": (
            "Jasmine Cole? Hi, Apex Staffing regarding your new application for the warehouse role in Gary.\n\n"
            "Hi, yes. I worked through you guys before at Steel City Logistics.\n\n"
            "I see that assignment. Can you tell me what happened when that ended?\n\n"
            "I had some car trouble and missed a few days. I should have called but I didn't.\n\n"
            "Our records show three no-call no-shows in six weeks. That's an automatic flag.\n\n"
            "I've got a new car now. It won't happen again.\n\n"
            "The client shares attendance data with us. They won't accept prior NCNS patterns "
            "without six clean months somewhere else.\n\n"
            "So I'm not eligible?\n\n"
            "Not for this account right now. Get six months steady elsewhere and reapply."
        ),
    },
    {
        "id": "wh-015",
        "vertical": "warehouse",
        "decision": "reject",
        "difficulty": "borderline",
        "ingest_format": "asr_noisy",
        "reason": "Only two months warehouse experience versus six-month minimum required; positive attitude but insufficient tenure.",
        "resume": (
            "Ethan Brooks | Picker/Packer\n"
            "15 Lakeview Dr, Spartanburg, SC 29301 | (864) 555-0583 | ebrooks.sc@yahoo.com\n\n"
            "EXPERIENCE\n"
            "Picker/Packer — QuickShip Fulfillment, Spartanburg SC (2025–Present)\n"
            "• Pick e-commerce orders; pack station with bubble mailers and boxes\n"
            "• Started March 2025 — two months tenure\n\n"
            "Retail Associate — Walmart, Spartanburg SC (2023–2025)\n"
            "• Stocked shelves; occasional online order pickup"
        ),
        "job_description": (
            "Picker/Packer — Apex Staffing / Client: High-Volume E-commerce FC, Spartanburg SC\n"
            "Shift: 1st (5:30 AM – 2:00 PM), Mon–Sat\n"
            "Pay: $17.00/hr\n\n"
            "Requirements:\n"
            "• Minimum 6 months pick/pack or fulfillment experience\n"
            "• Ability to maintain 280+ UPH pick rate within 30 days\n"
            "• Saturday required\n"
            "• Prior high-volume environment preferred"
        ),
        "transcript": (
            "Ethan Brooks? Uh, Apex Staffing about the picker packer job.\n\n"
            "Yeah that's me. I applied cause I'm looking for more hours.\n\n"
            "How long have you been at QuickShip?\n\n"
            "Since March, so like two months. But I'm picking fast — my lead said I'm one a the better new guys.\n\n"
            "This client wants six months minimum warehouse time. It's a high volume building.\n\n"
            "I learn quick though. At Walmart I was doing online orders too.\n\n"
            "Retail pickup counts a little but not enough for their cutoff. "
            "I'm sorry — you're close but not there yet.\n\n"
            "If I stick it out at QuickShip can I reapply?\n\n"
            "Absolutely. Four more months and call me back."
        ),
    },
    {
        "id": "wh-016",
        "vertical": "warehouse",
        "decision": "reject",
        "difficulty": "borderline",
        "ingest_format": "asr_noisy",
        "reason": "Shipping experience qualifies but candidate cannot meet fifty-pound lift requirement; comfortable maximum is thirty-five pounds.",
        "resume": (
            "Sandra Mitchell | Shipping Clerk\n"
            "602 Brookside Lane, Tulsa, OK 74105 | (918) 555-0432 | smitchell.tulsa@gmail.com\n\n"
            "EXPERIENCE\n"
            "Shipping Clerk — Tulsa Tool & Die Supply, Tulsa OK (2021–Present)\n"
            "• Process outbound parcels and LTL shipments\n"
            "• Create shipping labels; maintain carrier logs\n"
            "• Light lifting only — heaviest items routed to dock crew\n\n"
            "Data Entry Clerk — State Farm office, Tulsa OK (2019–2021)"
        ),
        "job_description": (
            "Shipping Clerk — Apex Staffing / Client: Industrial Equipment Wholesaler, Tulsa OK\n"
            "Shift: 1st (8:00 AM – 4:30 PM), Mon–Fri\n"
            "Pay: $18.25/hr\n\n"
            "Requirements:\n"
            "• 1+ year shipping clerk experience\n"
            "• Must independently lift and pack items up to 50 lbs regularly\n"
            "• UPS/FedEx shipping software experience\n"
            "• No separate dock crew — clerk handles heavy cartons"
        ),
        "transcript": (
            "Sandra Mitchell? Apex Staffing calling bout the shipping clerk opening.\n\n"
            "Hi, yes. I've been shipping at Tulsa Tool and Die for three years.\n\n"
            "Good background. This role you'd pack cartons up to fifty pounds yourself — no dock hand.\n\n"
            "Oh. At my job the heavy stuff goes to the warehouse guys. I do labels and paperwork "
            "mostly, maybe twenty pound boxes.\n\n"
            "What's the heaviest you can lift comfortably and repeatedly?\n\n"
            "Honestly about thirty five. I have a shoulder issue from twenty nineteen. "
            "I didn't want to lie on the application.\n\n"
            "I appreciate the honesty. Client won't budge on fifty pounds — it's in every job ticket.\n\n"
            "Would a different role work?\n\n"
            "I'll look for light-duty clerical warehouse openings. This one's not a fit physically."
        ),
    },
    {
        "id": "wh-017",
        "vertical": "warehouse",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": "Candidate disclosed failed pre-employment drug screen at prior staffing placement three months ago; client requires clean screen.",
        "resume": (
            "Marcus Delgado | Warehouse Associate\n"
            "3310 E Camelback Rd, Phoenix, AZ 85018 | (602) 555-0941 | mdelgado.phx@gmail.com\n\n"
            "EXPERIENCE\n"
            "Warehouse Associate — LaborReady @ Phoenix Building Supply (Temp, 2025)\n"
            "• Assignment ended after failed drug screen\n"
            "• Prior duties: load lumber, organize yard stock\n\n"
            "Landscaping Crew — Desert Green LLC, Phoenix AZ (2022–2024)\n"
            "• Manual labor, equipment operation"
        ),
        "job_description": (
            "Warehouse Associate — Apex Staffing / Client: Building Materials DC, Phoenix AZ\n"
            "Shift: 1st (5:00 AM – 1:30 PM), Mon–Fri\n"
            "Pay: $18.00/hr\n\n"
            "Requirements:\n"
            "• Warehouse or construction supply experience preferred\n"
            "• Pre-employment and random drug screens required\n"
            "• Must pass 10-panel urine screen\n"
            "• Early start time — 5 AM mandatory"
        ),
        "transcript": (
            "Marcus Delgado? Hi, um, Apex Staffing about the warehouse job in Phoenix.\n\n"
            "Yeah. Before we go further I should tell you something.\n\n"
            "Okay, go ahead.\n\n"
            "I failed a drug test at LaborReady like three months ago. I was doing landscaping before that "
            "clean. I'm not using anything now.\n\n"
            "Thanks for being upfront. Our client runs a ten panel on hire and randoms after.\n\n"
            "I can pass now. I stopped right after that test.\n\n"
            "Policy is we can't submit anyone with a failed screen in the last twelve months "
            "regardless. It's a compliance thing.\n\n"
            "Even if I test clean today?\n\n"
            "Even then. Reapply in nine months with clean tests from another employer if you can."
        ),
    },
    {
        "id": "wh-018",
        "vertical": "warehouse",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "labeled",
        "reason": "Available only for first shift; position is third shift 10 PM to 6 AM with no shift-swap option.",
        "resume": (
            "Brian Foster | Forklift Operator\n"
            "8901 Wurzbach Rd, San Antonio, TX 78240 | (210) 555-0678 | bfoster.sa@outlook.com\n\n"
            "EXPERIENCE\n"
            "Forklift Operator — H-E-B Distribution, San Antonio TX (2019–Present)\n"
            "• Sit-down and stand-up forklift; first shift dairy warehouse\n"
            "• OSHA certification valid through 2026\n"
            "• Seeking new role due to commute length\n\n"
            "Army Reserve — Motor transport operator (part-time)"
        ),
        "job_description": (
            "Forklift Operator — Apex Staffing / Client: Cold Storage DC, San Antonio TX\n"
            "Shift: 3rd (10:00 PM – 6:30 AM), Sun–Thu — no shift swaps\n"
            "Pay: $22.00/hr\n\n"
            "Requirements:\n"
            "• Current OSHA forklift certification\n"
            "• Third-shift availability mandatory\n"
            "• Cold storage experience preferred (-10°F zones)\n"
            "• Cannot accommodate first-shift requests"
        ),
        "transcript": (
            "Recruiter: Brian Foster? Hi, Apex Staffing on the forklift role at the cold storage DC.\n"
            "Candidate: Hey. I saw the pay and I've got the experience.\n"
            "Recruiter: Your H-E-B background looks great. This is third shift, ten PM to six thirty. "
            "Is that workable?\n"
            "Candidate: Oh, I didn't catch that in the posting. I only work days. "
            "I have Reserve drill some weekends but nights are a no-go.\n"
            "Recruiter: This account is strictly third shift. They don't offer rotations or swaps.\n"
            "Candidate: My wife works nights at the hospital — I need to be home evenings for the kids.\n"
            "Recruiter: Totally understand. I have a first-shift sit-down role at a different client "
            "but it's lower pay.\n"
            "Candidate: Send me that one instead. This shift won't work.\n"
            "Recruiter: Will do. I'll close out the cold storage req for you."
        ),
    },
    {
        "id": "wh-019",
        "vertical": "warehouse",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_paragraph",
        "reason": "No warehouse or manufacturing experience; background is retail cashier only, client requires six months fulfillment minimum.",
        "resume": (
            "Alyssa Turner | Retail Associate\n"
            "55 Main Street, Boise, ID 83702 | (208) 555-0312 | aturner.boise@gmail.com\n\n"
            "EXPERIENCE\n"
            "Cashier — Kohl's, Boise ID (2023–Present)\n"
            "• Register, customer service, folding apparel on sales floor\n"
            "• Occasional backup on stocking team during peak\n\n"
            "Barista — Dutch Bros Coffee, Boise ID (2021–2023)\n"
            "• Customer service, cash handling, opening/closing duties"
        ),
        "job_description": (
            "Picker/Packer — Apex Staffing / Client: Outdoor Gear Fulfillment, Boise ID\n"
            "Shift: 1st (6:30 AM – 3:00 PM), Mon–Fri\n"
            "Pay: $16.25/hr\n\n"
            "Requirements:\n"
            "• Minimum 6 months warehouse pick/pack or manufacturing experience\n"
            "• Retail stocking alone does not qualify\n"
            "• Ability to lift 40 lbs repeatedly\n"
            "• RF scanner training provided but prior warehouse exposure required"
        ),
        "transcript": (
            "Alyssa Turner? Hi, this is Apex Staffing calling about the picker packer position in Boise.\n\n"
            "Hi! I'm really interested in getting into warehouse work.\n\n"
            "Tell me about any warehouse or fulfillment experience on your resume.\n\n"
            "I work at Kohl's now. I fold clothes and sometimes help stock when they're busy. "
            "Before that Dutch Bros.\n\n"
            "Have you ever worked in a dedicated warehouse or distribution center?\n\n"
            "Not exactly. But I'm a hard worker and I want to learn.\n\n"
            "The client requires six months actual warehouse pick/pack. Retail floor stocking "
            "doesn't count for this account.\n\n"
            "Could I start at a lower level?\n\n"
            "Not with this client. I'd suggest applying to our general labor openings "
            "to get warehouse time first."
        ),
    },
    {
        "id": "wh-020",
        "vertical": "warehouse",
        "decision": "reject",
        "difficulty": "clear",
        "ingest_format": "asr_noisy",
        "reason": "OSHA certification covers stand-up forklift only; client requires sit-down and reach truck certification on day one.",
        "resume": (
            "Gregory Shaw | Forklift Operator\n"
            "1440 Harbor Blvd, Jacksonville, FL 32208 | (904) 555-0529 | gshaw.jax@yahoo.com\n\n"
            "EXPERIENCE\n"
            "Forklift Operator — Atlantic Grocery Wholesalers, Jacksonville FL (2021–Present)\n"
            "• Operate stand-up counterbalance forklifts in dry grocery warehouse\n"
            "• OSHA certification lists stand-up only (renewed February 2025)\n"
            "• No sit-down or reach truck training\n\n"
            "Dock Associate — CSX Intermodal, Jacksonville FL (2019–2021)"
        ),
        "job_description": (
            "Forklift Operator — Apex Staffing / Client: General Merchandise DC, Jacksonville FL\n"
            "Shift: 2nd (2:00 PM – 10:30 PM), Mon–Fri\n"
            "Pay: $19.75/hr\n\n"
            "Requirements:\n"
            "• OSHA certification must include sit-down AND reach truck\n"
            "• Stand-up only certification does not meet requirements\n"
            "• 2+ years operating both equipment types\n"
            "• Cannot provide additional equipment training"
        ),
        "transcript": (
            "Gregory Shaw? Apex Staffing, uh, following up on the forklift operator application.\n\n"
            "Yes sir. I've been running forklifts three years at Atlantic Grocery.\n\n"
            "Your cert — is it stand-up, sit-down, or both?\n\n"
            "Stand-up counterbalance only. That's all we use in our building. "
            "I renewed it in February.\n\n"
            "This DC needs sit-down and reach truck on day one. No training window.\n\n"
            "I could get trained on sit-down pretty quick. Reach might take longer.\n\n"
            "Client won't wait. We've had three no-starts this month on cert mismatches.\n\n"
            "So I'm out?\n\n"
            "For this role, yes. Get dual certified at a training center and call us back. "
            "The pay bump would be worth it."
        ),
    },
]

assert len(WAREHOUSE_RECORDS) == 20
assert sum(1 for r in WAREHOUSE_RECORDS if r["decision"] == "select") == 10
assert sum(1 for r in WAREHOUSE_RECORDS if r["decision"] == "reject") == 10
