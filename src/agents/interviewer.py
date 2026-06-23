"""Interviewer agent — optional follow-up before final score."""

from __future__ import annotations

from pathlib import Path

from src.agents.state import InterviewState
from src.llm.client import LLMClient

PROMPT_PATH = Path(__file__).resolve().parents[2] / "prompts" / "interviewer_v1.txt"


class InterviewerAgent:
    def __init__(self, llm: LLMClient | None = None):
        self.llm = llm or LLMClient.shared()
        self.system_prompt = PROMPT_PATH.read_text()

    def _user_message(self, state: InterviewState) -> str:
        return (
            f"Job description:\n{state.job_description}\n\n"
            f"Resume:\n{state.resume}\n\n"
            f"Conversation so far:\n{state.conversation_so_far()}"
        )

    async def amaybe_follow_up(self, state: InterviewState) -> str | None:
        result = await self.llm.acomplete(self.system_prompt, self._user_message(state))
        if result.get("done", True):
            return None
        question = result.get("question")
        return str(question) if question else None

    def maybe_follow_up(self, state: InterviewState) -> str | None:
        from src.llm.client import run_sync

        return run_sync(self.amaybe_follow_up(state))
