"""Graph metrics for Aurora."""

from __future__ import annotations

from collections.abc import Iterable

from .graph import Edge


def graph_summary(nodes: Iterable[str], edges: list[Edge]) -> dict[str, int | float]:
    """Return a small graph summary."""
    node_list = list(nodes)
    possible_edges = len(node_list) * (len(node_list) - 1) / 2
    density = 0.0 if possible_edges == 0 else len(edges) / possible_edges
    degrees = node_degrees(node_list, edges)
    return {
        "nodes": len(node_list),
        "edges": len(edges),
        "density": round(density, 4),
        "max_degree": max(degrees.values(), default=0),
        "average_degree": round(sum(degrees.values()) / len(node_list), 4) if node_list else 0.0,
    }


def node_degrees(nodes: Iterable[str], edges: list[Edge]) -> dict[str, int]:
    """Count thresholded relationships for each node."""
    counts = {node: 0 for node in nodes}
    for edge in edges:
        counts[edge.source] = counts.get(edge.source, 0) + 1
        counts[edge.target] = counts.get(edge.target, 0) + 1
    return counts


def strongest_edges(edges: list[Edge], limit: int = 5) -> list[Edge]:
    """Return the strongest absolute-correlation edges."""
    if limit < 1:
        raise ValueError("limit must be positive")
    return sorted(edges, key=lambda edge: abs(edge.correlation), reverse=True)[:limit]
