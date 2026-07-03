# Learning Paths 🗺️

A pile of articles isn't a curriculum. **Learning paths sequence Bee's content** so each concept
builds on the one before it. Pick the path that matches where you are — and where you want to go.

!!! tip "How to use a path"
    Follow it top to bottom. Each step links to a Bee page. Do the exercises — they're where the
    learning sticks. Paths reference content across the whole hive, including sections still
    being written (marked 🚧); those links light up as content lands.

## Choose your path

<div class="grid cards" markdown>

- 🟢 **AI Engineer — Fundamentals**

    *You can code, but LLMs are new to you.* Build a correct mental model of how these systems
    actually work.

- 🟡 **Building with LLMs**

    *You've made API calls.* Turn them into reliable features: structured output, tools, and
    good prompts.

- 🟡 **RAG Specialist**

    *You need models to use your data.* Master retrieval end-to-end.

- 🔴 **Agent Engineer**

    *You want autonomous, tool-using systems.* Planning, memory, and multi-agent design.

- 🔴 **Production & MLOps**

    *You need to ship.* Evaluation, safety, deployment, and monitoring.

</div>

---

## 🟢 Path 1 — AI Engineer: Fundamentals

**Goal:** understand what an LLM is doing well enough to reason about its behavior and cost.

1. [Setup & Prerequisites](../getting-started/setup.md)
2. [Your First LLM Call](../getting-started/first-llm-call.md)
3. [How LLMs Work](../concepts/how-llms-work.md)
4. [Tokenization](../concepts/tokenization.md) — why the model "sees" tokens, not characters
5. [The Transformer](../concepts/transformers.md) — attention, intuitively
6. [Embeddings](../concepts/embeddings.md) — turning meaning into numbers
7. [Prompt Engineering](../prompting/prompt-engineering.md) — your first real skill

**You'll be able to:** explain next-token prediction, estimate cost, and write clear prompts.

---

## 🟡 Path 2 — Building with LLMs

**Goal:** ship reliable LLM features, not demos.

1. [Prompt Engineering](../prompting/prompt-engineering.md)
2. [System Prompts](../prompting/system-prompts.md)
3. [Structured Outputs](../prompting/structured-outputs.md) — get JSON you can trust
4. [Function & Tool Calling](../prompting/function-calling.md) — let the model *do* things
5. [Evaluation](../evaluation/index.md) 🚧 — know if your changes help or hurt
6. [Security](../security/index.md) 🚧 — prompt injection and guardrails

**You'll be able to:** build a feature with validated output, tool use, and basic evals.

---

## 🟡 Path 3 — RAG Specialist

**Goal:** make a model answer accurately from *your* documents, with citations.

1. [Embeddings](../concepts/embeddings.md)
2. [RAG Overview](../rag/index.md)
3. [Chunking](../rag/chunking.md) — the single biggest lever on RAG quality
4. [Vector Databases](../rag/vector-databases.md)
5. [Hybrid Search & Reranking](../rag/hybrid-search-reranking.md)
6. [Evaluating RAG](../rag/evaluation.md)

**You'll be able to:** design, build, and evaluate a production RAG pipeline.

---

## 🔴 Path 4 — Agent Engineer

**Goal:** build systems that plan, use tools, and act over multiple steps.

1. [Function & Tool Calling](../prompting/function-calling.md)
2. [Agent Fundamentals](../agents/fundamentals.md)
3. [Memory](../agents/memory.md)
4. [Multi-Agent Systems](../agents/multi-agent.md)
5. [Model Context Protocol (MCP)](../agents/mcp.md)
6. [Evaluation](../evaluation/index.md) 🚧 — evaluating non-deterministic agents

**You'll be able to:** design an agent loop, give it memory and tools, and know its failure modes.

---

## 🔴 Path 5 — Production & MLOps

**Goal:** take an AI feature from laptop to reliable, observable production.

1. [Evaluation](../evaluation/index.md) 🚧
2. [Security](../security/index.md) 🚧
3. [Deployment](../deployment/index.md) 🚧 — Docker, serving, scaling
4. [MLOps](../mlops/index.md) 🚧 — CI/CD, observability, cost monitoring

**You'll be able to:** ship an AI service with tests, guardrails, monitoring, and cost controls.

---

!!! note "Want a path we don't have yet?"
    [Request one](https://github.com/bee-ai-labs/bee/issues/new/choose) or
    [design it yourself](../contributing/index.md) — learning paths are one of the most valuable
    things you can contribute.
