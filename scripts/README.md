# Scripts 🛠️

Repo tooling to make contributing easier.

| Script | What it does |
|--------|--------------|
| [`new-example.sh`](new-example.sh) | Scaffold a new example from `examples/_TEMPLATE/` |
| [`check.sh`](check.sh) | Run the same checks CI runs (format, lint, spelling, links, docs build) |

## Usage

```bash
# Create a new example
./scripts/new-example.sh 04-my-example

# Run all local checks before opening a PR
./scripts/check.sh
```

These are conveniences — everything they do is documented in
[CONTRIBUTING.md](../CONTRIBUTING.md) so you can run the steps manually too.
