"""Async batch eval runner — production concurrency and observability."""

from __future__ import annotations

import asyncio
import json
import logging
import os
import time
from dataclasses import asdict
from pathlib import Path

import numpy as np
import pandas as pd

from src.agents.orchestrator import InterviewOrchestrator
from src.data.loader import load_custom, load_eval_set
from src.data.schema import CandidateRecord
from src.eval.failure_report import PredictionRow, build_failure_report
from src.eval.metrics import compute_metrics, plot_calibration
from src.llm.client import runtime_info

RESULTS_DIR = Path(__file__).resolve().parents[2] / "results"
logger = logging.getLogger(__name__)


async def _score_one(
    record: CandidateRecord,
    semaphore: asyncio.Semaphore,
    enable_followups: bool,
    followup_mode: str,
) -> dict:
    async with semaphore:
        orchestrator = InterviewOrchestrator(
            enable_followups=enable_followups,
            followup_mode=followup_mode,
        )
        try:
            result = await orchestrator.arun(
                transcript=record.transcript,
                resume=record.resume,
                job_description=record.job_description,
            )
            return {
                "id": record.id,
                "predicted_decision": result.predicted_decision,
                "confidence": result.confidence,
                "reasoning": result.reasoning,
                "risk_flags": result.risk_flags,
                "escalate_to_human": result.escalate_to_human,
                "turns_processed": result.turns_processed,
                "llm_calls": result.llm_calls,
                "followups_asked": result.followups_asked,
                "latency_ms": round(result.total_latency_ms, 1),
                "actual_decision": record.decision,
                "actual_reason": record.reason,
                "vertical": record.vertical,
                "difficulty": record.difficulty,
                "ingest_format": record.ingest_format,
                "transcript_excerpt": record.transcript[:500],
                "error": "",
            }
        except Exception as exc:
            logger.exception("score failed id=%s", record.id)
            return {
                "id": record.id,
                "predicted_decision": "",
                "confidence": 0,
                "reasoning": "",
                "risk_flags": [],
                "escalate_to_human": True,
                "turns_processed": 0,
                "llm_calls": 0,
                "followups_asked": 0,
                "latency_ms": 0.0,
                "actual_decision": record.decision,
                "actual_reason": record.reason,
                "vertical": record.vertical,
                "difficulty": record.difficulty,
                "ingest_format": record.ingest_format,
                "transcript_excerpt": record.transcript[:500],
                "error": str(exc),
            }


def _latency_stats(latencies: list[float]) -> dict[str, float]:
    if not latencies:
        return {"p50_ms": 0.0, "p95_ms": 0.0, "mean_ms": 0.0}
    arr = np.array(latencies)
    return {
        "p50_ms": round(float(np.percentile(arr, 50)), 1),
        "p95_ms": round(float(np.percentile(arr, 95)), 1),
        "mean_ms": round(float(arr.mean()), 1),
    }


async def run_eval_async(
    sample_size: int | None = None,
    seed: int = 42,
    concurrency: int | None = None,
    enable_followups: bool = True,
    followup_mode: str | None = None,
    results_dir: Path | None = None,
    custom_path: Path | None = None,
) -> dict:
    out_dir = results_dir or RESULTS_DIR
    concurrency = concurrency or int(os.getenv("EVAL_CONCURRENCY", "10"))
    followup_mode = followup_mode or os.getenv("FOLLOWUP_MODE", "end")

    if custom_path:
        records = load_custom(custom_path)
        run_meta = {"dataset": "custom", "source": str(custom_path)}
    else:
        records = load_eval_set(sample=sample_size, seed=seed)
        run_meta = {"dataset": "staffing_screen_eval_v1", "sample_size": len(records), "seed": seed}

    out_dir.mkdir(parents=True, exist_ok=True)
    semaphore = asyncio.Semaphore(concurrency)
    started = time.perf_counter()

    tasks = [
        _score_one(r, semaphore, enable_followups, followup_mode) for r in records
    ]
    rows = await asyncio.gather(*tasks)

    total_wall_ms = (time.perf_counter() - started) * 1000
    rows.sort(key=lambda r: r["id"])

    ok_rows = [r for r in rows if not r.get("error")]
    failed = [r for r in rows if r.get("error")]

    pd.DataFrame(rows).to_csv(out_dir / "predictions.csv", index=False)

    y_true = [r["actual_decision"] for r in ok_rows]
    y_pred = [r["predicted_decision"] for r in ok_rows]
    confidences = [r["confidence"] for r in ok_rows]

    metrics = compute_metrics(y_true, y_pred, confidences) if ok_rows else None
    if ok_rows:
        plot_calibration(y_true, y_pred, confidences, str(out_dir / "calibration.png"))

    summary: dict = {}
    if metrics:
        summary = asdict(metrics)
    summary.update(run_meta)
    summary.update(runtime_info())
    summary["enable_followups"] = enable_followups
    summary["followup_mode"] = followup_mode
    summary["concurrency"] = concurrency
    summary["n"] = len(rows)
    summary["n_scored"] = len(ok_rows)
    summary["n_failed"] = len(failed)
    summary["wall_clock_ms"] = round(total_wall_ms, 1)
    summary["latency"] = _latency_stats([r["latency_ms"] for r in ok_rows])
    summary["total_llm_calls"] = sum(r["llm_calls"] for r in ok_rows)

    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")

    pred_rows = [
        PredictionRow(
            id=r["id"],
            predicted=r["predicted_decision"],
            actual=r["actual_decision"],
            confidence=r["confidence"],
            reasoning=r["reasoning"],
            transcript_excerpt=r["transcript_excerpt"],
            vertical=r.get("vertical", ""),
            difficulty=r.get("difficulty", ""),
        )
        for r in ok_rows
    ]
    (out_dir / "failure_cases.md").write_text(build_failure_report(pred_rows))

    if failed:
        fail_lines = ["# Scoring Failures", ""]
        for r in failed:
            fail_lines.append(f"- **{r['id']}**: {r['error']}")
        (out_dir / "failures.md").write_text("\n".join(fail_lines) + "\n")

    return summary


def run_eval(
    sample_size: int | None = None,
    seed: int = 42,
    concurrency: int | None = None,
    enable_followups: bool = True,
    followup_mode: str | None = None,
    results_dir: Path | None = None,
    custom_path: Path | None = None,
) -> dict:
    return asyncio.run(
        run_eval_async(
            sample_size=sample_size,
            seed=seed,
            concurrency=concurrency,
            enable_followups=enable_followups,
            followup_mode=followup_mode,
            results_dir=results_dir,
            custom_path=custom_path,
        )
    )
