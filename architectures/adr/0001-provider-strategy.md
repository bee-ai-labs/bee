# ADR-0001: Provider-agnostic concepts, Anthropic-first code

- **Status:** Accepted
- **Date:** 2026-07-03
- **Deciders:** Bee maintainers

## Context

Bee teaches AI engineering. LLM providers (Anthropic, OpenAI, Google, open models via Ollama/vLLM)
have different SDKs but largely the same underlying concepts. We must decide how to handle
providers across *concept docs* and *code examples* without (a) tying learners to one vendor or
(b) filling examples with untested multi-provider branching.

## Decision

1. **Concept documentation is provider-agnostic.** Articles teach transferable ideas (tokens,
   embeddings, tool calling, RAG) without assuming a specific vendor. Where an API detail is
   needed, it's framed as "the shape is the same across providers."
2. **Code examples default to the Anthropic SDK** for concreteness, because a single, consistent,
   *tested* SDK per example is more valuable to learners than partial multi-provider code.
3. **Examples note how to adapt** to other providers, and structure code so the LLM client is
   injectable (which also enables testing without a provider).

## Consequences

**Positive**

- Learners gain transferable understanding, not vendor lock-in.
- Examples stay runnable and testable (one SDK, mockable client).
- Consistent code style across examples lowers cognitive load.

**Negative / trade-offs**

- Examples show one provider's exact syntax; users of other providers must adapt (mitigated by
  notes and injectable clients).
- We must keep the chosen SDK version pinned and tested as APIs evolve (handled by Dependabot +
  CI example tests).

**Neutral**

- Community contributions may add provider-specific variants as separate, clearly-labeled
  examples where valuable.

## Notes

This ADR establishes the pattern; individual sections may revisit it (e.g. a "local models"
section will naturally center Ollama/vLLM). Supersede this ADR rather than editing it if the
strategy changes.
