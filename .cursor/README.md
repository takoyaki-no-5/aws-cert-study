# .cursor の構成

AWSに関する質問へ日本語で回答するための設定。

## 基本方針

- 結論を先に、理由を簡潔に説明する。
- 選択問題は正解と各選択肢の判断理由を示す。
- 学習計画、進捗、Anki、Discord、ファイルを自動更新しない。
- リポジトリを変更するのは、ユーザーが明示的に依頼した場合だけ。

## 主なファイル

| ファイル | 役割 |
|------|------|
| `rules/cert-study.mdc` | AWS質問回答モード |
| `rules/anki-term-qa.mdc` | 用語質問でAnkiを自動更新しない |
| `rules/maintain-cursor-context.mdc` | 設定を自動変更しない |
| `rules/prefer-wsl.mdc` | シェルはWSLを優先 |
| `rules/direct-push-main.mdc` | PRを使わず`main`へ直接push |
| `hooks/session-start.js` | 質問回答モードをセッションへ注入 |
| `permissions.json` | コマンドの自動承認設定 |

既存の学習データや補助スクリプトは過去データとして残すが、通常の質問では読み書きしない。

## コマンド承認の仕組み

- 自動承認は `permissions.json` の `terminalAllowlist` で行う（毎コマンド走る hooks より軽い・正攻法）
- `"wsl"` を許可しているので、WSL 経由のコマンドは実質すべて自動承認される
- さらに広げたいときは Cursor 設定 UI: Settings → Agents → Approvals & Execution

## hooks の注意（Windows）

- フックは Windows ホスト側で `cmd /c node ...` により起動される（`hooks.json` 参照）
- 現在は `sessionStart` のみ（セッション開始時に1回）。毎コマンド実行されるフックは置かない方針
- 効かないときは Cursor の Output → Hooks を確認、またはウィンドウを再読み込み
