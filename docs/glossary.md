# Glossary

Plain-language definitions of the terms you'll meet across Bee. Skim it once, return when a word
trips you up. Terms link to the Bee pages where they're explained in depth.

## A–C

**Agent**
: An LLM-driven system that decides *and acts* — choosing tools, taking steps, and reacting to
results in a loop, rather than answering once. See [Agent Fundamentals](agents/fundamentals.md).

**Attention**
: The mechanism that lets a transformer weigh how much each token should "pay attention" to every
other token. The core idea behind modern LLMs. See [The Transformer](concepts/transformers.md).

**Chunking**
: Splitting documents into smaller pieces before embedding them for retrieval. The single biggest
lever on RAG quality. See [Chunking](rag/chunking.md).

**Context window**
: The maximum number of tokens a model can consider at once (prompt + response). Exceed it and
earlier content is dropped.

**Cosine similarity**
: A measure of how similar two embedding vectors are, based on the angle between them. Ranges
from -1 (opposite) to 1 (identical direction).

## D–H

**Embedding**
: A list of numbers (a vector) that represents the *meaning* of text, so similar meanings sit
close together in vector space. See [Embeddings](concepts/embeddings.md).

**Fine-tuning**
: Continuing to train a pretrained model on your own data to specialize its behavior. An
alternative (or complement) to prompting and RAG.

**Guardrails**
: Checks that constrain model inputs/outputs — filtering unsafe content, validating format, or
blocking prompt injection. See [Security](security/index.md).

**Hallucination**
: When a model produces confident but false or unsupported information. Mitigated (not eliminated)
by RAG, grounding, and evaluation.

**Hybrid search**
: Combining keyword search (e.g. BM25) with vector search to get the best of exact matches and
semantic matches. See [Hybrid Search & Reranking](rag/hybrid-search-reranking.md).

## I–P

**Inference**
: Running a trained model to get outputs (as opposed to *training* it). Your API calls are
inference.

**LLM (Large Language Model)**
: A neural network trained to predict the next token over huge amounts of text, which turns out
to be a remarkably general capability. See [How LLMs Work](concepts/how-llms-work.md).

**MCP (Model Context Protocol)**
: An open standard for connecting LLM applications to tools and data sources through a common
interface. See [MCP](agents/mcp.md).

**Prompt engineering**
: The craft of writing inputs that reliably get good outputs from a model. See
[Prompt Engineering](prompting/prompt-engineering.md).

## Q–Z

**Quantization**
: Reducing the numeric precision of a model's weights (e.g. 16-bit → 4-bit) to shrink memory and
speed up inference, usually with a small quality cost.

**RAG (Retrieval-Augmented Generation)**
: Fetching relevant documents and putting them in the prompt so the model answers from *your*
data instead of only its training. See [RAG](rag/index.md).

**Reranking**
: A second, more accurate pass that reorders retrieved candidates by relevance before they reach
the model. See [Hybrid Search & Reranking](rag/hybrid-search-reranking.md).

**System prompt**
: Instructions that set a model's persona, rules, and output format for the whole conversation.
See [System Prompts](prompting/system-prompts.md).

**Temperature**
: A knob (0–1+) controlling output randomness. Low = consistent; high = creative.

**Token**
: The unit a model actually processes — roughly a word-piece. Billing and context limits are
counted in tokens. See [Tokenization](concepts/tokenization.md).

**Tool / function calling**
: Letting a model request that your code run a function (search, calculate, call an API) and use
the result. See [Function & Tool Calling](prompting/function-calling.md).

**Vector database**
: A database optimized for storing embeddings and finding the nearest ones to a query vector.
See [Vector Databases](rag/vector-databases.md).

---

!!! note "Missing a term?"
    [Suggest an addition](https://github.com/bee-ai-labs/bee/issues/new/choose) or add it yourself —
    the glossary is a great [first contribution](contributing/index.md).
