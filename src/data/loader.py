"""Load and validate the production eval dataset."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from src.data.normalize import normalize_decision, normalize_record_fields
from src.data.schema import CandidateRecord, DatasetManifest

DATA_ROOT = Path(__file__).resolve().parents[2] / "data"
EVAL_DIR = DATA_ROOT / "eval"
EVAL_RECORDS = EVAL_DIR / "records.jsonl"
EVAL_MANIFEST = EVAL_DIR / "manifest.json"

COL_ALIASES = {
    "id": ["id", "ID", "candidate_id"],
    "transcript": ["Transcript", "transcript", "Interview_Transcript"],
    "resume": ["Resume", "resume", "CV"],
    "job_description": ["Job_Description", "job_description", "JobDescription"],
    "decision": ["Decision", "decision", "Hiring_Decision"],
    "reason": ["Reason_for_decision", "reason_for_decision", "Reason"],
    "vertical": ["vertical", "Vertical"],
    "ingest_format": ["ingest_format", "Ingest_Format"],
    "difficulty": ["difficulty", "Difficulty"],
}


def _resolve_column(df: pd.DataFrame, aliases: list[str]) -> str | None:
    for name in aliases:
        if name in df.columns:
            return name
    return None


def validate_records(records: list[CandidateRecord]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()

    for r in records:
        if r.id in seen_ids:
            errors.append(f"Duplicate id: {r.id}")
        seen_ids.add(r.id)
        if len(r.transcript) < 80:
            errors.append(f"{r.id}: transcript too short ({len(r.transcript)} chars)")
        if len(r.resume) < 40:
            errors.append(f"{r.id}: resume too short")
        if len(r.job_description) < 40:
            errors.append(f"{r.id}: job_description too short")

    selects = sum(1 for r in records if r.decision == "select")
    rejects = len(records) - selects
    if len(records) >= 10 and abs(selects - rejects) > len(records) * 0.1:
        errors.append(f"Imbalanced decisions: {selects} select / {rejects} reject")

    return errors


def _records_from_jsonl(path: Path) -> list[CandidateRecord]:
    records: list[CandidateRecord] = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if line:
            records.append(CandidateRecord.model_validate_json(line))
    if not records:
        raise ValueError(f"No records in {path}")
    return records


def load_eval_set(
    sample: int | None = None,
    seed: int = 42,
    path: Path | None = None,
) -> list[CandidateRecord]:
    records_path = path or EVAL_RECORDS
    if not records_path.exists():
        raise FileNotFoundError(
            f"Eval dataset not found at {records_path}. Run: python scripts/build_dataset.py"
        )

    records = _records_from_jsonl(records_path)

    if sample is not None and sample < len(records):
        df = pd.DataFrame([{"id": r.id, "decision": r.decision} for r in records])
        idx, _ = train_test_split(
            df.index,
            train_size=sample,
            stratify=df["decision"],
            random_state=seed,
        )
        idx_set = set(idx)
        records = [r for i, r in enumerate(records) if i in idx_set]

    errors = validate_records(records)
    if errors:
        raise ValueError("Dataset validation failed:\n" + "\n".join(errors[:20]))

    return records


def load_manifest(path: Path | None = None) -> DatasetManifest:
    manifest_path = path or EVAL_MANIFEST
    if not manifest_path.exists():
        raise FileNotFoundError(f"Missing manifest: {manifest_path}")
    return DatasetManifest.model_validate_json(manifest_path.read_text())


def load_custom(path: Path) -> list[CandidateRecord]:
    if not path.exists():
        raise FileNotFoundError(path)

    if path.suffix.lower() == ".jsonl":
        records = _records_from_jsonl(path)
    elif path.suffix.lower() == ".csv":
        records = _records_from_csv(path)
    else:
        raise ValueError(f"Unsupported format: {path.suffix}. Use .jsonl or .csv")

    errors = validate_records(records)
    if errors:
        raise ValueError("Custom dataset validation failed:\n" + "\n".join(errors[:20]))
    return records


def _records_from_csv(path: Path) -> list[CandidateRecord]:
    df = pd.read_csv(path)
    id_col = _resolve_column(df, COL_ALIASES["id"])
    t = _resolve_column(df, COL_ALIASES["transcript"])
    r = _resolve_column(df, COL_ALIASES["resume"])
    j = _resolve_column(df, COL_ALIASES["job_description"])
    d = _resolve_column(df, COL_ALIASES["decision"])
    reason_col = _resolve_column(df, COL_ALIASES["reason"])
    v = _resolve_column(df, COL_ALIASES["vertical"])
    fmt = _resolve_column(df, COL_ALIASES["ingest_format"])
    diff = _resolve_column(df, COL_ALIASES["difficulty"])

    missing = [
        name
        for name, col in [
            ("transcript", t),
            ("resume", r),
            ("job_description", j),
            ("decision", d),
            ("reason", reason_col),
        ]
        if col is None
    ]
    if missing:
        raise KeyError(f"CSV missing columns: {missing}. Found: {list(df.columns)}")

    records: list[CandidateRecord] = []
    for idx, row in df.iterrows():
        tid, res, jd = normalize_record_fields(str(row[t]), str(row[r]), str(row[j]))
        records.append(
            CandidateRecord(
                id=str(row[id_col]) if id_col else str(idx),
                transcript=tid,
                resume=res,
                job_description=jd,
                decision=normalize_decision(row[d]),
                reason=str(row[reason_col]),
                vertical=str(row[v]) if v and pd.notna(row[v]) else "general",
                ingest_format=str(row[fmt]) if fmt and pd.notna(row[fmt]) else "labeled",
                difficulty=str(row[diff]) if diff and pd.notna(row[diff]) else "clear",
            )
        )
    return records


def save_eval_set(records: list[CandidateRecord], manifest: DatasetManifest) -> Path:
    EVAL_DIR.mkdir(parents=True, exist_ok=True)
    with EVAL_RECORDS.open("w") as f:
        for r in records:
            f.write(r.model_dump_json() + "\n")
    EVAL_MANIFEST.write_text(manifest.model_dump_json(indent=2) + "\n")
    return EVAL_RECORDS
