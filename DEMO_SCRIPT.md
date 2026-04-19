# Demo Script (5-7 min)

## 1) Setup Context (45 sec)

- Explain that this is a public showcase of a private-production architecture.
- Clarify the boundary: bot side is public, Engine core is private.

## 2) Architecture Walkthrough (90 sec)

- Open `docs/architecture.md`.
- Point out three bot personas and one shared Engine contract.
- Explain why namespace isolation matters.

## 3) Interface Walkthrough (90 sec)

- Open `docs/engine-interface.md` and `src/engine_adapter.py`.
- Explain how adapter pattern allows private implementation reuse.

## 4) Operational Readiness (90 sec)

- Open `PUBLISH_CHECKLIST.md`.
- Show security checks and deployment notes.

## 5) Scenarios (90 sec)

- Open `docs/demo-scenarios.md`.
- Show one successful flow and one failure-handling flow.

## 6) Close (30 sec)

- Emphasize reusable architecture and maintainability.
- Point to `SHOWCASE_BRIEF.md` and `METRICS.md` for portfolio summarization.
