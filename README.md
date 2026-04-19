# DiscordBot Showcase (Public)

A public showcase version of my multi-bot Discord project.

This repository is focused on learning, experimentation, and technical demonstration.
It is not a commercial product.

This repository intentionally exposes the application layer and architecture, while keeping the private `Engine` implementation out of scope.

## Why This Repo Exists

- Practice AI bot architecture through real Discord interactions.
- Test new ideas safely in an entertainment-oriented project.
- Show how one private Engine interface can be reused across different bot personas.
- Keep a clean portfolio record of technical growth.

## Project Highlights

- Multi-bot architecture (`bot1`, `bot2`, `bot3`) with isolated memory namespaces.
- Unified AI call flow through an Engine adapter (private Engine not published).
- Context strategy: user-turn memory + recent channel context.
- Guardrails for role identity and prompt contamination.
- Clear public/private boundary so the showcase is safe to publish.

## Public/Private Boundary

Published in this repo:

- Bot-side architecture
- Engine interface contract
- Environment contract and runbook
- Demo scenarios and decision records

Not published in this repo:

- Real API keys
- Private Engine core implementation
- Secrets, runtime logs, personal deployment details

## Where To Put Keys

This public repository only requires Discord bot runtime values in local `.env`.

- `DISCORD_BOT_TOKEN` goes in this repo's `.env`.
- AI provider keys do not go in this repo.
- If you use `ENGINE_MODE=external`, put provider keys in your private Engine's env/config.

This design keeps key-management logic private while still making the bot architecture explainable.

## Runtime Modes

- `ENGINE_MODE=mock`
  - Runs without real AI provider calls.
  - Best for code walkthrough, structure demo, and local testing.
- `ENGINE_MODE=external`
  - Expects your own private Engine integration.
  - This repo will not expose or ship your provider key handling.

## Quick Start

```bash
# 1) Create and activate Python environment
python3 -m venv .venv
source .venv/bin/activate

# 2) Install runtime dependencies
pip install -U pip
pip install discord.py python-dotenv

# 3) Prepare environment values
cp .env.example .env

# 4) Run in mock mode (default, no real AI key needed)
python src/bot_entrypoint.py
```

To run with your own private Engine:

1. Set `ENGINE_MODE=external` in `.env`.
2. Set `ENGINE_PATH` and `ENGINE_API_ENV_FILE` to your private setup.
3. Keep provider keys in that private Engine env/config, not in this public repo.

## Repository Layout

```text
discordbot-showcase-public/
├── README.md
├── SHOWCASE_BRIEF.md
├── METRICS.md
├── DEMO_SCRIPT.md
├── PUBLISH_CHECKLIST.md
├── .env.example
├── .gitignore
├── docs/
│   ├── architecture.md
│   ├── engine-interface.md
│   ├── demo-scenarios.md
│   └── decisions.md
├── src/
│   ├── engine_adapter.py
│   └── bot_entrypoint.py
└── tests/
    └── test_engine_adapter.py
```

## What To Read First

1. `SHOWCASE_BRIEF.md`
2. `docs/architecture.md`
3. `docs/engine-interface.md`
4. `docs/demo-scenarios.md`

## Notes for Notion Portfolio Agent

The following files are intentionally structured for direct transformation into a Notion project page:

- `SHOWCASE_BRIEF.md`
- `METRICS.md`
- `DEMO_SCRIPT.md`
- `docs/decisions.md`
