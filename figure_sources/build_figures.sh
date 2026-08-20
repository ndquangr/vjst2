#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
for f in fig*.tex; do
  echo "Building $f"
  xelatex -interaction=nonstopmode -halt-on-error "$f" >/dev/null
done
echo "Done. PDFs are in $(pwd)."
