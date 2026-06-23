"""Canonical eval record schema."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, field_validator


class CandidateRecord(BaseModel):
    """Single eval record. Ground-truth fields are never passed to the agent."""

    id: str
    transcript: str = Field(min_length=1)
    resume: str = Field(min_length=1)
    job_description: str = Field(min_length=1)
    decision: Literal["select", "reject"]
    reason: str = Field(min_length=1)

    vertical: str = "general"
    # How the transcript arrived — metadata only, not shown to agent
    ingest_format: Literal["labeled", "asr_paragraph", "asr_noisy"] = "labeled"
    difficulty: Literal["clear", "borderline"] = "clear"

    @field_validator("decision", mode="before")
    @classmethod
    def normalize_decision(cls, v: str) -> str:
        from src.data.normalize import normalize_decision

        return normalize_decision(v)

    def agent_inputs(self) -> dict[str, str]:
        return {
            "transcript": self.transcript,
            "resume": self.resume,
            "job_description": self.job_description,
        }


class DatasetManifest(BaseModel):
    version: str = "1.0"
    name: str = "staffing_screen_eval_v1"
    description: str
    record_count: int
    select_count: int
    reject_count: int
    verticals: dict[str, int]
    ingest_formats: dict[str, int]
    difficulties: dict[str, int]
    schema_version: str = "1.0"

    @classmethod
    def from_records(cls, description: str, records: list[CandidateRecord]) -> DatasetManifest:
        verticals: dict[str, int] = {}
        formats: dict[str, int] = {}
        difficulties: dict[str, int] = {}
        for r in records:
            verticals[r.vertical] = verticals.get(r.vertical, 0) + 1
            formats[r.ingest_format] = formats.get(r.ingest_format, 0) + 1
            difficulties[r.difficulty] = difficulties.get(r.difficulty, 0) + 1
        return cls(
            description=description,
            record_count=len(records),
            select_count=sum(1 for r in records if r.decision == "select"),
            reject_count=sum(1 for r in records if r.decision == "reject"),
            verticals=verticals,
            ingest_formats=formats,
            difficulties=difficulties,
        )
