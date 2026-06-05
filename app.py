"""Streamlit entry point for Aurora."""

from __future__ import annotations

import json

try:
    import streamlit as st
except ImportError:  # pragma: no cover
    st = None

from aurora.data import sample_prices
from aurora.data import sample_sectors
from aurora.graph import build_edges, correlation_matrix
from aurora.metrics import graph_summary, strongest_edges
from aurora.ui import disclaimer, edge_rows, node_rows


def main() -> None:
    prices = sample_prices()
    sectors = sample_sectors()
    if st is None:
        edges = build_edges(prices, threshold=0.6)
        print(graph_summary(prices.keys(), edges))
        print(edge_rows(strongest_edges(edges, limit=3)))
        return

    st.set_page_config(page_title="Aurora Market Network Explorer", layout="wide")
    st.title("Aurora Market Network Explorer")
    st.caption(disclaimer())
    threshold = st.slider("Correlation threshold", min_value=0.0, max_value=1.0, value=0.6, step=0.05)
    edges = build_edges(prices, threshold=threshold)
    symbols = list(prices)
    summary = graph_summary(symbols, edges)

    metric_cols = st.columns(4)
    metric_cols[0].metric("Nodes", summary["nodes"])
    metric_cols[1].metric("Edges", summary["edges"])
    metric_cols[2].metric("Density", summary["density"])
    metric_cols[3].metric("Max degree", summary["max_degree"])

    st.subheader("Sample Universe")
    st.dataframe(node_rows(symbols, sectors, edges), use_container_width=True)

    st.subheader("Correlation Matrix")
    st.dataframe(correlation_matrix(prices), use_container_width=True)

    st.subheader("Thresholded Edges")
    st.dataframe(edge_rows(strongest_edges(edges, limit=len(edges) or 1)), use_container_width=True)

    st.download_button(
        "Download summary JSON",
        data=json.dumps(summary, indent=2),
        file_name="aurora_summary.json",
        mime="application/json",
    )


if __name__ == "__main__":
    main()
