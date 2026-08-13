import math

from ai_journey.autodiff import Value


def test_chain_rule_with_shared_value() -> None:
    x = Value(3.0)
    result = x * x + 2.0 * x
    result.backward()
    assert math.isclose(result.data, 15.0)
    assert math.isclose(x.grad, 8.0)


def test_tanh_gradient() -> None:
    x = Value(0.7)
    y = x.tanh()
    y.backward()
    expected = 1.0 - math.tanh(0.7) ** 2
    assert math.isclose(x.grad, expected, rel_tol=1e-12)


def test_backward_resets_graph_gradients() -> None:
    x = Value(2.0)
    y = x**3
    y.backward()
    y.backward()
    assert math.isclose(x.grad, 12.0)

