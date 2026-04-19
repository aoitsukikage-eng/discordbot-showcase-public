"""Minimal bot-side entrypoint for public showcase.

This file demonstrates the boundary between bot logic and Engine adapter.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

from engine_adapter import EngineRequest, MockEngineAdapter


@dataclass
class Settings:
    bot_namespace: str
    discord_token: str


def load_settings() -> Settings:
    load_dotenv()
    token = os.getenv("DISCORD_BOT_TOKEN", "")
    namespace = os.getenv("BOT_NAMESPACE", "bot_showcase")
    return Settings(bot_namespace=namespace, discord_token=token)


def demo_call(user_message: str) -> str:
    adapter = MockEngineAdapter()
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
    print(demo_call("hello showcase"))
