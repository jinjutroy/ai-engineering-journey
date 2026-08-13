# Phase 06 — Transformers

## Objective

Implement a transformer block from array operations and understand each architectural decision, computational cost, and failure boundary.

## WHAT / WHY / WHEN / WHERE / WHO

A transformer processes sequences using attention for token-to-token information routing and position-wise feed-forward transformations, connected by residual paths and normalization. It enables parallel training and flexible long-range interaction, but attention cost and weak built-in structural priors make it unnecessary for many tasks. Tokenizers produce IDs; embedding layers produce vectors; attention consumes queries/keys/values; masks constrain information; feed-forward layers transform each position; residual and normalization paths stabilize the stack.

## HOW

Study in folder order. For one head:

\[
Q=XW_Q,\quad K=XW_K,\quad V=XW_V
\]

\[
\operatorname{Attention}(Q,K,V)=\operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}+M\right)V
\]

Track dimensions on every line. Implement stable softmax, padding and causal masks, head split/merge, feed-forward network, residual paths, and normalization. Compare fixed inputs/weights with a trusted implementation.

## FAILURE

Tokenizer/model mismatch, wrong positional behavior, mask polarity or broadcasting errors, NaNs from fully masked rows, missing scale factor, softmax overflow, head reshape/transposition bugs, quadratic memory, padding contamination, KV-cache mistakes, and false interpretation of attention weights as explanations.

## Exit gate

NumPy attention passes invariance, masking, shape, and numerical tests; a multi-head causal block matches a trusted implementation; complexity and memory are derived; failures are documented.

