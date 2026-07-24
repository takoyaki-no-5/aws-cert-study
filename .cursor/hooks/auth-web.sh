#!/bin/bash
# gh のデバイスフロー認証を疑似TTYで起動し、ワンタイムコードを抽出して表示する。
# ユーザーはブラウザ（エージェントが開く）でコード入力するだけでよい。
export PATH=$HOME/.local/bin:$PATH

# 既存の途中状態を掃除
pkill -f "gh auth login" 2>/dev/null
sleep 1
rm -f /tmp/gh-auth.log /tmp/gh-code.txt

# プロンプトの描画を待ってから順に入力を送る（Git認証=Y / Enterでブラウザ）
{ sleep 2; printf 'y\n'; sleep 2; printf '\n'; sleep 900; } | \
  script -qefc "gh auth login --web --git-protocol https --hostname github.com" /tmp/gh-auth.log &
flow_pid=$!

# ワンタイムコードが出るまで最大30秒待つ
for i in $(seq 1 30); do
  code=$(tr -d '\r' < /tmp/gh-auth.log 2>/dev/null | grep -aoE '[A-Z0-9]{4}-[A-Z0-9]{4}' | head -1)
  if [ -n "$code" ]; then
    echo "$code" > /tmp/gh-code.txt
    echo "CODE_READY: $code"
    break
  fi
  sleep 1
done
[ -z "$code" ] && echo "CODE_NOT_FOUND"

# 認証フローの完了を待つ（ユーザーがブラウザで承認するまで）
wait $flow_pid
echo "AUTH_FLOW_EXIT: $?"
