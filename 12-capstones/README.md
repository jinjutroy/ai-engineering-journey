# Phase 12 — Progressive Capstones

## Purpose

Prove ownership progressively. These projects are stepping stones to the
graduation system, not a collection of demos or a claim of organizational
production experience.

## WHAT / WHY / WHEN / WHERE / WHO

Each capstone integrates the mechanisms learned so far and makes trade-offs
visible from problem framing to operation. The engineer owns requirements,
architecture, experiments, failure analysis, and evidence; users and domain
owners define acceptable outcomes.

## HOW

1. Classical prediction: leakage-safe pipeline, calibration, drift, versioned API.
2. Transformer or retrieval: from-scratch core mechanism, offline/online evaluation, latency/memory profiling, evidence tracing.
3. Production AI application: model plus retrieval or bounded tools, authorization, context/memory, observability, fallback, cost, adversarial tests.

Every project includes a non-AI baseline, requirements/SLOs, ADRs, data lineage,
reproducible experiments, tests, slice evaluation with uncertainty, model card,
threat model, deployment/rollback, telemetry, incident drill, and postmortem.

## FAILURE

Do not hide failures behind a polished UI. Include data, model, context,
retrieval, memory, tool, serving, security, cost, and operational failures with
root cause and recovery evidence.

## VERIFY

Prerequisites: Phases 03–11 and all cross-cutting tracks. Enables Phase 13.
Exit when another engineer can reproduce, operate, diagnose, and safely roll
back the project using repository artifacts and you can defend every major
trade-off with measurements.
