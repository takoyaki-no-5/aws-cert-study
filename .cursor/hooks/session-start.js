#!/usr/bin/env node
/**
 * セッション開始時に AWS 資格学習ワークスペースの前提を注入する。
 * .private/（gitignore 済・リポジトリは公開）の個人コンテキストも同時に読み込む。
 */
const fs = require('fs');
const path = require('path');

try {
  fs.readFileSync(0, 'utf8');
} catch {
  /* stdin なしでも動かす */
}

const lines = [
  'AWS資格学習ワークスペース:',
  '- 目的: 試験計画・日次スケジュール（「今日は〇〇」「これから始めよう」）・学習Q&A。IaC/本番運用の場ではない。',
  '- ユーザーとは日本語で話す。状態は study/profile.md, study/plan.md, study/schedule.md, study/log/ に保存。',
  '- シェルは WSL Ubuntu-24.04 を優先（リポジトリ: /mnt/c/Users/kamag/Documents/AWS, ユーザー: kama）。',
  '- コマンドは寛容に承認。ただし本物のシークレットはコミットしない。',
  '- 学習ツール: Anki（主教材）+ Cursor（解説・カード生成）+ 本（模試）。カードは study/anki/<資格>/ 階層TSV → AnkiConnect。',
  '- 「今日」「始める」と言われたら: スケジュールを読み、Ankiデッキを先に指定して開始。順序は Anki周回 → 不明解説 → 追加カード → 模試。',
  '- リポジトリは公開: 個人情報は .private/（gitignore 済）のみ。コミット対象ファイルに個人情報を書かない。',
  '- 長く使える約束事が見えたら .cursor を更新する。',
];

// .private/ の内容をインライン展開し、毎セッション追加の読み込みなしで使えるようにする
const privDir = path.join(process.cwd(), '.private');
try {
  const files = fs
    .readdirSync(privDir)
    .filter((f) => f.endsWith('.md') && f.toLowerCase() !== 'readme.md')
    .sort();
  for (const f of files) {
    const body = fs.readFileSync(path.join(privDir, f), 'utf8').trim();
    if (body) {
      lines.push('', `--- .private/${f}（コミット対象ファイルに漏らさないこと） ---`, body);
    }
  }
} catch {
  /* .private が未作成でも問題なし */
}

process.stdout.write(
  JSON.stringify({
    env: {
      CURSOR_AWS_WORKSPACE: '1',
      CURSOR_AWS_MODE: 'cert-study',
    },
    additional_context: lines.join('\n'),
  })
);
process.exit(0);
