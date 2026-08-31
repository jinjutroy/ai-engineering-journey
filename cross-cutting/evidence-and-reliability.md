# Evidence and Reliability

## WHAT

Evidence engineering makes the basis of an AI answer or action explicit. It
distinguishes:

```text
FACT | OBSERVATION | INFERENCE | HYPOTHESIS | UNKNOWN | CONFLICT
```

## WHY

Relevance is not truth. Confidence is not correctness. Model output is not a
verified fact. Without an evidence boundary, fluent output can become an
unreviewed decision or unsafe action.

## WHEN

Require stronger evidence for high-impact decisions, external claims,
irreversible actions, and safety-sensitive workflows. Allow abstention or human
confirmation when evidence is incomplete or conflicting.

## WHERE

Evidence sits across retrieval, context construction, generation, tool use,
evaluation, and product decision layers.

## WHO

Sources provide evidence; retrievers and rankers select it; models propose
answers; validators check support; domain owners define acceptable authority;
operators monitor regressions and incidents.

## HOW

Use the decision policy:

```text
enough evidence       → answer or act
incomplete evidence   → retrieve or ask
conflicting evidence  → verify or escalate
no recoverable source → abstain
```

Record citations, source authority, timestamps, confidence, uncertainty, and
conflict status. Use code-based validation where possible and human review where
the cost of an incorrect action is high.

## FAILURE

- Citation does not support the claim
- Low-quality source outranks authoritative source
- Conflicting evidence is hidden
- Unsupported inference is stated as fact
- Confidence score is miscalibrated
- Agent acts without enough evidence
- Evaluation rewards plausible wording over correctness

## VERIFY

- Build a golden set with supported, unsupported, and conflicting cases.
- Measure citation correctness, abstention quality, factual correctness, and
  action safety.
- Add regression cases from production failures.
- Test that the system refuses or escalates when evidence is insufficient.
