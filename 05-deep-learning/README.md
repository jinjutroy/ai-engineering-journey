# Phase 05 — Deep Learning Architectures and Stability

## Purpose

Learn why architectures encode inductive bias and how information, gradients,
memory, and compute move through deeper models.

## WHAT / WHY / WHEN / WHERE / WHO

CNNs encode locality and weight sharing; RNNs encode sequential state; LSTMs
add gates to preserve useful information. Normalization, initialization,
regularization, and optimization shape training dynamics. Study LSTM only to
understand recurrence limits and why attention becomes attractive; do not make
it a second specialization.

## HOW

Implement a naive convolution, unroll an RNN through time, inspect LSTM gates,
and compare normalization, initialization, dropout, and weight decay through
single-variable ablations. Profile parameter, activation, and optimizer-state
memory. Connect each architecture to data locality, sequence length, latency,
and deployment constraints.

## FAILURE

Break receptive fields, padding, hidden-state reset, sequence masking,
vanishing/exploding gradients, normalization leakage, batch sensitivity,
over-regularization, mixed-precision ranges, memory limits, and reproducibility.

## VERIFY

Prerequisites: Phase 04 networks and Phase 02 gradients. Enables transformer
motivation and architecture judgment. Exit with one image and one sequence
experiment, a stability ablation, a reproduced failure, and a quality/latency/
memory trade-off report.
