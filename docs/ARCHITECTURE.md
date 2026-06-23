# Runtime Architecture

Production-oriented eval harness — async-first, bounded LLM calls, observable batch runs.

## Latency profile (per candidate)

| Mode | LLM calls | Typical latency |
|------|-----------|-----------------|
| `--no-followups` | **1** (scorer only) | ~0.8–1.5s on Groq |
| Default `FOLLOWUP_MODE=end` | **≤2** (1 follow-up check + score) | ~1.5–3s |
| `--followup-mode per_turn` | up to N turns | eval-strict, slower |

**Production default:** ingest all transcript turns locally (no LLM), then score once at end.

## Concurrency

- **Async** `asyncio` + `Semaphore(EVAL_CONCURRENCY)` — not thread pool
- Shared `AsyncGroq` / `AsyncOpenAI` client per process (connection reuse)
- Default concurrency: **10** (tune to provider rate limits)

## Reliability

| Feature | Implementation |
|---------|----------------|
| Retries | 3 attempts, exponential backoff (`LLM_MAX_RETRIES`) |
| Timeouts | `LLM_TIMEOUT_SEC=60` |
| JSON mode | OpenAI/Groq `response_format=json_object` with fallback |
| Per-record errors | Logged; written to `results/failures.md`; batch continues |
| Reproducibility | `summary.json` includes model + prompt SHA256 |

## Environment

```env
LLM_PROVIDER=groq
FOLLOWUP_MODE=end          # production
MAX_FOLLOWUPS=1
EVAL_CONCURRENCY=10
LLM_MAX_RETRIES=3
```

## Commands

```bash
# Fastest — 1 LLM call per record (recommended for headline eval)
python scripts/run_eval.py --no-followups --concurrency 10

# Production-shaped — max 2 LLM calls
python scripts/run_eval.py --followup-mode end

# Eval-strict turn replay (slow)
python scripts/run_eval.py --followup-mode per_turn
```

## Not included (true prod deployment)

HTTP API, queue workers, voice STT/TTS, multi-tenant auth, distributed tracing — add when serving live traffic.
