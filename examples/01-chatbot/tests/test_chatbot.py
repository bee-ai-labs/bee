"""Tests for the chatbot — using a fake LLM client, so no API key or network is needed."""
from __future__ import annotations

from dataclasses import dataclass

from app import Chatbot


# --- A fake client mimicking the slice of the Anthropic SDK we use ---
@dataclass
class _Usage:
    input_tokens: int
    output_tokens: int


@dataclass
class _FinalMessage:
    usage: _Usage


class _FakeStream:
    def __init__(self, reply: str, in_tok: int, out_tok: int):
        self._reply = reply
        self._final = _FinalMessage(_Usage(in_tok, out_tok))

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    @property
    def text_stream(self):
        # Stream the reply in small chunks to mimic token streaming.
        for word in self._reply.split(" "):
            yield word + " "

    def get_final_message(self):
        return self._final


class _FakeMessages:
    def __init__(self, reply: str, in_tok: int, out_tok: int):
        self._reply, self._in, self._out = reply, in_tok, out_tok
        self.calls: list[dict] = []

    def stream(self, **kwargs):
        self.calls.append(kwargs)
        return _FakeStream(self._reply, self._in, self._out)


class FakeClient:
    def __init__(self, reply="hello there", in_tok=10, out_tok=5):
        self.messages = _FakeMessages(reply, in_tok, out_tok)


def test_send_returns_reply_and_usage():
    bot = Chatbot(client=FakeClient(reply="hi friend", in_tok=12, out_tok=3))
    turn = bot.send("hello")
    assert turn.reply.strip() == "hi friend"
    assert turn.input_tokens == 12
    assert turn.output_tokens == 3


def test_history_accumulates_for_multi_turn_context():
    bot = Chatbot(client=FakeClient())
    bot.send("first")
    bot.send("second")
    roles = [m["role"] for m in bot.history]
    # user, assistant, user, assistant
    assert roles == ["user", "assistant", "user", "assistant"]
    # The second call must have received the full prior history.
    second_call_messages = bot.client.messages.calls[1]["messages"]
    assert second_call_messages[0]["content"] == "first"


def test_on_chunk_receives_streamed_text():
    bot = Chatbot(client=FakeClient(reply="a b c"))
    received: list[str] = []
    bot.send("go", on_chunk=received.append)
    assert "".join(received).strip() == "a b c"


def test_cost_tracking_accumulates():
    bot = Chatbot(client=FakeClient(in_tok=1_000_000, out_tok=1_000_000), model="claude-sonnet-5")
    bot.send("x")
    # 1M input @ $3 + 1M output @ $15 = $18.00
    assert round(bot.session_cost_usd(), 2) == 18.00


def test_reset_clears_history_but_keeps_cost():
    bot = Chatbot(client=FakeClient(in_tok=100, out_tok=50))
    bot.send("hi")
    bot.reset()
    assert bot.history == []
    assert bot.total_input_tokens == 100  # cumulative stats survive reset
