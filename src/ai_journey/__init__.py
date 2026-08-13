"""Small, inspectable AI implementations used as correctness laboratories."""

from .attention import scaled_dot_product_attention
from .autodiff import Value
from .linear_regression import LinearRegressionGD

__all__ = ["LinearRegressionGD", "Value", "scaled_dot_product_attention"]

