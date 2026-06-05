# Network Methodology

## Method

Aurora converts asset returns into a correlation matrix and then into a thresholded graph. Nodes represent assets. Edges represent correlations above the selected threshold.

## Interpretation

| Network Feature | Possible Meaning |
| --- | --- |
| Dense cluster | Assets moving together under current window assumptions |
| Isolated node | Asset behaving differently from the selected universe |
| High-degree node | Potential concentration or broad market sensitivity |
| Threshold break | Relationship is not robust under stricter filtering |

## Review Cautions

Correlation is window-dependent and does not imply causation. Sector labels, market regime, liquidity, and event timing should be reviewed before drawing conclusions from a network view.

## Next Enhancements

- Rolling-window comparison
- Sector-aware coloring
- Exportable graph metrics
- Stress-window examples using public data
