# Bee Roadmap 🗺️

Bee grows in public. This roadmap shows where we are and where we're headed. It's a living
document — priorities shift as the community weighs in via
[Discussions](https://github.com/bee-ai-labs/bee/discussions) and the
[Project Board](PROJECT_BOARD.md).

> [!NOTE]
> **How to influence the roadmap:** upvote or comment on Discussions, open a content request
> issue, or claim a `[WANTED]` topic and write it. Community demand drives ordering.

## Legend

`✅ Done` · `🚧 In progress` · `📋 Planned` · `💭 Exploring`

---

## Milestone M0 — Foundation ✅

The scaffolding that makes Bee credible and contributable from day one.

- ✅ Repository structure & branding (🐝)
- ✅ README, dual license (CC-BY-4.0 + MIT)
- ✅ MkDocs Material documentation site
- ✅ Community files (Contributing, CoC, Security, Support, Governance)
- ✅ CI/CD: format, lint, spelling, link-check, docs build
- ✅ Issue/PR templates, labels, Dependabot, CODEOWNERS

## Milestone M1 — Flagship Knowledge 🚧

Deep, polished coverage of the four highest-value areas. These set the quality bar for every
future contribution.

- 🚧 **Concepts** — how LLMs work, transformers, tokenization, embeddings
- 🚧 **Prompting** — prompt engineering, system prompts, structured outputs, tool calling
- 🚧 **RAG** — chunking, vector databases, hybrid search, reranking, evaluation
- 🚧 **Agents** — fundamentals, planning, reflection, memory, multi-agent, MCP

## Milestone M2 — Runnable Example Fleet 📋

Self-contained, tested example projects that people can clone and ship from.

- 📋 `01-chatbot` — streaming chat with cost tracking
- 📋 `02-rag-document-qa` — cited answers over your documents
- 📋 `03-research-agent` — planning + tool use
- 📋 `04-code-assistant` — repo-aware coding helper
- 📋 `05-voice-assistant` — STT → LLM → TTS loop
- 📋 Example scaffolder script (`scripts/new-example`)

## Milestone M3 — Breadth 📋

Fill out the remaining knowledge sections to first-article depth, with `[WANTED]` markers for
the community.

- 📋 **Vision** — multimodal models, OCR, image analysis
- 📋 **Speech** — ASR (Whisper), TTS, diarization
- 📋 **Evaluation** — evals, benchmarks, LLM-as-judge, hallucination detection
- 📋 **Security** — prompt injection, jailbreaks, guardrails
- 📋 **Deployment** — Docker, Kubernetes, serving (vLLM/TGI), autoscaling
- 📋 **MLOps** — CI/CD for AI, observability, cost monitoring

## Milestone M4 — Interactive & Multimodal 💭

Make Bee something you *do*, not just read.

- 💭 Jupyter/Colab notebook companions for key articles
- 💭 Interactive diagrams and playgrounds
- 💭 Video walkthroughs for flagship tutorials
- 💭 Downloadable learning-path PDFs / certificates of completion

## Milestone M5 — Ecosystem & Scale 💭

- 💭 Translations (i18n) — starting with the most-requested languages
- 💭 "Bee Bytes" — a short newsletter of new content
- 💭 Contributor mentorship program (pair newcomers with reviewers)
- 💭 Annual "State of AI Engineering" community survey & report

---

## Guiding Principles

Every roadmap decision is checked against these:

1. **Depth over breadth, but never fake depth.** Better to have 10 excellent pages than 100
   thin ones. No placeholders.
2. **Everything runs.** Code examples are tested in CI.
3. **Vendor-neutral concepts.** Teach transferable ideas; use SDKs only for concreteness.
4. **Community-owned.** Structure the work so contributors can own whole sections.
5. **Beginner-friendly, expert-respected.** Tier content; never condescend, never gatekeep.

---

*Want to help ship the next milestone? Start with [CONTRIBUTING.md](CONTRIBUTING.md) and the
[good first issues](GOOD_FIRST_ISSUES.md).* 🐝
