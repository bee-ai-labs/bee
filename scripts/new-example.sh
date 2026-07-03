#!/usr/bin/env bash
# Scaffold a new Bee example from the template.
# Usage: ./scripts/new-example.sh NN-example-name
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 NN-example-name   (e.g. 04-code-assistant)" >&2
  exit 1
fi

name="$1"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
src="$root/examples/_TEMPLATE"
dest="$root/examples/$name"

if [[ -e "$dest" ]]; then
  echo "❌ $dest already exists." >&2
  exit 1
fi

cp -r "$src" "$dest"
echo "✅ Created examples/$name from _TEMPLATE."
echo "Next steps:"
echo "  1. Edit examples/$name/README.md and app/"
echo "  2. Add at least one test in tests/ (mock the LLM)"
echo "  3. Verify: cd examples/$name && python -m app && pytest"
