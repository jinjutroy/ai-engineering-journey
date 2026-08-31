# Phase 07 — LLM Internals and Inference

## Purpose

Understand how next-token prediction becomes a trained and served language
system, including what model size and prompting cannot guarantee.

## WHAT / WHY / WHEN / WHERE / WHO

The flow is `Tokenizer → token IDs → embeddings → transformer → logits →
probabilities → decoding → next token`. Pretraining, supervised fine-tuning,
preference optimization, inference strategy, context use, and tools all affect
capability. A model is not a verified database or an authorization policy.

## HOW

Train/evaluate a tiny causal model. Cover cross-entropy, data/compute/model
architecture, SFT, preference optimization, instruction following, context
windows, prefill/decode, KV cache, greedy/temperature/top-k/top-p sampling,
quantization, calibration, batching, and parameter/memory accounting. Compare
decoding strategies empirically and separate quality from latency/cost.

## FAILURE

Break tokenizer contracts, data contamination, privacy leakage, hallucination,
context confusion, unbounded generation, nondeterminism, sampling assumptions,
quantization quality, KV-cache correctness, OOM, tail latency, and unsafe tool
authority.

## VERIFY

Prerequisites: Phase 06 transformer mechanisms. Enables retrieval, context,
agent, and serving design. Exit with a tiny model evaluation, decoding
comparison, prefill/decode and KV-cache explanation, quality/latency/cost
measurements, model card, and safe fallback policy.
