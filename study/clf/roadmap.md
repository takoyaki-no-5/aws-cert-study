# 学習ロードマップ

## 順番と工数

| # | 工程 | h |
|---|------|---|
| 1 | セキュリティとコンプライアンス（30%） | 1.5 |
| 2 | 請求・料金・サポート（12%） | 1.5 |
| 3 | クラウドの概念（24%） | 1.0 |
| 4 | クラウドテクノロジーとサービス（34%） | 1.5 |
| 5 | 模試60問 + 直し | 1.5 |
| 6 | Anki | 1.0 |
| | **合計** | **8.0** |

## 1. セキュリティとコンプライアンス（30%） — 1.5h

### 責任共有モデル — 15分

- [x] AWS の責任 / 顧客の責任 — 7分
- [x] EC2 / RDS / Lambda / S3 の境界 — 8分

### IAM — 25分

- [x] ユーザー / グループ / ロール / ポリシー — 5分
- [x] EC2 へはロール — 5分
- [x] ルートユーザー — 5分
- [x] MFA / パスワードポリシー / IAM Identity Center / フェデレーション — 5分
- [x] 最小権限 / Access Analyzer / 認証情報レポート — 5分

### マルチアカウント — 10分

- [x] Organizations — 4分
- [x] SCP — 3分
- [x] Control Tower — 3分

### 検出・保護 — 15分

- [x] GuardDuty / Inspector / Macie / Detective / Security Hub — 5分
- [x] Shield / WAF / Firewall Manager — 5分
- [x] Config / CloudTrail / Trusted Advisor — 5分

### データ保護 — 15分

- [x] KMS / CloudHSM — 4分
- [x] Secrets Manager / Parameter Store — 4分
- [x] ACM — 3分
- [x] 転送時 / 保存時の暗号化 — 4分

### ネットワークセキュリティ — 5分

- [x] セキュリティグループ / ネットワーク ACL — 5分

### コンプライアンス — 5分

- [x] Artifact / Audit Manager — 5分

## 2. 請求・料金・サポート（12%） — 1.5h

### 料金モデル — 35分

- [ ] オンデマンド / RI / Savings Plans / スポット — 12分
- [ ] Dedicated Hosts / Dedicated Instances — 7分
- [ ] 無料枠の3種類 — 8分
- [ ] データ転送料金 — 8分

### コスト管理 — 25分

- [ ] Cost Explorer / Budgets / CUR / Pricing Calculator — 12分
- [ ] コスト配分タグ — 8分
- [ ] Compute Optimizer — 5分

### 一括請求 — 10分

- [ ] Organizations 一括請求・ボリューム割引 — 10分

### サポートプラン — 15分

- [ ] Basic / Developer / Business / Enterprise（On-Ramp） — 15分

### その他 — 5分

- [ ] Marketplace / Professional Services / IQ / re:Post — 5分

## 3. クラウドの概念（24%） — 1.0h

### クラウドの価値提案 — 15分

- [ ] クラウドの6つのメリット — 5分
- [ ] CapEx / OpEx・従量課金 — 5分
- [ ] 弾力性 / スケーラビリティ / 高可用性 / 耐障害性 — 5分

### クラウドの形態 — 8分

- [ ] パブリック / ハイブリッド / オンプレミス — 4分
- [ ] IaaS / PaaS / SaaS — 4分

### Well-Architected — 10分

- [ ] 6本柱 — 5分
- [ ] キーワードから柱を当てる — 5分

### 移行と導入 — 12分

- [ ] CAF 6パースペクティブ — 4分
- [ ] 移行戦略 7R — 4分
- [ ] Migration Evaluator / Migration Hub — 4分

### グローバルインフラ — 15分

- [ ] リージョン / AZ / エッジロケーション — 5分
- [ ] マルチ AZ / マルチリージョン — 4分
- [ ] CloudFront / Global Accelerator — 3分
- [ ] Outposts / Local Zones / Wavelength — 3分

## 4. クラウドテクノロジーとサービス（34%） — 1.5h

### コンピューティング — 12分

- [ ] EC2・購入オプション — 3分
- [ ] Lambda — 2分
- [ ] ECS / EKS / Fargate — 3分
- [ ] Elastic Beanstalk / Lightsail — 2分
- [ ] Auto Scaling / ELB（ALB・NLB・GLB） — 2分

### ストレージ — 10分

- [ ] S3 ストレージクラス — 3分
- [ ] 耐久性・バージョニング・ライフサイクル — 3分
- [ ] EBS / EFS / FSx — 2分
- [ ] Storage Gateway / AWS Backup — 2分

### データベース — 10分

- [ ] RDS / Aurora — 3分
- [ ] DynamoDB — 2分
- [ ] ElastiCache — 2分
- [ ] Redshift — 2分
- [ ] Neptune / DocumentDB / QLDB — 1分

### ネットワーキング — 12分

- [ ] VPC（サブネット / IGW / NAT / ルートテーブル） — 5分
- [ ] VPN / Direct Connect / ピアリング / Transit Gateway — 4分
- [ ] Route 53 / CloudFront / API Gateway — 3分

### 分析 — 8分

- [ ] Athena / Glue — 3分
- [ ] Kinesis（Data Streams / Firehose） — 2分
- [ ] QuickSight — 2分
- [ ] EMR / OpenSearch — 1分

### ML・AI — 10分

- [ ] SageMaker — 3分
- [ ] Rekognition / Textract — 2分
- [ ] Polly / Transcribe / Translate — 2分
- [ ] Lex / Comprehend — 2分
- [ ] Kendra / Personalize / Forecast — 1分

### アプリケーション統合 — 5分

- [ ] SQS / SNS / EventBridge — 3分
- [ ] Step Functions — 2分

### 移行・データ転送 — 8分

- [ ] DMS — 2分
- [ ] Snow ファミリー — 2分
- [ ] DataSync / Transfer Family — 2分
- [ ] Application Migration Service (MGN) — 2分

### 開発者ツール・IaC — 8分

- [ ] CloudFormation / CDK — 3分
- [ ] CodeCommit / CodeBuild / CodeDeploy / CodePipeline — 3分
- [ ] コンソール / CLI / SDK / CloudShell — 2分

### 管理・監視 — 7分

- [ ] CloudWatch — 2分
- [ ] CloudTrail / Config — 2分
- [ ] Systems Manager — 1分
- [ ] Health Dashboard — 1分
- [ ] Service Catalog / X-Ray — 1分

## 5. 模試60問 + 直し — 1.5h

- [ ] 本の60問 — 1.0h
- [ ] 間違い直し — 0.5h

## 6. Anki — 1.0h

- [ ] 生成カードを周回 — 0.7h
- [ ] 弱点カード — 0.3h
