"""Input normalization — production ingestion layer."""

from __future__ import annotations

import re
import unicodedata


def normalize_decision(value: str) -> str:
    v = str(value).strip().lower()
    if v in {"select", "selected", "hire", "hired", "yes", "1", "pass", "approved"}:
        return "select"
    if v in {"reject", "rejected", "no", "0", "fail", "declined"}:
        return "reject"
    raise ValueError(f"Unknown decision label: {value!r}")


def normalize_text(text: str) -> str:
    """Strip BOM, normalize unicode, collapse excessive whitespace."""
    if not text:
        return ""
    text = text.replace("\ufeff", "")
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def normalize_record_fields(
    transcript: str,
    resume: str,
    job_description: str,
) -> tuple[str, str, str]:
    return (
        normalize_text(transcript),
        normalize_text(resume),
        normalize_text(job_description),
    )
