# Contributing to Bee

Bee is built by its community — and that includes you. This page is the quick version; the full
guide lives in [**CONTRIBUTING.md**](https://github.com/bee-ai-labs/bee/blob/main/CONTRIBUTING.md).

!!! tip "You don't need to be an expert"
    Some of the most valuable contributions come from learners who noticed something confusing.
    If it tripped you up, it's tripping up others.

## Ways to help

<div class="grid cards" markdown>

- :material-pencil:{ .lg .middle } **Fix & improve**

    ---

    Typos, broken links, wrong facts, clearer wording. Small fixes matter.

- :material-chart-timeline:{ .lg .middle } **Add a diagram**

    ---

    Turn a wall of text into a Mermaid diagram. Instantly more useful.

- :material-file-document-plus:{ .lg .middle } **Write content**

    ---

    Fill a `[WANTED]` topic or add a "Common Mistake" from your own experience.

- :material-language-python:{ .lg .middle } **Add an example**

    ---

    A runnable, tested project others can learn from and build on.

</div>

## The content contract

Every topic page follows the same skeleton so readers always know what to expect:

> **Overview** → **Learning Objectives** → **Theory** → **Practical Example** →
> **Best Practices** → **Common Mistakes** → **Exercises** → **References**

Tag difficulty honestly in the front matter:

```yaml
---
tags: [Beginner]   # or Intermediate / Advanced
---
```

## Your first contribution

```bash
git clone https://github.com/<you>/bee.git && cd bee
git checkout -b docs/my-improvement
mkdocs serve          # preview at http://127.0.0.1:8000
# ...make your change...
git commit -m "docs(concepts): clarify embeddings intro"
git push origin docs/my-improvement
# open a PR — CI checks format, spelling, and links for you
```

## Find something to do

- [Good first issues](https://github.com/bee-ai-labs/bee/labels/good%20first%20issue)
- [Help wanted](https://github.com/bee-ai-labs/bee/labels/help%20wanted)
- Search the repo for `[WANTED]` — topics we'd love someone to write

## The quality bar

Bee holds every contribution to a simple standard:

- ✅ **No placeholders** — every page is finished and useful.
- ✅ **Everything runs** — code examples are tested in CI.
- ✅ **Explain the why** — teach understanding, not just steps.
- ✅ **Be kind** — see the [Code of Conduct](https://github.com/bee-ai-labs/bee/blob/main/CODE_OF_CONDUCT.md).

---

Ready? Read the [**full Contributing guide**](https://github.com/bee-ai-labs/bee/blob/main/CONTRIBUTING.md)
and open your first PR. Welcome to the hive. 🐝
