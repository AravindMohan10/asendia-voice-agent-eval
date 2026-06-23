"""Multi-turn interview orchestrator — turn-replay with production latency profile."""

from __future__ import annotations

import os
import time
from dataclasses import dataclass

from src.agents.interviewer import InterviewerAgent
from src.agents.scorer import ScorerAgent, ScoreResult
from src.agents.state import InterviewState
from src.transcript_parser import parse_transcript


@dataclass
class OrchestratorResult(ScoreResult):
    """Score plus orchestration metadata."""

    followups_asked: int = 0
    total_latency_ms: float = 0.0


class InterviewOrchestrator:
    """Replays transcript turns sequentially; scores with at most 2 LLM calls.

    Production path (default ``followup_mode=end``):
      1. Ingest all turns (no LLM) — mirrors post-call scoring on full ASR transcript
      2. Optional single follow-up check if gaps exist
      3. Final score

    Eval-strict path (``followup_mode=per_turn``): follow-up check after each candidate turn.
    """

    def __init__(
        self,
        interviewer: InterviewerAgent | None = None,
        scorer: ScorerAgent | None = None,
        enable_followups: bool = True,
        max_followups: int | None = None,
        followup_mode: str | None = None,
    ):
        self.interviewer = interviewer or InterviewerAgent()
        self.scorer = scorer or ScorerAgent()
        self.enable_followups = enable_followups
        self.max_followups = max_followups if max_followups is not None else int(
            os.getenv("MAX_FOLLOWUPS", "1")
        )
        self.followup_mode = followup_mode or os.getenv("FOLLOWUP_MODE", "end")

    async def arun(
        self,
        transcript: str,
        resume: str,
        job_description: str,
    ) -> OrchestratorResult:
        started = time.perf_counter()
        turns = parse_transcript(transcript)
        state = InterviewState(resume=resume, job_description=job_description)
        followups_asked = 0
        llm_calls = 0
        llm_latency_ms = 0.0

        if self.followup_mode == "per_turn":
            for turn in turns:
                state.observed_turns.append(turn)
                if (
                    self.enable_followups
                    and followups_asked < self.max_followups
                    and turn.speaker in {"candidate", "unknown"}
                ):
                    resp = await self.interviewer.llm.acomplete_with_meta(
                        self.interviewer.system_prompt,
                        self.interviewer._user_message(state),
                    )
                    llm_calls += 1
                    llm_latency_ms += resp.latency_ms
                    if not resp.data.get("done", True) and resp.data.get("question"):
                        state.agent_questions.append(str(resp.data["question"]))
                        followups_asked += 1
        else:
            for turn in turns:
                state.observed_turns.append(turn)
            if self.enable_followups and self.max_followups > 0 and turns:
                resp = await self.interviewer.llm.acomplete_with_meta(
                    self.interviewer.system_prompt,
                    self.interviewer._user_message(state),
                )
                llm_calls += 1
                llm_latency_ms += resp.latency_ms
                if not resp.data.get("done", True) and resp.data.get("question"):
                    state.agent_questions.append(str(resp.data["question"]))
                    followups_asked = 1

        score = await self.scorer.ascore(state)
        llm_calls += score.llm_calls
        llm_latency_ms += score.latency_ms
        total_ms = (time.perf_counter() - started) * 1000

        return OrchestratorResult(
            predicted_decision=score.predicted_decision,
            confidence=score.confidence,
            reasoning=score.reasoning,
            risk_flags=score.risk_flags,
            escalate_to_human=score.escalate_to_human,
            turns_processed=score.turns_processed,
            llm_calls=llm_calls,
            latency_ms=llm_latency_ms,
            followups_asked=followups_asked,
            total_latency_ms=total_ms,
        )

    def run(
        self,
        transcript: str,
        resume: str,
        job_description: str,
    ) -> OrchestratorResult:
        from src.llm.client import run_sync

        return run_sync(self.arun(transcript, resume, job_description))
