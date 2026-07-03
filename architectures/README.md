# Architectures 🏗️

Reference architectures for real AI systems — the diagrams, components, and trade-offs — plus
**Architecture Decision Records (ADRs)** that capture *why* a design was chosen.

> [!NOTE]
> This is the "how the pieces fit together" section. For the *concepts* behind the pieces, see
> [`docs/`](../docs/). For *runnable* implementations, see [`examples/`](../examples/).

## What lives here

| File | What it is |
|------|-----------|
| `NN-name.md` | A reference architecture: diagram + components + trade-offs + when to use |
| `adr/NNNN-title.md` | An Architecture Decision Record — one decision, its context, and consequences |

## Reference architectures

Each reference architecture answers: *what components do I need, how do they connect, and what
are the trade-offs?* — using a [Mermaid](https://mermaid.js.org/) diagram and prose.

- ✅ [RAG chatbot](rag-chatbot.md) — retrieval-augmented chat with citations
- `[WANTED]` Multi-tenant RAG (per-customer isolation) 🔴
- `[WANTED]` Agentic workflow with human-in-the-loop 🔴
- `[WANTED]` Real-time voice assistant pipeline 🔴
- `[WANTED]` Self-hosted inference with vLLM behind an API 🔴

## Architecture Decision Records

ADRs are short documents that record a single significant decision, so future contributors
understand the *why*, not just the *what*. We use the classic
[Michael Nygard format](https://github.com/joelparkerhenderson/architecture-decision-record).

- ✅ [ADR-0001: Provider-agnostic concepts, Anthropic-first code](adr/0001-provider-strategy.md)
- Add yours: copy the format from ADR-0001.

## Contributing an architecture

1. Start from a real problem, not a hypothetical.
2. Include a Mermaid diagram, the component list, and — crucially — the **trade-offs** and
   **when to use / when not to**.
3. Link to the relevant [concepts](../docs/) and any [example](../examples/) that implements it.

See [CONTRIBUTING.md](../CONTRIBUTING.md).
