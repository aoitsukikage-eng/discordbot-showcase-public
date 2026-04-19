# Showcase Brief

## Project

DiscordBot Multi-Agent Assistant (Public Showcase)

## Problem

Many Discord communities need fast AI assistance but struggle with consistency, deployment reliability, and safe key management.

## Solution

A multi-bot Discord architecture where each bot has its own persona and memory namespace, while all AI calls are routed through one shared Engine contract.

## My Role

- Designed architecture and conversation flow.
- Implemented bot-side context, guardrails, and command workflow.
- Deployed and operated 3 running bots via `systemd --user`.
- Defined reusable Engine boundary for cross-project reuse.

## Tech Stack

- Python
- `discord.py`
- `python-dotenv`
- private `Engine` adapter contract
- Ubuntu `systemd --user`

## Key Design Choices

- Keep Engine private, publish adapter and interface.
- Isolate memory per bot namespace to prevent cross-bot contamination.
- Use deployment runbooks and documented operational commands.

## Results

- Reusable architecture across multiple bot personas.
- Reduced duplicated AI calling logic in bot code.
- Better maintainability and safer secret handling model.

## Next Steps

- Add test coverage around prompt assembly and memory behavior.
- Add structured logging and metrics export.
- Publish demo video and command walkthrough.
