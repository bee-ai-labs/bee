# Datasets 📊

Curated **pointers** to high-quality datasets for learning and building AI systems — for
fine-tuning, evaluation, RAG demos, and experimentation.

> [!IMPORTANT]
> Bee does **not** host large datasets in this repo. This is a *curated index* with links,
> licenses, and usage notes. Always check each dataset's license and terms before use, and never
> commit large data files (see [`.gitignore`](../.gitignore)).

## How entries are organized

Each entry lists: what it is, size, license, and what it's good for in an AI-engineering context.

## Instruction / chat data (for fine-tuning & prompting practice)

| Dataset | Size | License | Good for |
|---------|------|---------|----------|
| [Dolly 15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k) | 15k | CC-BY-SA-3.0 | Instruction-tuning basics |
| [OpenAssistant (OASST)](https://huggingface.co/datasets/OpenAssistant/oasst1) | ~161k | Apache-2.0 | Conversational data |

## Retrieval / RAG (for building and testing pipelines)

| Dataset | Size | License | Good for |
|---------|------|---------|----------|
| [Natural Questions](https://ai.google.com/research/NaturalQuestions) | 300k+ | CC-BY-SA-3.0 | QA over documents |
| [MS MARCO](https://microsoft.github.io/msmarco/) | 1M+ | Custom (research) | Passage retrieval, reranking |

## Evaluation / benchmarks

See [`benchmarks/`](../benchmarks/) for evaluation-focused datasets and harnesses.

## `[WANTED]` contributions

- Small, permissively-licensed RAG demo corpora that run in seconds
- Multilingual instruction datasets
- Domain-specific evaluation sets (with clear licenses)

## Contributing an entry

Add a row with an accurate **license** and a one-line "good for." Prefer permissive licenses and
datasets that are easy to obtain. Never add scraped data of unclear provenance. See
[CONTRIBUTING.md](../CONTRIBUTING.md).
