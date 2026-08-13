# Phase 01 — Programming Foundation

## Objective

Use Python as an engineering tool and arrays/tensors as explicit computational objects. This is not a language syntax course; focus on correctness, memory, performance, testability, and reproducibility.

## WHAT / WHY / WHEN / WHERE / WHO

Python orchestrates experiments and services; NumPy exposes array programming; pandas handles labeled tabular transformations; PyTorch supplies tensors, automatic differentiation, accelerators, and neural-network primitives. Learn them in that order so that PyTorch behavior is not magical. Use vectorized kernels where profiling justifies them, but retain readable reference implementations as correctness oracles. These tools sit between data sources, algorithms, training loops, and services; their outputs are consumed by evaluators and production code.

## HOW

- `python/`: types, mutability, iterators, context managers, exceptions, typing, packaging, tests, profiling, concurrency, and serialization.
- `numpy/`: shapes, strides, views/copies, broadcasting, indexing, reductions, numerical stability, and vectorization.
- `pandas/`: schemas, joins, missing values, group operations, time, leakage-safe transforms, and memory.
- `pytorch/`: tensors, devices/dtypes, autograd graph, modules, optimizers, datasets, checkpoints, and deterministic limits.

## FAILURE

Aliasing and mutation, accidental broadcasting, object dtypes, chained dataframe assignment, data leakage, CPU/GPU mismatch, detached graphs, nondeterminism, unstable reductions, silent copies, and serialization of untrusted objects.

## Build–break–debug labs

1. Implement linear regression using Python loops, NumPy, then PyTorch; compare outputs and profile.
2. Cause a broadcasting bug that returns a plausible shape; catch it with semantic shape assertions.
3. Create a train/test leakage bug in preprocessing and measure the false gain.
4. Save and resume training; prove optimizer and random state matter.

## Exit gate

The tested NumPy implementation in `src/` runs, all shapes and dtypes are documented, loop/vectorized complexity is explained, and a debug report covers one silent correctness bug.

