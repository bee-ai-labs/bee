"""A small, testable streaming chatbot.

The LLM client is injected, so the conversation logic can be tested with a fake client
(no API key or network). See tests/test_chatbot.py.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Protocol

# Approximate prices in USD per 1M tokens. Update as pricing changes; this is for
# *illustration* — always confirm current prices with your provider.
PRICING: dict[str, tuple[float, float]] = {
    # model: (input_per_mtok, output_per_mtok)
    "claude-sonnet-5": (3.00, 15.00),
    "claude-haiku-4-5-20251001": (1.00, 5.00),
}
DEFAULT_MODEL = "claude-sonnet-5"


@dataclass
class Turn:
    """The result of one exchange."""

    reply: str
    input_tokens: int
    output_tokens: int


class LLMClient(Protocol):
    """The slice of the Anthropic SDK we depend on — lets tests supply a fake."""

    @property
    def messages(self): ...  # pragma: no cover - structural typing only


@dataclass
class Chatbot:
    """Holds conversation state and talks to an injected LLM client."""

    client: LLMClient
    model: str = DEFAULT_MODEL
    system: str | None = None
    max_tokens: int = 1024
    history: list[dict] = field(default_factory=list)
    total_input_tokens: int = 0
    total_output_tokens: int = 0

    def reset(self) -> None:
        """Clear the conversation (but keep cumulative cost stats)."""
        self.history.clear()

    def send(self, user_text: str, on_chunk: Callable[[str], None] | None = None) -> Turn:
        """Send a user message, stream the reply, update history and usage.

        `on_chunk` is called with each streamed text fragment (e.g. to print live).
        """
        self.history.append({"role": "user", "content": user_text})

        kwargs = dict(model=self.model, max_tokens=self.max_tokens, messages=self.history)
        if self.system:
            kwargs["system"] = self.system

        chunks: list[str] = []
        with self.client.messages.stream(**kwargs) as stream:
            for text in stream.text_stream:
                chunks.append(text)
                if on_chunk:
                    on_chunk(text)
            final = stream.get_final_message()

        reply = "".join(chunks)
        # `history` must include the assistant turn so the next call has full context.
        self.history.append({"role": "assistant", "content": reply})

        in_tok = final.usage.input_tokens
        out_tok = final.usage.output_tokens
        self.total_input_tokens += in_tok
        self.total_output_tokens += out_tok
        return Turn(reply=reply, input_tokens=in_tok, output_tokens=out_tok)

    def session_cost_usd(self) -> float:
        """Estimated cost of the session so far, from tracked token usage."""
        in_price, out_price = PRICING.get(self.model, (0.0, 0.0))
        return (
            self.total_input_tokens / 1_000_000 * in_price
            + self.total_output_tokens / 1_000_000 * out_price
        )
