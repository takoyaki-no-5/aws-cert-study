# AWS 資格学習

資格取得のための計画・スケジュール管理・学習Q&A用ワークスペース。

## ここでやること

- 学習計画の立案・更新
- 日次スケジュール（「今日は〇〇」「これから始めよう」まで落とす）
- 進捗の記録・振り返り
- 試験範囲の質問・解説・演習のやりとり

IaC や本番変更の作業場ではない（ハンズオン用メモは可）。

## エージェントへの指針

- シェル作業は **WSL**（`Ubuntu-24.04`、ユーザー `kama`）を優先。
- コマンドは寛容に承認し、確認で何度も止めない。
- 本物のシークレット / AWS 認証情報はコミットしない。
- **リポジトリは公開**: 個人情報は `.private/`（gitignore 済）のみ。コミット対象ファイルは匿名に保つ。
- 計画と進捗はリポジトリに保存し、セッションをまたいで続きから始められるようにする。
- **学習範囲をエージェント判断で削らない・飛ばさない**（ユーザーの経験を理由に省略しない）。時間配分の重み付けは可。飛ばす・削るはユーザーの指示か承認があったときのみ。
- **合格最短・資格ホルダー優先**: 実務に生かせるか・実力になるかは無視。配点・頻出・誤答選択肢の区別だけを最適化する。ハンズオンや深い実装はユーザーが求めたとき以外やらない。
- **受験順**: 内容が近いものを連続し、再学習を最小化（全冠・最速）。**CLF→SAA→SAP 軸は維持**。Pro の直前にはその Pro に近い非 Pro を置く（例: SCS→SAP、DVA+SOA→DOP、SAP→ANS、AIF→MLA→AIP）。非重複を軸の途中に挟まない。詳細は `study/plan.md`。
- **`study/` の文章は題材のみ・短く**（見本: `study/clf/roadmap.md`）。飾り見出し・長い説明文は書かない。詳細は `.cursor/rules/study-file-style.mdc`
- 長く使える学習の約束事が見えたら `.cursor` / このファイルを更新する。
- ユーザーとの言語は**日本語**（切り替えられない限り）。

## 構成

| パス | 用途 |
|------|------|
| `study/README.md` | 階層の地図 |
| `study/profile.md` | 目標資格・期限・学習時間・前提スキル |
| `study/tools.md` | 使用ツール（Cursor / Anki / 本） |
| `study/books.md` | 教材の本一覧と読書進捗 |
| `study/plan.md` | 全体計画（受験日・必要工数・週負荷。受験日固定） |
| `study/schedule.md` | 薄いハブ（今どの試験か + 全資格リンク + 常時ルール） |
| `study/<資格>/` | 資格ごとのフォルダ（下記「資格フォルダ規約」参照） |
| `study/log/` | 日次ログ（`YYYY-MM-DD.md`・資格横断） |
| `study/notes/` | 資格横断のメモ（資格固有は `study/<資格>/notes.md`） |
| `study/questions/` | 資格横断の弱点（資格固有は `study/<資格>/questions.md`） |
| `study/anki/<資格>/` | Anki TSV（工程フォルダ階層。見本: `anki/clf/`） |
| `.private/` | 個人情報（gitignore 済・公開しない。セッション開始時に自動でコンテキスト化） |

## 資格フォルダ規約（`study/<資格>/`）

- フォルダ名は小文字の略称: `clf`, `saa`, `scs`, `sap`, `ans`, `dva`, `soa`, `dop`, `dea`, `aif`, `mla`, `aip`
- 全12資格とも**同じ構成**（差分を作らない。見本: `study/clf/` / `study/saa/`）:
  - `exam.md` — **試験概要**（時間・問題数/形式・合格点・学習時間の一般vs今回。**全資格同一フォーマット** = `_templates/exam.md`）
  - `roadmap.md` — **題材のみ**（順番と工数 → ドメイン → トピック → 短いチェック）。運用・長い説明は書かない（文体: `study-file-style.mdc`）
  - `schedule.md` — **運用**: 基本情報・教材・フェーズ・平日の型・日次・撤退基準・当日・振り返り（短文）。合格点の詳細は `exam.md` へ
  - `days/` — 日次（`YYYY-MM-DD.md`。立ち上げ前は空可）
  - 任意: `notes.md` / `questions.md`（資格固有）
- 立ち上げ日曜（受験2週間前、Pro は3〜4週間前）に日次を確定し、`days/` を埋める。新規追加時は `_templates/` をコピー（`exam.md` 必須）
- Anki: `study/anki/<資格>/<工程>/<番号>-<トピック>.tsv`（フラット置きしない。未着手は `README.md` のみ可）
- **ルートも資格も同型**: `study/README.md` の階層を正とする。片方だけに置くファイルを増やさない

## 学習ツール

- **Cursor** — 計画・解説・スケジュール・カード生成
- **Anki** — TSV を `study/anki/` に生成してインポート（スキル: `anki-tsv`）
- **本** — 主教材。章単位でスケジュールし、要点を notes / Anki へ

## 作業環境（複数ある）

このワークスペースは複数の環境から開かれる。どこで動いているかは `session-start.js` フックが毎回自動判別し、コンテキスト先頭の `- 現在の環境:` に出す。

| 環境 | 実体 | 判別の手がかり |
|------|------|----------------|
| Windows ワークスペース（WSL 併用） | ユーザーのローカル PC。リポジトリ `/mnt/c/Users/kamag/Documents/AWS`、WSL `Ubuntu-24.04`（ユーザー `kama`）。hooks は Windows ホストで `cmd /c node` 起動 | `process.platform === 'win32'`、または WSL 内なら `WSL_DISTRO_NAME` / `/proc/version` に microsoft |
| Cursor Cloud（モバイル）ワークスペース | クラウド上の Linux VM（`/workspace`・`HOSTNAME=cursor`・`CURSOR_AGENT=1`） | cwd `/workspace` / `CURSOR_AGENT=1` / `HOSTNAME=cursor` |

- 明示ラベルを付けたいマシンでは **`.private/environment.md` の1行目**に環境名を書く（フックが最優先で採用する）。`.private/` は gitignore 済みなので**マシンごとに手動で置く**（git/PR では同期されない）。無くても上表の自動判別で動く。
- ターミナルは `.vscode/settings.json` により WSL がデフォルト（Windows 側）。

## Cursor Cloud specific instructions

- このリポジトリは**アプリ/サーバではなく学習データ + 自動化スクリプト**。`package.json` / `requirements.txt` / lockfile は無い。実行コードは `.cursor/hooks/` の Node/Python のみで、いずれも**標準ライブラリのみ**（追加 install 不要。`node` と `python3` はプリインストール済み）。
- クラウド VM は **Linux**。ローカルは Windows ホストで `cmd /c node` 起動だが、クラウドでは `node .cursor/hooks/xxx.js` / `python3 .cursor/hooks/xxx.py` を直接実行する。
- 「lint/test」相当は `bash .cursor/hooks/validate-hooks.sh`（`session-start.js` が有効な JSON を出すか検証）。ビルド工程は無い。
- session コンテキスト自動化の確認: `node .cursor/hooks/session-start.js </dev/null`（`.private/` があればその中身も注入する。無くても動く）。
- **Anki 系スクリプト**（`anki-add.py` / `anki-manage.py` / `anki-dedupe.py` / `clf-anki-*.py`）は Anki Desktop + AnkiConnect（`localhost:8765`）が前提。**クラウド VM には Anki が無いため接続エラーになるのが正常**。TSV の生成・パースはオフラインで動く（例: `anki-add.py` の `parse_tsv` を import して `study/anki/**/*.tsv` を読める）。
- `finish-push.sh` / `auth-web.sh` / `manual-auth.sh` / `install-gh.sh` はユーザーのローカル WSL 用（`finish-push.sh` は Windows 絶対パス直書き）。クラウドでは使わない。git 操作は通常の `git` コマンドで行う。
- **`.private/` はクラウドでは基本残らない**（gitignore 済みで git/PR で運ばれず、新セッションはスナップショットから起動する別 VM）。環境の自己判別はフックの自動判定（上表）に依存し、`.private/environment.md` はあくまで任意の上書きラベル。
- **PR を使わず `main` に直接 push する（ユーザー方針）**。新セッションが `cursor/...` ブランチ起点で始まっても、まず `git checkout main` してから commit → `git push origin main`（ローカルの `finish-push.sh` と同じ運用）。PR は作らない。
