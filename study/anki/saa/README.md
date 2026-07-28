# Anki（SAA）

**目標: 覚え切れば本番イメージ約90点。** 対比・シナリオ中心。低頻度は入れない。
現状: **25ファイル / 319枚**（AnkiConnect 投入済み）。再投入: `python3 .cursor/hooks/saa-anki-generate.py`

```
study/anki/saa/
  01-secure/      → AWS::SAA::01-セキュア
  02-resilient/   → AWS::SAA::02-レジリエント
  03-performance/ → AWS::SAA::03-性能
  04-cost/        → AWS::SAA::04-コスト
  05-mock/        → AWS::SAA::05-模試
  06-review/      → 弱点。用語質問で工程不明のときだけ asked.tsv（追加前に anki 全範囲を探索）
```

## 周回順

1. `01-セキュア`（配点30%）
2. `02-レジリエント`
3. `03-性能` / `04-コスト`
4. 模試落ち → `06-review`

形式: UTF-8 / Tab / ヘッダなし / `表面` `裏面` `タグ`
