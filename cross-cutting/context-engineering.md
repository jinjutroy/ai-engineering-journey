# Context Engineering

## WHAT

Context is the information available to a model at request time: instructions,
user input, conversation history, retrieved evidence, tool results, state, and
policy constraints. Context engineering is the design of selecting, ordering,
compressing, and validating that information.

```text
storage → retrieval → ranking → compression → context builder → model
```

Context window, memory, and database are different concepts. A context window
is a model limit; memory is externalized state or knowledge; a database is a
storage and query system.

## WHY

More context is not always better. Irrelevant, stale, conflicting, or malicious
context can reduce quality, increase cost, hide important evidence, or cause
unsafe actions.

## WHEN

Retrieve when the answer depends on changing, private, or source-grounded
information. Summarize when detail is no longer needed for the task. Preserve
raw evidence when it may be needed for audit, correction, or future retrieval.

## WHERE

Context engineering sits in application orchestration between storage/retrieval
and model inference. It also interacts with policy, memory, evaluation, and
observability.

## WHO

Retrievers find candidates; rankers prioritize them; context builders assemble
the request; policy layers classify trusted and untrusted content; models
consume context; evaluators measure whether context improved the task.

## HOW

Track token budget, relevance, priority, ordering, freshness, provenance,
conflicts, and task fit. Keep system instructions separate from untrusted
documents and tool output. Record which context items were used for each run.

## FAILURE

- Context dilution and lost-in-the-middle behavior
- Missing or stale evidence
- Conflicting sources
- Token overflow and unsafe truncation
- Prompt injection inside retrieved content
- Sensitive data included without need
- Summary losing a required fact
- Context version not recorded

## VERIFY

- Compare no-context, full-context, and selected-context baselines.
- Measure answer quality, retrieval/usefulness, token count, latency, and cost.
- Test missing, stale, conflicting, malicious, and oversized context.
- Verify important claims can be traced to source evidence.
