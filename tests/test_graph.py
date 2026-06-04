from aurora.data import sample_prices
from aurora.graph import build_edges


def test_build_edges_returns_thresholded_edges() -> None:
    edges = build_edges(sample_prices(), threshold=0.6)
    assert all(abs(edge.correlation) >= 0.6 for edge in edges)
