# AI Engineering Journey

This repository is a long-term laboratory for becoming an AI engineer who can explain, implement, debug, optimize, and operate AI systems—not merely call frameworks.

The learning loop is:

> **Understand → Explain → Derive → Implement → Experiment → Break → Debug → Measure → Optimize → Verify → Apply → Document**

## Start here

1. Read [LEARNING_RULES.md](LEARNING_RULES.md).
2. Read [00-orientation/README.md](00-orientation/README.md).
3. Use [ROADMAP.md](ROADMAP.md) to choose the current phase.
4. Copy the templates in [`templates/`](templates/) for every new concept and experiment.
5. Record evidence—not confidence—in [PROGRESS.md](PROGRESS.md).

## Repository map

| Phase | Question answered | Exit evidence |
|---|---|---|
| 00 Orientation | What is AI and how does an AI system work end to end? | Core system flow, context/model distinction, failure analysis, and build-versus-buy decision |
| 01 Programming | Can I manipulate data and tensors without magic? | Tested Python/NumPy implementation and profiling notes |
| 02 Mathematics | Can I derive the operations learning depends on? | Derivations plus numerical verification |
| 03 Machine learning | Can I design and evaluate a valid learning experiment? | From-scratch baseline with leakage checks |
| 04 Neural networks | Can I implement backpropagation and debug gradients? | Gradient-checked MLP |
| 05 Deep learning | Can I train stable models and diagnose failure? | Ablation report for an image or sequence task |
| 06 Transformers | Can I implement and reason about a transformer block? | NumPy attention plus masked, multi-head variant |
| 07 LLM | How are language models trained and decoded? | Tiny language model and decoding comparison |
| 08 Retrieval and RAG | When should knowledge be retrieved instead of learned? | Evaluated retriever–generator pipeline |
| 09 Agents and tools | How do model-driven control loops fail? | Bounded tool loop with state, policy, and traces |
| 10 Serving and MLOps | How does a model become a reliable service? | Versioned, observable inference service |
| 11 Production systems | How do quality, cost, latency, and security interact? | Architecture review and failure drills |
| 12 Capstones | Can I own an AI system end to end? | Reproducible project with design and incident docs |
| 13 Graduation | Can I defend a complete AI system under failure and change? | Graduation system, evaluation suite, recovery drills, and technical defense |

Cross-cutting tracks are required throughout the phases: [Context Engineering](cross-cutting/context-engineering.md), [Memory Engineering](cross-cutting/memory-engineering.md), and [Evidence & Reliability](cross-cutting/evidence-and-reliability.md).

## System mental model

Reason through the full chain:

`Requirement → Problem formulation → Mathematical model → Learning mechanism → Model → Inference → Context → Retrieval → Memory → Agent → Evaluation → Serving → Production`

When something fails, trace backward from the output to the decision, context, retrieval, memory, tools/environment, model behavior, inference, and underlying mechanism. A model is one component of the system, not the system itself.

For AI-native development, the human owns problem framing, architecture, constraints, approval, and verification. Agents may plan, implement, test, and execute only within explicit boundaries.

Frameworks are allowed only after the underlying mechanism has been implemented or explained. The framework exercise must identify what it abstracts, what control is lost, and how to debug below it.

## Working conventions

- Python 3.11+; use a virtual environment. `uv` is recommended but not required.
- Small deterministic datasets come before large opaque ones.
- A notebook is for exploration; reusable logic belongs in `src/` and tests.
- Raw data is immutable. Generated data and model artifacts are ignored by Git.
- Every claim about improvement requires a baseline, metric, controlled change, and repeated run.
- Every major concept uses **WHAT / WHY / WHEN / WHERE / WHO / HOW / FAILURE / VERIFY**, plus prerequisites and measurable exit evidence.
- Context, memory, provenance, evidence, security, cost, latency, and observability are part of the design from the beginning.

## Environment

```bash
# with uv
uv venv
uv pip install -e ".[dev]"

# or standard Python
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -e ".[dev]"

pytest
python scripts/run_foundations.py
```

The core examples intentionally depend only on NumPy. PyTorch enters after manual tensor operations and gradients are understood.

## Current first milestone

Complete Phase 00 by producing the system-flow and failure-analysis evidence in `00-orientation/phase00-evidence.md`. Code is optional here; the foundation implementations in `src/ai_journey` are supporting artifacts for later implementation-focused phases.

