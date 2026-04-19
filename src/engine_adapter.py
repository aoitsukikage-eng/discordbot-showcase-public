"""Public Engine adapter contract for the showcase repository.

The real Engine implementation is private and intentionally excluded.
"""

import os
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


class ExternalEngineAdapter(EngineAdapter):
    """Adapter placeholder for private Engine integration.

    This class intentionally does not ship private key-management logic.
    """

    def __init__(self, engine_path: str, engine_api_env_file: str = "") -> None:
        self.engine_path = (engine_path or "").strip()
        self.engine_api_env_file = (engine_api_env_file or "").strip()

    def call_ai(self, req: EngineRequest) -> EngineResponse:
        msg = (
            "ENGINE_MODE=external requires your own private Engine integration. "
            "This public repo does not include API-key handling. "
            f"ENGINE_PATH='{self.engine_path or '<empty>'}', "
            f"ENGINE_API_ENV_FILE='{self.engine_api_env_file or '<unset>'}'. "
            "Put provider keys in your private Engine env/config, not in this repo."
        )
        if os.getenv("ENGINE_MODE", "mock").lower() == "external":
            raise RuntimeError(msg)
        raise RuntimeError("ExternalEngineAdapter called without external mode.")
