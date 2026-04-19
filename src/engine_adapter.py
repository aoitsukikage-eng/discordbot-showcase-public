"""Public Engine adapter contract for the showcase repository.

The real Engine implementation is private and intentionally excluded.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class EngineRequest:
    model: str
    system_prompt: str
    user_prompt: str
    timeout_sec: int = 20


@dataclass
class EngineResponse:
    text: str
    provider: str
    latency_ms: int
    error: Optional[str] = None


class EngineAdapter:
    """Minimal interface that bot-side code depends on."""

    def call_ai(self, req: EngineRequest) -> EngineResponse:
        raise NotImplementedError("Provide private Engine-backed implementation")


class MockEngineAdapter(EngineAdapter):
    """Safe local fallback for demo and tests."""

    def call_ai(self, req: EngineRequest) -> EngineResponse:
        preview = req.user_prompt.strip().replace("\n", " ")[:80]
        return EngineResponse(
            text=f"[mock-response] {preview}",
            provider="mock",
            latency_ms=10,
            error=None,
        )
