"""Tests for the RAG pipeline — fake embedder + fake LLM, no downloads or network."""
from __future__ import annotations

from dataclasses import dataclass

from app import RAGPipeline, chunk_text, cosine_similarity


# --------------------------------------------------------------- unit: chunking & math
def test_chunking_respects_max_size():
    text = "\n\n".join(f"Paragraph number {i} with some words." for i in range(20))
    chunks = chunk_text(text, max_chars=100, overlap=20)
    assert len(chunks) > 1
    assert all(len(c) <= 100 + 40 for c in chunks)  # allow small overlap slack


def test_cosine_similarity_bounds():
    assert cosine_similarity([1, 0], [1, 0]) == 1.0
    assert cosine_similarity([1, 0], [0, 1]) == 0.0
    assert round(cosine_similarity([1, 1], [1, 1]), 5) == 1.0


# ------------------------------------------------------------------- fakes for the pipeline
def _bag_of_words(text: str, vocab: list[str]) -> list[float]:
    """A tiny deterministic embedder so cosine search behaves meaningfully in tests."""
    words = text.lower().split()
    return [float(words.count(term)) for term in vocab]


VOCAB = ["refund", "shipping", "password", "days", "window", "30"]


def fake_embed(texts: list[str]) -> list[list[float]]:
    return [_bag_of_words(t, VOCAB) for t in texts]


@dataclass
class _Block:
    type: str
    text: str


@dataclass
class _Resp:
    content: list


class _FakeMessages:
    def __init__(self):
        self.last_prompt = None

    def create(self, **kwargs):
        # Echo back which chunk ids were in the context so we can assert retrieval worked.
        self.last_prompt = kwargs["messages"][0]["content"]
        return _Resp(content=[_Block("text", "Answer grounded in context. [source: chunk-0]")])


class FakeClient:
    def __init__(self):
        self.messages = _FakeMessages()


DOC = """The refund window is 30 days from purchase.

Standard shipping takes 3 to 5 days.

Reset your password from the sign-in page."""


def test_index_and_retrieve_finds_relevant_chunk():
    pipe = RAGPipeline(embed_fn=fake_embed, client=FakeClient())
    n = pipe.index(DOC, max_chars=60, overlap=0)  # small chunks so each paragraph is its own
    assert n == 3

    retrieved = pipe.retrieve("what is the refund window in days?", k=1)
    top_score, top_chunk = retrieved[0]
    assert "refund" in top_chunk.text.lower()  # the refund chunk is retrieved first


def test_answer_returns_text_and_sources():
    pipe = RAGPipeline(embed_fn=fake_embed, client=FakeClient())
    pipe.index(DOC, max_chars=60, overlap=0)
    answer, sources = pipe.answer("refund window?", k=2)
    assert "grounded" in answer
    assert len(sources) == 2
    # The prompt sent to the LLM must contain the retrieved context.
    assert "refund" in pipe.client.messages.last_prompt.lower()
