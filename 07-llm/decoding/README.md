# Decoding

## WHAT

Decoding converts a model’s conditional token probability distribution into an output sequence using a selection policy and stopping rules.

## WHY

Training produces probabilities, not one uniquely correct continuation. A decoding policy trades determinism, diversity, likelihood, repetition, latency, and constraint satisfaction. Without explicit policy, product behavior is underspecified.

## WHEN

Use greedy or constrained decoding for reproducible structured tasks when its quality is validated; sampling for creative or distributional diversity; beam search mainly where sequence-level likelihood correlates with task quality. Do not assume a decoding tweak repairs missing knowledge or reasoning.

## WHERE

Decoding is the iterative control loop around model inference: tokenize prompt, prefill, obtain logits, transform/select a token, append, update cache, and stop. Policy/validation may constrain accepted tokens or final output.

## WHO

The model produces logits; temperature and filters transform them; a sampler or search selects tokens; tokenizer decodes IDs; stop policy, schema validator, and application consume the sequence.

## HOW

Temperature \(T>0\) transforms logits \(z_i\) into \(p_i=\operatorname{softmax}(z_i/T)\). Top-k retains the k highest logits. Nucleus sampling retains the smallest sorted set whose cumulative probability reaches p, then renormalizes. Greedy selects the maximum. Constrained decoding masks invalid next tokens according to a grammar or state machine.

```text
state = prefill(prompt)
while within token/time budget:
    logits, state = model.next(state)
    logits = apply_constraints_penalties_temperature(logits)
    token = select(logits, seeded_rng)
    if token matches stop policy: break
    emit token
validate final structure and semantics
```

## FAILURE

Temperature zero/division errors, filters applied in the wrong order, empty candidate sets, infinite/repetitive loops, token-level stop strings split unexpectedly, nondeterministic tests, beam search length bias, invalid structured output, unbounded cost, cache/state mismatch, and unsafe output treated as authorization.

## Lab

Implement greedy, temperature, top-k, and top-p over a fixed toy distribution. Run thousands of seeded draws, compare empirical frequencies, measure diversity/repetition, and explain why higher likelihood does not necessarily mean better task utility.

