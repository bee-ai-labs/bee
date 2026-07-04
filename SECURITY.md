# Security Policy

Bee is a knowledge repository — it ships documentation and example code, not a hosted service.
Even so, security matters here in two specific ways, and we take both seriously.

## What "security" means for Bee

1. **Vulnerabilities in example code or dependencies.** An example that demonstrates an insecure
   pattern (leaking API keys, unsafe deserialization, prompt-injection-prone tool use) is a bug
   we want to fix, because people copy examples into real projects.
2. **Repository / supply-chain integrity.** CI workflows, dependencies (via Dependabot), and
   release artifacts.

Because Bee has no production servers or user data, there is **no live system to attack** — but
insecure teaching material can still cause real-world harm downstream. That's the threat model
we defend against.

## Reporting a Vulnerability

**Please do not open a public issue for security problems.** Instead:

- Use GitHub's [**private vulnerability reporting**](https://github.com/bee-ai-labs/bee/security/advisories/new)
  (Security → Report a vulnerability), **or**
- Email **niyitegekatresor@gmail.com** with details.

Please include:

- A description of the issue and where it lives (file path, example name, dependency).
- Steps to reproduce or a proof of concept.
- The potential impact as you see it.

### What to expect

| Stage | Target |
|-------|--------|
| Acknowledgement of your report | Within **3 business days** |
| Initial assessment & severity | Within **7 business days** |
| Fix or mitigation plan | Depends on severity; communicated in the assessment |
| Public disclosure | Coordinated with you, after a fix is available |

We will credit you in the advisory and `CHANGELOG.md` unless you prefer to remain anonymous.

## Supported Versions

Bee is a rolling, living document — **the `main` branch is the supported version.** Security
fixes land on `main` and are announced in the [Changelog](CHANGELOG.md).

## Security Practices in This Repo

If you contribute, please help us keep Bee safe to learn from:

- 🔑 **Never commit secrets.** Use `.env.example` with placeholder values; real keys go in
  `.env` (which is git-ignored). Our CI scans for accidentally committed secrets.
- 🧩 **Model security-conscious patterns in examples.** If an example intentionally omits a
  safeguard for brevity, add a `> [!WARNING]` callout explaining what production code must add.
- 🛡️ **Teach the risks.** The [`docs/security/`](docs/security/index.md) section covers prompt
  injection, jailbreaks, data exfiltration via tools, and guardrails — reference it when
  relevant.
- 📦 **Keep dependencies current.** Dependabot opens PRs for updates; review and merge them.

Thank you for helping keep the hive — and everyone who learns from it — safe. 🐝
