#!/usr/bin/env node
/**
 * セッション開始時に AWS 質問回答モードを注入する。
 */

try {
  require('fs').readFileSync(0, 'utf8');
} catch {
  /* stdin なしでも動かす */
}

const lines = [
  'AWS質問回答ワークスペース:',
  '- AWSに関する質問へ日本語で簡潔に回答する。',
  '- 結論を先に示し、理由・選択肢・試験上の対比を必要な範囲で説明する。',
  '- 学習計画、進捗、Anki、Discord、リポジトリ内ファイルは自動更新しない。',
  '- ファイル変更や外部操作は、ユーザーが明示的に依頼した場合だけ行う。',
];

process.stdout.write(
  JSON.stringify({
    env: {
      CURSOR_AWS_WORKSPACE: '1',
      CURSOR_AWS_MODE: 'qa',
    },
    additional_context: lines.join('\n'),
  })
);
process.exit(0);
