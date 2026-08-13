import numpy as np
import pytest

from ai_journey.linear_regression import LinearRegressionGD, mse_loss_and_gradients


def test_gradient_matches_central_difference() -> None:
    X = np.array([[1.0, 2.0], [3.0, -1.0], [0.5, 4.0]])
    y = np.array([2.0, -1.0, 3.0])
    weights = np.array([0.2, -0.4])
    bias = 0.3
    _, analytic, _ = mse_loss_and_gradients(X, y, weights, bias)
    epsilon = 1e-6
    numerical = np.zeros_like(weights)
    for index in range(weights.size):
        plus, minus = weights.copy(), weights.copy()
        plus[index] += epsilon
        minus[index] -= epsilon
        loss_plus = mse_loss_and_gradients(X, y, plus, bias)[0]
        loss_minus = mse_loss_and_gradients(X, y, minus, bias)[0]
        numerical[index] = (loss_plus - loss_minus) / (2 * epsilon)
    np.testing.assert_allclose(analytic, numerical, rtol=1e-6, atol=1e-7)


def test_fit_recovers_simple_line() -> None:
    X = np.arange(6, dtype=float).reshape(-1, 1)
    y = 2.0 * X[:, 0] + 1.0
    model = LinearRegressionGD(learning_rate=0.03, epochs=2_000).fit(X, y)
    np.testing.assert_allclose(model.predict(X), y, atol=1e-4)
    assert model.loss_history_[-1] < model.loss_history_[0]


def test_rejects_ambiguous_target_shape() -> None:
    with pytest.raises(ValueError, match="y must be 1D"):
        LinearRegressionGD().fit([[1.0], [2.0]], [[1.0], [2.0]])

