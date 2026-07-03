# Templates 📦

Copy-paste **starters** for common AI services — production-shaped skeletons you clone and fill
in, rather than tutorials you read.

> [!NOTE]
> **Templates vs. Examples.** [Examples](../examples/) *teach* a concept end-to-end.
> **Templates** are minimal, opinionated *starting points* for your own project. Examples are for
> learning; templates are for building.

## Available templates

- ✅ [`fastapi-llm-service/`](fastapi-llm-service/) — a streaming LLM API with FastAPI (SSE,
  config, health check, error handling)
- `[WANTED]` `rag-service/` — FastAPI + vector DB retrieval endpoint 🟡
- `[WANTED]` `agent-worker/` — background agent loop with a queue 🔴
- `[WANTED]` `mcp-server/` — a starter Model Context Protocol server 🔴

## How to use a template

```bash
cp -r templates/fastapi-llm-service my-new-service
cd my-new-service
# follow the template's own README
```

## Contributing a template

A good template is **minimal but complete**: it runs, has config and error handling, and doesn't
bake in choices the user should make. Include a README with setup steps. See
[CONTRIBUTING.md](../CONTRIBUTING.md).
