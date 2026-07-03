---
tags: [Beginner]
---

# Prompt Engineering

> Getting reliably good outputs from an LLM by writing better inputs. It's part craft, part
> experiment — and it's the fastest way to improve any AI feature.

## Overview

An LLM is extraordinarily sensitive to *how* you ask. The same request, phrased two ways, can
produce a vague ramble or a precise, correct answer. Prompt engineering is the disciplined
practice of designing inputs that steer the model toward what you want. This page covers the
techniques that consistently work, in rough order of how often you'll reach for them.

## Learning Objectives

By the end of this page you will be able to:

- Apply the core techniques: clear instructions, examples, and structured prompts.
- Use chain-of-thought to improve reasoning tasks.
- Decide when to use zero-shot vs. few-shot prompting.
- Iterate on prompts systematically instead of by guesswork.

## Theory & Techniques

### 1. Be clear, specific, and direct

The model can't read your mind. Vague prompts get vague answers. State the task, the constraints,
and the desired format explicitly.

=== "❌ Vague"

    ```text
    Tell me about this customer feedback.
    ```

=== "✅ Specific"

    ```text
    Classify the sentiment of this customer feedback as positive, negative, or neutral.
    Then list up to 3 specific issues mentioned. Respond in under 60 words.

    Feedback: "The app is fast but crashes when I upload photos, and support never replied."
    ```

The second prompt tells the model exactly what to do, the allowed categories, and the length.

### 2. Give the model a role and context

Setting a role primes relevant behavior. (For multi-turn apps, this belongs in the
[system prompt](system-prompts.md).)

```text
You are a senior Python code reviewer. Review the function below for bugs, security issues,
and style. Prioritize correctness over nitpicks.
```

### 3. Show, don't just tell: few-shot examples

**Zero-shot** = instructions only. **Few-shot** = instructions *plus* examples of the desired
input→output. Examples are often the single most effective technique for shaping format and
style.

```text
Extract the company and role from each job title.

Input: "Senior Engineer at Acme"   → {"company": "Acme", "role": "Senior Engineer"}
Input: "Google Product Manager"     → {"company": "Google", "role": "Product Manager"}
Input: "Designer, Figma"            →
```

The model continues the pattern. Use 2–5 diverse examples that cover edge cases.

### 4. Let the model think: chain-of-thought

For reasoning, math, or multi-step tasks, ask the model to work through steps *before*
answering. This "chain-of-thought" (CoT) reliably improves accuracy, because each intermediate
token gives the model more to reason with.

=== "❌ Straight to answer"

    ```text
    A shirt costs $40 after a 20% discount. What was the original price?
    ```

=== "✅ Chain-of-thought"

    ```text
    A shirt costs $40 after a 20% discount. What was the original price?
    Think step by step, then give the final answer on a line starting with "Answer:".
    ```

```mermaid
flowchart LR
    Q[Question] --> R[Reasoning<br/>step by step] --> A[Final answer]
    style R fill:#F5A623,stroke:#c77d00,color:#000
```

!!! tip "Separate reasoning from the final answer"
    Ask for the reasoning, then a clearly delimited final answer (e.g. `Answer: ...`). Your code
    can then reliably extract just the answer.

### 5. Structure the prompt

Long prompts benefit from clear structure — headings, delimiters, and sections. Put instructions
first, then data, and clearly mark boundaries so the model doesn't confuse your instructions with
the content it's processing (this also reduces [prompt injection](../security/index.md) risk).

```text
## Task
Summarize the document below in 3 bullet points.

## Document
<document>
{document_text}
</document>
```

Delimiters like XML-style tags (`<document>…</document>`) or triple backticks make it unambiguous
where data starts and ends.

### 6. Tell it what *to* do, not just what not to do

Positive instructions work better than prohibitions. Instead of "don't be verbose," say "respond
in at most 3 sentences."

## Practical Example: iterating a prompt

```python title="iterate.py"
from anthropic import Anthropic

client = Anthropic()

PROMPT = """You are a support-ticket classifier.
Classify the ticket into exactly one category: [billing, bug, feature_request, other].
Then rate urgency 1-5. Think briefly, then output the final result as:
category: <category>
urgency: <n>

Ticket: {ticket}
"""

def classify(ticket: str) -> str:
    resp = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=200,
        temperature=0,                       # consistent classification
        messages=[{"role": "user", "content": PROMPT.format(ticket=ticket)}],
    )
    return resp.content[0].text

print(classify("I was charged twice this month and can't reach anyone."))
```

Test it on 10–20 real tickets, inspect the misses, and refine the prompt. That loop — not
cleverness — is what produces reliable prompts.

## Best Practices

- ✅ Start simple; add complexity only when a real failure demands it.
- ✅ Use `temperature=0` for tasks that must be consistent.
- ✅ Add few-shot examples to lock in format and handle edge cases.
- ✅ Use delimiters to separate instructions from data.
- ✅ Protect a good prompt with an [eval](../evaluation/index.md) before iterating further.

## Common Mistakes

- ❌ Vague asks ("make it better") — specify the criteria.
- ❌ Only negative instructions ("don't do X") — say what to do instead.
- ❌ Burying the instruction after a huge block of data — put it first.
- ❌ Changing five things at once — change one, measure, repeat.
- ❌ Trusting one lucky good output — test on many inputs.

## Exercises

1. Take a vague prompt you've used and rewrite it with an explicit task, format, and length.
   Compare outputs.
2. Convert a zero-shot classification prompt to few-shot with 3 examples. Does accuracy improve?
3. Add chain-of-thought to a word problem. Measure how often the answer is now correct across 10
   variations.

## References

- [Anthropic — Prompt engineering overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [OpenAI — Prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering)
- ["Chain-of-Thought Prompting"](https://arxiv.org/abs/2201.11903) — the CoT paper
- Next in Bee: [System Prompts](system-prompts.md) · [Structured Outputs](structured-outputs.md)
