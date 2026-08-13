import numpy as np
import pytest

from ai_journey.attention import causal_mask, scaled_dot_product_attention


def test_attention_weights_are_probabilities() -> None:
    tokens = np.eye(3)
    output, weights = scaled_dot_product_attention(tokens, tokens, tokens)
    assert output.shape == (3, 3)
    np.testing.assert_allclose(weights.sum(axis=-1), np.ones(3))
    assert np.all(weights >= 0)


def test_causal_attention_cannot_use_future_values() -> None:
    query = np.ones((3, 2))
    key = np.ones((3, 2))
    first_values = np.array([[1.0], [2.0], [3.0]])
    changed_future = np.array([[1.0], [200.0], [300.0]])
    first, weights = scaled_dot_product_attention(
        query, key, first_values, causal_mask(3)
    )
    second, _ = scaled_dot_product_attention(query, key, changed_future, causal_mask(3))
    np.testing.assert_allclose(first[0], second[0])
    assert np.all(weights[np.triu_indices(3, k=1)] == 0)


def test_fully_masked_query_is_rejected() -> None:
    with pytest.raises(ValueError, match="at least one key"):
        scaled_dot_product_attention([[1.0]], [[1.0]], [[1.0]], [[False]])

