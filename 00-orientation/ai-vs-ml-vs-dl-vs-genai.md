# AI vs. ML vs. Deep Learning vs. Generative AI

## WHAT

- **AI** is the broad capability-oriented field, including rule systems, search, planning, optimization, learning, and hybrids.
- **Machine learning (ML)** creates behavior by fitting a model or policy from data rather than specifying every rule directly.
- **Deep learning (DL)** is ML using multi-layer differentiable neural networks that learn hierarchical representations.
- **Generative AI (GenAI)** models a data distribution or conditional distribution to produce new samples such as text, images, audio, code, or structured outputs.

The useful relationship is overlapping scope, not marketing categories: DL is a subset of ML; ML is one family within AI; modern GenAI is usually DL, while not all DL is generative.

## WHY

The distinctions expose different assumptions and operating costs. A rules engine offers explicit behavior. Classical ML can be data-efficient and interpretable for structured data. DL learns representations but usually demands more compute and data. Generative models support open-ended outputs but expand evaluation and safety difficulty. Without these distinctions, teams select technology based on labels rather than task structure.

## WHEN

- Use rules/optimization for stable constraints and exact policies.
- Use classical ML for structured prediction with strong features and modest data.
- Use DL for high-dimensional perception or representation learning where simpler baselines lose materially.
- Use generative models when multiple valid outputs exist and creation/transformation is the task.
- Do not use generation when retrieval, classification, templates, or deterministic transformations satisfy the requirement more safely.

## WHERE

All may occupy the decision component of a product architecture. They can also compose: rules validate inputs, retrieval supplies facts, a neural model generates a candidate, a classifier filters risk, and deterministic code executes an approved action.

## WHO

Data pipelines produce training/evaluation examples; training algorithms fit parameters; inference services consume inputs; policy layers validate outputs; product code turns scores or generated content into user-visible decisions; operators monitor outcomes.

## HOW

A discriminative classifier models \(p(y\mid x)\) or a decision boundary. A generative model estimates \(p(x)\) or \(p(x\mid c)\). An autoregressive language model factorizes a sequence:

\[
p(x_{1:T}) = \prod_{t=1}^{T} p(x_t \mid x_{<t})
\]

This next-token objective can produce flexible language behavior, but it does not by itself guarantee factuality, planning, or compliance. Those are system-level properties requiring evidence, evaluation, and controls.

## FAILURE

- Calling any conditional or automated feature “AI” hides the actual mechanism and risks.
- Assuming DL always beats classical methods ignores data size, latency, interpretability, and maintenance.
- Treating generated fluency as calibrated correctness leads to unsafe decisions.
- Comparing models across incompatible tokenizers, datasets, or metrics creates false conclusions.
- Adding a language model where deterministic code suffices increases nondeterminism, attack surface, cost, and debugging complexity.

## Decision exercise

For each of autocomplete, invoice totals, fraud detection, photo search, and contract summarization, propose a deterministic baseline, an ML option, and a decision criterion for escalating complexity.

