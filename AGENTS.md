# AWS 質問回答

AWSに関する質問へ回答するためのリポジトリ。

## エージェントへの指針

- ユーザーとは日本語で話す。
- 結論を先に示し、理由を簡潔に説明する。
- 選択問題では正解と各選択肢の判断理由を示す。
- 用語は用途と似たサービスとの違いが分かるように説明する。
- 学習計画、日次予定、進捗、Anki、Discord、ファイルを自動更新しない。
- ファイル変更や外部操作は、ユーザーが明示的に依頼した場合だけ行う。
- 本物のシークレットやAWS認証情報をコミットしない。
- シェル作業はWSLを優先する。
- Pull Requestは作らず、変更依頼時は`main`へ直接commit・pushする。

## Cursor Cloud specific instructions

- このリポジトリはアプリやサーバではない。`package.json`、`requirements.txt`、ビルド工程はない。
- クラウド VM は **Linux**。ローカルは Windows ホストで `cmd /c node` 起動だが、クラウドでは `node .cursor/hooks/xxx.js` / `python3 .cursor/hooks/xxx.py` を直接実行する。
- 「lint/test」相当は `bash .cursor/hooks/validate-hooks.sh`（`session-start.js` が有効な JSON を出すか検証）。ビルド工程は無い。
- sessionコンテキストの確認は`node .cursor/hooks/session-start.js </dev/null`を使う。
- **PR を使わず `main` に直接 push する（ユーザー方針）**。新セッションが `cursor/...` ブランチ起点で始まっても、まず `git checkout main` してから commit → `git push origin main`（ローカルの `finish-push.sh` と同じ運用）。PR は作らない。
