# Decision Log

## D-001: Keep Engine Private

Status: accepted

Reason:

- Engine is reused across personal learning projects.
- It contains sensitive and provider-specific key handling logic.

Tradeoff:

- External contributors cannot run full private behavior.
- Mitigated by publishing adapter contract and stubs.

## D-002: Multi-Bot Namespace Isolation

Status: accepted

Reason:

- Prevent memory contamination between personas.

Tradeoff:

- Slightly more bookkeeping for session keys.

## D-003: systemd User Services

Status: accepted

Reason:

- Simple and stable process management on Ubuntu for ongoing experiments.

Tradeoff:

- Requires server-side operational familiarity.

## D-004: Public Showcase Repository Instead of Raw Production Dump

Status: accepted

Reason:

- Avoid accidental exposure of secrets/runtime artifacts.
- Improve portfolio readability with curated docs.

Tradeoff:

- Extra maintenance to keep showcase docs aligned with actual learning progress.
