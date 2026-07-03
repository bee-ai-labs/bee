# FAQ

Common questions about Bee. For questions about *AI engineering itself*, check the relevant
section or ask in [Discussions](https://github.com/bee-ai-labs/bee/discussions).

## About the project

??? question "Is Bee affiliated with any AI company?"
    No. Bee is an independent, community-driven, open-source project. Examples use vendor SDKs,
    but the *concepts* are vendor-neutral.

??? question "Why 'Bee'?"
    A hive is a community that builds something bigger than any individual — exactly what this
    repository is. Plus, knowledge is the honey. 🍯

??? question "Is Bee free?"
    Yes. Content is [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) and code is MIT.
    Use it in your courses, blogs, and projects — just give credit.

## Using the content

??? question "Which LLM provider do the examples use?"
    Concepts are provider-agnostic. Code defaults to the Anthropic SDK for concreteness, with
    notes on adapting to OpenAI, Google, Ollama, and others. Most examples run against any
    provider with minor changes.

??? question "Do I need a GPU?"
    No. Almost everything uses hosted APIs. The few local-model sections say so explicitly and
    offer CPU-friendly alternatives.

??? question "Will the code examples go stale as APIs change?"
    We fight this two ways: each example pins its dependencies, and CI runs example tests. When a
    provider makes a breaking change, it surfaces as a failing check and gets fixed. Found one
    that's broken? [Open an issue](https://github.com/bee-ai-labs/bee/issues/new/choose).

??? question "How much will it cost me to run the examples?"
    Cents, usually. Examples use small models and short prompts by default, and always set
    `max_tokens`. Each example's README notes anything unusual.

## Learning with Bee

??? question "I'm a complete beginner. Where do I start?"
    [Getting Started](getting-started/index.md), then the
    [AI Engineer — Fundamentals](learning-paths/index.md) path. Don't read randomly — follow a
    path.

??? question "I'm experienced. Can I skip around?"
    Absolutely. Jump straight to [RAG](rag/index.md), [Agents](agents/index.md), or any topic.
    Difficulty tags (🟢🟡🔴) tell you what a page assumes.

??? question "How is this different from a framework's docs?"
    Framework docs assume you already know the concepts and want you to use *their* tool. Bee
    teaches the concepts first and stays vendor-neutral, so the understanding transfers no matter
    what you build with.

## Contributing

??? question "I found a mistake. What do I do?"
    [Open an issue](https://github.com/bee-ai-labs/bee/issues/new/choose) — or fix it and open a PR!
    See [Contributing](contributing/index.md).

??? question "Can I add content about a topic that isn't here yet?"
    Yes, please! Check for a `[WANTED]` marker in the relevant section, claim it, and use the
    templates. See [CONTRIBUTING.md](https://github.com/bee-ai-labs/bee/blob/main/CONTRIBUTING.md).

??? question "How do I get credited?"
    Every merged contribution earns you a spot via the
    [All Contributors](https://allcontributors.org/) spec — docs, code, design, and ideas all
    count.

---

!!! note "Didn't find your answer?"
    Ask in [Discussions](https://github.com/bee-ai-labs/bee/discussions) or read
    [SUPPORT.md](https://github.com/bee-ai-labs/bee/blob/main/SUPPORT.md).
