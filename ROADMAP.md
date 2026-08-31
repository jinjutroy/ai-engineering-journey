# AI Engineering Journey Roadmap

This is a dependency map and evidence system, not a list of tools to collect.
The target is deep AI Systems Engineer capability: understand mechanisms,
build small correctness oracles, diagnose failures by layer, and make
production trade-offs explicit.

The student already has professional software-engineering experience. Basic
programming, HTTP, Git, databases, and application architecture are assumed.
Time is allocated to AI-specific reasoning, mathematics, experiments, and
system ownership.

## Learning loop

```text
Understand → Explain → Derive → Implement → Experiment → Break → Debug
→ Measure → Optimize → Verify → Apply → Document
```

Implementation is required when it is the best way to expose a mechanism. For
orientation and architecture topics, a diagram, derivation, failure analysis,
or design defense may be stronger evidence than code.

## Dependency map

```text
Requirements and decision framing
        ↓
Mathematical foundations
        ↓
ML problem formulation and evaluation
        ↓
Neural networks and optimization
        ↓
Deep-learning architectures
        ↓
Transformer mechanisms
        ↓
LLM internals and inference
        ↓
Information retrieval and RAG
        ↓
Context engineering ─────┐
Memory engineering ──────┼→ Agent control systems
Evidence and reliability ┘
        ↓
Serving, operations, security, and recovery
        ↓
Capstones and AI Systems Graduation
```

Cross-dependencies are intentional: evaluation starts in Phase 00, data and
systems work starts before training, and context, memory, and evidence apply
across LLM, RAG, agents, and production systems.

## Stable versus fast-moving knowledge

Stable knowledge must dominate the curriculum:

- mathematics, probability, statistics, optimization, and numerical reliability;
- ML, neural-network, Transformer, and retrieval mechanisms;
- evaluation, distributed systems, reliability, security, and architecture.

Fast-moving tools are studied only as replaceable examples of mechanisms:

- model vendors and APIs;
- agent and orchestration frameworks;
- vector databases and serving frameworks;
- provider-specific prompting techniques.

For every tool, document its abstraction boundary, lost control, failure modes,
debugging escape hatch, and minimal framework-free equivalent.

## Phase sequence and gates

### Phase 00 — Orientation and AI System Flow

Build the mental model for traditional software versus learning systems. Trace
one feature through problem, policy, data/context, mechanism choice, model
output, validation, decision, product action, monitoring, and feedback. Define
AI, ML, DL, GenAI, LLM, model, context, state, memory, tools, policy,
evaluation, environment, observability, AI Engineer, and AI Systems Engineer.

Prerequisites: professional software engineering.

Exit evidence: one system-flow diagram, one request/prediction trace, five
failure scenarios with fallbacks, a build/buy/avoid decision, and a notes-free
knowledge check. Code is optional.

### Phase 01 — AI-Specific Programming Foundation

Focus on Python, NumPy, array/tensor semantics, shapes, broadcasting, memory,
dtypes, numerical computing, profiling, vectorization, and PyTorch fundamentals.

Sequence:

```text
NumPy → manual implementation → PyTorch equivalent → behavior comparison → profile
```

Build a loop and vectorized implementation, expose a silent broadcasting bug,
compare memory and runtime, and explain what PyTorch autograd and tensors are
doing. Do not reteach general programming.

Exit evidence: documented shape/dtype contracts, correctness tests, loop versus
vectorized profile, PyTorch comparison, and one debug report.

### Phase 02 — Mathematical Foundations for AI Engineering

Study Linear Algebra, Calculus, Probability, Statistics, Optimization,
Information Theory, and Numerical Reliability through concrete model problems.

Linear Algebra: vectors, spaces, bases, transformations, dot products,
matrices, norms, projections, rank, eigenvectors, SVD, conditioning, and
embeddings/attention connections.

Calculus: functions, derivatives, partial derivatives, gradients, directional
derivatives, chain rule, Jacobian, Hessian intuition, finite differences, and
gradient descent.

Probability and Statistics: distributions, expectation, variance, covariance,
Bayes, likelihood, MLE, MAP, sampling, estimators, confidence intervals,
hypothesis testing, correlation, and generalization.

Optimization and Information Theory: objectives, constraints, SGD, momentum,
Adam, regularization, entropy, cross-entropy, KL divergence, and mutual
information.

Numerical reliability: floating point, FP32, FP16, BF16, overflow, underflow,
stability, conditioning, and finite-difference limitations.

Exit evidence: MSE and logistic-loss derivations, shape audit, numerical
failure notes, finite-difference verification, and a multi-seed uncertainty
comparison. Do not pursue pure mathematics unrelated to AI judgment.

### Phase 03 — Machine Learning and Valid Experiments

Use the model:

```text
data → representation → model → prediction → loss → optimization
→ evaluation → generalization → decision
```

Cover linear/logistic regression, classification, generative versus
discriminative modeling, MLE/MAP, splits, leakage, overfitting, underfitting,
regularization, baselines, metrics, calibration, uncertainty, and slice-based
error analysis.

Every model note must state its objective, parameters, optimization method,
metric, assumptions, and failure modes.

Exit evidence: leakage-safe baseline, trusted-library comparison, predeclared
metric and ship/no-ship gate, slice analysis, uncertainty, and reproducible
experiment record.

### Phase 04 — Neural Networks from First Principles

Master perceptrons, activations, linear layers, forward propagation, losses,
computational graphs, backpropagation, gradients, gradient descent, and
autodiff.

Implement scalar autodiff, a vectorized MLP, backpropagation, and gradient
checking. Deliberately reproduce exploding gradients, vanishing gradients,
incorrect gradients, bad learning rates, numerical instability, and shape
mismatch.

Exit evidence: gradient-checked MLP that overfits a tiny batch, learns a
nonlinear toy task, and has debug reports for at least two broken assumptions.

### Phase 05 — Deep Learning Architectures and Training Dynamics

Learn why CNNs use locality, weight sharing, and receptive fields. Learn RNN
state and gradient flow, then study LSTM gates only deeply enough to understand
why recurrence struggles and why attention is attractive.

Connect normalization, initialization, dropout, weight decay, optimization,
mixed precision, memory, and distributed-training basics to training stability.

Exit evidence: one image and one sequence experiment, an ablation report, a
reproduced training failure, and quality/latency/memory trade-offs. Keep LSTM
depth proportional to its architectural value.

### Phase 06 — Transformers

This is a deep mechanism phase. Study tokenization, embeddings, positional
representation, Q/K/V, scaled dot-product attention, masks, multi-head
attention, residual connections, normalization, feed-forward networks, causal
attention, and the complete Transformer block.

Track tensor shapes at every step. Derive FLOPs and memory as a function of
sequence length, hidden dimension, and number of heads. Connect attention to
KV-cache behavior during inference.

Exit evidence: NumPy attention, masked attention, multi-head attention, and a
minimal Transformer block that match a trusted implementation on fixed inputs.
Document mask errors, softmax overflow, padding contamination, quadratic cost,
and long-context limitations.

### Phase 07 — LLM Internals and Inference

Trace:

```text
text → tokenizer → token IDs → embeddings → Transformer → logits
→ probabilities → decoding → next token
```

Study next-token prediction, cross-entropy, pretraining, SFT, preference
optimization, instruction following, context windows, prefill, decode, KV
cache, temperature, top-k, top-p, greedy decoding, sampling, quantization,
reasoning, calibration, and tool use.

Explain capability as a combination of architecture, parameters, data,
training, post-training, inference strategy, context utilization, tool use,
and evaluation. Model size alone is not capability.

Exit evidence: tiny causal language model or faithful training trace, decoding
comparison, prefill/decode and KV-cache analysis, quantization trade-off,
model card, and safety/evaluation boundaries.

### Phase 08 — Information Retrieval and RAG

Treat RAG as an information-retrieval system:

```text
documents → parsing → chunking → indexing → candidate retrieval → ranking
→ reranking → evidence selection → context construction → generation
→ citation → evaluation
```

Cover lexical search, dense retrieval, ANN, embeddings, hybrid search,
metadata filtering, reranking, and evidence tracing. Measure Recall@K,
Precision@K, MRR, NDCG, hit rate, answer correctness, and citation correctness.

Exit evidence: sparse/dense/hybrid comparison, retrieval-versus-generation
failure attribution, traceable citations, stale/conflicting evidence tests,
and prompt-injection boundary analysis. Relevance is not truth.

### Phase 09 — Agents and Tools as Control Systems

Model an agent as:

```text
model + state + tools + memory + policy + environment
+ control loop + evaluation
```

Study planning, tool selection, observation, action, termination, retries,
timeouts, budgets, idempotency, validation, human approval, and deterministic
replay. First implement a framework-free loop with at least two tools.

Only afterward compare frameworks. Explain their abstraction, lost control,
failure boundary, and debugging escape hatch.

Exit evidence: bounded tool loop, allowlist, cost/step/time budgets, approval
boundary, adversarial tool outputs, and drills for loops, wrong tools, retries,
timeouts, prompt injection, and unsafe actions.

### Phase 10 — Serving and MLOps for AI Systems

Focus on model serving and AI operations, not becoming a general
infrastructure specialist. Cover inference APIs, batching, streaming, caching,
autoscaling, GPU/VRAM, quantization, health checks, versioning, deployment,
rollback, tracing, monitoring, cost per request, and provider fallback.

Understand prefill versus decode, throughput versus latency, batching
trade-offs, memory constraints, and failure recovery. Defer deep Kubernetes,
Terraform, and service-mesh internals unless a project needs them.

Exit evidence: versioned service design, load test, SLOs, traces, resource
budget, canary/rollback plan, and reproducible artifact lineage.

### Phase 11 — Production AI Systems

Combine reliability, security, quality, cost, performance, governance,
observability, and recovery. Cover prompt injection, data leakage,
cross-tenant leakage, PII, provider outage, timeout cascades, rate limits,
quality regression, feedback corruption, unsafe automation, fallback,
circuit-breaking, human approval, incident response, and postmortems.

Exit evidence: architecture review plus drills for model outage, retrieval
outage, corrupted memory, context overflow, 5x cost increase, 20% quality drop,
unsafe tool, and provider failure. For each: detection, containment, recovery,
verification, and prevention.

### Phase 12 — Capstones

Build three progressive systems rather than one oversized demo:

1. Classical ML service with data validation and drift monitoring.
2. Transformer or retrieval system with offline/online evaluation.
3. Production-style application combining model, retrieval/context, bounded
   tools, security, observability, and cost controls.

Each includes problem, requirements, architecture, ADRs, implementation,
tests, experiments, failures, evaluation, performance, cost, security, and
lessons. These are preparation for, not substitutes for, the graduation system.

### Phase 13 — AI Systems Graduation

Defend one complete AI system from problem framing through recovery:

```text
problem → requirements → architecture → model → data → retrieval
→ context → memory → agent/tools → evidence → evaluation → serving
→ observability → security → recovery → postmortem
```

The system must support model replacement/routing, context selection and
compression, short-term state and long-term knowledge, bounded tool use,
provenance, evidence-aware abstention, offline regression evaluation, online
telemetry, and human approval for risky actions.

Exit evidence: golden dataset, baseline, regression suite, ADRs, model/context/
memory contracts, evaluation report, cost/latency report, trace examples,
security tests, recovery drills, and final technical defense. This demonstrates
system thinking; it does not pretend one personal project replaces years of
organizational production experience.

## Cross-cutting disciplines

These are not optional add-on topics. Apply them from Phase 03 onward and
explicitly revisit them in Phases 07–13:

- **Context engineering:** selection, ordering, priority, compression, token
  budgets, freshness, relevance, provenance, and context dilution.
- **Memory engineering:** state, events, facts, observations, decisions,
  lessons, consolidation, correction, conflicts, decay, and traceability.
- **Evidence and reliability:** fact, observation, inference, hypothesis,
  unknown, conflict, confidence, citation, verification, and abstention.
- **Evaluation and experimentation:** baseline, metric, uncertainty, failure
  analysis, regression suite, online feedback, and evidence-backed decisions.

## Overkill control

Before adding a topic, ask:

1. Does an AI Systems Engineer need this?
2. Does it explain an important mechanism?
3. Does it improve debugging or architecture judgment?
4. Does it improve production judgment?

If not, reduce it to conceptual awareness or remove it. Avoid unnecessary
depth in abstract algebra, real analysis, measure theory, exhaustive classical
ML algorithms, Kubernetes internals, Terraform internals, and AI history.
