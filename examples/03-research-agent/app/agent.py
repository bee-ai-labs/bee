"""A minimal ReAct-style agent loop.

The LLM client and tools are injected, so tests can drive the loop with a scripted fake
client (no API key or network). See docs/agents/fundamentals.md for the theory.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Protocol

SYSTEM = (
    "You are a research agent. Break the question into steps and use the provided tools to "
    "gather facts and do calculations. When you have enough information, give a concise final "
    "answer without calling more tools."
)


class LLMClient(Protocol):
    @property
    def messages(self): ...  # pragma: no cover


@dataclass
class Step:
    """One tool invocation, recorded for transparency/debugging."""

    tool: str
    args: dict
    result: str


@dataclass
class AgentResult:
    answer: str
    steps: list[Step]
    stopped_early: bool


@dataclass
class Agent:
    client: LLMClient
    tools: list[dict]
    tool_impl: dict[str, Callable[..., str]]
    model: str = "claude-sonnet-5"
    max_steps: int = 6
    on_step: Callable[[Step], None] | None = None
    steps: list[Step] = field(default_factory=list)

    def run(self, goal: str) -> AgentResult:
        messages: list[dict] = [{"role": "user", "content": goal}]

        for _ in range(self.max_steps):
            resp = self.client.messages.create(
                model=self.model,
                max_tokens=800,
                system=SYSTEM,
                tools=self.tools,
                messages=messages,
            )
            messages.append({"role": "assistant", "content": resp.content})

            if resp.stop_reason != "tool_use":
                text = "".join(
                    b.text for b in resp.content if getattr(b, "type", None) == "text"
                )
                return AgentResult(answer=text, steps=self.steps, stopped_early=False)

            # Execute every tool the model requested this turn.
            tool_results = []
            for block in resp.content:
                if getattr(block, "type", None) != "tool_use":
                    continue
                result = self._execute(block.name, block.input)
                step = Step(tool=block.name, args=dict(block.input), result=result)
                self.steps.append(step)
                if self.on_step:
                    self.on_step(step)
                tool_results.append(
                    {"type": "tool_result", "tool_use_id": block.id, "content": result}
                )
            messages.append({"role": "user", "content": tool_results})

        return AgentResult(
            answer="Stopped: reached the step budget without a final answer.",
            steps=self.steps,
            stopped_early=True,
        )

    def _execute(self, name: str, args: dict) -> str:
        """Dispatch a tool call, returning errors as strings so the agent can recover."""
        fn = self.tool_impl.get(name)
        if fn is None:
            return f"ERROR: unknown tool '{name}'."
        try:
            return fn(**args)
        except Exception as exc:  # noqa: BLE001
            return f"ERROR: {exc}"
