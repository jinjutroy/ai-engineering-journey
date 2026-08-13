# Phase 00 — Orientation

## Outcome

Build a correct map of the field before selecting tools. At the end, you should trace an AI feature from problem framing through data, learning, evaluation, deployment, monitoring, and feedback; identify the owner and failure boundary at each step; and distinguish AI engineering from API integration.

## Study order

1. [what-is-ai.md](what-is-ai.md)
2. [ai-vs-ml-vs-dl-vs-genai.md](ai-vs-ml-vs-dl-vs-genai.md)
3. [ai-engineer-role.md](ai-engineer-role.md)
4. [ai-stack.md](ai-stack.md)

## Deliverables

- Draw an architecture for one familiar frontend feature that uses AI.
- Trace one prediction from raw event to UI, including model version and feedback.
- Write five failure scenarios spanning data, model, service, user experience, and security.
- Explain why “the model returned JSON” does not prove the system is correct.

## Deliberate break lab

Take a hypothetical content classifier and inject: a missing field, a shifted label distribution, a slow model response, an adversarial input, and a silently stale model. For each, state where it should be detected, what telemetry is required, and the safe fallback.

## Exit gate

Without notes, explain the four documents in this folder and defend build-versus-buy for one AI feature. A reviewer should be able to challenge your assumptions about quality, cost, latency, privacy, and operations.

