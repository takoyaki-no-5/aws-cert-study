#!/bin/bash
# gh 認証の完了を待ってから、コミット → 公開リポジトリ作成 → push まで自動実行する
set -e
export PATH=$HOME/.local/bin:$PATH
cd /mnt/c/Users/kamag/Documents/AWS

echo "waiting for gh auth..."
ok=0
for i in $(seq 1 90); do
  if gh auth status >/dev/null 2>&1; then ok=1; break; fi
  sleep 10
done
if [ "$ok" != "1" ]; then
  echo "AUTH_TIMEOUT"
  exit 1
fi

login=$(gh api user -q .login)
uid=$(gh api user -q .id)
echo "authenticated as: $login"

# 公開リポジトリに個人 Gmail を出さないため noreply を使う（user.name は既存の匿名名を維持）
git config user.email "${uid}+${login}@users.noreply.github.com"

git add -A
if ! git diff --cached --quiet; then
  git commit -m "AWS資格学習ワークスペース初期化: 学習計画・スケジュール・.cursor 設定"
fi

repo="aws-cert-study"
if gh repo view "$login/$repo" >/dev/null 2>&1; then
  git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/$login/$repo.git"
  git push -u origin main
else
  gh repo create "$repo" --public --source=. --remote=origin --push
fi

echo "PUSH_DONE: https://github.com/$login/$repo"
