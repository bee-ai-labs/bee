"""A minimal streaming LLM API. Fill in auth, rate limiting, and observability for production."""
from __future__ import annotations

import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

load_dotenv()

MODEL = os.environ.get("BEE_MODEL", "claude-sonnet-5")
CORS_ORIGINS = [o for o in os.environ.get("CORS_ORIGINS", "").split(",") if o]

app = FastAPI(title="Bee — FastAPI LLM Service", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS or ["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    max_tokens: int = 512


def _client():
    """Create the LLM client, failing clearly if the key is missing."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise HTTPException(status_code=503, detail="ANTHROPIC_API_KEY is not configured.")
    from anthropic import Anthropic

    return Anthropic()


@app.get("/health")
def health() -> dict:
    """Liveness/readiness check for load balancers and orchestrators."""
    return {"status": "ok", "model": MODEL, "key_configured": bool(os.environ.get("ANTHROPIC_API_KEY"))}


@app.post("/chat")
def chat(req: ChatRequest) -> StreamingResponse:
    """Stream a response as Server-Sent Events so the client renders tokens as they arrive."""
    client = _client()

    def event_stream():
        try:
            with client.messages.stream(
                model=MODEL,
                max_tokens=req.max_tokens,
                messages=[{"role": "user", "content": req.message}],
            ) as stream:
                for text in stream.text_stream:
                    yield f"data: {text}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as exc:  # noqa: BLE001
            # Surface a clean error to the client instead of crashing the stream.
            yield f"event: error\ndata: {exc}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
