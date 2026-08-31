# Phase 10 — Serving and MLOps

## Purpose

Make AI behavior reproducible, deployable, observable, and maintainable. Keep
infrastructure depth proportional to the AI-system problem; this is not a
Kubernetes or Terraform specialization.

## WHAT / WHY / WHEN / WHERE / WHO

Serving connects versioned models and data contracts to inference APIs and
operators. It spans packaging, deployment, batching, streaming, caching,
autoscaling, GPU/VRAM, health checks, rollback, tracing, and quality/cost
monitoring. Training produces artifacts; services consume them; operators own
SLOs, recovery, and lineage.

## HOW

Separate prefill from decode. Measure latency distributions, throughput,
batching trade-offs, memory limits, cost/request, cache behavior, fallbacks,
provider failure, and version compatibility. Use schema validation, immutable
artifacts, canary/rollback, load tests, and privacy-safe telemetry.

## FAILURE

Break training/serving skew, incompatible artifacts, cold starts, overload,
retry storms, cache poisoning, silent drift, alert fatigue, unsafe logs,
provider outages, and rollback dependencies.

## VERIFY

Prerequisites: Phase 07 inference and Phase 03 evaluation. Enables Phase 11
production ownership and Phase 13 defense. Exit with a versioned service,
reproducible build, readiness/health checks, SLOs, load/cost report, traces,
canary plan, tested fallback, and rollback evidence.
