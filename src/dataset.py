"""Backward-compatible re-exports."""

from src.data.loader import load_eval_set
from src.data.schema import CandidateRecord
from src.data.normalize import normalize_decision

__all__ = ["CandidateRecord", "load_eval_set", "normalize_decision"]
