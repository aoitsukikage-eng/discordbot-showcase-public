"""Minimal bot-side entrypoint for public showcase.

This file demonstrates the boundary between bot logic and Engine adapter.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

from engine_adapter import EngineRequest, ExternalEngineAdapter, MockEngineAdapter


@dataclass
class Settings:
    bot_namespace: str
    discord_token: str
    engine_mode: str
    engine_path: str
    engine_api_env_file: str


def load_settings() -> Settings:
    load_dotenv()
    token = os.getenv("DISCORD_BOT_TOKEN", "")
    namespace = os.getenv("BOT_NAMESPACE", "bot_showcase")
    mode = os.getenv("ENGINE_MODE", "mock").strip().lower()
    engine_path = os.getenv("ENGINE_PATH", "")
    engine_api_env_file = os.getenv("ENGINE_API_ENV_FILE", "")
    return Settings(
        bot_namespace=namespace,
        discord_token=token,
        engine_mode=mode,
        engine_path=engine_path,
        engine_api_env_file=engine_api_env_file,
    )


def build_adapter(settings: Settings):
    if settings.engine_mode == "mock":
        return MockEngineAdapter()
    if settings.engine_mode == "external":
        return ExternalEngineAdapter(
            engine_path=settings.engine_path,
            engine_api_env_file=settings.engine_api_env_file,
        )
    raise RuntimeError(
        f"Unsupported ENGINE_MODE='{settings.engine_mode}'. Use 'mock' or 'external'."
    )


def demo_call(settings: Settings, user_message: str) -> str:
    adapter = build_adapter(settings)
    req = EngineRequest(
        model="demo-model",
        system_prompt="You are a helpful Discord assistant.",
        user_prompt=user_message,
        timeout_sec=15,
    )
    resp = adapter.call_ai(req)
    return resp.text


if __name__ == "__main__":
    settings = load_settings()
    print(f"namespace={settings.bot_namespace}")
    print(f"engine_mode={settings.engine_mode}")
    print(demo_call(settings, "hello showcase"))
