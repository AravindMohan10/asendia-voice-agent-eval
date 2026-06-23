"""Realistic ASR-style transcript overrides for ingest_format=asr_noisy.

Phone-screen ASR commonly produces:
- homophones / near-homophones (forklift → four lift, HIPAA → hippa)
- dropped punctuation and speaker labels
- number normalization (608 → six oh eight)
- filler words retained from speech
- occasional word merges (I can → I can still readable)

Applied at build time so corpus source stays readable for review.
"""

from __future__ import annotations

ASR_TRANSCRIPT_OVERRIDES: dict[str, str] = {
    "wh-006": (
        "Hi Robert um Apex Staffing calling about the four lift job in Kenosha. You still interested?\n\n"
        "Yeah definitely I'm on third shift now so the hours line up.\n\n"
        "I see six years on four lifts at Great Lakes Beverage. Cert status?\n\n"
        "So mine expired in April I slacked on renewal. I got the retest booked this Friday "
        "at the safety training center.\n\n"
        "Client won't let anyone on a lift without current Osha card. That's a problem.\n\n"
        "I know I know. I've been operating the whole time though zero incidents. "
        "I can email you the appointment confirmation.\n\n"
        "If you pass Friday and send the card Monday we'll move you to orientation Wednesday. "
        "No cert no start — fair?\n\n"
        "Fair enough. I'll get it done."
    ),
    "wh-009": (
        "Is this Christopher Vega? Apex Staffing uh calling about the shipping clerk role in Allentown.\n\n"
        "Yes ma'am that's me.\n\n"
        "I see hazmat awareness on your resume — is that current?\n\n"
        "Renewed January twenty twenty five yeah I process LTL and parcel outbound "
        "about sixty to ninety orders a day.\n\n"
        "First shift seven thirty to four. Any conflicts?\n\n"
        "No I'm on first now at Lehigh Valley Industrial. Same hours actually.\n\n"
        "Can you start after background clears next Tuesday?\n\n"
        "Yes I'll be there."
    ),
    "wh-015": (
        "Ethan Brooks? Uh Apex Staffing about the picker packer job.\n\n"
        "Yeah that's me. I applied last night.\n\n"
        "You started at QuickShip in March — so about two months warehouse?\n\n"
        "Yeah March. Before that Walmart stocking.\n\n"
        "Client wants six months minimum pick pack experience. How do you compare?\n\n"
        "I'm fast learner though. I'm hitting rate already.\n\n"
        "I hear you but they won't flex on tenure. I'd reapply in four months.\n\n"
        "Okay thanks for being straight with me."
    ),
    "wh-016": (
        "Sandra Mitchell? Apex Staffing calling bout the shipping clerk opening.\n\n"
        "Hi yes I'm interested.\n\n"
        "This role requires lifting up to fifty pounds regularly. Comfortable?\n\n"
        "Um honestly my max is about thirty five. Heavier stuff goes to the dock crew at my current job.\n\n"
        "Client won't accommodate light duty on lifts. It's industrial equipment parts.\n\n"
        "I understand. I don't want to get placed somewhere I can't do the work.\n\n"
        "I'll note that and keep you in mind for data entry openings."
    ),
    "wh-017": (
        "Marcus Delgado? Hi um Apex Staffing about the warehouse job in Phoenix.\n\n"
        "Yeah.\n\n"
        "Quick question — any issues on drug screen for recent assignments?\n\n"
        "Yeah I failed one at LaborReady about three months ago. Building supply temp job.\n\n"
        "This client requires clean screen day one. No exceptions.\n\n"
        "I figured. I'm clean now but I get it.\n\n"
        "Reapply after six months with documentation if you want."
    ),
    "wh-020": (
        "Gregory Shaw? Apex Staffing uh following up on the four lift operator application.\n\n"
        "Hey yeah still interested.\n\n"
        "Your cert is stand up counterbalance only. Client needs sit down and rich truck day one.\n\n"
        "I could get trained on sit down pretty quick. Rich might take longer.\n\n"
        "Client won't wait. Three no starts this month on cert mismatches.\n\n"
        "So I'm out for this one?\n\n"
        "For this role yes. Get dual certified and call us back."
    ),
    "hc-004": (
        "so Kim this is for an outpatient lab role um walk me through your certification\n\n"
        "yeah I've got active CPT one through the state board renewed um last year I've "
        "been at Quest three years doing forty to fifty five sticks a day\n\n"
        "are you on epic baker or another LIS\n\n"
        "baker mostly at Quest I verify orders print labels two identifier check "
        "before every draw per hippa protocol\n\n"
        "schedule is on site mornings including Saturday rotation okay\n\n"
        "yes I'm good with that I did Saturday rotation at Quest already no problem\n\n"
        "any incidents with mislabeled specimens or patient ID errors\n\n"
        "no I've never had a patient ID sentinel event I follow the two identifier "
        "rule every time"
    ),
    "hc-007": (
        "Jasmine I'm looking at your resume — it's mostly dental not medical front desk. "
        "why should we consider you\n\n"
        "um I know it's dental but I did insurance verification every day benefit breakdowns "
        "copays scheduling recall calls it's the same customer facing workflow\n\n"
        "any epic or athena\n\n"
        "not on the job but I finished epic fundamentals online last month I'm ready to learn on site fast\n\n"
        "this pediatrics clinic is on site five days sometimes Saturday vaccine clinics\n\n"
        "I can do that I don't need hybrid I have reliable childcare\n\n"
        "hippa experience\n\n"
        "we had hippa training at the dental office patient privacy charts I understand "
        "you can't discuss cases in the waiting room"
    ),
    "hc-011": (
        "Chris thanks for applying to medical billing tell me about your billing experience\n\n"
        "uh I haven't done billing yet I was cashier at Target for two years I'm a fast learner though\n\n"
        "any epic or athena any insurance verification claims\n\n"
        "no I haven't used those systems I looked up what epic resolute is online though\n\n"
        "this role needs two years professional claims experience day one\n\n"
        "I could maybe take a course if you train me\n\n"
        "client won't train from zero on resolute sorry — anything else in healthcare\n\n"
        "not yet but I'm willing to start somewhere"
    ),
    "hc-013": (
        "Ryan this front desk role needs epic or athena experience what's yours\n\n"
        "I work in the hospital cafeteria I see the check in kiosks but I don't use epic\n\n"
        "any insurance verification scheduling phones\n\n"
        "not really I run the cash register on the tray line sometimes catering orders\n\n"
        "did you apply thinking the cafeteria qualifies as hospital experience\n\n"
        "yeah it's the same building I know the campus\n\n"
        "client needs clinic front desk with registration workflows I can't submit this profile sorry"
    ),
    "hc-017": (
        "Diane you applied for billing your background is records release correct\n\n"
        "yes ROI mostly but I took an ICD ten intro course I know diagnosis codes on charts\n\n"
        "have you submitted professional claims in resolute or athena collector\n\n"
        "not exactly I haven't posted charges or worked denials I see codes when I pull records for attorneys\n\n"
        "client needs two years live billing um not coding literacy alone\n\n"
        "I could learn resolute fast I understand the revenue cycle conceptually\n\n"
        "they've rejected records only profiles before I'm gonna pass but keep billing certs on your radar"
    ),
    "hc-020": (
        "Brian tell me about your clinic administration background\n\n"
        "I haven't worked in a clinic I've been hotel front desk at Marriott four years managing guest check in and reservations\n\n"
        "any epic eclinicalworks hippa compliance staff supervision\n\n"
        "no opera is the hotel system I supervised two bell staff during rush hour not medical staff\n\n"
        "this is clinic admin for an urgent care chain three plus years required\n\n"
        "I figured hospitality transfers customer service wise\n\n"
        "client wants healthcare ops experience I can't put this through"
    ),
    "cc-003": (
        "um hi this is Sarah from Apex Staffing calling about the tier one tech support opening you applied for\n\n"
        "yeah I've been at TP about eighteen months on tier one ISP support modems routers Wi-Fi stuff "
        "we use Zendesk for tickets and Salesforce for customer history\n\n"
        "what's your average handle time uh around seven twenty team target is eight minutes "
        "QA I'm usually like eighty nine percent first call resolution high seventies\n\n"
        "schedule is rotating evenings and every third weekend that's fine I did swing at Best Buy before this\n\n"
        "training is four weeks on site then work from home I've got wired ethernet a good headset "
        "backup hotspot ready for the equipment check"
    ),
    "cc-006": (
        "hi Nicole Sarah with Apex Staffing about the work from home customer service role\n\n"
        "hi yes I saw it's inbound only no sales that's what I want\n\n"
        "tell me about your call center background\n\n"
        "two years at a utilities campaign inbound billing and outage tickets Salesforce for notes "
        "QA usually ninety one percent\n\n"
        "rotating weekends required\n\n"
        "my partner works opposite weekends so we're covered for childcare\n\n"
        "home office setup\n\n"
        "dedicated room wired internet quiet during shifts headset already"
    ),
    "cc-009": (
        "Christopher hi this is Sarah Apex Staffing tier one tech support screening\n\n"
        "two years tier one at a cable company modems and account verification\n\n"
        "AHT and QA\n\n"
        "around six ten AHT QA eighty eight to ninety two percent\n\n"
        "this campaign is inbound only no upsell comfortable\n\n"
        "yes I prefer support over hard sales honestly\n\n"
        "rotating weekends including every other Saturday\n\n"
        "I can do that no conflicts"
    ),
    "cc-012": (
        "Kayla hi Sarah Apex Staffing collections agent screening\n\n"
        "I've been at Zappos two years but that's retail customer service not collections\n\n"
        "any FDCPA or outbound collections experience\n\n"
        "no I haven't done collections calls or payment arrangements on past due accounts\n\n"
        "this client requires six months plus collections experience FDCPA trained\n\n"
        "I could learn the regulations fast though\n\n"
        "they won't train from zero on collections I'll pass for now"
    ),
    "cc-015": (
        "Jordan hi Sarah Apex Staffing work from home customer service role\n\n"
        "I did about six months remote at my last job\n\n"
        "equipment audit requires hardwired ethernet separate workspace no background noise\n\n"
        "I was on Wi-Fi in the kitchen sometimes kids home\n\n"
        "client failed last candidate on audit for that reason\n\n"
        "I don't have a dedicated room right now honestly\n\n"
        "I'd wait until you can pass the audit setup"
    ),
    "cc-018": (
        "Ryan Apex Staffing tier one tech support screening\n\n"
        "I've been Frontier tier one about eight months\n\n"
        "QA and AHT\n\n"
        "QA runs around seventy nine percent team minimum is eighty five\n\n"
        "what happened\n\n"
        "I was new and had long calls on provisioning issues getting better but not there yet\n\n"
        "client minimum is eighty five QA for ninety days I can't submit this profile"
    ),
    "st-006": (
        "hi Lisa um tell me about your H vac service background\n\n"
        "I've been with QuickCool about six months mostly residential service you know like under a senior tech\n\n"
        "E P A cert status\n\n"
        "I had type one from a class in twenty twenty two but uh I think it expired last year "
        "I haven't renewed yet\n\n"
        "this job needs current type two or universal and two years experience how do you compare\n\n"
        "I'm probably short on years I learn quick though definately willing to retest for E P A\n\n"
        "experience on commercial units\n\n"
        "not really mostly houses and some small storefront units once or twice"
    ),
    "st-020": (
        "Miguel tell me about your diesel background for this fleet account\n\n"
        "four years at TransWest on class eight engines brakes after treatment the whole thing\n\n"
        "C D L status\n\n"
        "I had class A but it's uh suspended right now D U I last year I can get it back in like eight months\n\n"
        "this client requires active C D L for road tests insurance won't budge\n\n"
        "mechanically I'm strong I just can't legally drive on the road till reinstatement\n\n"
        "A S E T two current\n\n"
        "it expired twenty twenty four I was gonna renew when the license thing got sorted"
    ),
    "ad-003": (
        "hi Kevin um Apex Staffing calling about the data entry temp role. You still interested?\n\n"
        "yeah I need something steady\n\n"
        "typing speed and accuracy from your last role\n\n"
        "about seventy five W P M ninety eight percent accuracy on ten key at the insurance office\n\n"
        "this is five days on site downtown parking not reimbursed\n\n"
        "that's fine I take the bus\n\n"
        "ninety day temp to perm if client likes you. Start Monday if background clears?\n\n"
        "yes I can start Monday"
    ),
    "ad-006": (
        "Carmen Apex Staffing here executive assistant temp to perm in Miami\n\n"
        "tell me about calendar and travel coordination experience\n\n"
        "three years supporting a VP at a logistics firm Outlook travel booking expense reports\n\n"
        "advanced excel powerpoint required\n\n"
        "yes pivot tables exec presentations weekly\n\n"
        "bilingual Spanish required for this executive\n\n"
        "fluent Spanish written and spoken\n\n"
        "I'll submit to client for interview"
    ),
    "ad-009": (
        "Thomas um Kelly Services office coordinator temp to perm Cambridge\n\n"
        "what systems have you used for scheduling and supply ordering\n\n"
        "Microsoft office sharepoint ordered supplies for forty person office managed conference rooms\n\n"
        "any experience with vendor invoices or A P\n\n"
        "light A P coding not full accounts payable\n\n"
        "client wants someone who can cover reception and coordinate facilities\n\n"
        "that's exactly what I did at my last job"
    ),
    "ad-012": (
        "Samantha Apex receptionist temp to perm. Office experience?\n\n"
        "two years front desk multi line phone system twelve lines greet visitors mail routing\n\n"
        "professional appearance and attendance important\n\n"
        "business casual every day no attendance issues at last job\n\n"
        "pay is eighteen an hour temp to perm after ninety days\n\n"
        "that works for me"
    ),
    "ad-015": (
        "Derek Kelly A P clerk temp to perm. A P background?\n\n"
        "I was A P specialist two years invoice matching three way match quickbooks\n\n"
        "volume and accuracy\n\n"
        "about two hundred invoices weekly ninety nine point five percent match rate\n\n"
        "hybrid one day remote after training\n\n"
        "that's fine I prefer mostly on site anyway"
    ),
    "ad-018": (
        "Amanda Apex data entry temp to perm. Your stats?\n\n"
        "Ninety two W P M ninety seven percent accuracy alpha numeric medical forms\n\n"
        "any hippa exposure\n\n"
        "yes at the clinic I signed hippa acknowledgment handled patient intake forms\n\n"
        "strict on site no phones on floor\n\n"
        "understood I can comply"
    ),
    "ad-020": (
        "Victor Kelly A P temp to perm. How much A P experience?\n\n"
        "mostly A R at my last job I applied thinking it's close\n\n"
        "this client needs two years live A P not receivables\n\n"
        "I processed customer payments not vendor bills\n\n"
        "can't submit as A P clerk I'd look at A R openings instead"
    ),
}


def apply_asr_overrides(records: list[dict]) -> list[dict]:
    out = []
    for r in records:
        rec = dict(r)
        if rec.get("ingest_format") == "asr_noisy" and rec["id"] in ASR_TRANSCRIPT_OVERRIDES:
            rec["transcript"] = ASR_TRANSCRIPT_OVERRIDES[rec["id"]]
        out.append(rec)
    return out
