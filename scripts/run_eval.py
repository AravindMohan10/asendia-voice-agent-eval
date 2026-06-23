#!/usr/bin/env python3
"""Run batch eval against held-out hiring decisions."""

from __future__ import annotations

import argparse
import logging
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv

from src.eval.runner import run_eval

load_dotenv(ROOT / ".env")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run screening agent eval")
    parser.add_argument("--input", type=Path, help="Optional custom JSONL/CSV")
    parser.add_argument("--sample", type=int, default=None, help="Subsample size")
    parser.add_argument("--seed", type=int, default=int(os.getenv("EVAL_RANDOM_SEED", 42)))
    parser.add_argument(
        "--concurrency",
        type=int,
        default=int(os.getenv("EVAL_CONCURRENCY", 10)),
        help="Max concurrent candidate scores (async)",
    )
    parser.add_argument("--no-followups", action="store_true", help="Scorer only — 1 LLM call")
    parser.add_argument(
        "--followup-mode",
        choices=["end", "per_turn"],
        default=os.getenv("FOLLOWUP_MODE", "end"),
        help="end=1 follow-up max after all turns (prod default); per_turn=eval-strict",
    )
    args = parser.parse_args()

    out_dir = ROOT / ("results/custom" if args.input else "results")
    summary = run_eval(
        custom_path=args.input,
        sample_size=args.sample,
        seed=args.seed,
        concurrency=args.concurrency,
        enable_followups=not args.no_followups,
        followup_mode=args.followup_mode,
        results_dir=out_dir,
    )

    print("\n=== Eval complete ===")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print(f"\nResults written to {out_dir}/")


if __name__ == "__main__":
    main()
