# Phase 01 — AI Programming Foundation

## Purpose

Use Python as an engineering tool and arrays/tensors as explicit computational
objects. General programming is assumed; this phase focuses on numerical
correctness, memory, performance, reproducibility, and framework boundaries.

## WHAT / WHY / WHEN / WHERE / WHO

NumPy and PyTorch expose data, tensor, and autodiff semantics used by later
models. They sit between data, algorithms, experiments, and services. Use
vectorized operations when measurement supports them, while retaining a clear
reference implementation. The learner owns shape/dtype/device contracts;
frameworks provide kernels and abstractions but do not own understanding.

## HOW

Follow `NumPy → manual implementation → PyTorch equivalent → behavior comparison → profile`.
Cover shapes, broadcasting, strides, views/copies, dtypes, devices, memory,
vectorization, profiling, serialization, datasets, modules, optimizers,
autograd, and deterministic limits. Use the existing `src/` and `tests/` as
supporting implementation artifacts.

## FAILURE

Break accidental broadcasting, aliasing, silent copies, object dtypes,
train/test leakage, CPU/GPU mismatch, detached graphs, nondeterminism, unstable
reductions, and unsafe serialization. Record whether each failure is semantic,
numerical, performance, or operational.

## VERIFY

Prerequisites: professional software engineering. Enables Phase 02–04 tensor
and gradient work. Exit only after a tested loop/NumPy/PyTorch comparison,
shape and dtype assertions, a profile showing the bottleneck, and a debug report
for one plausible-but-wrong result.
