# Phase 06 — Transformers

## Purpose

Implement and reason about a transformer block at tensor-operation level. This
is one of the deepest phases because later LLM behavior depends on these
mechanisms and shape contracts.

## WHAT / WHY / WHEN / WHERE / WHO

Attention routes information between sequence positions; positional
representation supplies order; feed-forward layers transform each position;
residual paths and normalization support optimization. Tokenizers produce IDs,
embeddings produce vectors, attention consumes Q/K/V, masks constrain access,
and the block feeds LLM training and inference.

## HOW

Implement stable softmax, scaled dot-product attention, causal/padding masks,
multi-head split/merge, positional representation, feed-forward network,
residuals, normalization, and a minimal block in NumPy. Track every shape.
Derive `softmax(QKᵀ / √d_k + M)V`, FLOPs, attention memory, sequence-length and
head-width trade-offs, then connect incremental decoding to the KV cache.

## FAILURE

Break tokenizer mismatch, mask polarity/broadcasting, fully masked rows,
missing scaling, softmax overflow, reshape/transposition, padding
contamination, quadratic memory, long-context quality, and KV-cache reuse.
Attention weights are not automatically explanations.

## VERIFY

Prerequisites: Phase 02 linear algebra/calculus and Phase 04–05 networks.
Enables Phase 07 LLMs and inference optimization. Exit with NumPy attention,
masked and multi-head variants, trusted-reference comparison, shape/invariance/
numerical tests, complexity derivation, and documented failure drills.
