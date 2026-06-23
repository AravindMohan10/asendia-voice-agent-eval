#!/usr/bin/env python3
"""Validate eval dataset — no LLM required."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.loader import load_custom, load_eval_set, load_manifest
from src.transcript_parser import parse_transcript


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate eval dataset")
    parser.add_argument("--input", type=Path, help="Custom JSONL or CSV")
    args = parser.parse_args()

    if args.input:
        records = load_custom(args.input)
        label = str(args.input)
    else:
        records = load_eval_set()
        manifest = load_manifest()
        label = manifest.name

    parse_stats = {"0_turns": 0, "1_turn": 0, "multi_turn": 0}
    for r in records:
        turns = parse_transcript(r.transcript)
        if not turns:
            parse_stats["0_turns"] += 1
        elif len(turns) == 1:
            parse_stats["1_turn"] += 1
        else:
            parse_stats["multi_turn"] += 1

    print(f"Dataset: {label}")
    print(f"  Records: {len(records)}")
    print(f"  Select: {sum(1 for r in records if r.decision == 'select')}")
    print(f"  Reject: {sum(1 for r in records if r.decision == 'reject')}")

    verticals: dict[str, int] = {}
    formats: dict[str, int] = {}
    for r in records:
        verticals[r.vertical] = verticals.get(r.vertical, 0) + 1
        formats[r.ingest_format] = formats.get(r.ingest_format, 0) + 1
    print(f"  Verticals: {verticals}")
    print(f"  Ingest formats: {formats}")
    print(f"  Turn parsing: {parse_stats}")
    print("\nValidation OK")


if __name__ == "__main__":
    main()
