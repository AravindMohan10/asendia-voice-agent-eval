# High-Confidence Failures

Cases where confidence ≥ 80 but prediction was **wrong**.
These are the most dangerous failures in production — the agent is confident but incorrect.

## Case 1 (ad-018)

- **Predicted:** select
- **Actual:** reject
- **Confidence:** 80
- **Vertical:** admin | **Difficulty:** clear
- **Reasoning:** Amanda meets the data entry requirements with 3 years of experience, 9,800 KPH, and Excel skills. She also has HIPAA exposure and is willing to comply with the on-site phone policy. However, her lack of on-site office experience is a minor concern.
- **Transcript excerpt:** Amanda Apex data entry temp to perm. Your stats?

Ninety two W P M ninety seven percent accuracy alpha numeric medical forms

any hippa exposure

yes at the clinic I signed hippa acknowledgment handled patient intake forms

strict on site no phones on floor

understood I can comply...
