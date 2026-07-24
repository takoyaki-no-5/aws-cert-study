# 学習ロードマップ

## クラウドの概念（24%）

### クラウドの価値提案

- [ ] クラウドの6つのメリット
- [ ] CapEx / OpEx・従量課金
- [ ] 弾力性 / スケーラビリティ / 高可用性 / 耐障害性

### クラウドの形態

- [ ] パブリック / ハイブリッド / オンプレミス
- [ ] IaaS / PaaS / SaaS

### Well-Architected

- [ ] 6本柱
- [ ] キーワードから柱を当てる

### 移行と導入

- [ ] CAF 6パースペクティブ
- [ ] 移行戦略 7R
- [ ] Migration Evaluator / Migration Hub

### グローバルインフラ

- [ ] リージョン / AZ / エッジロケーション
- [ ] マルチ AZ / マルチリージョン
- [ ] CloudFront / Global Accelerator
- [ ] Outposts / Local Zones / Wavelength

## セキュリティとコンプライアンス（30%）

### 責任共有モデル

- [ ] AWS の責任 / 顧客の責任
- [ ] EC2 / RDS / Lambda / S3 の境界

### IAM

- [ ] ユーザー / グループ / ロール / ポリシー
- [ ] EC2 へはロール
- [ ] ルートユーザー
- [ ] MFA / パスワードポリシー / IAM Identity Center / フェデレーション
- [ ] 最小権限 / Access Analyzer / 認証情報レポート

### マルチアカウント

- [ ] Organizations
- [ ] SCP
- [ ] Control Tower

### 検出・保護

- [ ] GuardDuty / Inspector / Macie / Detective / Security Hub
- [ ] Shield / WAF / Firewall Manager
- [ ] Config / CloudTrail / Trusted Advisor

### データ保護

- [ ] KMS / CloudHSM
- [ ] Secrets Manager / Parameter Store
- [ ] ACM
- [ ] 転送時 / 保存時の暗号化

### ネットワークセキュリティ

- [ ] セキュリティグループ / ネットワーク ACL

### コンプライアンス

- [ ] Artifact / Audit Manager

## クラウドテクノロジーとサービス（34%）

### コンピューティング

- [ ] EC2・購入オプション
- [ ] Lambda
- [ ] ECS / EKS / Fargate
- [ ] Elastic Beanstalk / Lightsail
- [ ] Auto Scaling / ELB（ALB・NLB・GLB）

### ストレージ

- [ ] S3 ストレージクラス
- [ ] 耐久性・バージョニング・ライフサイクル
- [ ] EBS / EFS / FSx
- [ ] Storage Gateway / AWS Backup

### データベース

- [ ] RDS / Aurora
- [ ] DynamoDB
- [ ] ElastiCache
- [ ] Redshift
- [ ] Neptune / DocumentDB / QLDB

### ネットワーキング

- [ ] VPC（サブネット / IGW / NAT / ルートテーブル）
- [ ] VPN / Direct Connect / ピアリング / Transit Gateway
- [ ] Route 53 / CloudFront / API Gateway

### 分析

- [ ] Athena / Glue
- [ ] Kinesis（Data Streams / Firehose）
- [ ] QuickSight
- [ ] EMR / OpenSearch

### ML・AI

- [ ] SageMaker
- [ ] Rekognition / Textract
- [ ] Polly / Transcribe / Translate
- [ ] Lex / Comprehend
- [ ] Kendra / Personalize / Forecast

### アプリケーション統合

- [ ] SQS / SNS / EventBridge
- [ ] Step Functions

### 移行・データ転送

- [ ] DMS
- [ ] Snow ファミリー
- [ ] DataSync / Transfer Family
- [ ] Application Migration Service (MGN)

### 開発者ツール・IaC

- [ ] CloudFormation / CDK
- [ ] CodeCommit / CodeBuild / CodeDeploy / CodePipeline
- [ ] コンソール / CLI / SDK / CloudShell

### 管理・監視

- [ ] CloudWatch
- [ ] CloudWatch / CloudTrail / Config
- [ ] Systems Manager
- [ ] Health Dashboard
- [ ] Service Catalog / X-Ray

## 請求・料金・サポート（12%）

### 料金モデル

- [ ] オンデマンド / RI / Savings Plans / スポット
- [ ] Dedicated Hosts / Dedicated Instances
- [ ] 無料枠の3種類
- [ ] データ転送料金

### コスト管理

- [ ] Cost Explorer / Budgets / CUR / Pricing Calculator
- [ ] コスト配分タグ
- [ ] Compute Optimizer

### 一括請求

- [ ] Organizations 一括請求・ボリューム割引

### サポートプラン

- [ ] Basic / Developer / Business / Enterprise（On-Ramp）

### その他

- [ ] Marketplace / Professional Services / IQ / re:Post
