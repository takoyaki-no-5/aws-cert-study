#!/bin/bash
# GitHub OAuth デバイスフローを直接実行し、取得したトークンで gh を非対話ログインさせる。
# gh CLI の公開 client_id を使用（gh 本体と同じ認可アプリ）。
set -u
export PATH=$HOME/.local/bin:$PATH

# 以前の対話フローの残骸を掃除
pkill -f "gh auth login" 2>/dev/null
pkill -f "script -qefc" 2>/dev/null
sleep 1

CLIENT_ID="178c6fc778ccc68e1d6a"

resp=$(curl -s -X POST -H "Accept: application/json" https://github.com/login/device/code \
  -d "client_id=${CLIENT_ID}&scope=repo,read:org,gist,workflow")

device_code=$(echo "$resp" | grep -o '"device_code":"[^"]*"' | cut -d'"' -f4)
user_code=$(echo "$resp" | grep -o '"user_code":"[^"]*"' | cut -d'"' -f4)
interval=$(echo "$resp" | grep -o '"interval":[0-9]*' | grep -o '[0-9]*')
interval=${interval:-5}

if [ -z "$user_code" ]; then
  echo "DEVICE_CODE_FAILED: $resp"
  exit 1
fi

echo "CODE_READY: $user_code"

# ユーザーのブラウザ承認を最大15分待つ
for i in $(seq 1 180); do
  sleep "$interval"
  tok=$(curl -s -X POST -H "Accept: application/json" https://github.com/login/oauth/access_token \
    -d "client_id=${CLIENT_ID}&device_code=${device_code}&grant_type=urn:ietf:params:oauth:grant-type:device_code")
  access_token=$(echo "$tok" | grep -o '"access_token":"[^"]*"' | cut -d'"' -f4)
  if [ -n "$access_token" ]; then
    printf '%s' "$access_token" | gh auth login --with-token --hostname github.com
    gh auth setup-git --hostname github.com
    echo "AUTH_DONE: $(gh api user -q .login)"
    exit 0
  fi
  if echo "$tok" | grep -q '"expired_token"\|"access_denied"'; then
    echo "AUTH_FAILED: $tok"
    exit 1
  fi
done
echo "AUTH_TIMEOUT"
exit 1
