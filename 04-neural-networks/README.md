# Phase 04 — Neural Networks from First Principles

## Purpose

Understand a neural network as a parameterized computation graph and training
as numerical optimization, not as a sequence of library calls.

## WHAT / WHY / WHEN / WHERE / WHO

Affine layers and nonlinearities compose flexible functions. During training,
the forward graph produces predictions and loss; reverse-mode autodiff produces
gradients; an optimizer updates parameters. Use this capacity only when the
data/task justifies it. The learner must own the derivative and gradient
contracts; PyTorch is a comparison oracle after the manual version.

## HOW

Build scalar reverse-mode autodiff, vectorized layers, an MLP, losses, and a
training loop. Derive backpropagation with the chain rule and verify each
parameter with central finite differences. Make a tiny batch overfit before
training a nonlinear toy task.

## FAILURE

Break symmetry, activation saturation, dead units, exploding/vanishing
gradients, unstable softmax/logs, wrong loss reduction, stale gradients,
broadcasting, train/eval mode, bad learning rate, and label pipelines.

## VERIFY

Prerequisites: Phase 01 tensors and Phase 02 calculus/optimization. Enables
Phase 05 deep architectures and Phase 06 attention. Exit with scalar autodiff,
a gradient-checked MLP, tiny-batch overfit evidence, and debug reports for an
incorrect gradient, numerical instability, and learning-rate divergence.
