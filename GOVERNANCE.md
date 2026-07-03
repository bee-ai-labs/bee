# Governance

This document describes how decisions get made in Bee. It's intentionally lightweight — Bee is a
community knowledge project, and the goal of governance here is to keep the hive healthy,
welcoming, and moving, not to add bureaucracy.

## Principles

1. **Openness** — decisions and discussions happen in public (issues, PRs, Discussions).
2. **Meritocracy of contribution** — influence grows with helpful, sustained participation.
3. **Kindness over ego** — we optimize for a welcoming community, especially to newcomers.
4. **Quality bar is non-negotiable** — no placeholders, everything runs, concepts are correct.

## Roles

### Contributors

Anyone who opens an issue, PR, or Discussion. **This is most people, and it's the most important
role.** No prior permission needed — see [CONTRIBUTING.md](CONTRIBUTING.md).

### Reviewers

Trusted contributors who review PRs in areas they know well. Reviewers are recognized for
consistent, high-quality contributions and reviews. They can approve PRs but not merge to
protected branches.

**Becoming a reviewer:** after several merged, high-quality PRs, a maintainer may invite you, or
you may nominate yourself in a Discussion. Reviewers are listed in
[`.github/CODEOWNERS`](.github/CODEOWNERS) for their area.

### Maintainers

Contributors with merge rights and repository administration responsibilities. Maintainers:

- Merge PRs after review and passing CI
- Triage issues and manage labels/milestones
- Steward the roadmap and quality standards
- Enforce the [Code of Conduct](CODE_OF_CONDUCT.md)

**Becoming a maintainer:** by invitation from existing maintainers, based on a track record of
excellent contributions, good judgment, and community stewardship.

## Decision-Making

We use **lazy consensus**: proposals move forward unless someone raises a reasoned objection.

- **Everyday changes** (content, examples, fixes): a single maintainer/reviewer approval + green
  CI is enough to merge.
- **Significant changes** (new top-level sections, structural changes, policy changes): open a
  Discussion or an issue labeled `proposal`. Give the community a reasonable window (typically a
  week) to weigh in. If there's rough consensus and no blocking objection, it proceeds.
- **Disagreements** are resolved by discussion first. If consensus can't be reached, maintainers
  make the final call, explaining their reasoning publicly.

## Adding & Removing Access

Reviewer and maintainer additions are proposed and agreed among current maintainers. Access may
be removed for Code of Conduct violations, or reverted to "emeritus" status after long inactivity
(with thanks — you're always welcome back).

## Changing This Document

Governance changes follow the "significant change" process above: propose in a Discussion, allow
time for input, seek rough consensus.

---

*This is a living document. As the community grows, we'll evolve governance to fit — always in
public, always with the community.* 🐝
