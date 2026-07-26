# study/

AWS 資格学習の実体。**ルートも資格フォルダも同じ型**で揃える（構造的に扱えること優先）。

## 階層（固定）

```
study/
  README.md / plan.md / profile.md / schedule.md / books.md / tools.md
  _templates/          ← exam.md / roadmap.md / schedule.md / day.md
  <資格>/              ← 下表の必須セット（全12同一）
  anki/<資格>/         ← 工程フォルダ + TSV（未着手は README のみ可）
  log/                 ← YYYY-MM-DD.md
  notes/ / questions/  ← 資格横断のみ（固有は資格フォルダへ）
```

略称（12・順不同）: `clf` `saa` `scs` `sap` `ans` `dva` `soa` `dop` `dea` `aif` `mla` `aip`

## 資格フォルダ（必須・全同一）

| パス | 役割 |
|------|------|
| `exam.md` | 試験概要（時間・形式・合格点・学習時間。**共通フォーマット**） |
| `roadmap.md` | 題材のみ（順番と工数 → ドメイン → トピック → チェック） |
| `schedule.md` | 運用のみ（基本情報・フェーズ・日次・撤退・当日・振り返り） |
| `days/` | 日次（`YYYY-MM-DD.md`。立ち上げ前は空でよい） |
| `notes.md` / `questions.md` | 任意（資格固有） |

テンプレ: `_templates/` をコピー。見本: `clf/`（済） / `saa/`（進行中）。

## 今どこを見るか

1. `schedule.md`（ハブ）→ 進行中の試験
2. `study/<資格>/exam.md` → `schedule.md` + `roadmap.md`
3. 今日の `days/YYYY-MM-DD.md` / `log/YYYY-MM-DD.md`

## 立ち上げ

受験2週間前の日曜（Pro は3〜4週間前）。`exam.md` 確認 → `roadmap`/`schedule`/`days`/`anki` を埋める。
