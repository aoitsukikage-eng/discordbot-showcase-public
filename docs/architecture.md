# Architecture

## Overview

This project runs multiple Discord bots (`bot1`, `bot2`, `bot3`) with separate behavior and memory namespaces.
All AI calls are routed through a shared Engine adapter contract.
The goal is to support iterative learning and experimentation in a real chat environment.

## Components

- Discord command/mention handlers
- Context builder (user memory + channel history)
- Identity guardrail layer
- Engine adapter (public interface)
- Private Engine implementation (not in this repo)

## Data Flow

1. User triggers slash command or mention.
2. Bot builds prompt context from recent interactions.
3. Guardrails are appended to reduce role confusion.
4. Request is sent through Engine adapter.
5. AI response is post-processed and sent back to channel.
6. Session memory is updated under bot namespace key.

## Namespace Strategy

Session key format example:

```text
{bot_namespace}:{guild_id}:{channel_id}:{user_id}
```

This prevents cross-bot memory contamination and supports multi-persona deployment.

## Deployment Model

Runtime is managed by `systemd --user` service units, one per bot.
Each service can be configured with auto-restart and independent working directory.
This setup is used for technical practice and operational learning.
