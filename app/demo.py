"""Gradio demo — single candidate screen. Deploy to Hugging Face Spaces."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import gradio as gr
from dotenv import load_dotenv

from src.agents.orchestrator import InterviewOrchestrator

load_dotenv(ROOT / ".env")


def screen_candidate(transcript: str, resume: str, job_description: str) -> str:
    if not all([transcript.strip(), resume.strip(), job_description.strip()]):
        return json.dumps({"error": "All fields are required."}, indent=2)

    orchestrator = InterviewOrchestrator()
    result = orchestrator.run(
        transcript=transcript,
        resume=resume,
        job_description=job_description,
    )
    return json.dumps(
        {
            "predicted_decision": result.predicted_decision,
            "confidence": result.confidence,
            "reasoning": result.reasoning,
            "risk_flags": result.risk_flags,
            "escalate_to_human": result.escalate_to_human,
            "turns_processed": result.turns_processed,
            "llm_calls": result.llm_calls,
            "latency_ms": round(result.total_latency_ms, 1),
        },
        indent=2,
    )


demo = gr.Interface(
    fn=screen_candidate,
    inputs=[
        gr.Textbox(label="Interview Transcript", lines=10, placeholder="Interviewer: ...\nCandidate: ..."),
        gr.Textbox(label="Resume", lines=8),
        gr.Textbox(label="Job Description", lines=6),
    ],
    outputs=gr.Textbox(label="Screening Result (JSON)", lines=12),
    title="Asendia-style Screening Agent Eval",
    description="Paste transcript + resume + JD. Agent replays turns and returns decision + confidence.",
    examples=[],
)

if __name__ == "__main__":
    demo.launch()
