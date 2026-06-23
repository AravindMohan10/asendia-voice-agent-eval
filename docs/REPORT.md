# Eval Report

**Run:** hand-curated golden set `staffing_screen_eval_v1` · n=100 · seed=42 · Groq `llama-3.3-70b-versatile` · scorer-only (1 LLM call/record)

## Summary

| Metric | Value |
|--------|-------|
| Sample size | 100 |
| Accuracy | **95.0%** |
| Precision (select) | 97.9% |
| Recall (select) | 92.0% |
| **ECE (calibration)** | **0.48** |
| High-confidence error rate (conf ≥ 80, wrong) | **1.1%** (1 case) |
| Scoring latency (p50) | 640 ms / candidate |

![Calibration](results/calibration.png)

## Primary finding: accuracy ≠ calibration

The agent achieves **95% agreement** with held-out recruiter decisions on this golden set — but **confidence scores are poorly calibrated** (ECE ≈ 0.48).

What that means in production:

- When the agent says "85% confident," that number does **not** reliably map to an 85% chance of being correct on this distribution.
- **High-confidence failures are rare** (1/95 high-conf predictions wrong) — the bigger gap is mid-range confidence not matching outcome rates across bins (see chart).
- This is exactly why you gate deployment on **calibration**, not accuracy alone: a 95% accurate agent with miscalibrated confidence will still auto-submit bad decisions if you threshold at 80%.

**Borderline cases behaved better:** 4/5 errors were on `difficulty=borderline` records at **60% confidence** — the agent flagged uncertainty rather than blasting a wrong answer at 90%.

## High-confidence failures

Only **one** case met the danger threshold (conf ≥ 80, wrong):

### Case 1 — `ad-018` (admin, clear)

- **Predicted:** select · **Actual:** reject · **Confidence:** 80
- **What happened:** Candidate has strong data-entry metrics (92 WPM, HIPAA exposure) but resume shows **fully remote** history. Ground truth: client requires **3 days on-site** — recruiter rejected for hybrid policy mismatch.
- **Why it failed:** Agent treated on-site as a minor concern ("lack of on-site office experience") instead of a hard disqualifier. Reasoning acknowledged the gap but confidence stayed at 80 and decision was select.
- **Production risk:** Auto-submit at 80% threshold would forward a candidate the client cannot place.

See full list: [failure_cases.md](../results/failure_cases.md)

## Other misses (appropriately uncertain)

| ID | Pred / Actual | Conf | Notes |
|----|---------------|------|-------|
| `hc-007` | reject / select | 60 | Dental → medical transfer; recruiter advanced on transferable skills |
| `hc-005` | reject / select | 60 | Short billing tenure; borderline submit |
| `hc-010` | reject / select | 60 | New phlebotomist; recruiter took chance |
| `wh-005` | reject / select | 60 | Limited RF scanner time; recruiter flagged but sent to client |

These are **judgment calls**, not clear-cut errors — 60% confidence is appropriate.

## Limitations

- **Synthetic golden set** — staffing-realistic, not Asendia production data.
- **Text turn-replay (Phase 1)** — same scoring path as post-ASR transcript; voice latency/codec not modeled.
- **Single model/prompt** — no regression CI yet; prompt hash recorded in `summary.json`.
- **Scorer-only run** — 1 LLM call/record; follow-up agent not exercised in this eval.

## If I joined Asendia

Before deploying Sarah to a **new agency or vertical**:

1. **Build a vertical golden set** (~100 real anonymized screens) with recruiter submit decisions held out.
2. **Run this harness weekly** — track accuracy, **ECE**, and high-confidence failure count; block release if ECE or high-conf error rate regresses.
3. **Threshold on calibrated confidence**, not raw accuracy — e.g. auto-submit only when conf ≥ 80 *and* ECE bin is validated on recent data.
4. **Phase 2:** plug live ASR turn stream into the same orchestrator; add voice-specific robustness cases.

The harness is the product — Sarah's weights and prompts change; the eval loop stays.
