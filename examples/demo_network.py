"""Run a sample Aurora network summary."""

from __future__ import annotations

from aurora.data import sample_prices
from aurora.graph import build_edges
from aurora.metrics import graph_summary


if __name__ == "__main__":
    prices = sample_prices()
    edges = build_edges(prices, threshold=0.6)
    summary = graph_summary(prices.keys(), edges)
    for key, value in summary.items():
        print(f"{key}={value}")

