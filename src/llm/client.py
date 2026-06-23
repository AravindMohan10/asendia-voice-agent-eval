"""Production LLM client — async-first, connection reuse, retries, JSON mode."""

from __future__ import annotations

import asyncio
import json
import logging
import os
import re
import time
from dataclasses import dataclass
from typing import Any

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


def _extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    if text.startswith("{"):
        return json.loads(text)
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError(f"No JSON object found in LLM response: {text[:200]}")
    return json.loads(match.group())


@dataclass
class LLMResponse:
    data: dict[str, Any]
    latency_ms: float
    model: str
    provider: str


class LLMClient:
    """Async-first client. Use ``acomplete`` in hot paths; ``complete`` for sync callers."""

    _instances: dict[str, LLMClient] = {}

    def __init__(self, provider: str | None = None):
        self.provider = (provider or os.getenv("LLM_PROVIDER", "openai")).lower()
        self.max_retries = int(os.getenv("LLM_MAX_RETRIES", "3"))
        self.timeout_sec = float(os.getenv("LLM_TIMEOUT_SEC", "60"))
        self._groq_client: Any = None
        self._openai_client: Any = None
        self._lock = asyncio.Lock()

    @classmethod
    def shared(cls, provider: str | None = None) -> LLMClient:
        key = (provider or os.getenv("LLM_PROVIDER", "openai")).lower()
        if key not in cls._instances:
            cls._instances[key] = cls(provider=key)
        return cls._instances[key]

    def _model_name(self) -> str:
        if self.provider == "openai":
            return os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        if self.provider == "gemini":
            return os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
        if self.provider == "groq":
            return os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        raise ValueError(f"Unknown provider: {self.provider}")

    async def acomplete(self, system: str, user: str) -> dict[str, Any]:
        resp = await self.acomplete_with_meta(system, user)
        return resp.data

    async def acomplete_with_meta(self, system: str, user: str) -> LLMResponse:
        last_err: Exception | None = None
        for attempt in range(1, self.max_retries + 1):
            started = time.perf_counter()
            try:
                raw = await self._call_async(system, user)
                data = _extract_json(raw)
                latency_ms = (time.perf_counter() - started) * 1000
                model = self._model_name()
                logger.debug(
                    "llm ok provider=%s model=%s latency_ms=%.0f attempt=%d",
                    self.provider,
                    model,
                    latency_ms,
                    attempt,
                )
                return LLMResponse(
                    data=data,
                    latency_ms=latency_ms,
                    model=model,
                    provider=self.provider,
                )
            except Exception as exc:
                last_err = exc
                logger.warning(
                    "llm attempt %d/%d failed: %s",
                    attempt,
                    self.max_retries,
                    exc,
                )
                if attempt < self.max_retries:
                    await asyncio.sleep(min(2**attempt, 8))
        raise RuntimeError(f"LLM failed after {self.max_retries} attempts") from last_err

    def complete(self, system: str, user: str) -> dict[str, Any]:
        return run_sync(self.acomplete(system, user))

    async def _call_async(self, system: str, user: str) -> str:
        if self.provider == "openai":
            return await self._openai_async(system, user)
        if self.provider == "gemini":
            return await self._gemini_async(system, user)
        if self.provider == "groq":
            return await self._groq_async(system, user)
        raise ValueError(f"Unknown LLM_PROVIDER: {self.provider}")

    async def _get_groq(self) -> Any:
        if self._groq_client is None:
            async with self._lock:
                if self._groq_client is None:
                    from groq import AsyncGroq

                    self._groq_client = AsyncGroq(
                        api_key=os.environ["GROQ_API_KEY"],
                        timeout=self.timeout_sec,
                    )
        return self._groq_client

    async def _get_openai(self) -> Any:
        if self._openai_client is None:
            async with self._lock:
                if self._openai_client is None:
                    from openai import AsyncOpenAI

                    self._openai_client = AsyncOpenAI(
                        api_key=os.environ["OPENAI_API_KEY"],
                        timeout=self.timeout_sec,
                    )
        return self._openai_client

    async def _groq_async(self, system: str, user: str) -> str:
        client = await self._get_groq()
        model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]
        kwargs: dict[str, Any] = {"model": model, "messages": messages, "temperature": 0.2}
        try:
            resp = await client.chat.completions.create(
                **kwargs,
                response_format={"type": "json_object"},
            )
        except Exception:
            resp = await client.chat.completions.create(**kwargs)
        return resp.choices[0].message.content or ""

    async def _openai_async(self, system: str, user: str) -> str:
        client = await self._get_openai()
        model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        resp = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=0.2,
            response_format={"type": "json_object"},
        )
        return resp.choices[0].message.content or ""

    async def _gemini_async(self, system: str, user: str) -> str:
        # Gemini SDK is sync — run in thread pool to avoid blocking the event loop
        return await asyncio.to_thread(self._gemini_sync, system, user)

    def _gemini_sync(self, system: str, user: str) -> str:
        import google.generativeai as genai

        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-2.0-flash"))
        resp = model.generate_content(f"{system}\n\n{user}")
        return resp.text or ""


def run_sync(coro: Any) -> Any:
    """Run coroutine from sync context (CLI, Gradio)."""
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)
    raise RuntimeError("Use async API inside a running event loop")


def runtime_info() -> dict[str, str]:
    """Provider/model/prompt versions for reproducibility in results."""
    from pathlib import Path

    client = LLMClient.shared()
    root = Path(__file__).resolve().parents[2]
    scorer_path = root / "prompts" / "scorer_v1.txt"
    interviewer_path = root / "prompts" / "interviewer_v1.txt"
    return {
        "llm_provider": client.provider,
        "llm_model": client._model_name(),
        "scorer_prompt": "scorer_v1.txt",
        "interviewer_prompt": "interviewer_v1.txt",
        "scorer_prompt_sha256_8": _file_hash_prefix(str(scorer_path)),
        "interviewer_prompt_sha256_8": _file_hash_prefix(str(interviewer_path)),
    }


def _file_hash_prefix(path: str) -> str:
    import hashlib
    from pathlib import Path

    p = Path(path)
    if not p.exists():
        return "missing"
    return hashlib.sha256(p.read_bytes()).hexdigest()[:8]
