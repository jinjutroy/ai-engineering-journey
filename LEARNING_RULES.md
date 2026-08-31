# Learning Rules

## The contract

The unit of progress is demonstrated capability, not pages read, videos watched, or APIs called.

For each major concept:

1. **Understand** — explain it precisely using the concept template.
2. **Explain** — reconstruct the mechanism, assumptions, and boundaries without notes.
3. **Derive** — derive the central equation or algorithm and check dimensions.
4. **Implement** — build the smallest correct version with limited dependencies.
5. **Experiment** — form a falsifiable hypothesis, define controls and metrics, then run it.
6. **Break** — deliberately violate assumptions and preserve the failure evidence.
7. **Debug** — localize the cause using assertions, tests, visualizations, and traces.
8. **Measure** — report a baseline, uncertainty, resource use, and acceptance threshold.
9. **Optimize** — improve one measured bottleneck without changing correctness.
10. **Verify** — compare with an oracle, regression suite, or numerical check.
11. **Apply** — use it inside a system where its trade-offs matter.
12. **Document** — leave reproducible evidence, decisions, and limitations.

## Non-negotiable rules

- Derive before importing. Using a library is not a substitute for knowing the operation it performs.
- Baseline before complexity. The simplest credible solution is the comparison point.
- Split before preprocessing. Fit transforms only on training data to avoid leakage.
- Shapes, dtypes, devices, ranges, units, and seeds are part of the interface.
- Test invariants, not only happy-path examples.
- Never call a model “better” using only training loss or one lucky seed.
- Never hide a failed experiment. Record why it failed and what evidence changed your mind.
- Optimize only after profiling; preserve a correctness oracle.
- Security, privacy, cost, latency, and observability are design inputs, not deployment polish.
- A framework may be used after you can name its abstraction boundary and escape hatch.
- Stable mechanisms come before fast-moving vendors, SDKs, and framework APIs.
- Every new concept records prerequisites, dependencies, and what it enables; do not study an advanced layer with missing foundations.
- Relevance is not truth, confidence is not correctness, and model output is not verified evidence.

## Concept completion gate

A concept is complete only when all boxes have evidence:

- [ ] I can explain WHAT, WHY, WHEN, WHERE, WHO, HOW, and FAILURE without notes.
- [ ] I can state prerequisites, dependencies, and what this concept enables.
- [ ] I derived the central equation or algorithm and checked dimensions.
- [ ] I implemented a simplified version and tested it.
- [ ] I compared it with a trusted implementation or known result.
- [ ] I created at least three failures: data, numerical/algorithmic, and system/operational.
- [ ] I wrote a debug report identifying root cause rather than symptoms.
- [ ] I measured one trade-off and justified an optimization.
- [ ] I applied it in a small end-to-end system.
- [ ] I can state when not to use it.
- [ ] I verified expected behavior against a baseline with an explicit metric or invariant.
- [ ] I know which evidence is fact, observation, inference, hypothesis, unknown, or conflict.

## Evidence states

Use the strongest state honestly earned: `introduced`, `explained`, `derived`,
`implemented`, `experimented`, `broken`, `debugged`, `measured`,
`production-aware`, and finally `mastered` after delayed retrieval reviews.
Reading alone earns only `introduced`.

## Framework boundary

Before adopting a framework, answer: what problem does it solve, what mechanism
does it abstract, what control is lost, how can it fail, how will we debug below
the abstraction, and can we implement a minimal version ourselves?

## Overkill control

For every topic ask whether it explains an important mechanism, improves
debugging, architectural judgment, or production safety. If not, reduce it to
conceptual awareness or defer it. Do not expand the curriculum merely because a
computer-science topic exists.

See [MENTOR_RULES.md](MENTOR_RULES.md) for how future teaching requests should
be handled.

## Experiment discipline

Every experiment records: question, hypothesis, variables, controls, dataset version, split policy, seed policy, metric, acceptance threshold, environment, result, uncertainty, artifacts, and next decision. Change one explanatory variable at a time unless the experiment explicitly studies interactions.

Run a smoke test first, then a full run. Confirm that a model can overfit a tiny batch before spending meaningful compute. For stochastic comparisons, report the distribution across seeds, not only the maximum.

## Debugging ladder

Debug from the cheapest layer upward:

1. Input schema, labels, duplicates, leakage, and split integrity.
2. Tensor shape, dtype, device, range, missing values, and normalization.
3. Forward-pass invariants and a hand-calculated example.
4. Loss behavior and numerical stability.
5. Analytical gradients versus finite differences.
6. Optimizer state and parameter updates.
7. Evaluation pipeline and metric implementation.
8. Serving skew, concurrency, resource limits, and dependency failures.

Do not tune hyperparameters to repair a broken pipeline.

## Spaced mastery

Review a completed concept after roughly 1 day, 1 week, and 1 month. Each review must use retrieval practice: explain, derive, or implement from memory. Re-reading alone does not count.

## Allowed use of AI assistants

Use an assistant as a reviewer, Socratic tutor, test generator, or debugging partner. Before accepting generated code, predict its behavior, run tests, inspect failure cases, and explain every important line. Never submit an explanation you cannot reconstruct independently.

