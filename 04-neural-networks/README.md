# Phase 04 — Neural Networks from First Principles

## Objective

Understand a neural network as a parameterized computation graph and training as numerical optimization—not as a sequence of library layers.

## WHAT / WHY / WHEN / WHERE / WHO

Neural networks compose affine transformations and nonlinearities to learn flexible functions. Depth supports reusable hierarchical computation. They are appropriate when task/data complexity warrants learned representations, but not automatically better for small structured datasets or strict interpretability/latency constraints. Layers produce activations; losses produce scalar objectives; reverse-mode autodiff produces gradients; optimizers consume gradients and update parameters.

## HOW

Study `perceptron/`, `activation-functions/`, `loss-functions/`, `forward-propagation/`, `backpropagation/`, `gradient-descent/`, then `training/`. Build scalar reverse-mode autodiff first, then a vectorized two-layer MLP. Check every parameter gradient using central differences:

\[
\frac{\partial L}{\partial \theta_i}\approx \frac{L(\theta_i+\epsilon)-L(\theta_i-\epsilon)}{2\epsilon}
\]

## FAILURE

Symmetry from initialization, saturated activations, dead units, exploding/vanishing gradients, unstable softmax/logarithms, wrong loss reduction, stale gradients, incorrect broadcasting, failure to switch train/eval behavior, and data/label bugs disguised as optimization problems.

## Exit gate

The scalar autodiff engine and MLP pass gradient checks, overfit a tiny batch, learn a nonlinear toy task, and include debug evidence for at least one broken gradient and one unstable loss.

