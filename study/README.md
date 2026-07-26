# study/

AWS 資格学習の実体。全体計画はルート、進行中の詳細は資格フォルダ。

## 階層

```
study/
  plan.md / profile.md / schedule.md / books.md / tools.md
  _templates/          ← 立ち上げ時にコピー
  <資格>/              ← clf 型（下記）
  anki/<資格>/         ← 工程フォルダ + TSV
  log/                 ← 日次ログ（資格横断）
  notes/ / questions/  ← 資格横断のみ（固有は資格フォルダへ）
```

## 資格フォルダ（見本: `clf/`）

| パス | 役割 |
|------|------|
| `exam.md` | 試験概要（時間・問題形式・合格点・学習時間。全資格共通フォーマット） |
| `roadmap.md` | 題材のみ（順番と工数 → ドメイン → トピック → チェック） |
| `schedule.md` | 運用のみ（基本情報・フェーズ・日次・撤退・当日・振り返り） |
| `days/YYYY-MM-DD.md` | その日のゴール・時間割・題材チェック（当日生成） |
| `notes.md` / `questions.md` | 任意（資格固有） |

略称: `clf` `saa` `scs` `sap` `ans` `dva` `soa` `dop` `dea` `aif` `mla` `aip`

立ち上げ: 受験2週間前の日曜（Pro は3〜4週間前）。`_templates/` をコピーして埋める（`exam.md` 含む）。

## 今どこを見るか

1. `schedule.md`（ハブ）→ 進行中の試験
2. `study/<資格>/exam.md`（概要）→ `schedule.md` + `roadmap.md`
3. 今日の `days/YYYY-MM-DD.md` / `log/YYYY-MM-DD.md`
