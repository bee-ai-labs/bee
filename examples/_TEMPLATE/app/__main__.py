"""Entry point so the example runs with `python -m app`.

Replace this with your example. Keep the shape:
  - load config/env
  - fail clearly if the API key is missing
  - do the thing, cheaply (set max_tokens)
"""
from __future__ import annotations

import os
import sys


def main() -> None:
    from dotenv import load_dotenv

    load_dotenv()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("❌ ANTHROPIC_API_KEY is not set. Copy .env.example to .env and add your key.")

    print("Replace this with your example. See app/__main__.py.")


if __name__ == "__main__":
    main()
