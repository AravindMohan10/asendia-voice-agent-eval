"""Scorer agent — final hire/reject decision with confidence."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from src.agents.state import InterviewState
from src.llm.client import LLMClient

PROMPT_PATH = Path(__file__).resolve().parents[2] / "prompts" / "scorer_v1.txt"


@dataclass
class ScoreResult:
    predicted_decision: str
    confidence: int
    reasoning: str
    risk_flags: list[str]
    escalate_to_human: bool
    turns_processed: int
    llm_calls: int = 0
    latency_ms: float = 0.0


class ScorerAgent:
    def __init__(self, llm: LLMClient | None = None):
        self.llm = llm or LLMClient.shared()
        self.system_prompt = PROMPT_PATH.read_text()

    def _user_message(self, state: InterviewState) -> str:
        return (
            f"Job description:\n{state.job_description}\n\n"
            f"Resume:\n{state.resume}\n\n"
            f"Interview transcript:\n{state.conversation_so_far()}"
        )

    async def ascore(self, state: InterviewState) -> ScoreResult:
        from src.llm.client import LLMResponse

        resp: LLMResponse = await self.llm.acomplete_with_meta(
            self.system_prompt, self._user_message(state)
        )
        result = resp.data

        decision = str(result.get("predicted_decision", "reject")).lower()
        if decision not in {"select", "reject"}:
            decision = "reject"

        return ScoreResult(
            predicted_decision=decision,
            confidence=int(result.get("confidence", 50)),
            reasoning=str(result.get("reasoning", "")),
            risk_flags=list(result.get("risk_flags") or []),
            escalate_to_human=bool(result.get("escalate_to_human", False)),
            turns_processed=len(state.observed_turns),
            llm_calls=1,
            latency_ms=resp.latency_ms,
        )

    def score(self, state: InterviewState) -> ScoreResult:
        from src.llm.client import run_sync

        return run_sync(self.ascore(state))
