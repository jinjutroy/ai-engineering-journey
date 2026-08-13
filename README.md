# AI Engineering Journey

This repository is a long-term laboratory for becoming an AI engineer who can explain, implement, debug, optimize, and operate AI systems—not merely call frameworks.

The learning loop is:

> **Understand → Implement → Experiment → Break → Debug → Optimize → Apply**

## Start here

1. Read [LEARNING_RULES.md](LEARNING_RULES.md).
2. Read [00-orientation/README.md](00-orientation/README.md).
3. Use [ROADMAP.md](ROADMAP.md) to choose the current phase.
4. Copy the templates in [`templates/`](templates/) for every new concept and experiment.
5. Record evidence—not confidence—in [PROGRESS.md](PROGRESS.md).

## Repository map

| Phase | Question answered | Exit evidence |
|---|---|---|
| 00 Orientation | What is the field and where does an AI engineer fit? | Explain the stack and trace one request end to end |
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

Frameworks are allowed only after the underlying mechanism has been implemented or explained. The framework exercise must identify what it abstracts, what control is lost, and how to debug below it.

## Working conventions

- Python 3.11+; use a virtual environment. `uv` is recommended but not required.
- Small deterministic datasets come before large opaque ones.
- A notebook is for exploration; reusable logic belongs in `src/` and tests.
- Raw data is immutable. Generated data and model artifacts are ignored by Git.
- Every claim about improvement requires a baseline, metric, controlled change, and repeated run.
- Every major concept uses **WHAT / WHY / WHEN / WHERE / WHO / HOW / FAILURE**.

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

Complete Phase 00, then run the three foundation implementations in `src/ai_journey`: linear regression, reverse-mode autodiff, and scaled dot-product attention. Do not rush past a failed gradient check; it is the first real debugging gate.

