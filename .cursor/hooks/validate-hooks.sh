#!/bin/bash
# フックが有効な JSON を出力するかの簡易チェック（WSL から実行）
set -u
cd "$(dirname "$0")/../.."
for f in session-start; do
  out=$(node ".cursor/hooks/$f.js" </dev/null)
  if echo "$out" | node -e 'JSON.parse(require("fs").readFileSync(0,"utf8"))'; then
    echo "$f: JSON OK (${#out} bytes)"
  else
    echo "$f: INVALID JSON"
    exit 1
  fi
done
