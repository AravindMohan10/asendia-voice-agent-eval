#!/usr/bin/env python3
"""Materialize the staffing screen eval corpus → data/eval/records.jsonl"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.corpus.records import ALL_RECORDS
from src.data.loader import save_eval_set, validate_records
from src.data.schema import CandidateRecord, DatasetManifest


def main() -> None:
    records = [CandidateRecord.model_validate(r) for r in ALL_RECORDS]
    errors = validate_records(records)
    if errors:
        print("Validation failed:")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)

    manifest = DatasetManifest.from_records(
        description=(
            "Staffing-agency phone screen eval set. Models Sarah-style ingestion: "
            "mixed labeled transcripts, ASR paragraph blocks, and light ASR noise. "
            "50/50 select/reject. Ground truth = recruiter submit decision."
        ),
        records=records,
    )
    path = save_eval_set(records, manifest)
    print(f"Wrote {len(records)} records → {path}")
    print(f"  select/reject: {manifest.select_count}/{manifest.reject_count}")
    print(f"  verticals: {manifest.verticals}")
    print(f"  ingest formats: {manifest.ingest_formats}")
    print(f"  difficulty: {manifest.difficulties}")


if __name__ == "__main__":
    main()
