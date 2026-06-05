"""UI helper structures for Aurora."""

from __future__ import annotations

from .graph import Edge
from .metrics import node_degrees


def disclaimer() -> str:
    """Return the dashboard disclaimer."""
    return "Educational sample dashboard. Not financial advice."


def edge_rows(edges: list[Edge]) -> list[dict[str, str | float]]:
    """Convert edges into dashboard table rows."""
    return [
        {
            "source": edge.source,
            "target": edge.target,
            "correlation": edge.correlation,
            "absolute_correlation": abs(edge.correlation),
        }
        for edge in edges
    ]


def node_rows(nodes: list[str], sectors: dict[str, str], edges: list[Edge]) -> list[dict[str, str | int]]:
    """Convert node metrics into dashboard table rows."""
    degrees = node_degrees(nodes, edges)
    return [
        {
            "symbol": node,
            "sector": sectors.get(node, "Unknown"),
            "degree": degrees[node],
        }
        for node in nodes
    ]
