# Memory Engineering

## WHAT

Memory is externalized experience or state used across interactions. It is not
the model's weights and should not silently replace authoritative records.

```text
raw events → facts → observations → decisions → lessons → consolidation
```

Useful categories include working memory, short-term state, episodic memory,
semantic memory, procedural memory, and long-term knowledge.

## WHY

Long-running systems need continuity, but blindly storing every interaction
creates noise, privacy risk, contradictions, and unbounded context. Memory
engineering controls what is retained, corrected, retrieved, and forgotten.

## WHEN

Use short-term state for the current task, episodic memory for past events,
semantic memory for reusable facts, and procedural memory for validated
workflows. Do not store a claim as fact without source, scope, and confidence.

## WHERE

Memory sits between the application state layer and context builder. It feeds
agents and LLMs but must remain separately inspectable and correctable.

## WHO

Event producers create observations; consolidation logic proposes memories;
retrievers select memories; policy decides retention and access; humans or
domain owners correct important facts; evaluators test recall and harmful use.

## HOW

Every durable memory should record source references, creation time, scope,
confidence, status, and correction history. Support daily, weekly, monthly, or
task-level consolidation without deleting the underlying evidence.

## FAILURE

- False memory or hallucinated fact
- Summary becomes the only source of truth
- Conflicting memories are silently merged
- Stale memory overrides current evidence
- Memory retrieval leaks another user or tenant
- Unbounded growth increases latency and cost
- User correction does not propagate
- Sensitive information is retained unnecessarily

## VERIFY

- Test memory creation, retrieval, correction, conflict handling, and expiry.
- Trace each important memory to source evidence.
- Measure recall, precision, freshness, cost, and privacy behavior.
- Demonstrate safe behavior when memory is missing or corrupted.
