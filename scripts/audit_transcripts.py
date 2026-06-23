#!/usr/bin/env python3
"""Audit transcript realism — no LLM required."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.loader import load_eval_set

# Patterns that suggest real ASR output (not clean labeled dialogue)
ASR_SIGNALS = [
    (r"\bfour lift\b", "homophone: four lift"),
    (r"\brich truck\b", "homophone: rich truck"),
    (r"\bhippa\b", "homophone: hippa"),
    (r"\bepic baker\b", "homophone: epic baker"),
    (r"\bflattery role\b", "homophone: phlebotomy"),
    (r"\bOsha\b", "ASR: Osha"),
    (r"\bE P A\b", "ASR: spaced EPA"),
    (r"\bC D L\b", "ASR: spaced CDL"),
    (r"\bH vac\b", "ASR: H vac"),
    (r"\bW P M\b", "ASR: spaced WPM"),
    (r"\bdefinately\b", "common misspelling"),
    (r"\bbout\b", "informal: bout"),
]

SPEAKER_LABELS = re.compile(
    r"^(Interviewer|Recruiter|Sarah|Candidate|Agent)\s*:",
    re.I | re.M,
)


def main() -> None:
    records = load_eval_set()

    print("=== Transcript realism audit ===\n")
    for fmt in ["labeled", "asr_paragraph", "asr_noisy"]:
        subset = [r for r in records if r.ingest_format == fmt]
        print(f"{fmt} ({len(subset)} records)")
        if fmt == "labeled":
            labeled = sum(1 for r in subset if SPEAKER_LABELS.search(r.transcript))
            print(f"  speaker labels present: {labeled}/{len(subset)}")
        if fmt == "asr_noisy":
            unlabeled = sum(1 for r in subset if not SPEAKER_LABELS.search(r.transcript))
            with_signals = 0
            for r in subset:
                hits = [name for pat, name in ASR_SIGNALS if re.search(pat, r.transcript, re.I)]
                if hits:
                    with_signals += 1
            print(f"  unlabeled (no Recruiter:/Candidate:): {unlabeled}/{len(subset)}")
            print(f"  with ASR error signals: {with_signals}/{len(subset)}")
        if fmt == "asr_paragraph":
            unlabeled = sum(1 for r in subset if not SPEAKER_LABELS.search(r.transcript))
            print(f"  unlabeled paragraph blocks: {unlabeled}/{len(subset)}")
        print()

    print("Sample ASR-noisy excerpt (wh-020):")
    wh20 = next(r for r in records if r.id == "wh-020")
    print(wh20.transcript[:400])
    print("...")


if __name__ == "__main__":
    main()
