"""Tools the agent can call. Each has a JSON schema (for the model) and an implementation.

`search` returns canned results so the example is offline and deterministic. Replace its body
with a real search API to make the agent live.
"""
from __future__ import annotations

# --- Implementations -------------------------------------------------------------
_CANNED_SEARCH: dict[str, str] = {
    "city of the eiffel tower": "The Eiffel Tower is in Paris (population ~2,100,000).",
    "vega x manufacturer": "The Vega X is made by Orion Corp, founded in 1998.",
    "orion corp ceo": "Orion Corp's CEO is Jane Doe.",
}


def search(query: str) -> str:
    """Look up a short factual query (canned; swap for a real search API)."""
    return _CANNED_SEARCH.get(query.lower().strip(), "No results found.")


def calculator(expression: str) -> str:
    """Evaluate a simple arithmetic expression, safely (no names/builtins)."""
    allowed = set("0123456789+-*/(). eE")
    if not set(expression) <= allowed:
        return "ERROR: only numbers and + - * / ( ) are allowed."
    try:
        # Safe: the character allow-list above forbids names, calls, and attribute access.
        return str(eval(expression, {"__builtins__": {}}, {}))  # noqa: S307
    except Exception as exc:  # noqa: BLE001
        return f"ERROR: {exc}"


# --- Registry + schemas the model sees ------------------------------------------
TOOL_IMPL = {"search": search, "calculator": calculator}

TOOLS = [
    {
        "name": "search",
        "description": "Search for a short factual answer to a query. Use for facts you don't know.",
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string", "description": "A concise search query"}},
            "required": ["query"],
        },
    },
    {
        "name": "calculator",
        "description": "Evaluate an arithmetic expression, e.g. '2100000 * 0.15'.",
        "input_schema": {
            "type": "object",
            "properties": {"expression": {"type": "string"}},
            "required": ["expression"],
        },
    },
]
