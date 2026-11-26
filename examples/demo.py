"""Call the AUREN /risk endpoint directly to verify the integration works."""
import json
import os

import httpx

API = os.environ.get("AUREN_API_URL", "https://auren-api-8yrq.onrender.com").rstrip("/")

PORTFOLIO = {"NVDA": 40, "AAPL": 30, "MSFT": 30}


def main() -> None:
    print(f"POST {API}/risk  weights={PORTFOLIO}")
    r = httpx.post(f"{API}/risk", json={"weights": PORTFOLIO}, timeout=120.0)
    r.raise_for_status()
    data = r.json()
    print(json.dumps(data, indent=2)[:1200])
    print("
score =", data.get("score"), "| level =", data.get("level"))


if __name__ == "__main__":
    main()
