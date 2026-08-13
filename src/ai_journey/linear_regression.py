"""Linear regression using explicit NumPy gradients.

This module favors inspectability over features. Shapes are part of the API:
X is (n_samples, n_features), y is (n_samples,), weights are (n_features,).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from numpy.typing import ArrayLike, NDArray

FloatArray = NDArray[np.float64]


def _validated_xy(X: ArrayLike, y: ArrayLike) -> tuple[FloatArray, FloatArray]:
    features = np.asarray(X, dtype=np.float64)
    targets = np.asarray(y, dtype=np.float64)
    if features.ndim != 2:
        raise ValueError(f"X must be 2D (samples, features), got {features.shape}")
    if targets.ndim != 1:
        raise ValueError(f"y must be 1D (samples,), got {targets.shape}")
    if features.shape[0] != targets.shape[0]:
        raise ValueError("X and y must contain the same number of samples")
    if features.shape[0] == 0:
        raise ValueError("at least one sample is required")
    if not np.isfinite(features).all() or not np.isfinite(targets).all():
        raise ValueError("X and y must contain only finite values")
    return features, targets


def mse_loss_and_gradients(
    X: FloatArray, y: FloatArray, weights: FloatArray, bias: float
) -> tuple[float, FloatArray, float]:
    """Return mean squared error and its exact gradients.

    L = (1/n) * sum((Xw + b - y)^2)
    dL/dw = (2/n) X^T(Xw + b - y); dL/db = (2/n) sum(error)
    """

    errors = X @ weights + bias - y
    n_samples = X.shape[0]
    loss = float(np.mean(errors**2))
    weight_gradient = (2.0 / n_samples) * (X.T @ errors)
    bias_gradient = float((2.0 / n_samples) * np.sum(errors))
    return loss, weight_gradient, bias_gradient


@dataclass
class LinearRegressionGD:
    """Batch gradient-descent linear regression with a deliberately small API."""

    learning_rate: float = 0.05
    epochs: int = 1_000
    weights_: FloatArray | None = field(default=None, init=False)
    bias_: float = field(default=0.0, init=False)
    loss_history_: list[float] = field(default_factory=list, init=False)

    def fit(self, X: ArrayLike, y: ArrayLike) -> LinearRegressionGD:
        features, targets = _validated_xy(X, y)
        if self.learning_rate <= 0 or self.epochs <= 0:
            raise ValueError("learning_rate and epochs must be positive")

        self.weights_ = np.zeros(features.shape[1], dtype=np.float64)
        self.bias_ = 0.0
        self.loss_history_.clear()

        for _ in range(self.epochs):
            loss, weight_gradient, bias_gradient = mse_loss_and_gradients(
                features, targets, self.weights_, self.bias_
            )
            if not np.isfinite(loss):
                raise FloatingPointError(
                    "loss became non-finite; inspect scaling and learning rate"
                )
            self.weights_ -= self.learning_rate * weight_gradient
            self.bias_ -= self.learning_rate * bias_gradient
            self.loss_history_.append(loss)
        return self

    def predict(self, X: ArrayLike) -> FloatArray:
        if self.weights_ is None:
            raise RuntimeError("fit must be called before predict")
        features = np.asarray(X, dtype=np.float64)
        if features.ndim != 2 or features.shape[1] != self.weights_.shape[0]:
            raise ValueError("X must be 2D with the fitted feature count")
        if not np.isfinite(features).all():
            raise ValueError("X must contain only finite values")
        return features @ self.weights_ + self.bias_

