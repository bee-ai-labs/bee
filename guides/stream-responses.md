# Guide: Stream Responses to a User

> **Task:** show LLM output token-by-token so your app feels fast, instead of making the user wait
> for the whole response.

**Level:** 🟢 Beginner · **Concept:** [Your First LLM Call](../docs/getting-started/first-llm-call.md)

## Why

An LLM can take several seconds to finish a long answer. Streaming lets the user start reading the
first words immediately — the generation isn't faster, but the *experience* is dramatically
better. Use it for anything user-facing.

## Do it

```python title="stream.py"
from anthropic import Anthropic

client = Anthropic()

with client.messages.stream(
    model="claude-sonnet-5",
    max_tokens=500,
    messages=[{"role": "user", "content": "Explain vector databases in 3 sentences."}],
) as stream:
    for text in stream.text_stream:        # each chunk arrives as it's generated
        print(text, end="", flush=True)    # flush so it appears immediately
    print()
    final = stream.get_final_message()      # token usage, stop reason, etc.

print(f"\n[{final.usage.output_tokens} output tokens]")
```

## Streaming over HTTP (Server-Sent Events)

For a web app, forward each chunk to the browser as it arrives. See the
[FastAPI LLM service template](../templates/fastapi-llm-service/) for a complete, runnable
version:

```python
from fastapi.responses import StreamingResponse

def event_stream():
    with client.messages.stream(model="claude-sonnet-5", max_tokens=500, messages=msgs) as s:
        for text in s.text_stream:
            yield f"data: {text}\n\n"       # SSE frame
        yield "data: [DONE]\n\n"

return StreamingResponse(event_stream(), media_type="text/event-stream")
```

## Gotchas

- ✅ **Flush output** (`flush=True`, or don't buffer the HTTP response) or chunks appear all at
  once.
- ✅ **Handle mid-stream errors** — wrap the loop so a failure sends a clean error event, not a
  half-response.
- ✅ **Get usage from the final message**, not per chunk.
- ❌ Don't stream for background/batch jobs — there's no user watching; just await the full
  result.

## Related

- Runnable: [`examples/01-chatbot`](../examples/01-chatbot/) (streaming CLI chat)
- Template: [`templates/fastapi-llm-service`](../templates/fastapi-llm-service/)
