"""Smoke-run the first three inspectable implementations."""

from __future__ import annotations

import numpy as np

from ai_journey import LinearRegressionGD, Value, scaled_dot_product_attention
from ai_journey.attention import causal_mask


def main() -> None:
    X = np.array([[0.0], [1.0], [2.0], [3.0]])
    y = 2.0 * X[:, 0] + 1.0
    model = LinearRegressionGD(learning_rate=0.05, epochs=1_000).fit(X, y)
    print("linear regression:", model.weights_, model.bias_, model.loss_history_[-1])

    x, w, b = Value(2.0), Value(-3.0), Value(10.0)
    loss = (x * w + b - 5.0) ** 2
    loss.backward()
    print("autodiff:", loss.data, {"dx": x.grad, "dw": w.grad, "db": b.grad})

    tokens = np.eye(3)
    output, weights = scaled_dot_product_attention(
        tokens, tokens, tokens, causal_mask(len(tokens))
    )
    print("attention output:\n", output)
    print("attention row sums:", weights.sum(axis=-1))


if __name__ == "__main__":
    main()

