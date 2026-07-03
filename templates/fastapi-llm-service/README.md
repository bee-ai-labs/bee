# Template: FastAPI LLM Service

> A minimal, production-shaped starting point for an HTTP API that streams LLM responses.

Includes: streaming endpoint (Server-Sent Events), config from environment, a health check,
graceful handling of a missing API key, and CORS. Not included (on purpose — add what *you* need):
auth, rate limiting, persistence, observability.

## Use it

```bash
cp -r templates/fastapi-llm-service my-service && cd my-service
cp .env.example .env            # add your ANTHROPIC_API_KEY
uv sync                         # or: pip install -e .
uvicorn app.main:app --reload   # http://127.0.0.1:8000/docs
```

Try the streaming endpoint:

```bash
curl -N -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Explain streaming in one sentence."}'
```

## What to add before production

- 🔐 **Auth & rate limiting** — see [Security](../../docs/security/index.md)
- 📊 **Observability** — tracing, token/cost metrics ([MLOps](../../docs/mlops/index.md))
- 🚢 **Containerization & deploy** — see [Deployment](../../docs/deployment/index.md)

## References

- [FastAPI](https://fastapi.tiangolo.com/) · Bee [Deployment](../../docs/deployment/index.md)
