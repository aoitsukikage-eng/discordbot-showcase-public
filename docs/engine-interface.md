# Engine Interface (Public Contract)

The Engine core is private.
This document defines the integration contract used by bot-side code.

## Goals

- Keep key management and provider-specific logic out of bot code.
- Standardize AI invocation across different applications.
- Preserve portability between local and server environments.

## Contract

Input fields:

- `model`: target model identifier
- `system_prompt`: instruction context
- `user_prompt`: user message or assembled context
- `timeout_sec`: timeout budget
- `metadata`: optional tracing or namespace values

Output fields:

- `text`: generated response text
- `provider`: provider used
- `latency_ms`: observed latency
- `error`: optional error info

## Error Semantics

Expected error categories:

- `timeout`
- `rate_limit`
- `provider_unavailable`
- `invalid_request`

Bot-side logic should treat errors as user-safe messages and avoid leaking internals.

## Privacy Boundary

This repository does not publish:

- key rotation logic
- provider fallback strategy internals
- private rate-limit heuristics

## Key Placement Guidance

- `DISCORD_BOT_TOKEN` belongs to this project's local `.env`.
- AI provider keys should be stored in your private Engine environment/config.
- Do not commit provider keys into this public repository.

## Runtime Expectation

- `ENGINE_MODE=mock`: no real provider key required.
- `ENGINE_MODE=external`: user must provide private Engine integration and key loading.
