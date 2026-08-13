# Phase 02 — Mathematics for AI Engineering

## Objective

Build operational mathematics: derive, compute, visualize, and use each concept to debug an implementation.

## WHAT / WHY / WHEN / WHERE / WHO

Linear algebra represents data and transformations; probability models uncertainty; statistics connects samples to populations; calculus describes local change; optimization selects parameters under an objective. Together they form the language connecting data, loss, gradients, training algorithms, and evaluation. Use the minimum mathematical machinery that makes assumptions and trade-offs explicit; do not perform symbolic work detached from an engineering question.

## HOW

- `linear-algebra/`: vectors, bases, matrix products, rank, projections, eigenvalues, SVD, norms, and conditioning.
- `probability/`: random variables, conditional probability, Bayes, expectation, variance, common distributions, and Monte Carlo.
- `statistics/`: estimators, sampling, intervals, hypothesis tests, effect size, multiple comparisons, and bootstrap.
- `calculus/`: derivatives, partials, gradients, Jacobians, chain rule, and computational graphs.
- `optimization/`: convexity intuition, gradient methods, momentum, adaptive methods, constraints, and learning-rate behavior.

Every topic follows: hand calculation → NumPy verification → deliberate numerical failure → application to a model.

## FAILURE

Dimension errors, confusing probability with likelihood, independence assumptions, biased samples, p-value misuse, ill-conditioning, floating-point cancellation, incorrect chain-rule paths, saddle points, exploding gradients, and drawing causal claims from correlations.

## Exit gate

Derive matrix-form MSE gradients, verify them by central finite differences, explain conditioning effects, and report statistical uncertainty for a multi-seed model comparison.

