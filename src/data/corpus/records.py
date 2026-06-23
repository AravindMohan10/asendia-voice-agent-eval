"""Curated staffing-agency phone screen records — source of truth for the eval set."""

from __future__ import annotations

from src.data.corpus.warehouse import WAREHOUSE_RECORDS
from src.data.corpus.healthcare import HEALTHCARE_RECORDS
from src.data.corpus.call_center import CALL_CENTER_RECORDS
from src.data.corpus.skilled_trades import SKILLED_TRADES_RECORDS
from src.data.corpus.admin import ADMIN_RECORDS
from src.data.corpus.asr_layer import apply_asr_overrides

_RAW: list[dict] = (
    WAREHOUSE_RECORDS
    + HEALTHCARE_RECORDS
    + CALL_CENTER_RECORDS
    + SKILLED_TRADES_RECORDS
    + ADMIN_RECORDS
)

ALL_RECORDS: list[dict] = apply_asr_overrides(_RAW)

assert len(ALL_RECORDS) == 100, f"Expected 100 records, got {len(ALL_RECORDS)}"

_ids = [r["id"] for r in ALL_RECORDS]
assert len(_ids) == len(set(_ids)), "Duplicate record IDs"

_selects = sum(1 for r in ALL_RECORDS if r["decision"] == "select")
assert _selects == 50, f"Expected 50 select, got {_selects}"
