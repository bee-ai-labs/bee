"""CLI entry point: `python -m app`."""
from __future__ import annotations

import os
import sys

from .agent import Agent
from .tools import TOOL_IMPL, TOOLS


def main() -> None:
    from dotenv import load_dotenv

    load_dotenv()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("❌ ANTHROPIC_API_KEY is not set. Copy .env.example to .env and add your key.")

    from anthropic import Anthropic

    def show(step) -> None:
        print(f"  [tool] {step.tool}({step.args}) → {step.result}")

    agent = Agent(
        client=Anthropic(),
        tools=TOOLS,
        tool_impl=TOOL_IMPL,
        model=os.environ.get("BEE_MODEL", "claude-sonnet-5"),
        on_step=show,
    )

    print("🐝 Research Agent — ask a multi-step question ('exit' to quit).")
    while True:
        try:
            goal = input("goal › ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if goal.lower() in {"exit", "quit"}:
            break
        if not goal:
            continue
        result = agent.run(goal)
        print(f"answer › {result.answer}")


if __name__ == "__main__":
    main()
