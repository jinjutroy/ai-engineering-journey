# Roadmap

This is a dependency map, not a deadline. A typical part-time path may take 18–30 months. Depth and evidence determine pacing.

## Phase sequence and gates

### Phase 00 — Orientation

Learn the vocabulary, AI stack, role boundaries, and lifecycle. Gate: draw and explain how data becomes a deployed prediction, including feedback and monitoring.

### Phase 01 — Programming foundation

Deepen Python, NumPy, pandas, and PyTorch fundamentals: memory model, vectorization, broadcasting, data pipelines, tensors, autograd, and profiling. Build a NumPy data pipeline before using PyTorch `DataLoader`.

Gate: implement and test vectorized linear regression, explain time/space complexity, and profile loop versus vectorized versions.

### Phase 02 — Mathematics

Study linear algebra, probability, statistics, calculus, and optimization in the order demanded by implementations. Derivations must be paired with numerical experiments.

Gate: derive mean-squared-error gradients in matrix form and verify them with finite differences.

### Phase 03 — Machine learning

Cover problem framing, bias/variance, splits, features, supervised and unsupervised algorithms, metrics, calibration, uncertainty, and experiment design.

Gate: build a leakage-safe baseline, justify the metric, conduct error analysis by slice, and reproduce the run from configuration.

### Phase 04 — Neural networks

Implement perceptrons, activations, losses, forward propagation, reverse-mode autodiff, gradient descent, initialization, and a training loop.

Gate: train a two-layer MLP whose gradients pass finite-difference checks and which intentionally overfits a tiny dataset.

### Phase 05 — Deep learning

Study CNNs, recurrent networks, LSTMs, normalization, regularization, initialization, optimization, and distributed-training basics.

Gate: produce an ablation report that isolates at least three training decisions and explains unstable or failed runs.

### Phase 06 — Transformers

Implement tokenization, embeddings, position information, attention, masking, multi-head attention, feed-forward layers, residual paths, layer normalization, and the full block. Read the original paper critically.

Gate: implement causal self-attention from array operations, test masking and shape invariants, then match a trusted implementation on fixed weights.

### Phase 07 — Large language models

Study data curation, objectives, scaling, pretraining, fine-tuning, alignment, context windows, KV cache, inference, quantization, decoding, evaluation, hallucination, and safety.

Gate: train a tiny causal language model, compare decoding strategies, profile memory/latency, and write a model card.

### Phase 08 — Retrieval and RAG

Study information retrieval, chunking, sparse/dense retrieval, embeddings, vector indexes, reranking, context construction, citations, evaluation, and prompt-injection boundaries.

Gate: demonstrate whether failures originate in retrieval or generation using separate metrics and traceable evidence.

### Phase 09 — Agents and tools

Only now introduce model-driven control loops. Study state machines, planning, tool schemas, permissions, retries, idempotency, memory, termination, human approval, and evaluation.

Gate: implement a bounded agent loop without an agent framework, including an allowlist, budgets, traces, deterministic tests, and adversarial tool outputs.

### Phase 10 — Serving and MLOps

Study packaging, APIs, batching, caching, queues, model registries, data/model versioning, CI, deployment strategies, observability, drift, rollback, and cost engineering.

Gate: deploy a versioned service with SLOs, load tests, dashboards, canary/rollback design, and reproducible artifacts.

### Phase 11 — Production AI systems

Design systems under real constraints: availability, latency, throughput, privacy, abuse, multi-tenancy, data governance, evaluation in production, and incident response.

Gate: pass an architecture review and two failure drills with written postmortems.

### Phase 12 — Capstones

Complete three increasingly difficult systems:

1. Classical ML service with data validation and drift monitoring.
2. Transformer or retrieval system with offline/online evaluation.
3. Production-style AI application combining model, retrieval/tools, security, observability, and cost controls.

Each capstone ships a problem statement, ADRs, dataset card, experiment log, tests, model card, threat model, runbook, load-test report, incident simulation, and retrospective.

## Parallel tracks

Starting in Phase 03, maintain four parallel tracks:

- **Theory:** derivations and papers.
- **Implementation:** algorithms built from primitives.
- **Systems:** data, serving, monitoring, and reliability.
- **Communication:** design docs, model cards, postmortems, and teach-back.

Do not let the systems track wait until after model training; production readiness is a continuous discipline.

