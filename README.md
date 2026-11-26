# auren-mcp

An [MCP](https://modelcontextprotocol.io) server that exposes the **AUREN** deterministic portfolio risk engine (`POST /risk`) as a tool any MCP-compatible agent (Claude Desktop, Cursor, Continue, custom LangGraph/OpenAI agents) can call.

Built as a submission for the AUREN **API Integration Bounty ($25 USDC)**.

## Why MCP

The Vercel AI SDK integration covers Next.js/TypeScript apps. MCP covers the *agent runtime* side: Claude Desktop, Cursor, and any host that speaks the Model Context Protocol. One install gives every MCP host the ability to answer "how risky is this portfolio?" with audited, deterministic numbers instead of a hallucinated guess.

## Install

```bash
pip install "mcp[cli]" httpx
```

## Run

```bash
python -m auren_mcp.server
```

## Wire into Claude Desktop

`~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "auren-risk": {
      "command": "python",
      "args": ["-m", "auren_mcp.server"],
      "env": { "AUREN_API_URL": "https://auren-api-8yrq.onrender.com" }
    }
  }
}
```

## Tool

`auren_portfolio_risk(weights: dict[str, float]) -> str`

```
weights: {"NVDA": 40, "AAPL": 30, "MSFT": 30}   # percentages
```

Returns the full AUREN JSON: `score`, `level`, `reasons`, `concentration`, `volatility`, `max_drawdown`, `sector_exposure`, `stress`.

## Verify without an MCP host

```bash
python examples/demo.py
```

Prints the live AUREN response for a sample portfolio, proving the integration calls the real endpoint.

## License

MIT
