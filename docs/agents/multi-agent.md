---
tags: [Advanced]
---

# Multi-Agent Systems

> Sometimes one agent isn't enough — you split work across several specialized agents that
> coordinate. Powerful for complex tasks, but easy to over-engineer. Here's how to do it well.

## Overview

A **multi-agent system** decomposes a problem across multiple agents, each with its own role,
tools, and prompt, coordinating to reach a goal. Think of it as moving from one generalist to a
*team* of specialists with a manager. This can improve quality on complex, parallelizable tasks —
but it multiplies cost, latency, and failure surface. The art is knowing when the team beats the
soloist.

## Learning Objectives

By the end of this page you will be able to:

- Recognize when multiple agents help vs. when one agent (or none) is better.
- Apply the main coordination patterns (orchestrator–worker, pipeline, debate).
- Implement a simple orchestrator–worker system.
- Anticipate the failure modes of multi-agent designs.

## Theory

### When multiple agents actually help

> [!IMPORTANT]
> **Start with one agent.** Add more only when a single agent genuinely struggles — usually
> because the task has *distinct sub-skills* or *parallelizable* parts. Multiple agents add real
> cost and complexity; make them earn it.

| Multi-agent helps when… | One agent is better when… |
|---|---|
| Subtasks need different expertise/tools | The task is cohesive and sequential |
| Parts can run in parallel | Latency and cost are tight |
| You want independent review/critique | Coordination overhead exceeds the benefit |

### Coordination patterns

=== "Orchestrator–Worker"

    A lead agent decomposes the goal, delegates subtasks to workers, and synthesizes their
    results. The most common and generally useful pattern.

    ```mermaid
    flowchart TB
        O[Orchestrator] --> W1[Worker: research]
        O --> W2[Worker: analysis]
        O --> W3[Worker: writing]
        W1 --> O2[Orchestrator<br/>synthesizes]
        W2 --> O2
        W3 --> O2
        O2 --> R[Result]
    ```

=== "Pipeline"

    Agents form an assembly line: each transforms the output of the previous. Good when stages
    are clear and ordered (draft → edit → fact-check).

    ```mermaid
    flowchart LR
        A[Draft agent] --> B[Editor agent] --> C[Fact-check agent] --> R[Result]
    ```

=== "Debate / Review"

    Agents critique each other's work to improve quality or reduce errors — e.g. a "generator"
    and a "critic," or several agents voting.

    ```mermaid
    flowchart LR
        G[Generator] --> C[Critic]
        C -->|feedback| G
        C -->|approved| R[Result]
    ```

### The coordination tax

Every hand-off is a chance to lose information, add latency, and add cost. Agents communicate in
natural language, which is lossy. More agents ≠ more intelligence — often it's just more ways to
go wrong. Measure whether the multi-agent version actually beats a good single agent on your
[evals](../evaluation/index.md).

## Practical Example: orchestrator–worker

A minimal system where an orchestrator delegates to specialized workers and synthesizes:

```python title="multi_agent.py"
from anthropic import Anthropic

client = Anthropic()

def agent(system: str, task: str, max_tokens: int = 600) -> str:
    resp = client.messages.create(
        model="claude-sonnet-5", max_tokens=max_tokens,
        system=system, messages=[{"role": "user", "content": task}],
    )
    return "".join(b.text for b in resp.content if b.type == "text")

# --- Specialized workers ---
def researcher(topic: str) -> str:
    return agent("You are a researcher. List key facts as concise bullets.",
                 f"Gather key facts about: {topic}")

def analyst(facts: str) -> str:
    return agent("You are an analyst. Identify the 3 most important insights.",
                 f"Analyze these facts and extract insights:\n{facts}")

def writer(insights: str) -> str:
    return agent("You are a writer. Produce a tight 1-paragraph summary.",
                 f"Write a summary based on these insights:\n{insights}")

# --- Orchestrator: a fixed pipeline here; a real orchestrator could plan dynamically ---
def run(topic: str) -> str:
    facts = researcher(topic)
    insights = analyst(facts)
    return writer(insights)

print(run("the impact of vector databases on search"))
```

This uses a fixed pipeline for clarity. A dynamic orchestrator would itself be an
[agent](fundamentals.md) that decides *which* workers to call and *when*, using them as tools.

!!! tip "Workers as tools"
    A clean way to build orchestrator–worker: expose each worker agent as a
    [tool](../prompting/function-calling.md) the orchestrator can call. The orchestrator's agent
    loop then naturally decides how to delegate.

## Frameworks

Multi-agent frameworks handle orchestration, messaging, and state for you:

- **LangGraph** — model agents as nodes in a graph with explicit control flow (great for
  reliability and cycles).
- **CrewAI** — define agents by role and let them collaborate on tasks.
- **AutoGen**, **OpenAI Agents SDK**, and others.

Learn the patterns here first; a framework then just saves you plumbing. Framework deep-dives are
`[WANTED]` — [contribute one](../contributing/index.md)!

## Best Practices

- ✅ Default to one agent; introduce more only when evals show it helps.
- ✅ Give each agent a narrow role, clear inputs/outputs, and only the tools it needs.
- ✅ Keep hand-offs structured to reduce information loss.
- ✅ Cap total steps/cost across the *whole* system, not just per agent.
- ✅ Compare against a strong single-agent baseline.

## Common Mistakes

- ❌ Reaching for multi-agent when a single well-prompted agent would do.
- ❌ Vague roles that overlap, so agents duplicate or contradict work.
- ❌ Unbounded delegation → runaway cost and latency.
- ❌ Lossy natural-language hand-offs dropping key details.
- ❌ Never benchmarking against one agent — assuming "more agents = better."

## Exercises

1. Run the pipeline example, then convert it to an orchestrator that calls workers *as tools* and
   decides the order itself.
2. Add a "critic" agent that reviews the writer's summary and requests one revision. Does quality
   improve enough to justify the extra call?
3. Benchmark the multi-agent version against a single agent doing the whole task. Which wins on
   quality, cost, and latency?

## References

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [LangGraph](https://langchain-ai.github.io/langgraph/) · [CrewAI](https://docs.crewai.com/)
- Bee: [Agent Fundamentals](fundamentals.md) · [Evaluation](../evaluation/index.md)
