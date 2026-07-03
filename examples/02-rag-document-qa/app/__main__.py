"""CLI entry point: `python -m app`. Indexes data/sample.md, then answers questions."""
from __future__ import annotations

import os
import sys
from pathlib import Path

from .rag import RAGPipeline

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "sample.md"


def main() -> None:
    from dotenv import load_dotenv

    load_dotenv()
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("❌ ANTHROPIC_API_KEY is not set. Copy .env.example to .env and add your key.")

    # Local embeddings (CPU-friendly). First run downloads a small model.
    from sentence_transformers import SentenceTransformer

    print("Loading local embedding model (first run downloads ~80 MB)…")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(texts: list[str]) -> list[list[float]]:
        return model.encode(texts, normalize_embeddings=True).tolist()

    from anthropic import Anthropic

    pipeline = RAGPipeline(
        embed_fn=embed,
        client=Anthropic(),
        model=os.environ.get("BEE_MODEL", "claude-sonnet-5"),
    )

    n = pipeline.index(DATA_FILE.read_text(encoding="utf-8"))
    print(f"Indexed {n} chunks from {DATA_FILE.name}. Ask a question ('exit' to quit).")

    while True:
        try:
            question = input("ask › ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue
        answer, sources = pipeline.answer(question)
        print(f"answer › {answer}")
        print(f"         (retrieved: {', '.join(sources)})")


if __name__ == "__main__":
    main()
