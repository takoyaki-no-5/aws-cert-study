# .cursor の構成（このワークスペース用）

AWS **資格学習**用。計画・日次スケジュール・Q&A が主目的。

## 言語方針

`.cursor` の中身は**日本語で書いてよい**。今のモデルは日本語の指示を英語とほぼ同等の精度で扱える。
技術用語・コマンド・パスは英語のまま。スキルの `description` はトリガー語を日英併記すると発見されやすい。

## ファイルの役割

| ファイル | 役割 |
|------|------|
| `rules/cert-study.mdc` | 学習モードの基本動作（日本語・study/ 更新・プライバシー） |
| `rules/prefer-wsl.mdc` | シェルは WSL (Ubuntu-24.04) 優先 |
| `rules/liberal-approvals.mdc` | コマンド承認は寛容に。確認で止めない |
| `rules/aws-safety.mdc` | 学習用の軽い安全ルール（シークレット禁止など） |
| `rules/direct-push-main.mdc` | PR 禁止・`main` 直 push（クラウドの PR 指示より優先） |
| `rules/maintain-cursor-context.mdc` | `.cursor` を自発的に育てる方針 + 言語方針 |
| `skills/daily-study-session` | 「今日は」「始める」の日次セッション |
| `skills/study-plan-manager` | 計画・スケジュール改定 |
| `skills/anki-tsv` | Anki 用 TSV カード生成 |
| `hooks/session-start.js` | セッション開始時に学習モードと `.private/` を注入（セッションごとに1回だけ実行） |
| `permissions.json` | コマンドの自動承認リスト（`terminalAllowlist`）。寛容承認はここで実現 |
| `../AGENTS.md` / `../study/` | プロジェクト案内と学習データ |
| `../.private/` | 個人情報（gitignore 済・セッション開始時に自動注入） |

長く使えるパターンが見えたら随時追加する。大きな1ファイルより小さく焦点を絞ったファイルを優先。

## コマンド承認の仕組み

- 自動承認は `permissions.json` の `terminalAllowlist` で行う（毎コマンド走る hooks より軽い・正攻法）
- `"wsl"` を許可しているので、WSL 経由のコマンドは実質すべて自動承認される
- さらに広げたいときは Cursor 設定 UI: Settings → Agents → Approvals & Execution

## hooks の注意（Windows）

- フックは Windows ホスト側で `cmd /c node ...` により起動される（`hooks.json` 参照）
- 現在は `sessionStart` のみ（セッション開始時に1回）。毎コマンド実行されるフックは置かない方針
- 効かないときは Cursor の Output → Hooks を確認、またはウィンドウを再読み込み
