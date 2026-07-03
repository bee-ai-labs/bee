# Benchmarks 📏

How AI systems are measured — standard benchmarks explained, their limitations, and **runnable
evaluation harnesses** you can adapt to your own system.

> [!NOTE]
> The most important benchmark is the one that reflects *your* use case. Public benchmarks are
> useful signals, but a small eval set built from your real inputs beats a leaderboard score
> every time. See [Evaluation](../docs/evaluation/index.md).

## Standard benchmarks (and what they actually measure)

| Benchmark | Measures | Watch out for |
|-----------|----------|---------------|
| [MMLU](https://arxiv.org/abs/2009.03300) | Broad knowledge across 57 subjects | Saturation; contamination in training data |
| [GSM8K](https://arxiv.org/abs/2110.14168) | Grade-school math word problems | Prompt/format sensitivity |
| [HumanEval](https://arxiv.org/abs/2107.03374) | Code generation (functional correctness) | Narrow; Python-only |
| [MT-Bench](https://arxiv.org/abs/2306.05685) | Multi-turn conversational quality (LLM-judged) | Judge bias |
| [MTEB](https://huggingface.co/spaces/mteb/leaderboard) | Embedding model quality | Task mix may not match yours |

> [!WARNING]
> **Benchmark contamination** is real — models may have seen benchmark data in training,
> inflating scores. Treat public numbers as rough signals, not ground truth.

## Evaluation harnesses

Reusable patterns for measuring *your* system — the practical counterpart to the theory in
[Evaluation](../docs/evaluation/index.md) and [Evaluating RAG](../docs/rag/evaluation.md).

- ✅ Retrieval metrics (recall@k, precision@k, MRR) — see the runnable code in
  [Evaluating RAG](../docs/rag/evaluation.md)
- ✅ LLM-as-judge faithfulness — see [Evaluating RAG](../docs/rag/evaluation.md)
- `[WANTED]` A packaged, reusable eval-harness module 🟡
- `[WANTED]` Regression-testing evals wired into CI 🟡

## `[WANTED]` contributions

- A minimal, runnable benchmark runner for a small open model
- Guides on interpreting benchmark results honestly
- Cost/latency benchmarking harness

## Contributing

Benchmarks must be **reproducible** and **honestly caveated** — state what they do *not* measure.
See [CONTRIBUTING.md](../CONTRIBUTING.md).
