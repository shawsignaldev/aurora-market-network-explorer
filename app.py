"""Streamlit entry point for Aurora."""

from __future__ import annotations

try:
    import streamlit as st
except ImportError:  # pragma: no cover
    st = None

from aurora.data import sample_prices
from aurora.graph import build_edges
from aurora.metrics import graph_summary


def main() -> None:
    prices = sample_prices()
    if st is None:
        edges = build_edges(prices, threshold=0.6)
        print(graph_summary(prices.keys(), edges))
        return

    st.set_page_config(page_title="Aurora Market Network Explorer", layout="wide")
    st.title("Aurora Market Network Explorer")
    st.caption("Educational sample dashboard. Not financial advice.")
    threshold = st.slider("Correlation threshold", min_value=0.0, max_value=1.0, value=0.6, step=0.05)
    edges = build_edges(prices, threshold=threshold)
    st.write("Sample universe:", ", ".join(prices.keys()))
    st.dataframe(edges)
    st.json(graph_summary(prices.keys(), edges))


if __name__ == "__main__":
    main()

