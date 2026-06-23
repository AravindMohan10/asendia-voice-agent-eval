"""Split interview transcripts into turns for sequential replay."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Turn:
    speaker: str  # "interviewer" | "candidate" | "unknown"
    text: str
    index: int


SPEAKER_PATTERNS = [
    (re.compile(r"^(interviewer|recruiter|agent|sarah)\s*:", re.I), "interviewer"),
    (re.compile(r"^(candidate|applicant|user)\s*:", re.I), "candidate"),
    (re.compile(r"^Q\s*:", re.I), "interviewer"),
    (re.compile(r"^A\s*:", re.I), "candidate"),
]


def parse_transcript(transcript: str) -> list[Turn]:
    """Parse labeled transcript into turns. Falls back to paragraph split."""
    lines = [ln.strip() for ln in transcript.splitlines() if ln.strip()]
    if not lines:
        return [Turn(speaker="unknown", text=transcript.strip(), index=0)]

    turns: list[Turn] = []
    current_speaker = "unknown"
    current_text: list[str] = []

    def flush(index: int) -> None:
        if current_text:
            turns.append(
                Turn(
                    speaker=current_speaker,
                    text=" ".join(current_text).strip(),
                    index=index,
                )
            )

    turn_idx = 0
    for line in lines:
        matched = False
        for pattern, speaker in SPEAKER_PATTERNS:
            m = pattern.match(line)
            if m:
                flush(turn_idx)
                turn_idx += 1
                current_speaker = speaker
                remainder = line[m.end() :].strip()
                current_text = [remainder] if remainder else []
                matched = True
                break
        if not matched:
            current_text.append(line)

    flush(turn_idx)

    if len(turns) <= 1 and len(transcript) > 200:
        # Fallback: split on double newlines
        chunks = [c.strip() for c in re.split(r"\n\s*\n", transcript) if c.strip()]
        return [Turn(speaker="unknown", text=c, index=i) for i, c in enumerate(chunks)]

    return turns


def format_conversation(turns: list[Turn]) -> str:
    return "\n".join(f"{t.speaker}: {t.text}" for t in turns)
