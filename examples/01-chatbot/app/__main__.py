"""CLI entry point: `python -m app`."""
from __future__ import annotations

import os
import sys

from . import DEFAULT_MODEL, Chatbot


def main() -> None:
    from dotenv import load_dotenv

    load_dotenv()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("❌ ANTHROPIC_API_KEY is not set. Copy .env.example to .env and add your key.")

    from anthropic import Anthropic

    model = os.environ.get("BEE_MODEL", DEFAULT_MODEL)
    bot = Chatbot(client=Anthropic(), model=model)

    print("🐝 Bee Chatbot — type 'exit' to quit, 'reset' to clear history.")
    while True:
        try:
            user = input("you › ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if user.lower() in {"exit", "quit"}:
            break
        if user.lower() == "reset":
            bot.reset()
            print("(history cleared)")
            continue
        if not user:
            continue

        print("bot › ", end="", flush=True)
        turn = bot.send(user, on_chunk=lambda t: print(t, end="", flush=True))
        print(
            f"\n      [turn: {turn.input_tokens} in + {turn.output_tokens} out tokens · "
            f"session: {bot.total_input_tokens + bot.total_output_tokens} tokens · "
            f"~${bot.session_cost_usd():.4f}]"
        )

    print(f"\n👋 Session total: ~${bot.session_cost_usd():.4f}. Bye!")


if __name__ == "__main__":
    main()
