# CLF Anki 意味的重複レポート

- 対象（スキャン時）: 477 枚
- 類似ペア（cosine≥0.42）: 86
- **整理済み: 明らかな同一知識 18 枚を削除** → 現在約 **459 枚**
- 残した類似は「定義と別角度」「対比の別側面」など学習価値があるもの

## 削除した例（同じ知識の二重化）

- Trusted Advisor の説明 ↔ カテゴリ例
- CloudTrail/Config の区別が2箇所
- Secrets vs Parameter Store が3〜4枚 → 1系統に
- Business最低プラン / Dev vs Business 差 / Basic範囲の言い換え重複
- DNSフェイルオーバ、Fargate、DynamoDB、Pricing Calculator、CUR などの定義⇔シナリオ二重

詳細ペア一覧は下記（削除前のスキャン結果）。

## 強い重複候補（上位）

### 0.74
- A: Trusted Advisor は？
  - コスト・性能・セキュリティ・耐障害性・サービスの制限のベストプラクティス検査
  - `study/anki/clf/01-security/04-detect-protect.tsv:10`
- B: Trusted Advisorのカテゴリ例は？
  - コスト・性能・セキュリティ・耐障害性・サービス制限
  - `study/anki/clf/01-security/11-hy-detect-protect.tsv:13`

### 0.70
- A: CloudTrailとConfigを一言で区別すると？
  - Trail=操作 / Config=状態
  - `study/anki/clf/01-security/11-hy-detect-protect.tsv:12`
- B: CloudTrail と Config の違いは？（再確認）
  - Trail=操作ログ / Config=構成履歴と準拠
  - `study/anki/clf/04-services/10-management.tsv:2`

### 0.70
- A: Secrets Manager と Parameter Store の違いは？
  - Secrets=秘密の自動ローテ向け有料寄り / Parameter=設定値中心（SecureString可）
  - `study/anki/clf/01-security/05-data-protection.tsv:2`
- B: 「秘密鍵を自動ローテさせたい」Secrets Manager と Parameter Store どちら？
  - Secrets Manager
  - `study/anki/clf/01-security/08-scenarios.tsv:12`

### 0.69
- A: Secrets Manager と Parameter Store の違いは？
  - Secrets=秘密の自動ローテ向け有料寄り / Parameter=設定値中心（SecureString可）
  - `study/anki/clf/01-security/05-data-protection.tsv:2`
- B: Systems Manager Parameter StoreとSecretsの使い分け再確認は？
  - 設定=Parameter寄り / 秘密ローテ=Secrets寄り
  - `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:17`

### 0.66
- A: CUR（Cost and Usage Report）は？
  - 最も詳細な利用明細をS3へ出力
  - `study/anki/clf/02-billing/02-cost-management.tsv:3`
- B: 「最も詳細な利用内訳CSVが欲しい」何？
  - CUR（Cost and Usage Report）
  - `study/anki/clf/02-billing/06-scenarios.tsv:7`

### 0.66
- A: 「DNSフェイルオーバ」何？
  - Route 53
  - `study/anki/clf/04-services/11-scenarios.tsv:28`
- B: 「DNSでプライマリ死んだらセカンダリ」何？
  - Route 53フェイルオーバ
  - `study/anki/clf/04-services/13-hy-db-net.tsv:19`

### 0.64
- A: 「秘密鍵を自動ローテさせたい」Secrets Manager と Parameter Store どちら？
  - Secrets Manager
  - `study/anki/clf/01-security/08-scenarios.tsv:12`
- B: Systems Manager Parameter StoreとSecretsの使い分け再確認は？
  - 設定=Parameter寄り / 秘密ローテ=Secrets寄り
  - `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:17`

### 0.62
- A: 本番障害で24/365サポートが必要な最低プランは？
  - Business 以上
  - `study/anki/clf/02-billing/04-support-plans.tsv:5`
- B: 「本番障害で電話サポートが要る」最低プランは？
  - Business
  - `study/anki/clf/02-billing/06-scenarios.tsv:10`

### 0.62
- A: Developer と Business の最大の差は？
  - 本番向け24/365と応答目標・Trusted Advisor全項目はBusiness側
  - `study/anki/clf/02-billing/06-scenarios.tsv:18`
- B: DeveloperとBusinessの決定的差を一言で？
  - 本番向けの緊急度・チャネル・Trusted Advisor範囲
  - `study/anki/clf/02-billing/07-hy-support.tsv:10`

### 0.60
- A: Business サポートは？
  - 本番向け。24時間電話・Trusted Advisor全項目・短めの応答目標
  - `study/anki/clf/02-billing/04-support-plans.tsv:3`
- B: Developer と Business の最大の差は？
  - 本番向け24/365と応答目標・Trusted Advisor全項目はBusiness側
  - `study/anki/clf/02-billing/06-scenarios.tsv:18`

### 0.59
- A: PaaSの例は？
  - Elastic Beanstalk 等
  - `study/anki/clf/03-concepts/08-hy-basics-7r.tsv:10`
- B: 「コードをzipで上げるとURLが欲しい」Paas的？
  - Elastic Beanstalk
  - `study/anki/clf/04-services/12-hy-compute-storage.tsv:6`

### 0.58
- A: Basic サポートは？
  - 無料。アカウント/請求のサポートとTrusted Advisorのコアチェック等
  - `study/anki/clf/02-billing/04-support-plans.tsv:1`
- B: Basicで使えるサポート範囲の中心は？
  - アカウントと請求、＋Trusted Advisorの限定チェック等
  - `study/anki/clf/02-billing/07-hy-support.tsv:1`

### 0.58
- A: PaaSの例は？
  - Elastic Beanstalk 等
  - `study/anki/clf/03-concepts/08-hy-basics-7r.tsv:10`
- B: Elastic Beanstalk は？
  - アプリを上げると環境を自動構築するPaaS的サービス
  - `study/anki/clf/04-services/01-compute.tsv:4`

### 0.57
- A: Firewall Manager は？
  - Organizations全体にWAF/Shield等のルールを中央配布
  - `study/anki/clf/01-security/04-detect-protect.tsv:7`
- B: Firewall Managerの前提になりやすいものは？
  - Organizationsでの中央管理
  - `study/anki/clf/01-security/11-hy-detect-protect.tsv:9`

### 0.57
- A: EC2 に AWS API 権限を付ける正しい方法は？
  - インスタンスプロファイル（IAM ロール）。アクセスキーを埋め込まない
  - `study/anki/clf/01-security/02-iam.tsv:2`
- B: 「EC2上のアプリがS3にアクセス」正しい権限の付け方は？
  - EC2にIAMロール（インスタンスプロファイル）。キーを埋め込まない
  - `study/anki/clf/01-security/08-scenarios.tsv:1`

### 0.56
- A: 「コンテナはあるがサーバは管理したくない」何？
  - Fargate（ECS/EKSの起動タイプ）
  - `study/anki/clf/04-services/11-scenarios.tsv:2`
- B: 「コンテナのサーバ管理をしたくない」何？
  - Fargate
  - `study/anki/clf/04-services/12-hy-compute-storage.tsv:5`

### 0.56
- A: Pricing Calculator は？
  - 導入前の見積もりツール
  - `study/anki/clf/02-billing/02-cost-management.tsv:4`
- B: 「導入前に月額を概算したい」何？
  - Pricing Calculator
  - `study/anki/clf/02-billing/06-scenarios.tsv:6`

### 0.56
- A: Trusted Advisor全チェックが見られるプラン帯は？
  - Business以上（Basicは限定）
  - `study/anki/clf/01-security/11-hy-detect-protect.tsv:14`
- B: 「無料のTrusted Advisorは全部使える？」
  - いいえ。Basicはコアチェック限定。全項目はBusiness以上
  - `study/anki/clf/02-billing/06-scenarios.tsv:12`

### 0.56
- A: Secrets Manager と Parameter Store の違いは？
  - Secrets=秘密の自動ローテ向け有料寄り / Parameter=設定値中心（SecureString可）
  - `study/anki/clf/01-security/05-data-protection.tsv:2`
- B: Parameter Storeの向きは？
  - 設定値・階層パラメータ（秘密もSecureString可）
  - `study/anki/clf/01-security/12-hy-crypto-nacl.tsv:4`

### 0.55
- A: Control Tower は何用？
  - マルチアカウント環境のランディングゾーンを自動セットアップ・ガバナンス
  - `study/anki/clf/01-security/03-multi-account.tsv:3`
- B: Control Towerのランディングゾーンとは？
  - 推奨される初期マルチアカウント構成の土台
  - `study/anki/clf/01-security/13-hy-orgs.tsv:5`

### 0.54
- A: DMSの均一移行とは？
  - 同じエンジン同士（例: Oracle→Oracle）
  - `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:1`
- B: DMSの異種移行とは？
  - エンジンが違う（例: Oracle→Aurora PostgreSQL）
  - `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:2`

### 0.54
- A: 「秘密鍵を自動ローテさせたい」Secrets Manager と Parameter Store どちら？
  - Secrets Manager
  - `study/anki/clf/01-security/08-scenarios.tsv:12`
- B: Secrets Managerの売りの一つは？
  - 秘密の自動ローテーション連携
  - `study/anki/clf/01-security/12-hy-crypto-nacl.tsv:3`

### 0.54
- A: 「外部に公開されているS3がないか」何で点検？
  - IAM Access Analyzer（またはTrusted Advisor/Security Hub）
  - `study/anki/clf/01-security/08-scenarios.tsv:17`
- B: 「公開バケット」を見つけたい第一候補は？
  - Access Analyzer / Trusted Advisor / MacieやSecurity Hub連携も
  - `study/anki/clf/01-security/11-hy-detect-protect.tsv:18`

### 0.54
- A: 「キーバリューでミリ秒、サーバレスDB」何？
  - DynamoDB
  - `study/anki/clf/04-services/11-scenarios.tsv:9`
- B: 「超高トラフィックのキーバリュー」何？
  - DynamoDB
  - `study/anki/clf/04-services/13-hy-db-net.tsv:2`

### 0.53
- A: Pricing Calculator は？
  - 導入前の見積もりツール
  - `study/anki/clf/02-billing/02-cost-management.tsv:4`
- B: Pricing Calculatorはアカウント作成後専用？
  - いいえ。見積もりは事前にも使える
  - `study/anki/clf/02-billing/09-hy-tools.tsv:5`

### 0.53
- A: Migration Evaluator は？
  - 移行のコスト評価・ビジネスケース作成支援
  - `study/anki/clf/03-concepts/04-migration.tsv:3`
- B: Migration Evaluatorの価値は？
  - コスト試算で移行の正当化材料を作る
  - `study/anki/clf/03-concepts/08-hy-basics-7r.tsv:16`

### 0.52
- A: 「HTTPのパスで振り分け」LBはどれ？
  - ALB
  - `study/anki/clf/04-services/11-scenarios.tsv:4`
- B: 「ホストヘッダで振り分け」LBは？
  - ALB
  - `study/anki/clf/04-services/12-hy-compute-storage.tsv:9`

### 0.51
- A: Control Tower は何用？
  - マルチアカウント環境のランディングゾーンを自動セットアップ・ガバナンス
  - `study/anki/clf/01-security/03-multi-account.tsv:3`
- B: 「マルチアカウントの初期セットアップを標準化」何？
  - Control Tower
  - `study/anki/clf/01-security/08-scenarios.tsv:18`

### 0.51
- A: Developer と Business の最大の差は？
  - 本番向け24/365と応答目標・Trusted Advisor全項目はBusiness側
  - `study/anki/clf/02-billing/06-scenarios.tsv:18`
- B: Businessで初めて得られる代表的なものと言えば？
  - 24/365の技術サポート、Trusted Advisor全項目、短い応答目標
  - `study/anki/clf/02-billing/07-hy-support.tsv:3`

### 0.51
- A: S3 Standard向きは？
  - 頻繁にアクセスするデータ
  - `study/anki/clf/04-services/12-hy-compute-storage.tsv:11`
- B: S3 Standard-IA向きは？
  - アクセスは少ないがすぐ取りたい
  - `study/anki/clf/04-services/12-hy-compute-storage.tsv:12`

### 0.50
- A: 責任共有で「物理DC・ラック・電源」は誰？
  - AWS
  - `study/anki/clf/01-security/09-hy-shared.tsv:1`
- B: 責任共有で「ハイパーバイザ」は誰？
  - AWS
  - `study/anki/clf/01-security/09-hy-shared.tsv:2`

### 0.50
- A: Elastic Beanstalk は？
  - アプリを上げると環境を自動構築するPaaS的サービス
  - `study/anki/clf/04-services/01-compute.tsv:4`
- B: 「コードをzipで上げるとURLが欲しい」Paas的？
  - Elastic Beanstalk
  - `study/anki/clf/04-services/12-hy-compute-storage.tsv:6`

### 0.50
- A: AWS Organizations の主な用途は？
  - 複数アカウントの統合管理・一括請求・SCP
  - `study/anki/clf/01-security/03-multi-account.tsv:1`
- B: Organizationsの管理アカウントの役割は？
  - 組織の作成・一括請求の支払い側など
  - `study/anki/clf/01-security/13-hy-orgs.tsv:1`

### 0.50
- A: Lex / Comprehend は？
  - Lex=チャットボット / Comprehend=テキストの感情・エンティティ分析
  - `study/anki/clf/04-services/06-ml-ai.tsv:5`
- B: Comprehendは？
  - テキストの洞察（感情・キーフレーズ等）
  - `study/anki/clf/04-services/14-hy-integration-analytics-ml.tsv:19`

### 0.50
- A: Business サポートは？
  - 本番向け。24時間電話・Trusted Advisor全項目・短めの応答目標
  - `study/anki/clf/02-billing/04-support-plans.tsv:3`
- B: Businessで初めて得られる代表的なものと言えば？
  - 24/365の技術サポート、Trusted Advisor全項目、短い応答目標
  - `study/anki/clf/02-billing/07-hy-support.tsv:3`

### 0.49
- A: Audit Manager は？
  - 監査証拠の継続収集を自動化し評価を支援
  - `study/anki/clf/01-security/07-compliance.tsv:2`
- B: Audit Managerの価値は？
  - 監査用エビデンス収集の自動化
  - `study/anki/clf/01-security/12-hy-crypto-nacl.tsv:14`

### 0.49
- A: Security Hub は？
  - 複数セキュリティサービスの検出結果を集約・準拠チェック
  - `study/anki/clf/01-security/04-detect-protect.tsv:5`
- B: 「セキュリティ検出結果を1画面に集めたい」何？
  - Security Hub
  - `study/anki/clf/01-security/08-scenarios.tsv:20`

### 0.49
- A: Cost Explorer は？
  - 過去・予測のコスト可視化・分析UI
  - `study/anki/clf/02-billing/02-cost-management.tsv:1`
- B: Cost Explorerでできることの中心は？
  - 可視化・フィルタ・予測の確認
  - `study/anki/clf/02-billing/09-hy-tools.tsv:1`

### 0.48
- A: 「オブジェクトを安く長期保管、すぐ読まなくてよい」S3は？
  - Glacier / Glacier Deep Archive 系
  - `study/anki/clf/04-services/11-scenarios.tsv:6`
- B: S3 Glacier Flexible / Deep Archive向きは？
  - 取り出しが遅くてよい超長期保管
  - `study/anki/clf/04-services/12-hy-compute-storage.tsv:14`

### 0.48
- A: Pollyの入力と出力は？
  - テキスト→音声
  - `study/anki/clf/04-services/14-hy-integration-analytics-ml.tsv:16`
- B: Transcribeの入力と出力は？
  - 音声→テキスト
  - `study/anki/clf/04-services/14-hy-integration-analytics-ml.tsv:17`

### 0.48
- A: IAM Identity Center（旧SSO）は何用？
  - 複数アカウント／アプリへのシングルサインオン・中央での権限管理
  - `study/anki/clf/01-security/02-iam.tsv:5`
- B: IAM Identity Centerが向くケースは？
  - 多数アカウント/多数ユーザーへのSSO
  - `study/anki/clf/01-security/10-hy-iam.tsv:13`

### 0.48
- A: 「最小権限・暗号化」はどの柱？
  - セキュリティ
  - `study/anki/clf/03-concepts/03-well-architected.tsv:3`
- B: セキュリティでよく出る設計は？
  - 最小権限・暗号化・監視
  - `study/anki/clf/03-concepts/07-hy-wa.tsv:9`

### 0.47
- A: 「障害から自動復旧」はどの柱？
  - 信頼性
  - `study/anki/clf/03-concepts/03-well-architected.tsv:2`
- B: 「故障は起きる前提」はどの柱？
  - 信頼性
  - `study/anki/clf/03-concepts/07-hy-wa.tsv:15`

### 0.47
- A: Kinesis Data Streams と Firehose の違いは？
  - Streams=リアルタイム処理用ストリーム / Firehose=S3等へほぼ準備なしで配信
  - `study/anki/clf/04-services/05-analytics.tsv:3`
- B: 「リアルタイムに自分で消費者を書くストリーム」何？
  - Kinesis Data Streams
  - `study/anki/clf/04-services/11-scenarios.tsv:14`

### 0.47
- A: Trusted Advisor全チェックが見られるプラン帯は？
  - Business以上（Basicは限定）
  - `study/anki/clf/01-security/11-hy-detect-protect.tsv:14`
- B: Trusted Advisorが一部しか見えないプランは？
  - Basic（と条件により限定）
  - `study/anki/clf/02-billing/07-hy-support.tsv:7`

### 0.47
- A: ElastiCache は？
  - マネージドRedis/Memcachedキャッシュ
  - `study/anki/clf/04-services/03-database.tsv:4`
- B: 「セッションを高速キャッシュ」何？
  - ElastiCache
  - `study/anki/clf/04-services/13-hy-db-net.tsv:3`

### 0.47
- A: Migration Hub は？
  - 移行プロジェクトの進捗を中央で追跡
  - `study/anki/clf/03-concepts/04-migration.tsv:4`
- B: Migration Hubの価値は？
  - 複数移行ツールの進捗を一箇所で追う
  - `study/anki/clf/03-concepts/08-hy-basics-7r.tsv:15`

### 0.47
- A: 「ペタバイト分析DWH」何？
  - Redshift
  - `study/anki/clf/04-services/11-scenarios.tsv:11`
- B: 「BI用に列指向で集計」何？
  - Redshift
  - `study/anki/clf/04-services/13-hy-db-net.tsv:4`

### 0.46
- A: CLI / SDK / CloudShell は？
  - CLI=コマンド / SDK=コードからAPI / CloudShell=ブラウザの用意されたシェル
  - `study/anki/clf/04-services/09-devtools-iac.tsv:4`
- B: CloudShellの利点は？
  - ブラウザですぐCLI、認証済み
  - `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:13`

### 0.46
- A: Polly / Transcribe / Translate は？
  - Polly=音声合成 / Transcribe=音声→文字 / Translate=翻訳
  - `study/anki/clf/04-services/06-ml-ai.tsv:4`
- B: 「音声を字幕に」何？
  - Transcribe
  - `study/anki/clf/04-services/11-scenarios.tsv:21`

### 0.46
- A: 「ログをほぼ自動でS3へストリーム」何？
  - Kinesis Data Firehose
  - `study/anki/clf/04-services/11-scenarios.tsv:13`
- B: 「リアルタイムに自分で消費者を書くストリーム」何？
  - Kinesis Data Streams
  - `study/anki/clf/04-services/11-scenarios.tsv:14`

### 0.46
- A: 「まだ移さない」7Rは？
  - Retain
  - `study/anki/clf/03-concepts/06-scenarios.tsv:13`
- B: 「捨てる」7Rは？
  - Retire
  - `study/anki/clf/03-concepts/06-scenarios.tsv:14`

### 0.46
- A: 「誰がいつIAMを変えたか知りたい」何を見る？
  - CloudTrail
  - `study/anki/clf/01-security/08-scenarios.tsv:7`
- B: 「誰がいつセキュリティグループを変えた」一次情報は？
  - CloudTrail
  - `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:22`

### 0.46
- A: EMR / OpenSearch は？
  - EMR=ビッグデータ（Spark等） / OpenSearch=検索・ログ分析
  - `study/anki/clf/04-services/05-analytics.tsv:5`
- B: OpenSearchの典型用途は？
  - ログ検索・全文検索
  - `study/anki/clf/04-services/14-hy-integration-analytics-ml.tsv:12`

### 0.46
- A: Service Catalog は？
  - 承認済み製品をユーザーにセルフサービス提供
  - `study/anki/clf/04-services/10-management.tsv:5`
- B: Service Catalogの利用者メリットは？
  - 承認済み構成だけをポータルから起動
  - `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:21`

### 0.46
- A: 「無料のTrusted Advisorは全部使える？」
  - いいえ。Basicはコアチェック限定。全項目はBusiness以上
  - `study/anki/clf/02-billing/06-scenarios.tsv:12`
- B: Developer と Business の最大の差は？
  - 本番向け24/365と応答目標・Trusted Advisor全項目はBusiness側
  - `study/anki/clf/02-billing/06-scenarios.tsv:18`

### 0.45
- A: 「全アカウントで特定サービスを禁止したい」何を使う？
  - Organizations の SCP
  - `study/anki/clf/01-security/08-scenarios.tsv:3`
- B: 「アカウントを増やしても請求書は1枚にしたい」何？
  - Organizations 一括請求
  - `study/anki/clf/02-billing/06-scenarios.tsv:13`

### 0.45
- A: Trusted Advisor全チェックが見られるプラン帯は？
  - Business以上（Basicは限定）
  - `study/anki/clf/01-security/11-hy-detect-protect.tsv:14`
- B: Developer と Business の最大の差は？
  - 本番向け24/365と応答目標・Trusted Advisor全項目はBusiness側
  - `study/anki/clf/02-billing/06-scenarios.tsv:18`

### 0.45
- A: Polly / Transcribe / Translate は？
  - Polly=音声合成 / Transcribe=音声→文字 / Translate=翻訳
  - `study/anki/clf/04-services/06-ml-ai.tsv:4`
- B: Translateは？
  - テキストの言語変換
  - `study/anki/clf/04-services/14-hy-integration-analytics-ml.tsv:18`

### 0.45
- A: 「プライベートサブネットからパッチ適用したいがSSH鍵は嫌」何？
  - Systems Manager Session Manager 等
  - `study/anki/clf/04-services/11-scenarios.tsv:27`
- B: Session Managerの利点は？
  - SSHポートを開けずにシェル
  - `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:18`

### 0.45
- A: 責任共有で「セキュリティグループ設定」は誰？
  - 顧客
  - `study/anki/clf/01-security/09-hy-shared.tsv:4`
- B: 責任共有で「IAMユーザー作成」は誰？
  - 顧客
  - `study/anki/clf/01-security/09-hy-shared.tsv:9`

### 0.45
- A: Kinesis Data Streams と Firehose の違いは？
  - Streams=リアルタイム処理用ストリーム / Firehose=S3等へほぼ準備なしで配信
  - `study/anki/clf/04-services/05-analytics.tsv:3`
- B: 「ログをほぼ自動でS3へストリーム」何？
  - Kinesis Data Firehose
  - `study/anki/clf/04-services/11-scenarios.tsv:13`

### 0.45
- A: 「BYOLで物理ソケットが必要」何？
  - Dedicated Hosts
  - `study/anki/clf/02-billing/06-scenarios.tsv:15`
- B: Dedicated Hostが必要な典型理由は？
  - 既存ソケット/コア課金ライセンス、規制で物理専有
  - `study/anki/clf/02-billing/08-hy-pricing.tsv:7`

### 0.45
- A: Health Dashboard は？
  - AWS側の障害・メンテが自アカウントに与える影響を表示
  - `study/anki/clf/04-services/10-management.tsv:4`
- B: Health Dashboardでわかることの例は？
  - AWS側障害が自分のリソースに関係するか
  - `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:19`

### 0.45
- A: 「本番障害で電話サポートが要る」最低プランは？
  - Business
  - `study/anki/clf/02-billing/06-scenarios.tsv:10`
- B: インフラ障害で電話したい → 最低どのプラン？
  - Business
  - `study/anki/clf/02-billing/07-hy-support.tsv:5`

### 0.45
- A: AWS Marketplace は？
  - サードパーティのソフト/AMI/SaaSを調達・課金する場
  - `study/anki/clf/02-billing/05-other.tsv:1`
- B: 「サードパーティのAMIを課金付きで買いたい」どこ？
  - Marketplace
  - `study/anki/clf/02-billing/06-scenarios.tsv:16`

### 0.45
- A: Business サポートは？
  - 本番向け。24時間電話・Trusted Advisor全項目・短めの応答目標
  - `study/anki/clf/02-billing/04-support-plans.tsv:3`
- B: DeveloperとBusinessの決定的差を一言で？
  - 本番向けの緊急度・チャネル・Trusted Advisor範囲
  - `study/anki/clf/02-billing/07-hy-support.tsv:10`

### 0.45
- A: 「マルチアカウントの初期セットアップを標準化」何？
  - Control Tower
  - `study/anki/clf/01-security/08-scenarios.tsv:18`
- B: Control Towerのランディングゾーンとは？
  - 推奨される初期マルチアカウント構成の土台
  - `study/anki/clf/01-security/13-hy-orgs.tsv:5`

### 0.45
- A: DynamoDB は？
  - サーバレスNoSQLキーバリュー/ドキュメント。超低レイテンシ
  - `study/anki/clf/04-services/03-database.tsv:3`
- B: 「キーバリューでミリ秒、サーバレスDB」何？
  - DynamoDB
  - `study/anki/clf/04-services/11-scenarios.tsv:9`

### 0.44
- A: 責任共有で「データの分類・暗号化の選択」は誰？
  - 顧客
  - `study/anki/clf/01-security/09-hy-shared.tsv:8`
- B: 責任共有で「IAMユーザー作成」は誰？
  - 顧客
  - `study/anki/clf/01-security/09-hy-shared.tsv:9`

### 0.44
- A: Polly / Transcribe / Translate は？
  - Polly=音声合成 / Transcribe=音声→文字 / Translate=翻訳
  - `study/anki/clf/04-services/06-ml-ai.tsv:4`
- B: Transcribeの入力と出力は？
  - 音声→テキスト
  - `study/anki/clf/04-services/14-hy-integration-analytics-ml.tsv:17`

### 0.44
- A: 責任共有で「S3バケットを公開にするか」は誰？
  - 顧客
  - `study/anki/clf/01-security/09-hy-shared.tsv:5`
- B: 責任共有で「IAMユーザー作成」は誰？
  - 顧客
  - `study/anki/clf/01-security/09-hy-shared.tsv:9`

### 0.44
- A: 「自社DCでAWSのAPIを使いたい」何？
  - Outposts
  - `study/anki/clf/03-concepts/06-scenarios.tsv:18`
- B: Outpostsの一言は？
  - AWSを自社DCに延長
  - `study/anki/clf/03-concepts/08-hy-basics-7r.tsv:22`

### 0.44
- A: Secrets Manager と Parameter Store の違いは？
  - Secrets=秘密の自動ローテ向け有料寄り / Parameter=設定値中心（SecureString可）
  - `study/anki/clf/01-security/05-data-protection.tsv:2`
- B: Secrets Managerの売りの一つは？
  - 秘密の自動ローテーション連携
  - `study/anki/clf/01-security/12-hy-crypto-nacl.tsv:3`

### 0.44
- A: 「オンプレとAWSを専用線」何？
  - Direct Connect
  - `study/anki/clf/04-services/11-scenarios.tsv:29`
- B: Direct Connectの利点は？
  - 安定帯域・低揺らぎ・閉域寄り接続
  - `study/anki/clf/04-services/13-hy-db-net.tsv:15`

### 0.43
- A: Trusted Advisor全チェックが見られるプラン帯は？
  - Business以上（Basicは限定）
  - `study/anki/clf/01-security/11-hy-detect-protect.tsv:14`
- B: Business サポートは？
  - 本番向け。24時間電話・Trusted Advisor全項目・短めの応答目標
  - `study/anki/clf/02-billing/04-support-plans.tsv:3`

### 0.43
- A: 「導入前に月額を概算したい」何？
  - Pricing Calculator
  - `study/anki/clf/02-billing/06-scenarios.tsv:6`
- B: Pricing Calculatorはアカウント作成後専用？
  - いいえ。見積もりは事前にも使える
  - `study/anki/clf/02-billing/09-hy-tools.tsv:5`

### 0.43
- A: Transfer Family は？
  - SFTP/FTPS/FTPでS3/EFSへアクセスさせる
  - `study/anki/clf/04-services/08-migration-transfer.tsv:4`
- B: Transfer Familyが効くのは？
  - 既存SFTPクライアントを変えずにS3へ
  - `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:5`

### 0.43
- A: 「請求の問い合わせだけ」どのプランでもできる？
  - Basicでもアカウント/請求のサポートは受けられる
  - `study/anki/clf/02-billing/06-scenarios.tsv:20`
- B: 「請求額の問い合わせ」だけならBasicで足りる？
  - 足りる（アカウント/請求サポート）
  - `study/anki/clf/02-billing/07-hy-support.tsv:9`

### 0.43
- A: CodeCommit / CodeBuild / CodeDeploy は？
  - Commit=Gitリポ / Build=ビルド / Deploy=デプロイ自動化
  - `study/anki/clf/04-services/09-devtools-iac.tsv:3`
- B: CodeCommitは何の代替？
  - マネージドGitリポジトリ
  - `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:9`

### 0.43
- A: Organizationsの管理アカウントの役割は？
  - 組織の作成・一括請求の支払い側など
  - `study/anki/clf/01-security/13-hy-orgs.tsv:1`
- B: 「アカウントを増やしても請求書は1枚にしたい」何？
  - Organizations 一括請求
  - `study/anki/clf/02-billing/06-scenarios.tsv:13`

### 0.42
- A: IaaS / PaaS / SaaS の違いは？
  - IaaS=基盤貸し（EC2） / PaaS=実行基盤（Beanstalk等） / SaaS=完成アプリ
  - `study/anki/clf/03-concepts/02-cloud-models.tsv:2`
- B: PaaSの例は？
  - Elastic Beanstalk 等
  - `study/anki/clf/03-concepts/08-hy-basics-7r.tsv:10`

### 0.42
- A: CloudFront と Global Accelerator の違いは？
  - CloudFront=コンテンツキャッシュCDN / GA=エニーキャストで最適経路（非キャッシュ用途も）
  - `study/anki/clf/03-concepts/05-global-infrastructure.tsv:5`
- B: CloudFrontのキャッシュの利点は？
  - オリジン負荷低減＋低遅延
  - `study/anki/clf/03-concepts/08-hy-basics-7r.tsv:20`

### 0.42
- A: 「音声を字幕に」何？
  - Transcribe
  - `study/anki/clf/04-services/11-scenarios.tsv:21`
- B: Transcribeの入力と出力は？
  - 音声→テキスト
  - `study/anki/clf/04-services/14-hy-integration-analytics-ml.tsv:17`

### 0.42
- A: Parameter Storeの向きは？
  - 設定値・階層パラメータ（秘密もSecureString可）
  - `study/anki/clf/01-security/12-hy-crypto-nacl.tsv:4`
- B: Systems Manager Parameter StoreとSecretsの使い分け再確認は？
  - 設定=Parameter寄り / 秘密ローテ=Secrets寄り
  - `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:17`

### 0.42
- A: 責任共有で「セキュリティグループ設定」は誰？
  - 顧客
  - `study/anki/clf/01-security/09-hy-shared.tsv:4`
- B: 責任共有で「データの分類・暗号化の選択」は誰？
  - 顧客
  - `study/anki/clf/01-security/09-hy-shared.tsv:8`

## クラスタ（同じ知識塊の可能性）

### 5枚
- Secrets Manager と Parameter Store の違いは？ → `study/anki/clf/01-security/05-data-protection.tsv:2`
- 「秘密鍵を自動ローテさせたい」Secrets Manager と Parameter Store どちら？ → `study/anki/clf/01-security/08-scenarios.tsv:12`
- Secrets Managerの売りの一つは？ → `study/anki/clf/01-security/12-hy-crypto-nacl.tsv:3`
- Parameter Storeの向きは？ → `study/anki/clf/01-security/12-hy-crypto-nacl.tsv:4`
- Systems Manager Parameter StoreとSecretsの使い分け再確認は？ → `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:17`

### 4枚
- Business サポートは？ → `study/anki/clf/02-billing/04-support-plans.tsv:3`
- Developer と Business の最大の差は？ → `study/anki/clf/02-billing/06-scenarios.tsv:18`
- Businessで初めて得られる代表的なものと言えば？ → `study/anki/clf/02-billing/07-hy-support.tsv:3`
- DeveloperとBusinessの決定的差を一言で？ → `study/anki/clf/02-billing/07-hy-support.tsv:10`

### 3枚
- Control Tower は何用？ → `study/anki/clf/01-security/03-multi-account.tsv:3`
- 「マルチアカウントの初期セットアップを標準化」何？ → `study/anki/clf/01-security/08-scenarios.tsv:18`
- Control Towerのランディングゾーンとは？ → `study/anki/clf/01-security/13-hy-orgs.tsv:5`

### 3枚
- Pricing Calculator は？ → `study/anki/clf/02-billing/02-cost-management.tsv:4`
- 「導入前に月額を概算したい」何？ → `study/anki/clf/02-billing/06-scenarios.tsv:6`
- Pricing Calculatorはアカウント作成後専用？ → `study/anki/clf/02-billing/09-hy-tools.tsv:5`

### 3枚
- PaaSの例は？ → `study/anki/clf/03-concepts/08-hy-basics-7r.tsv:10`
- Elastic Beanstalk は？ → `study/anki/clf/04-services/01-compute.tsv:4`
- 「コードをzipで上げるとURLが欲しい」Paas的？ → `study/anki/clf/04-services/12-hy-compute-storage.tsv:6`

### 2枚
- EC2 に AWS API 権限を付ける正しい方法は？ → `study/anki/clf/01-security/02-iam.tsv:2`
- 「EC2上のアプリがS3にアクセス」正しい権限の付け方は？ → `study/anki/clf/01-security/08-scenarios.tsv:1`

### 2枚
- AWS Organizations の主な用途は？ → `study/anki/clf/01-security/03-multi-account.tsv:1`
- Organizationsの管理アカウントの役割は？ → `study/anki/clf/01-security/13-hy-orgs.tsv:1`

### 2枚
- Firewall Manager は？ → `study/anki/clf/01-security/04-detect-protect.tsv:7`
- Firewall Managerの前提になりやすいものは？ → `study/anki/clf/01-security/11-hy-detect-protect.tsv:9`

### 2枚
- Trusted Advisor は？ → `study/anki/clf/01-security/04-detect-protect.tsv:10`
- Trusted Advisorのカテゴリ例は？ → `study/anki/clf/01-security/11-hy-detect-protect.tsv:13`

### 2枚
- 「外部に公開されているS3がないか」何で点検？ → `study/anki/clf/01-security/08-scenarios.tsv:17`
- 「公開バケット」を見つけたい第一候補は？ → `study/anki/clf/01-security/11-hy-detect-protect.tsv:18`

### 2枚
- 責任共有で「物理DC・ラック・電源」は誰？ → `study/anki/clf/01-security/09-hy-shared.tsv:1`
- 責任共有で「ハイパーバイザ」は誰？ → `study/anki/clf/01-security/09-hy-shared.tsv:2`

### 2枚
- CloudTrailとConfigを一言で区別すると？ → `study/anki/clf/01-security/11-hy-detect-protect.tsv:12`
- CloudTrail と Config の違いは？（再確認） → `study/anki/clf/04-services/10-management.tsv:2`

### 2枚
- Trusted Advisor全チェックが見られるプラン帯は？ → `study/anki/clf/01-security/11-hy-detect-protect.tsv:14`
- 「無料のTrusted Advisorは全部使える？」 → `study/anki/clf/02-billing/06-scenarios.tsv:12`

### 2枚
- CUR（Cost and Usage Report）は？ → `study/anki/clf/02-billing/02-cost-management.tsv:3`
- 「最も詳細な利用内訳CSVが欲しい」何？ → `study/anki/clf/02-billing/06-scenarios.tsv:7`

### 2枚
- Basic サポートは？ → `study/anki/clf/02-billing/04-support-plans.tsv:1`
- Basicで使えるサポート範囲の中心は？ → `study/anki/clf/02-billing/07-hy-support.tsv:1`

### 2枚
- 本番障害で24/365サポートが必要な最低プランは？ → `study/anki/clf/02-billing/04-support-plans.tsv:5`
- 「本番障害で電話サポートが要る」最低プランは？ → `study/anki/clf/02-billing/06-scenarios.tsv:10`

### 2枚
- Migration Evaluator は？ → `study/anki/clf/03-concepts/04-migration.tsv:3`
- Migration Evaluatorの価値は？ → `study/anki/clf/03-concepts/08-hy-basics-7r.tsv:16`

### 2枚
- 「コンテナはあるがサーバは管理したくない」何？ → `study/anki/clf/04-services/11-scenarios.tsv:2`
- 「コンテナのサーバ管理をしたくない」何？ → `study/anki/clf/04-services/12-hy-compute-storage.tsv:5`

### 2枚
- 「HTTPのパスで振り分け」LBはどれ？ → `study/anki/clf/04-services/11-scenarios.tsv:4`
- 「ホストヘッダで振り分け」LBは？ → `study/anki/clf/04-services/12-hy-compute-storage.tsv:9`

### 2枚
- 「キーバリューでミリ秒、サーバレスDB」何？ → `study/anki/clf/04-services/11-scenarios.tsv:9`
- 「超高トラフィックのキーバリュー」何？ → `study/anki/clf/04-services/13-hy-db-net.tsv:2`

### 2枚
- 「DNSフェイルオーバ」何？ → `study/anki/clf/04-services/11-scenarios.tsv:28`
- 「DNSでプライマリ死んだらセカンダリ」何？ → `study/anki/clf/04-services/13-hy-db-net.tsv:19`

### 2枚
- S3 Standard向きは？ → `study/anki/clf/04-services/12-hy-compute-storage.tsv:11`
- S3 Standard-IA向きは？ → `study/anki/clf/04-services/12-hy-compute-storage.tsv:12`

### 2枚
- DMSの均一移行とは？ → `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:1`
- DMSの異種移行とは？ → `study/anki/clf/04-services/15-hy-migrate-devops-mgmt.tsv:2`

