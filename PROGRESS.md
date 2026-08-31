# Progress

Status vocabulary: `introduced`, `explained`, `derived`, `implemented`,
`experimented`, `broken`, `debugged`, `measured`, `production-aware`, and
`mastered`. Only evidence links can advance a concept beyond `introduced`;
`mastered` also requires delayed retrieval reviews.

## Current focus

- Phase: `00-orientation`
- Concept: `AI stack and lifecycle`
- Status: `introduced`
- Next action: complete the Phase 00 evidence checklist and knowledge check
- Current blocker: none

## Environment verification

The repository's last recorded environment check is historical and does not
prove current topic mastery. Re-run checks when changing implementation code.

- Python: 3.11.9 (recorded 2026-08-10)
- Local environment: `.venv`
- Automated checks: Ruff passed; pytest 9/9 passed (recorded 2026-08-10)

## Phase 00 evidence checklist

- [ ] Draw the AI system flow from problem to feedback.
- [ ] Explain AI, ML, DL, and GenAI with one concrete example.
- [ ] Explain model, context, state, memory, tools, policy, evaluation, environment, and observability boundaries.
- [ ] Trace one input from source data to product action.
- [ ] Analyze five failure scenarios and define fallbacks.
- [ ] Decide whether one feature should use rules, ML, DL, GenAI, or no AI.
- [ ] Explain why valid output format does not prove correctness.
- [ ] Complete the [Phase 00 knowledge check](00-orientation/knowledge-check/index.html) with at least 8/10.
- [ ] Complete a notes-free review and record the date below.

Notes/evidence: `00-orientation/phase00-evidence.md`

## Phase ledger

| Phase | Status | Implementation evidence | Failure/debug evidence | Evaluation evidence | Production/application evidence | Review dates |
|---|---|---|---|---|---|---|
| 00 Orientation | introduced | — | — | knowledge check pending | — | — |
| 01 Programming | not-started | — | — | — | — | — |
| 02 Mathematics | not-started | — | — | — | — | — |
| 03 Machine learning | not-started | — | — | — | — | — |
| 04 Neural networks | not-started | — | — | — | — | — |
| 05 Deep learning | not-started | — | — | — | — | — |
| 06 Transformers | not-started | — | — | — | — | — |
| 07 LLM | not-started | — | — | — | — | — |
| 08 Retrieval and RAG | not-started | — | — | — | — | — |
| 09 Agents and tools | not-started | — | — | — | — | — |
| 10 Serving and MLOps | not-started | — | — | — | — | — |
| 11 Production systems | not-started | — | — | — | — | — |
| 12 Capstones | not-started | — | — | — | — | — |
| 13 Graduation | not-started | — | — | — | — | — |

## Cross-cutting track

| Track | Status | Evidence expected |
|---|---|---|
| Context engineering | not-started | token-budget experiment, provenance trace, context-ablation report |
| Memory engineering | not-started | event-to-memory pipeline, correction/conflict drill, source trace |
| Evidence and reliability | not-started | evidence taxonomy, abstention policy, conflict and recovery drill |

## Evidence log

Add one row only when there is a durable artifact.

| Date | Concept | Evidence state / loop stage | Evidence | Result | Next action |
|---|---|---|---|---|---|
| YYYY-MM-DD | example | implemented | link to code/test | pass/fail plus measurement | one concrete action |

## Weekly review

- What can I now explain and derive from memory?
- What did I implement without copying?
- What assumption did I break?
- What root cause did I find?
- What baseline and metric justified an optimization?
- What evidence distinguishes fact, observation, inference, hypothesis, unknown, or conflict?
- Where did I apply the concept, and when should I not use it?
- Which weak concept needs retrieval practice next week?
