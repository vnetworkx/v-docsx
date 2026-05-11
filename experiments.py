"""Small reference utilities for Vector Network experiments.

This file is intentionally simple and deterministic. It is not a full node
implementation. It exists to help researchers test the mathematics of vectors,
drain, normalization guards, and settlement-style transformations.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple


Number = float


@dataclass(frozen=True)
class Vector:
    components: Tuple[Number, ...]
    type_id: str = "default"

    def __post_init__(self) -> None:
        if len(self.components) == 0:
            raise ValueError("Vector must have at least one component.")
        if any(c != c or c == float("inf") or c == float("-inf") for c in self.components):
            raise ValueError("Vector components must be finite numbers.")

    @property
    def magnitude(self) -> Number:
        return float(sum(self.components))

    def is_zero(self) -> bool:
        return all(c == 0 for c in self.components)

    def normalized(self) -> "Vector":
        mag = self.magnitude
        if mag == 0:
            raise ZeroDivisionError("Normalization is undefined for the zero vector.")
        return Vector(tuple(c / mag for c in self.components), type_id=f"{self.type_id}:normalized")

    def add(self, other: "Vector") -> "Vector":
        _assert_same_dimension(self, other)
        return Vector(tuple(a + b for a, b in zip(self.components, other.components)), type_id=self.type_id)

    def sub(self, other: "Vector") -> "Vector":
        _assert_same_dimension(self, other)
        return Vector(tuple(a - b for a, b in zip(self.components, other.components)), type_id=self.type_id)

    def scale(self, factor: Number) -> "Vector":
        return Vector(tuple(c * factor for c in self.components), type_id=self.type_id)

    def split(self, amount: Number, component_index: int = 0) -> tuple["Vector", "Vector"]:
        if amount < 0:
            raise ValueError("Split amount must be non-negative.")
        if component_index < 0 or component_index >= len(self.components):
            raise IndexError("component_index out of range.")
        if self.components[component_index] < amount:
            raise ValueError("Insufficient value for split.")
        left = list(self.components)
        right = [0.0] * len(self.components)
        left[component_index] -= amount
        right[component_index] = amount
        return Vector(tuple(left), self.type_id), Vector(tuple(right), self.type_id)


def apply_drain(vector: Vector, rate: Number) -> tuple[Vector, Number]:
    """Apply proportional drain and return (net_vector, drained_amount)."""
    if rate < 0 or rate > 1:
        raise ValueError("rate must be between 0 and 1.")
    drained = vector.scale(rate)
    net = vector.sub(drained)
    return net, drained.magnitude


def transfer(source: Vector, amount: Number, component_index: int = 0) -> tuple[Vector, Vector]:
    """Move value from the source into a destination-shaped vector."""
    if amount < 0:
        raise ValueError("amount must be non-negative.")
    if component_index < 0 or component_index >= len(source.components):
        raise IndexError("component_index out of range.")
    if source.components[component_index] < amount:
        raise ValueError("Insufficient source balance.")
    source_after = list(source.components)
    source_after[component_index] -= amount
    dest = [0.0] * len(source.components)
    dest[component_index] = amount
    return Vector(tuple(source_after), source.type_id), Vector(tuple(dest), source.type_id)


def settlement_return(projected: Vector, gain: Number = 0.0, loss: Number = 0.0) -> Vector:
    """A toy settlement function for experimentation."""
    if gain < 0 or loss < 0:
        raise ValueError("gain and loss must be non-negative.")
    delta = gain - loss
    if projected.is_zero() and delta != 0:
        # This is allowed mathematically, but implementations may reject it by policy.
        pass
    return Vector(tuple(c + (delta / len(projected.components)) for c in projected.components), projected.type_id)


def _assert_same_dimension(a: Vector, b: Vector) -> None:
    if len(a.components) != len(b.components):
        raise ValueError("Vector dimensions must match.")


if __name__ == "__main__":
    v = Vector((10.0, 5.0, 0.0))
    print("vector:", v)
    print("magnitude:", v.magnitude)
    print("normalized:", v.normalized())
    net, drained = apply_drain(v, 0.1)
    print("after drain:", net, "drained:", drained)
