"""Inspectable scaled dot-product attention implemented with NumPy."""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray

FloatArray = NDArray[np.float64]


def stable_softmax(values: FloatArray, axis: int = -1) -> FloatArray:
    """Compute softmax after subtracting the maximum for numerical stability."""

    shifted = values - np.max(values, axis=axis, keepdims=True)
    exponentials = np.exp(shifted)
    return exponentials / np.sum(exponentials, axis=axis, keepdims=True)


def scaled_dot_product_attention(
    query: ArrayLike,
    key: ArrayLike,
    value: ArrayLike,
    allowed_mask: ArrayLike | None = None,
) -> tuple[FloatArray, FloatArray]:
    """Return attention output and weights for one head.

    Shapes: query=(q,d), key=(k,d), value=(k,dv), output=(q,dv).
    If supplied, ``allowed_mask`` broadcasts to (q,k); True means attention is
    allowed. Every query must have at least one allowed key.
    """

    q = np.asarray(query, dtype=np.float64)
    k = np.asarray(key, dtype=np.float64)
    v = np.asarray(value, dtype=np.float64)
    if q.ndim != 2 or k.ndim != 2 or v.ndim != 2:
        raise ValueError("query, key, and value must all be rank-2 arrays")
    if q.shape[1] != k.shape[1]:
        raise ValueError("query and key feature dimensions must match")
    if k.shape[0] != v.shape[0]:
        raise ValueError("key and value sequence lengths must match")
    if q.shape[1] == 0:
        raise ValueError("key dimension must be positive")
    if not np.isfinite(q).all() or not np.isfinite(k).all() or not np.isfinite(v).all():
        raise ValueError("query, key, and value must contain only finite values")

    scores = (q @ k.T) / np.sqrt(q.shape[1])
    if allowed_mask is not None:
        mask = np.asarray(allowed_mask, dtype=bool)
        try:
            mask = np.broadcast_to(mask, scores.shape)
        except ValueError as error:
            raise ValueError(f"mask cannot broadcast to score shape {scores.shape}") from error
        if np.any(~np.any(mask, axis=-1)):
            raise ValueError("every query row must allow at least one key")
        scores = np.where(mask, scores, -np.inf)

    weights = stable_softmax(scores)
    return weights @ v, weights


def causal_mask(sequence_length: int) -> NDArray[np.bool_]:
    """Return a lower-triangular mask where True means visible."""

    if sequence_length <= 0:
        raise ValueError("sequence_length must be positive")
    return np.tril(np.ones((sequence_length, sequence_length), dtype=bool))

