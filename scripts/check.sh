#!/usr/bin/env bash
# Run the same quality checks CI runs. Skips any tool that isn't installed (with a note).
set -uo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"
fail=0

run() {
  local name="$1"; shift
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "⏭️  $name — '$1' not found, skipping."
    return
  fi
  echo "▶️  $name"
  if "$@"; then echo "✅ $name"; else echo "❌ $name"; fail=1; fi
}

run "Prettier"      npx --yes prettier@3 --check .
run "markdownlint"  npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#site"
run "cspell"        npx --yes cspell@8 "**/*.md" --no-progress
run "MkDocs build"  mkdocs build --strict

if [[ $fail -eq 0 ]]; then
  echo "🐝 All available checks passed."
else
  echo "Some checks failed — see above."
fi
exit $fail
