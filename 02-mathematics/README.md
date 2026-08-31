# Phase 02 — Mathematical Foundations for AI Engineering

## Purpose

Study mathematics through implementation. Every high-priority topic must have
an explanation, derivation, numerical example, failure case, and application.
Do not turn this into a pure mathematics degree.

## WHAT / WHY / WHEN / WHERE / WHO

Linear algebra represents data and transformations; calculus describes change;
probability and statistics describe uncertainty and evidence; optimization
selects parameters under an objective; information theory explains predictive
distributions and coding costs; numerical reliability keeps computation honest.
These mechanisms connect data to losses, gradients, models, and evaluation.

## HOW

- Linear algebra: vectors, bases, matrices, transformations, products, norms, projections, rank, eigenpairs, SVD, conditioning.
- Calculus: functions, limits, derivatives, partials, gradients, Jacobians, Hessians, chain rule, autodiff, finite differences.
- Probability/statistics: conditional probability, distributions, expectation, covariance, Bayes, MLE/MAP, estimators, sampling, intervals, testing, generalization.
- Optimization: objectives, constraints, convexity intuition, GD/SGD, momentum, Adam, regularization, saddle points, learning-rate behavior.
- Information/numerics: entropy, cross-entropy, KL, mutual information, floating point, FP32/FP16/BF16, overflow/underflow, stability.

## FAILURE

Break dimension assumptions, independence assumptions, biased samples, p-value
misuse, ill-conditioning, cancellation, incorrect chain-rule paths, unstable
softmax/logarithms, gradient divergence, and false causal claims from correlation.

## VERIFY

Prerequisites: Phase 01 array semantics. Enables ML objectives, backpropagation,
attention, and reliable experiments. Exit with hand matrix multiplication,
matrix-form MSE derivation, finite-difference gradient check, conditioning
experiment, and a multi-seed comparison reporting uncertainty.
