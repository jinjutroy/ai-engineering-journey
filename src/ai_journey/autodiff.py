"""A scalar reverse-mode automatic-differentiation engine.

The implementation makes the computational graph and chain rule visible. It is
for learning and gradient checking, not performance or production workloads.
"""

from __future__ import annotations

import math
from collections.abc import Callable


class Value:
    def __init__(
        self,
        data: float,
        children: tuple[Value, ...] = (),
        operation: str = "",
        label: str = "",
    ) -> None:
        self.data = float(data)
        self.grad = 0.0
        self._previous = set(children)
        self._operation = operation
        self._backward: Callable[[], None] = lambda: None
        self.label = label

    def __repr__(self) -> str:
        return f"Value(data={self.data:.6g}, grad={self.grad:.6g})"

    @staticmethod
    def _coerce(value: float | Value) -> Value:
        return value if isinstance(value, Value) else Value(value)

    def __add__(self, other: float | Value) -> Value:
        right = self._coerce(other)
        out = Value(self.data + right.data, (self, right), "+")

        def _backward() -> None:
            self.grad += out.grad
            right.grad += out.grad

        out._backward = _backward
        return out

    def __radd__(self, other: float | Value) -> Value:
        return self + other

    def __mul__(self, other: float | Value) -> Value:
        right = self._coerce(other)
        out = Value(self.data * right.data, (self, right), "*")

        def _backward() -> None:
            self.grad += right.data * out.grad
            right.grad += self.data * out.grad

        out._backward = _backward
        return out

    def __rmul__(self, other: float | Value) -> Value:
        return self * other

    def __neg__(self) -> Value:
        return self * -1.0

    def __sub__(self, other: float | Value) -> Value:
        return self + (-self._coerce(other))

    def __rsub__(self, other: float | Value) -> Value:
        return self._coerce(other) - self

    def __pow__(self, exponent: float) -> Value:
        if not isinstance(exponent, (int, float)):
            raise TypeError("only scalar numeric exponents are supported")
        out = Value(self.data**exponent, (self,), f"**{exponent}")

        def _backward() -> None:
            self.grad += exponent * (self.data ** (exponent - 1)) * out.grad

        out._backward = _backward
        return out

    def __truediv__(self, other: float | Value) -> Value:
        return self * self._coerce(other) ** -1

    def tanh(self) -> Value:
        result = math.tanh(self.data)
        out = Value(result, (self,), "tanh")

        def _backward() -> None:
            self.grad += (1.0 - result**2) * out.grad

        out._backward = _backward
        return out

    def exp(self) -> Value:
        result = math.exp(self.data)
        out = Value(result, (self,), "exp")

        def _backward() -> None:
            self.grad += result * out.grad

        out._backward = _backward
        return out

    def backward(self) -> None:
        """Apply reverse-mode chain rule from this scalar output."""

        ordered: list[Value] = []
        visited: set[Value] = set()

        def visit(node: Value) -> None:
            if node in visited:
                return
            visited.add(node)
            for parent in node._previous:
                visit(parent)
            ordered.append(node)

        visit(self)
        for node in ordered:
            node.grad = 0.0
        self.grad = 1.0
        for node in reversed(ordered):
            node._backward()
