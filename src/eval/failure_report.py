"""High-confidence failure report."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PredictionRow:
    id: str
    predicted: str
    actual: str
    confidence: int
    reasoning: str
    transcript_excerpt: str
    vertical: str = ""
    difficulty: str = ""


def build_failure_report(
    rows: list[PredictionRow],
    confidence_threshold: int = 80,
    top_k: int = 5,
) -> str:
    failures = [
        r
        for r in rows
        if r.confidence >= confidence_threshold and r.predicted != r.actual
    ]
    failures.sort(key=lambda r: r.confidence, reverse=True)
    failures = failures[:top_k]

    lines = [
        "# High-Confidence Failures",
        "",
        f"Cases where confidence ≥ {confidence_threshold} but prediction was **wrong**.",
        "These are the most dangerous failures in production — the agent is confident but incorrect.",
        "",
    ]

    if not failures:
        lines.append("_No high-confidence failures in this run._")
        return "\n".join(lines)

    for i, f in enumerate(failures, 1):
        meta = []
        if f.vertical:
            meta.append(f"**Vertical:** {f.vertical}")
        if f.difficulty:
            meta.append(f"**Difficulty:** {f.difficulty}")

        lines.extend(
            [
                f"## Case {i} ({f.id})",
                "",
                f"- **Predicted:** {f.predicted}",
                f"- **Actual:** {f.actual}",
                f"- **Confidence:** {f.confidence}",
            ]
        )
        if meta:
            lines.append(f"- {' | '.join(meta)}")
        lines.extend(
            [
                f"- **Reasoning:** {f.reasoning}",
                f"- **Transcript excerpt:** {f.transcript_excerpt[:400]}...",
                "",
            ]
        )

    return "\n".join(lines)
