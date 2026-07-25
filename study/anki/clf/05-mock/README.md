# 模試（CLF）

| ファイル | デッキ | 問数 |
|----------|--------|------|
| `01-mock-a.tsv` | `AWS::CLF::05-模試A` | 65 |
| `02-mock-b.tsv` | `AWS::CLF::05-模試B` | 65 |

## 構成（本番の配点比）

| ドメイン | 問数 |
|----------|------|
| クラウドの概念（24%） | 16 |
| セキュリティ（30%） | 19 |
| 技術とサービス（34%） | 22 |
| 請求・サポート（12%） | 8 |

複数選択（5択から2つ）は各セット9問。表面に選択肢、裏面に正解と1行の理由。

## 使い方

1セット65問を90分以内。表面で答えを決めてから裏面を見る。

```bash
python3 .cursor/hooks/anki-add.py --deck AWS::CLF::05-模試A study/anki/clf/05-mock/01-mock-a.tsv
python3 .cursor/hooks/anki-validate.py study/anki/clf/05-mock
```

間違えたものは `../06-review/` にカード化する。
