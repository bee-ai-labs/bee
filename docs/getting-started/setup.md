---
tags: [Beginner]
---

# Setup & Prerequisites

> Get a clean Python environment and an API key so every example in Bee just works.

## Overview

You need three things: **Python 3.10+**, an **isolated environment** (so projects don't clash),
and an **API key**. This page sets all three up in about five minutes.

## Learning Objectives

After this page you will be able to:

- Create an isolated Python environment with `uv` (or `venv`).
- Store an API key safely using a `.env` file.
- Verify your setup with a one-line check.

## 1. Install Python 3.10+

Check what you have:

```bash
python3 --version
```

If it's older than 3.10 (or missing), install a current version from
[python.org](https://www.python.org/downloads/) or via your package manager
(`brew install python`, `apt install python3`).

## 2. Choose an environment tool

We recommend [**uv**](https://docs.astral.sh/uv/) — it's fast and manages both Python versions
and dependencies. Standard `venv` + `pip` works everywhere too.

=== "uv (recommended)"

    ```bash
    # Install uv (macOS/Linux)
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # In an example folder, uv handles the venv for you:
    cd examples/01-chatbot
    uv sync            # creates .venv and installs pinned deps
    uv run python -m app
    ```

=== "venv + pip"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate      # Windows: .venv\Scripts\activate
    pip install anthropic python-dotenv
    ```

!!! tip "Why isolate?"
    A virtual environment keeps each project's dependencies separate, so upgrading one project
    never breaks another. Never `pip install` into your system Python.

## 3. Get an API key

Bee's examples default to [Anthropic](https://console.anthropic.com/), but any provider works —
the concepts are the same.

1. Create an account with a provider (e.g. [Anthropic Console](https://console.anthropic.com/)).
2. Generate an API key.
3. **Never commit it.** Store it in a `.env` file (which is git-ignored):

```bash title=".env"
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Load it in Python with [`python-dotenv`](https://pypi.org/project/python-dotenv/):

```python
import os
from dotenv import load_dotenv

load_dotenv()                       # reads .env into environment variables
api_key = os.environ["ANTHROPIC_API_KEY"]
```

!!! warning "Protect your key"
    An API key is a password that can spend real money. Never paste it into code, commit it, or
    share it in an issue. If a key leaks, **revoke it immediately** in your provider's console.

## 4. Verify your setup

```bash
python3 -c "import anthropic, dotenv; print('✅ Ready to build with Bee')"
```

If that prints the success message, you're ready.

## Best Practices

- ✅ One virtual environment per project.
- ✅ Keep secrets in `.env`; commit a `.env.example` with placeholder values.
- ✅ Pin dependency versions so examples stay reproducible.

## Common Mistakes

- ❌ Installing packages globally — leads to version conflicts. Use a venv.
- ❌ Committing your `.env` — add it to `.gitignore` (Bee's already does).
- ❌ Hardcoding the API key in your script — load it from the environment.

## Exercises

1. Create a fresh environment and install the `anthropic` SDK.
2. Add your key to a `.env` file and load it in a script — print only the *length* of the key to
   confirm it loaded (never print the key itself).

## References

- [uv documentation](https://docs.astral.sh/uv/)
- [Python venv guide](https://docs.python.org/3/library/venv.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

Next: [**Your First LLM Call →**](first-llm-call.md)
