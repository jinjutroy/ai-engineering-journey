# Phase 07 — Large Language Models

## Objective

Understand how a next-token model becomes a trained and served language system, including the limits that no prompt or framework removes.

## WHAT / WHY / WHEN / WHERE / WHO

An LLM is a high-capacity language model, commonly a decoder-only transformer, trained on large token sequences to estimate conditional next-token distributions. It is useful for flexible language/code transformation and generation but should not replace deterministic computation, authoritative retrieval, or accountable human judgment where guarantees matter. Data curators, tokenizers, trainers, evaluators, inference engines, policy systems, applications, and users all influence its behavior.

## HOW

- `pretraining/`: corpora, filtering, deduplication, objective, scaling, distributed optimization, and checkpoints.
- `tokenization/`: vocabulary learning, segmentation, normalization, special tokens, and version contracts.
- `context-window/`: attention limits, position behavior, long-context degradation, truncation, and memory.
- `inference/`: prefill/decode, KV cache, batching, quantization, throughput, latency, and memory.
- `decoding/`: greedy, beam search, temperature, top-k, nucleus sampling, repetition control, and constrained output.

Train a tiny causal model so the complete loop is observable; then profile prefill separately from token-by-token decode.

## FAILURE

Memorization/privacy leakage, data contamination, toxic or biased outputs, hallucination, prompt injection, context confusion, nondeterminism, exposure bias, reward hacking, benchmark gaming, tokenizer mismatch, OOM, tail latency, cache corruption, unbounded generation, and unsafe tool authority.

## Exit gate

Train and evaluate a tiny model, compare decoding distributions empirically, explain KV-cache memory, measure quality/latency/cost, produce a model card, and define safe fallback behavior.

