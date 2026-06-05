"""Sample market data for Aurora."""

from __future__ import annotations


def sample_prices() -> dict[str, list[float]]:
    """Return deterministic sample price series."""
    return {
        "SPY": [100, 101, 102, 101, 103, 104, 105],
        "QQQ": [100, 102, 103, 102, 105, 106, 108],
        "NVDA": [100, 104, 106, 105, 109, 112, 116],
        "AMD": [100, 103, 104, 103, 107, 109, 112],
        "XOM": [100, 99, 100, 101, 100, 102, 101],
        "GLD": [100, 100.5, 100.2, 101, 101.5, 101.2, 102],
    }


def sample_sectors() -> dict[str, str]:
    """Return deterministic sample sector labels."""
    return {
        "SPY": "Index",
        "QQQ": "Index",
        "NVDA": "Semiconductors",
        "AMD": "Semiconductors",
        "XOM": "Energy",
        "GLD": "Commodity",
    }


def returns(prices: list[float]) -> list[float]:
    """Compute simple returns."""
    if len(prices) < 2:
        return []
    return [(prices[index] / prices[index - 1]) - 1.0 for index in range(1, len(prices))]
