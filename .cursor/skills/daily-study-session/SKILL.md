---
name: daily-study-session
description: >-
  AWS資格学習の1日を開始・継続する: スケジュールとプロフィールを読み、今日のタスクを提案し、
  最初のブロックを開始してログに記録する。Use when the user says 今日, これから始める,
  勉強する, スケジュール, or asks what to do next (today's study session).
---

# 日次学習セッション

## 開始時

1. `study/profile.md`・`study/schedule.md`（ハブ）→ そこにリンクされた進行中の `study/<資格>/schedule.md`・今日の `study/log/YYYY-MM-DD.md`（あれば。前日ログも有用なら）を読む。
2. プロフィールに目標資格・期限・学習時間が欠けていれば、足りない分だけ聞いて `study/profile.md` に書く。
3. 今日の `study/<資格>/days/YYYY-MM-DD.md` が無ければ `study/_templates/day.md` から生成（題材チェック・時間割のみ・短文）。あればそれを提示。
4. 最初のブロックの開始を促す（「始めて」なら即開始）。

## セッション中

- day ファイルのタイムテーブルに沿って1ブロックずつ進める。カリキュラム全体を一気に出さない。
- ブロックが終わるたびに day ファイルのチェックボックスを埋める。
- 質問には**試験合格目線**で回答（実務・実装の深掘りはしない。紛らわしい選択肢の対比を添える）。
- 計画が途中で変わったら進行中の `study/<資格>/schedule.md` を更新（ハブの `study/schedule.md` は試験が切り替わるときだけ）。

## 終了時（またはユーザーが切り上げたとき）

- `study/log/YYYY-MM-DD.md` に追記・更新: できたこと / できなかったこと / 次にやること。
- 進行中の `study/<資格>/schedule.md` の 状態 列を「済」にし、必要なら翌日分を調整。
- 一言の励まし + 明確な次のアクションで締める。
