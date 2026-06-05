import pytest

from aurora.data import returns, sample_prices, sample_sectors
from aurora.graph import Edge, build_edges, correlation, correlation_matrix
from aurora.metrics import graph_summary, node_degrees, strongest_edges
from aurora.ui import edge_rows, node_rows


def test_correlation_handles_identity_inverse_and_constant_series() -> None:
    assert correlation([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]) == pytest.approx(1.0)
    assert correlation([1.0, 2.0, 3.0], [3.0, 2.0, 1.0]) == pytest.approx(-1.0)
    assert correlation([1.0, 1.0, 1.0], [3.0, 4.0, 5.0]) == 0.0


def test_build_edges_rejects_invalid_threshold() -> None:
    with pytest.raises(ValueError):
        build_edges({"A": [1, 2, 3], "B": [1, 2, 3]}, threshold=1.2)


def test_graph_summary_reports_density() -> None:
    summary = graph_summary(["A", "B", "C"], [Edge("A", "B", 0.8)])

    assert summary == {
        "nodes": 3,
        "edges": 1,
        "density": 0.3333,
        "max_degree": 1,
        "average_degree": 0.6667,
    }


def test_matrix_node_rows_and_edge_rows_are_dashboard_ready() -> None:
    prices = sample_prices()
    edges = build_edges(prices, threshold=0.6)
    sectors = sample_sectors()

    matrix = correlation_matrix(prices)
    nodes = node_rows(list(prices), sectors, edges)
    edge_table = edge_rows(strongest_edges(edges, limit=2))

    assert matrix["SPY"]["SPY"] == 1.0
    assert {row["sector"] for row in nodes} >= {"Index", "Semiconductors"}
    assert len(edge_table) == 2


def test_returns_and_degree_helpers_handle_boundaries() -> None:
    assert returns([100.0]) == []
    assert node_degrees(["A"], []) == {"A": 0}
    with pytest.raises(ValueError):
        strongest_edges([], limit=0)
