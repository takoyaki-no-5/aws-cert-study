# ツール

| ツール | 使い方 |
|--------|--------|
| Cursor | 計画・解説・Anki TSV・メモ |
| Anki | `study/anki/<資格>/` の TSV をインポート |
| 本 | `books.md` |
| Discord | 今日の予定通知のみ（**現在 OFF**・`study/discord.off`。オン指示まで送らない） |

## Anki

- Front / Back / Tags（タブ・UTF-8・ヘッダなし）
- 詳細: `.cursor/skills/anki-tsv/SKILL.md`

## Discord

- **状態: OFF**（`study/discord.off` あり。ユーザーが「オンにして」と言うまで送信しない）
- スキル: `.cursor/skills/daily-plan-discord/SKILL.md`
- 送信: `python3 .cursor/hooks/discord-notify.py "..."`（off 時はスクリプトも拒否）
- Secret 名: `discord_daily_bot`（Webhook URL。リポジトリには置かない）
- オン時: 予定も **ユーザーが伝えたときだけ** 送る（**進捗は送らない**）
- 文面は **友達向け**（分野外でもわかる・フランク）。先頭は **「たこやきの…」**（Discord 名・公開OK）
- **帰宅後枠だけ**（電車 Anki は書かない）。章は1行ずつ・分数付き

## 本

- 一覧: `books.md`
