"""Graph-building helpers for Aurora."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .data import returns


@dataclass(frozen=True)
class Edge:
    """Correlation edge between two symbols."""

    source: str
    target: str
    correlation: float


def correlation(left: list[float], right: list[float]) -> float:
    """Compute a simple Pearson correlation."""
    if len(left) != len(right) or len(left) < 2:
        raise ValueError("series must have equal length and at least two observations")
    left_mean = sum(left) / len(left)
    right_mean = sum(right) / len(right)
    numerator = sum((a - left_mean) * (b - right_mean) for a, b in zip(left, right))
    left_var = sum((a - left_mean) ** 2 for a in left)
    right_var = sum((b - right_mean) ** 2 for b in right)
    denominator = (left_var * right_var) ** 0.5
    return 0.0 if denominator == 0 else numerator / denominator


def correlation_matrix(price_map: dict[str, list[float]]) -> dict[str, dict[str, float]]:
    """Build a rounded return-correlation matrix."""
    symbols = list(price_map)
    matrix: dict[str, dict[str, float]] = {}
    for source in symbols:
        row: dict[str, float] = {}
        for target in symbols:
            if source == target:
                row[target] = 1.0
            else:
                row[target] = round(correlation(returns(price_map[source]), returns(price_map[target])), 4)
        matrix[source] = row
    return matrix


def build_edges(price_map: dict[str, list[float]], threshold: float) -> list[Edge]:
    """Build thresholded correlation edges."""
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")
    edges: list[Edge] = []
    for source, target in combinations(price_map.keys(), 2):
        value = correlation(returns(price_map[source]), returns(price_map[target]))
        if abs(value) >= threshold:
            edges.append(Edge(source=source, target=target, correlation=round(value, 4)))
    return edges
