---
name: anki-tsv
description: >-
  AWS資格学習用に Anki カードを生成・投入する（AnkiConnect 優先、だめなら TSV）。
  Use when the user asks for Anki, カード, TSV, デッキ, flashcards, or wants to turn
  notes/mistakes into spaced-repetition cards.
---

# Anki カード生成・投入

## 優先順位

1. **AnkiConnect で直接追加**（Anki Desktop が起動中でアドオン導入済みのとき）
2. **TSV 生成** → ユーザーが Anki で Import（フォールバック）

## AnkiConnect（コマンドから追加）

前提:

- Anki Desktop を起動
- アドオン **AnkiConnect**（コード `2055492159`）をインストールして再起動

投入コマンド（WSL 内）:

```bash
python3 .cursor/hooks/anki-add.py --deck 'AWS::CLF' study/anki/clf_YYYY-MM-DD_topic.tsv
# または1枚
python3 .cursor/hooks/anki-add.py --deck 'AWS::CLF' --front 'Q' --back 'A' --tags 'clf billing'
```

接続確認:

```bash
curl -s localhost:8765 -d '{"action":"version","version":6}'
```

デッキ名の目安: `AWS::CLF` / `AWS::AIF` / `AWS::SAA` など。

## TSV（フォールバック）

### 出力先

- `study/anki/` 配下（資格フォルダには置かない）
- ファイル名: `<資格略称>_YYYY-MM-DD_<トピックのスラッグ>.tsv`

### フォーマット

- UTF-8 / タブ区切り / ヘッダなし
- `表面` `<TAB>` `裏面` `<TAB>` `タグ`（3列目任意）
- フィールド内改行は `<br>`。フィールド内にタブを入れない

### カードの作り方

- 表面: 1枚1論点（日本語OK。試験用語は英語併記）
- 裏面: 短い答え + 1行の理由
- タグ例: `clf billing source:cursor`

### 生成後

- AnkiConnect が使えれば `anki-add.py` で投入
- 使えなければ File → Import → その TSV（区切り Tab、HTML 許可）
- 今日のログに枚数とトピックを記録
