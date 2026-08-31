# Curriculum Upgrade Review

## Scope

This review compares the existing repository with the target of producing a
deep AI Systems Engineer from an experienced software-engineering background.
The repository remains a process-and-evidence curriculum; implementation is
required where it exposes a mechanism, not as a vanity requirement.

## A. Curriculum assessment

| Phase | Status | Why | Missing | Overkill control | Recommended depth |
|---|---|---|---|---|---|
| 00 Orientation | KEEP | Strong system-flow foundation | Explicit context/state/memory/evidence vocabulary | Keep conceptual | One stable mental model and design defense |
| 01 Programming | UPGRADE | Useful NumPy/PyTorch bridge | AI-specific tensor, dtype, memory, profiling | Skip generic programming | Enough to inspect framework behavior |
| 02 Mathematics | UPGRADE | Correct dependency, previously too narrow | Probability, statistics, information theory, numerical reliability | Avoid pure math | Operational derivations and failure intuition |
| 03 ML | UPGRADE | Good experiment orientation | MLE/MAP, calibration, uncertainty, slice analysis | Avoid algorithm catalog | Valid baselines and generalization judgment |
| 04 Neural Networks | UPGRADE | Correct first-principles direction | Vectorized MLP and failure drills | Keep scalar engine small | Backpropagation mastery |
| 05 Deep Learning | REDUCE | Architecture and stability matter | Explicit purpose/trade-offs | Limit LSTM and distributed depth | CNN, sequence intuition, training dynamics |
| 06 Transformers | UPGRADE | Central AI mechanism | Full block, complexity, KV-cache bridge | No framework-first implementation | Deep mechanism and shape reasoning |
| 07 LLM | UPGRADE | Good high-level scope | Post-training, inference, capability factors | Avoid vendor trivia | Internals, inference, evaluation, safety |
| 08 RAG | UPGRADE | Correctly identifies retrieval | Full IR pipeline and metrics | Avoid vector-DB product focus | Retrieval/generation attribution |
| 09 Agents | UPGRADE | Correctly delays agents | Control-system semantics and drills | Frameworks after minimal loop | Bounded tool-use and authorization |
| 10 Serving/MLOps | REDUCE | Necessary production bridge | AI-specific inference economics | Defer deep infra internals | Serving, performance, rollback |
| 11 Production | UPGRADE | Good risk categories | Recovery drills and evidence boundary | Use concrete scenarios | Reliability, security, governance |
| 12 Capstones | UPGRADE | Good progressive idea | Separate graduation requirements | Avoid oversized demo | Three focused systems |
| 13 Graduation | ADD | Needed final defense | New phase | Explicitly bounded scope | End-to-end architecture defense |

## B. Architecture dependency map

```text
Math → ML → Neural Networks → Deep Learning → Transformers → LLM
  → Retrieval → Context → Memory → Agents → Evaluation → Production
```

Cross-dependencies:

- Evaluation begins in Phase 00 and is required in every later phase.
- Data quality and systems constraints begin before model training.
- Context depends on retrieval, memory, policy, evidence, and token budgets.
- Agents depend on state, tools, policy, evidence, context, and termination.
- Production depends on every upstream contract plus observability and recovery.

## C. Change plan applied

### Created

- `cross-cutting/README.md`
- `cross-cutting/context-engineering.md`
- `cross-cutting/memory-engineering.md`
- `cross-cutting/evidence-and-reliability.md`
- `13-ai-systems-graduation/README.md`
- `CURRICULUM_REVIEW.md`
- `MENTOR_RULES.md`

### Modified

- `README.md`
- `ROADMAP.md`
- `LEARNING_RULES.md`
- `PROGRESS.md`
- `GLOSSARY.md`
- `templates/CONCEPT_TEMPLATE.md`
- `templates/EXPERIMENT_TEMPLATE.md`
- `templates/DEBUG_REPORT_TEMPLATE.md`
- `scripts/verify_structure.ps1`
- Phase 01–12 README files

### Moved or removed

None. Existing material and links are preserved.

## D. Updated curriculum

The actual phase outlines live in [ROADMAP.md](ROADMAP.md). Phase-specific
README files provide local scope and exit criteria. The cross-cutting tracks
provide the deeper context, memory, and evidence mechanisms without creating
unnecessary numbered phases.

## E. Mentor behavior

The mentor contract is defined in [MENTOR_RULES.md](MENTOR_RULES.md). It
requires mechanism-first teaching, diagnostic questions, counterexamples,
broken implementations, evidence, and production connections.
