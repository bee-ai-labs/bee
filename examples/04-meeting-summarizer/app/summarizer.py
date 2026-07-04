"""Map-reduce meeting summarizer with structured action-item extraction.

Demonstrates two patterns at once:
  - map-reduce over long text (summarize chunks, then combine) to handle transcripts
    that don't fit comfortably in one prompt;
  - structured output (tool-enforced schema) to extract action items your code can use.

The LLM client is injected, so tests drive it with a fake (no API key or network).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from pydantic import BaseModel


# --------------------------------------------------------------------------- schema
class ActionItem(BaseModel):
    task: str
    owner: str = "unassigned"
    due: str | None = None


class ActionItems(BaseModel):
    items: list[ActionItem]


@dataclass
class MeetingSummary:
    summary: str
    action_items: list[ActionItem]


# --------------------------------------------------------------------------- chunking
def chunk_transcript(text: str, max_chars: int = 2000) -> list[str]:
    """Split a transcript into chunks on blank lines, packing up to max_chars."""
    blocks = [b.strip() for b in text.split("\n\n") if b.strip()]
    chunks: list[str] = []
    current = ""
    for block in blocks:
        if len(current) + len(block) + 2 <= max_chars:
            current = f"{current}\n\n{block}".strip()
        else:
            if current:
                chunks.append(current)
            current = block
    if current:
        chunks.append(current)
    return chunks


# --------------------------------------------------------------------------- protocol
class LLMClient(Protocol):
    @property
    def messages(self): ...  # pragma: no cover


# --------------------------------------------------------------------------- summarizer
@dataclass
class MeetingSummarizer:
    client: LLMClient
    model: str = "claude-sonnet-5"

    def _text(self, prompt: str, system: str, max_tokens: int = 500) -> str:
        resp = self.client.messages.create(
            model=self.model, max_tokens=max_tokens, system=system,
            messages=[{"role": "user", "content": prompt}],
        )
        return "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")

    # ---- map: summarize each chunk ----
    def summarize_chunk(self, chunk: str) -> str:
        return self._text(
            f"Summarize this part of a meeting transcript in 2-3 sentences:\n\n{chunk}",
            system="You summarize meeting transcripts concisely and factually.",
        )

    # ---- reduce: combine chunk summaries ----
    def combine(self, summaries: list[str]) -> str:
        joined = "\n".join(f"- {s}" for s in summaries)
        return self._text(
            f"Combine these partial summaries into one coherent meeting summary "
            f"(5-7 sentences):\n\n{joined}",
            system="You synthesize partial summaries into one clear summary.",
        )

    # ---- structured extraction: action items ----
    def extract_action_items(self, summary: str) -> list[ActionItem]:
        resp = self.client.messages.create(
            model=self.model, max_tokens=600,
            tools=[{
                "name": "record_action_items",
                "description": "Record the action items found in the meeting.",
                "input_schema": ActionItems.model_json_schema(),
            }],
            tool_choice={"type": "tool", "name": "record_action_items"},
            messages=[{"role": "user",
                       "content": f"Extract all action items from this meeting summary. "
                                  f"Include an owner and due date when stated.\n\n{summary}"}],
        )
        tool_use = next(b for b in resp.content if getattr(b, "type", None) == "tool_use")
        return ActionItems.model_validate(tool_use.input).items

    # ---- orchestration ----
    def run(self, transcript: str, max_chars: int = 2000) -> MeetingSummary:
        chunks = chunk_transcript(transcript, max_chars=max_chars)
        partials = [self.summarize_chunk(c) for c in chunks]           # map
        summary = self.combine(partials) if len(partials) > 1 else partials[0]  # reduce
        action_items = self.extract_action_items(summary)
        return MeetingSummary(summary=summary, action_items=action_items)
