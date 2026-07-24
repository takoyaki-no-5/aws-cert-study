# 学習ロードマップ

## AI と ML の基礎（20%）

### 基本用語

- [ ] AI / ML / ディープラーニング
- [ ] 教師あり / 教師なし / 強化学習
- [ ] 分類 / 回帰 / クラスタリング

### モデル品質

- [ ] 過学習 / 過少学習
- [ ] 訓練 / 検証 / テスト
- [ ] バイアス / 分散・データ品質

### ライフサイクルと推論

- [ ] 収集 → 前処理 → 学習 → 評価 → デプロイ → 監視
- [ ] リアルタイム推論 / バッチ推論
- [ ] ML が向く / 向かないケース

### AWS の層

- [ ] 上位 AI サービス / SageMaker / インフラ
- [ ] Rekognition / Textract / Polly / Transcribe / Translate / Lex / Comprehend / Kendra / Personalize / Forecast

## 生成 AI の基礎（24%）

### 中核概念

- [ ] 基盤モデル（FM）/ LLM
- [ ] トークン / コンテキストウィンドウ
- [ ] 埋め込み / ベクトル検索
- [ ] トランスフォーマー・自己注意

### できること・限界

- [ ] 要約 / 生成 / チャット / 翻訳
- [ ] ハルシネーション / 非決定性 / カットオフ / 毒性
- [ ] RAG・人間レビュー

### AWS サービス

- [ ] Bedrock
- [ ] Amazon Q（Business / Developer）
- [ ] PartyRock
- [ ] SageMaker JumpStart

## 基盤モデルの応用（28%）

### モデル選択・推論パラメータ

- [ ] コスト / レイテンシ / 多言語 / モダリティ / コンテキスト長 / カスタマイズ
- [ ] temperature / top-p / 最大トークン / 停止シーケンス

### カスタマイズ4手段

- [ ] プロンプトエンジニアリング
- [ ] RAG
- [ ] ファインチューニング
- [ ] 継続事前学習

### プロンプト技法

- [ ] zero-shot / few-shot / Chain of Thought
- [ ] インジェクション / ジェイルブレイク
- [ ] テンプレート / ネガティブプロンプト

### エージェント

- [ ] Bedrock Agents
- [ ] Bedrock Knowledge Bases
- [ ] Bedrock Guardrails

### 評価

- [ ] ROUGE / BLEU / BERTScore
- [ ] 人間評価

## 責任ある AI（14%）

### 柱

- [ ] 公平性 / 説明可能性 / 堅牢性 / プライバシー / 透明性 / ガバナンス
- [ ] データセットのバイアス

### ツール

- [ ] SageMaker Clarify
- [ ] SageMaker Model Monitor
- [ ] Bedrock Guardrails
- [ ] AI Service Cards / モデルカード

### リスク

- [ ] 著作権・幻覚・開示
- [ ] Human-in-the-loop（A2I）

## セキュリティ・コンプライアンス・ガバナンス（14%）

### セキュリティ

- [ ] IAM（Bedrock / SageMaker）
- [ ] KMS / TLS / PrivateLink
- [ ] Macie / Secrets Manager

### ガバナンス

- [ ] データリネージ・品質・ライフサイクル
- [ ] CloudTrail / Config / Audit Manager
- [ ] Model Registry / Model Cards

### コンプライアンス

- [ ] Artifact・データレジデンシー
- [ ] 自社データとモデル学習（Bedrock）
