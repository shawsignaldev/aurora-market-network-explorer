"""Graph metrics for Aurora."""

from __future__ import annotations

from collections.abc import Iterable

from .graph import Edge


def graph_summary(nodes: Iterable[str], edges: list[Edge]) -> dict[str, int | float]:
    """Return a small graph summary."""
    node_list = list(nodes)
    possible_edges = len(node_list) * (len(node_list) - 1) / 2
    density = 0.0 if possible_edges == 0 else len(edges) / possible_edges
    return {
        "nodes": len(node_list),
        "edges": len(edges),
        "density": round(density, 4),
    }

