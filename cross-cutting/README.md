# Cross-Cutting AI Systems Disciplines

These disciplines apply across the roadmap. They are not framework-specific
features and should be revisited whenever a system gains more state, tools,
retrieval, users, or operational responsibility.

## Tracks

- [Context engineering](context-engineering.md): decide what information the
  model receives and why.
- [Memory engineering](memory-engineering.md): externalize state and
  experience without losing source traceability.
- [Evidence and reliability](evidence-and-reliability.md): distinguish facts,
  uncertainty, conflicts, and actions that deserve verification.

Evaluation and experimentation remain a discipline in every phase. Use the
existing experiment and debug templates to record baselines, metrics, failures,
and decisions.

## Shared principle

```text
Storage → retrieval → selection → context/memory → model/agent
→ validation → action → evidence → evaluation
```

No generated summary, memory, or model output is a substitute for authoritative
source evidence.
