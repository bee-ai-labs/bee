"""Tests for the agent loop and tools — scripted fake client, no network."""
from __future__ import annotations

from dataclasses import dataclass, field

from app import Agent, TOOL_IMPL, TOOLS
from app.tools import calculator, search


# ------------------------------------------------------------------ tool unit tests
def test_search_returns_canned_result():
    assert "Paris" in search("city of the Eiffel Tower")


def test_calculator_evaluates():
    assert calculator("2100000 * 0.15") == "315000.0"


def test_calculator_rejects_unsafe_input():
    assert calculator("__import__('os').system('ls')").startswith("ERROR")


# ------------------------------------------------------ scripted fake LLM client
@dataclass
class TextBlock:
    text: str
    type: str = "text"


@dataclass
class ToolUseBlock:
    name: str
    input: dict
    id: str = "tu_1"
    type: str = "tool_use"


@dataclass
class Resp:
    content: list
    stop_reason: str


class ScriptedMessages:
    """Returns a queued sequence of responses, one per create() call."""

    def __init__(self, responses: list[Resp]):
        self._responses = list(responses)
        self.calls: list[dict] = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return self._responses.pop(0)


class ScriptedClient:
    def __init__(self, responses):
        self.messages = ScriptedMessages(responses)


def test_agent_uses_tool_then_answers():
    # 1st turn: model asks to search. 2nd turn: model gives a final answer.
    responses = [
        Resp(content=[ToolUseBlock(name="search", input={"query": "Vega X manufacturer"})],
             stop_reason="tool_use"),
        Resp(content=[TextBlock("The Vega X is made by Orion Corp.")], stop_reason="end_turn"),
    ]
    agent = Agent(client=ScriptedClient(responses), tools=TOOLS, tool_impl=TOOL_IMPL)
    result = agent.run("Who makes the Vega X?")

    assert not result.stopped_early
    assert "Orion Corp" in result.answer
    assert len(result.steps) == 1
    assert result.steps[0].tool == "search"
    # The tool result must have been fed back to the model on the 2nd call.
    second_call_messages = agent.client.messages.calls[1]["messages"]
    assert any(m["role"] == "user" and isinstance(m["content"], list)
               for m in second_call_messages)


def test_agent_respects_step_budget():
    # Model always asks for a tool → the budget must stop it.
    always_tool = Resp(
        content=[ToolUseBlock(name="search", input={"query": "loop"})], stop_reason="tool_use"
    )
    agent = Agent(
        client=ScriptedClient([always_tool] * 10),
        tools=TOOLS, tool_impl=TOOL_IMPL, max_steps=3,
    )
    result = agent.run("never-ending question")
    assert result.stopped_early
    assert len(result.steps) == 3  # exactly the budget


def test_agent_handles_unknown_tool_gracefully():
    responses = [
        Resp(content=[ToolUseBlock(name="nonexistent", input={})], stop_reason="tool_use"),
        Resp(content=[TextBlock("done")], stop_reason="end_turn"),
    ]
    agent = Agent(client=ScriptedClient(responses), tools=TOOLS, tool_impl=TOOL_IMPL)
    result = agent.run("call a bad tool")
    assert result.steps[0].result.startswith("ERROR: unknown tool")
    assert result.answer == "done"
