---
name: anki-tsv
description: >-
  AWS資格学習用に Anki カードを生成・投入する（AnkiConnect 優先、だめなら TSV）。
  Use when the user asks for Anki, カード, TSV, デッキ, flashcards, or wants to turn
  notes/mistakes into spaced-repetition cards.
---

# Anki カード生成・投入

## 用語質問時（自動）

「〇〇って何 / 教えて」系（詳細: `.cursor/rules/anki-term-qa.mdc`）:

1. 先に回答
2. **`study/anki/` 全範囲**（全資格・全工程・asked.tsv 含む）を探索
3. **どこにも同様の論点が無ければ** 1枚だけ追加（工程ファイル優先。無理なら `06-review/asked.tsv`）
4. AnkiConnect 可なら `anki-add.py`、だめなら TSV のみ

`asked.tsv` は置き場の一つ。追加前の捜索を省略しない。

**安全**: `addNote` + 重複スキップのみ。他カード削除・学習記録消去はしない。

## 優先順位

1. **AnkiConnect で直接追加**（Anki Desktop が起動中でアドオン導入済みのとき）
2. **TSV 生成** → ユーザーが Anki で Import（フォールバック）

## AnkiConnect（コマンドから追加）

前提:

- Anki Desktop を起動
- アドオン **AnkiConnect**（コード `2055492159`）をインストールして再起動

投入コマンド（WSL 内）:

```bash
python3 .cursor/hooks/anki-add.py --deck 'AWS::CLF' study/anki/clf/.../topic.tsv
```

閲覧・削除:

```bash
python3 .cursor/hooks/anki-manage.py list 'deck:AWS::CLF*' --limit 20
python3 .cursor/hooks/anki-manage.py delete --query '接続テスト' --yes
```

接続確認:

```bash
curl -s localhost:8765 -d '{"action":"version","version":6}'
```

デッキ名の目安: `AWS::CLF` / `AWS::AIF` / `AWS::SAA` など。
ノートタイプは日本語版 Anki なら自動で `基本`（表面/裏面）を使う。

## TSV（フォールバック）

### 出力先

- `study/anki/<資格>/` 配下を**工程ごとの階層**で管理（例: `study/anki/clf/01-security/02-iam.tsv`）
- 資格フォルダ直下にフラット置きしない
- ファイル名: `<番号>-<トピックのスラッグ>.tsv`
- CLF 一括再生成: `python3 .cursor/hooks/clf-anki-generate.py`

### フォーマット

- UTF-8 / タブ区切り / ヘッダなし
- `表面` `<TAB>` `裏面` `<TAB>` `タグ`（3列目任意）
- フィールド内改行は `<br>`。フィールド内にタブを入れない

### カードの作り方

- 表面: 1枚1論点（日本語OK。試験用語は英語併記）
- 裏面: 短い答え + 1行の理由
- **量の目安**: その資格を「全部できたら約90点」と言える密度。低頻度は入れない。対比・シナリオを厚くする
- タグ例: `clf billing hy source:cursor`

### 生成後

- AnkiConnect が使えれば `anki-add.py` で投入
- 使えなければ File → Import → その TSV（区切り Tab、HTML 許可）
- 今日のログに枚数とトピックを記録
