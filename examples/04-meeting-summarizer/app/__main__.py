"""CLI entry point: `python -m app`. Summarizes data/sample_transcript.txt."""
from __future__ import annotations

import os
import sys
from pathlib import Path

from .summarizer import MeetingSummarizer

TRANSCRIPT = Path(__file__).resolve().parent.parent / "data" / "sample_transcript.txt"


def main() -> None:
    from dotenv import load_dotenv

    load_dotenv()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("❌ ANTHROPIC_API_KEY is not set. Copy .env.example to .env and add your key.")

    from anthropic import Anthropic

    summarizer = MeetingSummarizer(
        client=Anthropic(),
        model=os.environ.get("BEE_MODEL", "claude-sonnet-5"),
    )

    result = summarizer.run(TRANSCRIPT.read_text(encoding="utf-8"))

    print("=== SUMMARY ===")
    print(result.summary)
    print("\n=== ACTION ITEMS ===")
    if not result.action_items:
        print("(none found)")
    for i, item in enumerate(result.action_items, 1):
        due = f" (due {item.due})" if item.due else ""
        print(f"{i}. {item.task} — {item.owner}{due}")


if __name__ == "__main__":
    main()
