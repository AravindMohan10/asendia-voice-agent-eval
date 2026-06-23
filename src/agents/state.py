"""Shared interview state for turn-replay orchestration."""

from __future__ import annotations

from dataclasses import dataclass, field

from src.transcript_parser import Turn


@dataclass
class InterviewState:
    resume: str
    job_description: str
    observed_turns: list[Turn] = field(default_factory=list)
    agent_questions: list[str] = field(default_factory=list)

    def conversation_so_far(self) -> str:
        lines = []
        for t in self.observed_turns:
            lines.append(f"{t.speaker}: {t.text}")
        for q in self.agent_questions:
            lines.append(f"interviewer: {q}")
        return "\n".join(lines)
