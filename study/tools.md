# ツール

| ツール | 使い方 |
|--------|--------|
| Cursor | 計画・解説・Anki TSV・メモ |
| Anki | `study/anki/<資格>/` の TSV をインポート |
| 本 | `books.md` |
| Discord | 今日の予定・進捗通知（Webhook Secret `discord_daily_bot`） |

## Anki

- Front / Back / Tags（タブ・UTF-8・ヘッダなし）
- 詳細: `.cursor/skills/anki-tsv/SKILL.md`

## Discord

- スキル: `.cursor/skills/daily-plan-discord/SKILL.md`
- 送信: `python3 .cursor/hooks/discord-notify.py "..."`
- Secret 名: `discord_daily_bot`（Webhook URL。リポジトリには置かない）
- 予定（📅）も進捗（📊）も **ユーザーが伝えたときだけ** 送る

## 本

- 一覧: `books.md`
