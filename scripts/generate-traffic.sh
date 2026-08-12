#!/usr/bin/env bash
# Simple traffic generator to exercise the demo app.
set -euo pipefail

HOST=${HOST:-http://localhost:8000}

echo "Hitting index and login endpoints..."
for i in $(seq 1 20); do
  curl -sS "${HOST}/" >/dev/null || true
  curl -sS -X POST "${HOST}/login" -d "username=user${i}" >/dev/null || true
  sleep 0.5
done

echo "Done."
