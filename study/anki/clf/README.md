# Anki（CLF）

**目標: このデッキを覚え切れば本番イメージ約90点。**  
低頻度・マニアックは入れない。頻出の対比・シナリオ中心。

```
study/anki/clf/
  01-security/  → AWS::CLF::01-セキュリティ
  02-billing/   → AWS::CLF::02-請求
  03-concepts/  → AWS::CLF::03-概念
  04-services/  → AWS::CLF::04-サービス
  05-mock/      → AWS::CLF::05-模試A / 05-模試B（各65問）
  06-review/    → 弱点（後から）
```

## 枚数

| 世代 | 枚数 |
|------|------|
| 基礎定義 | 135 |
| シナリオ | 90 |
| 高頻度増強 (`*-hy-*`) | 252 |
| **合計（整理後）** | **約459** |
| 模試A / B（4択・5択2つ選択） | 130 |

タグに `hy` が付いているのが高頻度枠。

## 周回順（合格用）

1. `01-セキュリティ`（責任共有・IAM・サポートに効く検知系）
2. `02-請求`（サポートプラン・料金4種が最優先）
3. `03-概念`（WA柱・7R・グローバル）
4. `04-サービス`（「何を使う？」シナリオ）
5. 模試 → 落ちたものだけ `06-review`

## 閲覧・削除

```bash
python3 .cursor/hooks/anki-manage.py decks
python3 .cursor/hooks/anki-manage.py count 'deck:AWS::CLF*'
python3 .cursor/hooks/anki-manage.py list 'deck:AWS::CLF::01-セキュリティ' --limit 20
python3 .cursor/hooks/anki-manage.py show <noteId>
python3 .cursor/hooks/anki-manage.py search 'サポート'
python3 .cursor/hooks/anki-manage.py delete --query '接続テスト' --yes
```

重複削除（表面が同じものを1枚残して削除）:

```bash
python3 .cursor/hooks/anki-dedupe.py --query 'deck:AWS::CLF*' --yes
```
