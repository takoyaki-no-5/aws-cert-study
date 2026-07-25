# Anki TSV

資格ごとに工程フォルダで階層管理する。

```
study/anki/<資格>/
  01-.../
  02-.../
  ...
  05-mock/
  06-review/
```

| パス | 内容 |
|------|------|
| `clf/` | CLF（完成見本） |
| `saa/` … `aip/` | 各資格（立ち上げ後に TSV 追加） |

形式: UTF-8 / Tab / ヘッダなし / `表面` `裏面` `タグ`

投入: AnkiConnect（`anki-add.py`）優先。詳細は各資格フォルダの README。
