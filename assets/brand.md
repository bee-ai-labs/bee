# Bee Brand Guide 🎨

Keep Bee visually consistent. This guide covers the logo, colors, typography, and voice. When in
doubt, favor **clarity and warmth** — Bee is welcoming and precise.

## The name

Always **Bee** (capital B). The 🐝 emoji is our friendly shorthand and pairs well with headings
and the wordmark.

## Logo

| Asset | File | Use |
|-------|------|-----|
| Logo mark | [`logo.svg`](logo.svg) | App icons, headers, favicons at larger sizes |
| Favicon | [`../docs/assets/favicon.svg`](../docs/assets/favicon.svg) | Browser tab, small sizes |
| Banner | [`banner.svg`](banner.svg) | README hero, social cards |

**Do:** keep clear space around the mark; scale proportionally.
**Don't:** recolor the mark outside the palette, add drop shadows, stretch, or rotate it.

## Color palette

The palette is honey/amber — warm, energetic, legible.

| Role | Hex | Notes |
|------|-----|-------|
| Honey (primary) | `#F5A623` | Primary brand color, links, accents |
| Light honey | `#FFD54A` | Gradients, highlights |
| Deep amber | `#8A5A00` | Outlines, borders |
| Charcoal | `#1a1206` | Dark backgrounds, text on light |
| Cream | `#FFE9B0` | Text on dark |

Gradient: `#FFD54A → #F5A623` (top-left to bottom-right).

```text
Honey    #F5A623   ██████
Light    #FFD54A   ██████
Amber    #8A5A00   ██████
Charcoal #1a1206   ██████
Cream    #FFE9B0   ██████
```

## Typography

- **Headings & UI:** Inter (fallback: system sans-serif).
- **Code:** JetBrains Mono (fallback: monospace).

These match the [MkDocs Material](../mkdocs.yml) configuration.

## Difficulty tiers

Use these consistently across all content:

- 🟢 **Beginner**
- 🟡 **Intermediate**
- 🔴 **Advanced**

## Callouts

Use GitHub/Material callout syntax with consistent intent:

- `NOTE` — background info
- `TIP` — a helpful shortcut
- `IMPORTANT` — don't miss this
- `WARNING` — a common footgun
- `CAUTION` — real harm (cost, security, data loss)

## Voice & tone

- **Warm, not stiff.** We're a community, not a manual.
- **Clear before clever.** Explain the idea, then the jargon.
- **Encouraging.** Everyone was a beginner once; never gatekeep.
- **Honest.** No hype, no placeholders, no unverified claims.

## Emoji usage

A little goes a long way. Use topic emoji as visual anchors in headings (🧠 concepts, 🔎 RAG,
🤖 agents, 🏭 production) but don't overload paragraphs.

---

*Questions about brand usage? Open a [Discussion](https://github.com/bee-ai-labs/bee/discussions).*
