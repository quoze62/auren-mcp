"""AUREN Risk MCP server.

Exposes the AUREN deterministic risk engine (POST /risk) as an MCP tool.
"""
from __future__ import annotations

import json
import os

import httpx
from mcp.server.fastmcp import FastMCP

AUREN_API_URL = os.environ.get("AUREN_API_URL", "https://auren-api-8yrq.onrender.com").rstrip("/")

mcp = FastMCP("auren-risk")


@mcp.tool()
async def auren_portfolio_risk(weights: dict[str, float]) -> str:
    """Compute deterministic risk metrics for a portfolio using AUREN.

    Args:
        weights: Mapping of ticker symbol to percentage weight,
            e.g. {"NVDA": 40, "AAPL": 30, "MSFT": 30}. Weights should sum to 100.

    Returns:
        JSON string with score (0-100), level, reasons, concentration,
        volatility, max_drawdown, sector_exposure and stress scenarios.
    """
    if not weights:
        raise ValueError("weights must be a non-empty mapping of ticker -> percent")
    async with httpx.AsyncClient(timeout=120.0) as client:
        resp = await client.post(f"{AUREN_API_URL}/risk", json={"weights": weights})
        resp.raise_for_status()
        return json.dumps(resp.json(), indent=2)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
