"""A minimal, readable RAG pipeline.

Every stage is a small pure function or an injectable dependency, so the whole thing is
testable without a model download or API key (see tests/).
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Callable, Protocol

# An embed function maps a list of texts to a list of vectors (lists of floats).
EmbedFn = Callable[[list[str]], list[list[float]]]


# --------------------------------------------------------------------------- chunking
def chunk_text(text: str, max_chars: int = 600, overlap: int = 80) -> list[str]:
    """Recursive-ish chunking: pack paragraphs up to max_chars, with a little overlap.

    See docs/rag/chunking.md for the theory behind size and overlap.
    """
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    current = ""
    for para in paragraphs:
        if len(current) + len(para) + 2 <= max_chars:
            current = f"{current}\n\n{para}".strip()
        else:
            if current:
                chunks.append(current)
            tail = current[-overlap:] if current else ""
            current = f"{tail}\n\n{para}".strip() if tail else para
    if current:
        chunks.append(current)
    return chunks


# ----------------------------------------------------------------------- vector store
def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


@dataclass
class Chunk:
    id: str
    text: str
    embedding: list[float]


@dataclass
class InMemoryVectorStore:
    """The simplest possible vector store: a list + brute-force cosine search.

    Real apps use an ANN index (see docs/rag/vector-databases.md); this is for learning.
    """

    chunks: list[Chunk] = field(default_factory=list)

    def add(self, chunks: list[Chunk]) -> None:
        self.chunks.extend(chunks)

    def search(self, query_vec: list[float], k: int = 3) -> list[tuple[float, Chunk]]:
        scored = [(cosine_similarity(query_vec, c.embedding), c) for c in self.chunks]
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return scored[:k]


# --------------------------------------------------------------------------- protocol
class LLMClient(Protocol):
    @property
    def messages(self): ...  # pragma: no cover


# --------------------------------------------------------------------------- pipeline
_SYSTEM = (
    "You answer questions using ONLY the provided context. "
    "Cite the chunk id(s) you used like [source: chunk-2]. "
    "If the answer is not in the context, say you don't know based on the document."
)


@dataclass
class RAGPipeline:
    embed_fn: EmbedFn
    client: LLMClient
    model: str = "claude-sonnet-5"
    store: InMemoryVectorStore = field(default_factory=InMemoryVectorStore)

    def index(self, text: str, max_chars: int = 600, overlap: int = 80) -> int:
        """Chunk, embed, and store a document. Returns the number of chunks."""
        pieces = chunk_text(text, max_chars=max_chars, overlap=overlap)
        vectors = self.embed_fn(pieces)
        chunks = [
            Chunk(id=f"chunk-{i}", text=p, embedding=v)
            for i, (p, v) in enumerate(zip(pieces, vectors))
        ]
        self.store.add(chunks)
        return len(chunks)

    def retrieve(self, question: str, k: int = 3) -> list[tuple[float, Chunk]]:
        query_vec = self.embed_fn([question])[0]
        return self.store.search(query_vec, k=k)

    def build_prompt(self, question: str, retrieved: list[tuple[float, Chunk]]) -> str:
        context = "\n\n".join(f"[{c.id}]\n{c.text}" for _, c in retrieved)
        return f"Context:\n{context}\n\nQuestion: {question}"

    def answer(self, question: str, k: int = 3) -> tuple[str, list[str]]:
        """Retrieve relevant chunks and generate a grounded, cited answer."""
        retrieved = self.retrieve(question, k=k)
        prompt = self.build_prompt(question, retrieved)
        resp = self.client.messages.create(
            model=self.model,
            max_tokens=500,
            system=_SYSTEM,
            messages=[{"role": "user", "content": prompt}],
        )
        text = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")
        sources = [c.id for _, c in retrieved]
        return text, sources
