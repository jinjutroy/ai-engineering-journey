# What Is Artificial Intelligence?

## WHAT

Artificial intelligence is the engineering and scientific field concerned with systems that perform tasks requiring perception, representation, prediction, reasoning, decision-making, generation, or action under uncertainty. “AI” names a capability-oriented field, not one algorithm. A production AI system includes far more than its model: data contracts, learned or programmed components, evaluation, software, infrastructure, interfaces, policies, monitoring, and human oversight.

## WHY

Many useful problems cannot be specified exhaustively with deterministic rules. Images, language, behavior, and changing environments contain variation that makes hand-written coverage expensive or brittle. AI provides mechanisms that infer useful structure from data or search over possible actions. Without it, some systems require infeasible rule sets; with it, exact guarantees may be traded for probabilistic behavior that must be measured and bounded.

## WHEN

Use AI when the task has a measurable objective, relevant evidence exists, uncertainty is acceptable or manageable, and a learned/generalizing mapping has clear value. Prefer ordinary software when rules are stable and complete, exactness is required, data is insufficient, the cost of errors is unacceptable, or a simple heuristic meets the need. “Can use AI” is not the same as “should use AI.”

## WHERE

AI sits inside a larger sociotechnical system:

`problem → policy/metric → data → representation → model/algorithm → evaluation → serving → product decision → feedback`

The model transforms representations; the surrounding system determines what inputs it sees, how outputs affect people, and whether failures are noticed.

## WHO

Domain experts define meaning and acceptable risk. Data producers and pipelines create evidence. ML/AI engineers build training and inference systems. Researchers develop algorithms. Software/platform engineers integrate and operate them. Security, privacy, legal, and product teams constrain use. Users supply inputs, experience outcomes, and may adapt behavior in response.

## HOW

A common learning formulation chooses parameters \(\theta\) for a function \(f_\theta(x)\) that minimizes expected risk:

\[
\theta^* = \arg\min_\theta \; \mathbb{E}_{(x,y)\sim P}[L(f_\theta(x), y)]
\]

Because the true distribution \(P\) is unknown, training minimizes empirical risk on sampled data, often plus a regularizer:

\[
\hat\theta = \arg\min_\theta \frac{1}{n}\sum_{i=1}^{n} L(f_\theta(x_i), y_i) + \lambda R(\theta)
\]

The critical gap is between the finite training sample and future reality. Evaluation estimates this gap; deployment exposes it to changing data and feedback. Other AI systems may use search, planning, constraints, retrieval, or hybrids rather than parameter learning alone.

```text
define objective and harm constraints
collect/version evidence
construct representation
fit or configure candidate system
evaluate quality, slices, safety, latency, and cost
if acceptance gates pass: deploy gradually
monitor inputs, outputs, outcomes, and system health
feed verified outcomes into the next iteration
```

## FAILURE

- **Specification:** the metric rewards behavior different from the real goal.
- **Data:** biased sampling, poor labels, leakage, missing consent, or distribution shift.
- **Model:** underfitting, overfitting, spurious correlations, overconfidence, or instability.
- **Evaluation:** contaminated test sets, weak baselines, wrong metrics, or hidden subgroups.
- **System:** training-serving skew, timeouts, stale features, version mismatch, or cascading retries.
- **Security/privacy:** poisoned data, adversarial inputs, model extraction, prompt injection, or sensitive-data leakage.
- **Human:** automation bias, inaccessible explanations, unsafe fallback, or feedback that reinforces harm.
- **Assumption:** treating probabilistic output as truth rather than evidence with uncertainty.

## Mastery exercise

Choose spam filtering, demand forecasting, or image moderation. Define the target, unit of prediction, decision threshold, cost of each error, non-AI baseline, data source, validation design, fallback, and monitoring signal.

