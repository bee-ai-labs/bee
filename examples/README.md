# Examples 🏃

Self-contained, **runnable** AI projects. Each folder is an independent project with its own
dependencies, a `.env.example`, and tests — clone it, add an API key, and run it. No pseudo-code,
no "coming soon."

> [!NOTE]
> **The golden rule:** if it doesn't run, it doesn't merge. Every example is tested in
> [CI](../.github/workflows/examples-test.yml).

## The examples

| # | Example | What it teaches | Level |
|---|---------|-----------------|-------|
| 01 | [chatbot](01-chatbot/) | Streaming chat, conversation memory, cost tracking | 🟢 |
| 02 | [rag-document-qa](02-rag-document-qa/) | Chunking, embeddings, retrieval, cited answers | 🟡 |
| 03 | [research-agent](03-research-agent/) | Tool use, the agent loop, multi-step reasoning | 🔴 |

More are on the [roadmap](../ROADMAP.md) — and this is a great place to
[contribute](../CONTRIBUTING.md).

## How to run any example

Every example follows the same steps:

```bash
cd examples/01-chatbot
cp .env.example .env          # then add your API key to .env
uv sync                       # or: pip install -e .
python -m app                 # run it
```

Run the tests (they mock the LLM, so no API key or network needed):

```bash
uv run pytest                 # or: pytest
```

## The example contract

Every example — and every new one you contribute — has this shape:

```text
NN-example-name/
├── README.md          What it does, how to run, what you learn
├── pyproject.toml     Pinned dependencies
├── .env.example       Every required variable, documented
├── app/               The source code
│   ├── __init__.py
│   └── __main__.py    Entry point: `python -m app`
└── tests/             At least one test (mocks the LLM)
    └── test_app.py
```

## Contributing an example

1. Copy [`_TEMPLATE/`](_TEMPLATE/) to `examples/NN-your-example/`.
2. Fill in the code, README, and at least one test.
3. Make sure `python -m app` runs and `pytest` passes.
4. Open a PR. See [CONTRIBUTING.md](../CONTRIBUTING.md).

**Design principles for examples:**

- ✅ Runnable and tested (mock the LLM in tests — no live calls in CI).
- ✅ Handle a missing API key with a clear message, not a stack trace.
- ✅ Set `max_tokens`; keep default runs cheap.
- ✅ Small, focused, and heavily commented — these are for *learning*.
- ✅ Link back to the relevant [docs](../docs/) concepts.
