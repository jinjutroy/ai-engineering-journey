# Backpropagation

## WHAT

Backpropagation is an algorithm that computes derivatives of a scalar output with respect to intermediate values and parameters by traversing a computational graph in reverse topological order. In modern systems it is usually reverse-mode automatic differentiation.

## WHY

For a model with millions of parameters and one scalar loss, independently perturbing every parameter is prohibitively expensive. Reverse mode reuses local derivatives so all parameter gradients cost on the same order as a small number of forward passes. Without it, gradient-based training at current scale would be impractical.

## WHEN

Use it for differentiable programs with many inputs/parameters and few scalar outputs. Do not confuse it with an optimizer: backprop computes gradients; gradient descent consumes them. It is unsuitable through truly discrete/non-differentiable operations without a surrogate, estimator, or alternative method.

## WHERE

It runs after the forward pass creates values and a scalar loss, before the optimizer updates parameters. The graph or saved activations connects model operations to the autodiff engine.

## WHO

Operators produce outputs and define local vector–Jacobian products. The loss seeds an upstream gradient of 1. Parameters and earlier activations accumulate gradient contributions. The optimizer later consumes parameter gradients.

## HOW

For \(z=f(x,y)\) and scalar \(L\), each node receives \(\bar z=\partial L/\partial z\) and distributes:

\[
\bar x \mathrel{+}= \bar z\frac{\partial z}{\partial x},\qquad
\bar y \mathrel{+}= \bar z\frac{\partial z}{\partial y}
\]

The `+=` is essential when one value reaches the loss through multiple paths. A topological ordering guarantees consumers run before producers during reversal.

```text
forward: build graph and save values needed by local derivatives
order = topological_sort(loss)
set every gradient to zero; loss.gradient = 1
for node in reverse(order):
    apply node's local backward rule and accumulate into parents
```

Run `src/ai_journey/autodiff.py`, draw its graph for `(x*w+b-5)^2`, calculate derivatives by hand, and compare.

## FAILURE

Overwriting rather than accumulating gradients; traversing in the wrong order; stale gradients between steps; detaching values; in-place mutation of saved activations; incorrect broadcasting reductions; non-scalar backward seeds; nondifferentiable points; vanishing/exploding products; and memory growth from retaining graphs. A plausible decreasing loss does not prove every gradient is correct.

## Lab

Break multiplication’s local derivative, demonstrate which test detects it, perform central-difference checks across random inputs, then add one activation to the engine and document its unstable region.

