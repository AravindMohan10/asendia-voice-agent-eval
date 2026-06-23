# Eval Dataset

One production eval set — not multiple tiers, not Kaggle dump-and-pray.

## What this models

Each record is a **staffing-agency phone screen** — the same inputs Sarah would score after a recruiter call:

| Field | Agent sees? | Notes |
|-------|-------------|-------|
| `transcript` | Yes | Mixed ingest formats (see below) |
| `resume` | Yes | As submitted to agency |
| `job_description` | Yes | Client requisition |
| `decision` | **No** | Held-out ground truth |
| `reason` | **No** | Recruiter submit rationale |

## Why we built our own (not just Kaggle)

We don't know Asendia's internal dataset. Kaggle recruitment data is generic ML resume-screening — not staffing-agency phone screens with shift checks, cert verification, and temp-to-perm context.

This corpus is curated to resemble **what Sarah actually evaluates**:

- 5 staffing verticals (20 records each): warehouse, healthcare, call_center, skilled_trades, admin
- Recruiter screening questions: certs, shifts, start date, commute, pay, background/drug screen
- 50/50 select/reject with **23 borderline cases** — ambiguous enough to test calibration
- Mixed ingest formats in one dataset (how real pipelines look):
  - **labeled** (44%): `Recruiter:` / `Sarah:` / `Candidate:` turns — post-processed diarization
  - **asr_paragraph** (29%): unlabeled paragraph blocks — raw ASR segmentation, clean words
  - **asr_noisy** (27%): unlabeled + speech artifacts — homophones (`four lift`, `hippa`), spaced acronyms (`E P A`, `C D L`), fillers, dropped punctuation

`asr_noisy` records use curated word-level ASR overrides (`src/data/corpus/asr_layer.py`) — what the candidate said vs what the transcript captured.

## Files

```
data/eval/
  records.jsonl    ← 100 records (committed)
  manifest.json    ← stats + schema version
src/data/corpus/   ← source definitions (reviewable)
scripts/build_dataset.py
```

## Build / validate

```bash
python scripts/build_dataset.py      # regenerate from corpus
python scripts/validate_dataset.py   # schema + turn-parser check, no API key
```

## Record schema

```json
{
  "id": "wh-003",
  "vertical": "warehouse",
  "decision": "select",
  "difficulty": "clear",
  "ingest_format": "asr_paragraph",
  "reason": "Recruiter rationale (held out)",
  "resume": "...",
  "job_description": "...",
  "transcript": "..."
}
```

## Honest limitations (state in README)

- Synthetic corpus inspired by staffing workflows — not Asendia production data
- Text turn-replay (Phase 1); voice latency/codec/barge-in is Phase 2
- Strong here ≠ guaranteed strong on their data — that's why the harness matters more than one number

## What we claim in outreach

> Built a 100-record hand-curated staffing screen eval set with mixed ASR-style ingest, 50/50 outcomes, and borderline cases. Calibration results included in-repo. The harness is what we'd run on your golden set before a new vertical launch.

We do **not** claim this IS their dataset. We claim we understand **how to eval Sarah** before shipping.
