# Good First Issues 🌱

New to Bee — or to open source? **Start here.** This page explains how to find beginner-friendly
work and turn your first contribution into a merged PR.

> [!TIP]
> You don't need to be an AI expert. Fixing a confusing sentence, adding a diagram, or testing
> whether an example runs are all genuinely valuable — and exactly how most contributors start.

## 🔎 Find something to work on

1. **Browse the [`good first issue`](https://github.com/bee-ai-labs/bee/labels/good%20first%20issue)
   label.** These are scoped, well-described, and mentor-friendly.
2. **Look for [`help wanted`](https://github.com/bee-ai-labs/bee/labels/help%20wanted).** Slightly
   bigger, still welcoming.
3. **Search the repo for `[WANTED]`.** Section READMEs list topics we'd love someone to write —
   claim one by opening an issue.

## 🍯 Types of great first contributions

| Type | Example | Skill needed |
|------|---------|--------------|
| ✍️ **Typo / grammar fix** | Fix a sentence in a concept page | Reading English |
| 🔗 **Broken link fix** | CI flagged a dead link; repoint it | Basic Git |
| 🎨 **Add a diagram** | Turn a wall of text into a Mermaid flowchart | Mermaid basics |
| ❌ **Add a "Common Mistake"** | Share a footgun you hit | Your own experience |
| 🧪 **Test an example** | Clone it, run it, report or fix what breaks | Running Python |
| 📝 **Write a short concept** | Fill a `[WANTED]` gap | Topic knowledge |
| 📚 **Add a reference** | Link an authoritative source to a page | Research |

## 🪜 Your first PR, step by step

```bash
# 1. Comment on the issue: "I'd like to work on this!" (avoids duplicate effort)
# 2. Fork and clone
git clone https://github.com/<you>/bee.git && cd bee
# 3. Branch
git checkout -b docs/fix-embeddings-typo
# 4. Make your change
# 5. (Optional) preview
mkdocs serve
# 6. Commit with a conventional message
git commit -m "docs(concepts): fix typo in embeddings intro"
# 7. Push and open a PR — fill in the template
git push origin docs/fix-embeddings-typo
```

Then relax — CI checks formatting/spelling/links automatically, and a maintainer will give you
kind, specific feedback.

## 🐝 The unwritten rules (that we're writing down)

- **It's okay to ask.** Stuck on setup? Comment on the issue or ask in
  [Discussions](https://github.com/bee-ai-labs/bee/discussions). No question is too basic.
- **Small is beautiful.** A one-line fix is a real, welcome contribution.
- **Claim before you build** on anything non-trivial, so two people don't do the same work.
- **Done > perfect.** Open a draft PR early; we'll help you get it over the line.

## 🏅 What happens after you merge

- You're added to the contributors list (we use
  [All Contributors](https://allcontributors.org/) — docs, code, design, and ideas all count).
- You'll probably find the second contribution easier than the first. 😉
- If you keep contributing thoughtfully, you may be invited to become a **reviewer** (see
  [GOVERNANCE.md](GOVERNANCE.md)).

---

**Maintainers:** when filing a good first issue, include: the goal, the specific file(s), a hint
at the approach, and the "definition of done." A great issue is half the mentorship.

Welcome to the hive. We're glad you're here. 💛
