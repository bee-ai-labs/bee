---
tags: [Intermediate]
---

# Text-to-Speech (TTS)

> Turning text into natural-sounding speech — the "voice" half of any voice application, from
> accessibility to voice assistants.

## Overview

**Text-to-Speech (TTS)** synthesizes spoken audio from text. Modern neural TTS sounds strikingly
human, supports many voices and languages, and can stream audio as it's generated. It's the
output stage of the voice loop whose input stage is [speech-to-text](speech-to-text.md), usually
wrapped around an [LLM](../concepts/how-llms-work.md) that decides *what* to say.

## Learning Objectives

By the end of this page you will be able to:

- Synthesize speech from text with a TTS engine.
- Choose between local and hosted TTS for your latency, cost, and quality needs.
- Stream TTS so a voice assistant starts speaking sooner.
- Control voice, pace, and pronunciation.

## Theory

### Where TTS sits in the voice loop

```mermaid
flowchart LR
    A[🎙️ User speech] --> B[ASR → text]
    B --> C[🧠 LLM decides reply]
    C --> D[TTS → audio]
    D --> E[🔊 Reply spoken]
    style D fill:#F5A623,stroke:#c77d00,color:#000
```

For a natural conversation, the whole loop must feel fast (roughly under a second of perceived
lag). TTS latency is a big part of that — which is why **streaming** matters.

### Local vs. hosted

| | **Local** (e.g. Piper, Coqui) | **Hosted API** (e.g. ElevenLabs, OpenAI, cloud TTS) |
|---|---|---|
| Cost | Free compute (your hardware) | Per character/second of audio |
| Voice quality | Good → very good | Often the most natural / expressive |
| Privacy | Text never leaves your machine | Text sent to provider |
| Latency | Depends on hardware | Low, and usually streamable |
| Best for | Privacy, offline, high volume | Top quality, fast start, many voices |

### Streaming: speak before the whole reply is ready

Two streams compound for a responsive assistant:

1. The **LLM streams** its reply token-by-token (see [streaming](../getting-started/first-llm-call.md)).
2. You feed sentences to a **streaming TTS** as they complete, so audio starts while the LLM is
   still writing.

This overlap is the difference between a snappy assistant and an awkward multi-second pause.

### Controlling the voice

- **Voice selection** — pick a voice ID (gender, accent, style).
- **Pace & pitch** — many engines expose rate/pitch controls.
- **Pronunciation** — some engines accept [SSML](https://www.w3.org/TR/speech-synthesis11/)
  (Speech Synthesis Markup Language) to fix names, spell out acronyms, or add pauses.

## Practical Example

### Local synthesis with Piper

```python title="tts_local.py"
# Piper is a fast, local neural TTS. Download a voice model (.onnx) first.
# pip install piper-tts
import wave
from piper import PiperVoice

voice = PiperVoice.load("en_US-lessac-medium.onnx")

with wave.open("reply.wav", "wb") as wav:
    voice.synthesize("Hello! Your order shipped today.", wav)
print("Wrote reply.wav")
```

### Hosted synthesis (provider-agnostic shape)

```python title="tts_hosted.py"
# Hosted TTS APIs share the same shape: text in -> audio bytes out.
# (Pseudocode-style; swap in your provider's SDK.)
audio_bytes = tts_client.synthesize(
    text="Hello! Your order shipped today.",
    voice="warm-female-en",
    format="mp3",
)
with open("reply.mp3", "wb") as f:
    f.write(audio_bytes)
```

### Streaming for a responsive assistant

```python title="stream_voice.py"
# Feed each completed sentence to the TTS as the LLM streams it.
import re

buffer = ""
with llm.messages.stream(model="claude-sonnet-5", max_tokens=300,
                         messages=[{"role": "user", "content": question}]) as stream:
    for chunk in stream.text_stream:
        buffer += chunk
        # When a sentence completes, synthesize and play it immediately.
        while match := re.search(r"[.!?]\s", buffer):
            sentence, buffer = buffer[: match.end()], buffer[match.end():]
            play(tts_client.synthesize(sentence))   # audio starts before the LLM finishes
if buffer.strip():
    play(tts_client.synthesize(buffer))
```

!!! tip "Sentence-level chunking beats word-level"
    Synthesize whole sentences, not individual words — TTS needs sentence context for natural
    prosody, and per-word synthesis sounds robotic and adds overhead.

## Best Practices

- ✅ Stream sentence-by-sentence to minimize perceived latency in conversations.
- ✅ Match engine choice to your needs — local for privacy/offline, hosted for top quality.
- ✅ Use SSML (or a pronunciation map) for names, acronyms, numbers, and pauses.
- ✅ Cache audio for repeated, static phrases ("Please hold…") to save cost and time.
- ✅ Pick a consistent voice that fits your product's tone.

## Common Mistakes

- ❌ Waiting for the full LLM reply before starting TTS — creates an awkward pause.
- ❌ Synthesizing word-by-word, which sounds robotic.
- ❌ Ignoring pronunciation of domain terms/acronyms (fix with SSML).
- ❌ Re-synthesizing identical static prompts instead of caching them.

## Exercises

1. Synthesize the same sentence with two different voices/engines. Compare naturalness and
   latency.
2. Build the sentence-streaming loop above (mock the LLM and TTS). Measure time-to-first-audio
   vs. waiting for the full reply.
3. Use SSML to correct the pronunciation of a tricky name or spell out an acronym.

## References

- [Piper (local neural TTS)](https://github.com/rhasspy/piper)
- [SSML specification](https://www.w3.org/TR/speech-synthesis11/)
- Bee: [Speech-to-Text](speech-to-text.md) · [Speech overview](index.md)
