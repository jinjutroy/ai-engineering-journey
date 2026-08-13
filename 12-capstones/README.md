# Phase 12 — Capstones

Capstones prove ownership, not novelty. Each must answer WHAT, WHY, WHEN, WHERE, WHO, HOW, and FAILURE in its design docs and execute the complete learning loop.

## Required artifacts

Problem and non-AI baseline; requirements/SLOs; architecture and ADRs; dataset card and lineage; reproducible experiments; tested implementation; evaluation by slice with uncertainty; model card; threat model/privacy review; deployment and rollback; telemetry; load/cost report; incident drill and postmortem; retrospective.

## Projects

1. **Classical prediction service:** structured data, leakage-safe pipeline, calibration, drift, and versioned API.
2. **Transformer or retrieval system:** from-scratch core mechanism, offline/online evaluation, latency/memory profiling, and evidence tracing.
3. **Production AI application:** model plus retrieval or bounded tools, authorization, observability, fallback, cost budgets, and adversarial evaluation.

## Exit gate

Another engineer can reproduce, operate, diagnose, and safely roll back the system using only repository artifacts. You can defend every major trade-off and identify the next bottleneck from evidence.

