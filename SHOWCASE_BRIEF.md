# Showcase Brief

## Project

DiscordBot Multi-Persona Playground (Public Showcase)

## Problem

Most of my learning projects were one-off scripts.
I wanted a reusable playground where I could test AI conversation design, memory handling, and bot personas in a real Discord environment.

## Solution

A multi-bot Discord setup where each bot has its own persona and memory namespace, while all AI calls route through one shared Engine contract.
This keeps experimentation fast without rewriting core AI calling logic every time.

## My Role

- Designed architecture and conversation flow.
- Implemented bot-side context, guardrails, and command workflow.
- Operated 3 bots on Ubuntu via `systemd --user` for continuous learning iteration.
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
- Keep the public repo focused on educational value and reproducibility.

## Results

- Built a reusable AI bot architecture for rapid idea testing.
- Reduced duplicated AI calling logic in bot-side code.
- Improved practical experience in bot operations, guardrails, and debugging.

## Next Steps

- Add test coverage around prompt assembly and memory behavior.
- Add lightweight local metrics for learning review.
- Publish demo screenshots and a short walkthrough video.
