"""Tests for the meeting summarizer — fake client returns text for summaries and a
scripted tool call for action items. No API key or network needed."""
from __future__ import annotations

from dataclasses import dataclass

from app import MeetingSummarizer, chunk_transcript


# ------------------------------------------------------------------ unit: chunking
def test_chunking_splits_long_transcript():
    text = "\n\n".join(f"[00:{i:02d}] Speaker: line number {i} with some words." for i in range(40))
    chunks = chunk_transcript(text, max_chars=200)
    assert len(chunks) > 1
    assert all(len(c) <= 200 + 100 for c in chunks)  # small slack for block boundaries


def test_single_short_transcript_is_one_chunk():
    assert len(chunk_transcript("Just a short line.", max_chars=2000)) == 1


# ------------------------------------------------------------------ fake LLM client
@dataclass
class TextBlock:
    text: str
    type: str = "text"


@dataclass
class ToolUseBlock:
    input: dict
    name: str = "record_action_items"
    id: str = "tu_1"
    type: str = "tool_use"


@dataclass
class Resp:
    content: list


class FakeMessages:
    def __init__(self, action_items):
        self._action_items = action_items
        self.text_calls = 0
        self.tool_calls = 0

    def create(self, **kwargs):
        if "tools" in kwargs:                      # the action-item extraction call
            self.tool_calls += 1
            return Resp(content=[ToolUseBlock(input={"items": self._action_items})])
        self.text_calls += 1                       # a summary (map or reduce) call
        return Resp(content=[TextBlock("A concise summary sentence.")])


class FakeClient:
    def __init__(self, action_items=None):
        self.messages = FakeMessages(action_items or [])


TRANSCRIPT = "\n\n".join(f"[00:{i:02d}] Alice: point number {i}." for i in range(30))


def test_run_returns_summary_and_action_items():
    items = [
        {"task": "Investigate upload crash", "owner": "Bob", "due": "Friday"},
        {"task": "Update getting-started guide", "owner": "Carol", "due": "Wednesday"},
    ]
    summarizer = MeetingSummarizer(client=FakeClient(action_items=items))
    result = summarizer.run(TRANSCRIPT)

    assert isinstance(result.summary, str) and result.summary
    assert len(result.action_items) == 2
    assert result.action_items[0].owner == "Bob"
    assert result.action_items[0].due == "Friday"


def test_action_item_defaults_when_owner_missing():
    items = [{"task": "Follow up on pricing"}]         # no owner/due
    summarizer = MeetingSummarizer(client=FakeClient(action_items=items))
    result = summarizer.run("Short transcript.")
    assert result.action_items[0].owner == "unassigned"
    assert result.action_items[0].due is None


def test_map_reduce_makes_multiple_summary_calls_for_long_input():
    summarizer = MeetingSummarizer(client=FakeClient())
    summarizer.run(TRANSCRIPT, max_chars=200)      # small chunks → force multiple map calls
    # Several chunk summaries (map) + 1 combine (reduce).
    assert summarizer.client.messages.text_calls >= 2
    assert summarizer.client.messages.tool_calls == 1
