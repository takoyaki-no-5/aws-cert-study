#!/usr/bin/env python3
"""SAA ロードマップ向け階層 TSV を生成し AnkiConnect へ投入する（約90点密度）。"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "study" / "anki" / "saa"
ADD = ROOT / ".cursor" / "hooks" / "anki-add.py"

PACKS: list[tuple[str, str, list[tuple[str, str, str]]]] = []


def pack(rel: str, deck: str, cards: list[tuple[str, str, str]]) -> None:
    PACKS.append((rel, deck, cards))


def write_tsv(path: Path, cards: list[tuple[str, str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"{f}\t{b}\t{t}" for f, b, t in cards]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ========== 01 Secure ==========
pack(
    "01-secure/01-iam.tsv",
    "AWS::SAA::01-セキュア",
    [
        ("IAM ユーザー / グループ / ロール / ポリシーの違いは？", "ユーザー=永続ID / グループ=ユーザー集合 / ロール=一時権限 / ポリシー=権限文書", "saa secure iam"),
        ("EC2 に S3 権限を付ける正しい方法は？", "インスタンスプロファイル（IAMロール）。アクセスキーを埋め込まない", "saa secure iam"),
        ("クロスアカウントで権限を渡す定石は？", "相手アカウントのロールを AssumeRole（STS）。長期キー共有は非推奨", "saa secure iam"),
        ("権限境界（Permissions boundary）は何用？", "ユーザー/ロールが持てる最大権限の上限。委任時の暴走防止", "saa secure iam"),
        ("セッションポリシーとは？", "AssumeRole 時にさらに絞る一時的ポリシー。元の権限以上は付与できない", "saa secure iam"),
        ("リソースベースポリシーとアイデンティティベースの違いは？", "リソース側（S3等）に付けるか、ユーザー/ロール側に付けるか。両方必要な場合あり", "saa secure iam"),
        ("IAM Identity Center の用途は？", "複数アカウントへのSSO・権限セットの中央管理", "saa secure iam"),
        ("フェデレーションの典型用途は？", "社内IdPや Cognito ユーザーを一時認証で AWS に入れる", "saa secure iam"),
        ("最小権限の実践ポイントは？", "必要アクションのみ・条件キー活用・定期見直し・ロール優先", "saa secure iam"),
        ("ルートユーザーの正しい扱い方は？", "MFA必須・日常使わない・アクセスキー作らない", "saa secure iam"),
        ("S3 バケットポリシーで拒否するとどうなる？", "明示的 Deny は他の許可より優先（明示的拒否が最優先）", "saa secure iam"),
        ("同一アカウントでロールを使う主な理由は？", "人・サービスごとに一時権限を分離し、長期鍵を減らす", "saa secure iam"),
    ],
)
pack(
    "01-secure/02-orgs.tsv",
    "AWS::SAA::01-セキュア",
    [
        ("Organizations の主用途は？", "マルチアカウント統合・一括請求・SCP", "saa secure orgs"),
        ("SCP は何をする？", "OU/アカウントで使えるAPIの上限ガードレール。権限付与そのものではない", "saa secure orgs"),
        ("SCP と IAM の両方が必要な理由は？", "SCPで許可されても IAM で許可が必要（両方通って初めて実行可）", "saa secure orgs"),
        ("Control Tower は何用？", "ランディングゾーン自動構築・ガードレール・アカウント発行標準化", "saa secure orgs"),
        ("マルチアカウント分割の定石は？", "本番/開発/セキュリティ/ログ/共有サービス等をアカウント分離", "saa secure orgs"),
        ("組織のルート（管理アカウント）で避けるべきことは？", "ワークロード実行。請求・組織管理に限定", "saa secure orgs"),
    ],
)
pack(
    "01-secure/03-vpc-network.tsv",
    "AWS::SAA::01-セキュア",
    [
        ("パブリックサブネットとプライベートの違いは？", "パブリック=IGWへのルートあり / プライベート=なし（外向きはNAT等）", "saa secure vpc"),
        ("SG と NACL の違いは？", "SG=ENI単位・ステートフル・許可のみ / NACL=サブネット・ステートレス・許可と拒否", "saa secure vpc"),
        ("ステートフルとは？", "戻り通信を自動許可。SGはステートフル、NACLは往復ルールが必要", "saa secure vpc"),
        ("NAT Gateway の用途は？", "プライベートサブネットからインターネットへ外向きのみ", "saa secure vpc"),
        ("VPC エンドポイント（Gateway）が向くサービスは？", "S3 / DynamoDB。ルートテーブル経由・データ転送料を抑えやすい", "saa secure vpc"),
        ("Interface エンドポイント（PrivateLink）の用途は？", "他AWSサービスや自社サービスへプライベート接続（ENI経由）", "saa secure vpc"),
        ("PrivateLink を選ぶ典型シナリオは？", "他アカウントのサービスをインターネット経由せず安全に利用", "saa secure vpc"),
        ("VPN と Direct Connect の違いは？", "VPN=インターネット上のIPsec（速い導入） / DX=専用線（安定帯域）", "saa secure vpc"),
        ("Transit Gateway の用途は？", "多数VPC/オンプレ接続をハブ&スポークで集約", "saa secure vpc"),
        ("VPC ピアリングの制約は？", "推移的ルーティング不可。多数接続は TGW の方が楽", "saa secure vpc"),
        ("踏み台（Bastion）の代替としてよく出るのは？", "SSM Session Manager（インバウンド22不要）", "saa secure vpc"),
        ("0.0.0.0/0 を SG のインバウンドに開けるのはいつ？", "原則避ける。必要なポートのみ・送信元を絞る", "saa secure vpc"),
    ],
)
pack(
    "01-secure/04-edge-protect.tsv",
    "AWS::SAA::01-セキュア",
    [
        ("WAF と Shield の違いは？", "WAF=L7ルール（SQLi/XSS等） / Shield=DDoS防護", "saa secure edge"),
        ("Shield Standard と Advanced の違いは？", "Standard=無料の基本DDoS / Advanced=高度検知・補償・専門サポート", "saa secure edge"),
        ("Firewall Manager の用途は？", "Organizations全体へWAF/Shield等ルールを中央配布", "saa secure edge"),
        ("CloudFront + WAF の定石は？", "エッジで脅威を止め、オリジンを直接公開しない", "saa secure edge"),
        ("ALB の前に置く保護は？", "WAF（L7）・必要なら Shield Advanced", "saa secure edge"),
        ("Cognito の用途は？", "アプリのユーザー認証・認可（ユーザープール/IDプール）", "saa secure edge"),
        ("Secrets Manager の強みは？", "秘密情報保管＋自動ローテーション連携", "saa secure edge"),
        ("Parameter Store との使い分けは？", "Secrets=秘密のローテ中心 / Parameter=設定値中心（SecureString可）", "saa secure edge"),
    ],
)
pack(
    "01-secure/05-data-crypto.tsv",
    "AWS::SAA::01-セキュア",
    [
        ("保存時暗号と転送時暗号の違いは？", "保存時=ディスク上（SSE/KMS） / 転送時=通信中（TLS）", "saa secure crypto"),
        ("SSE-S3 / SSE-KMS / SSE-C の違いは？", "S3管理鍵 / KMS顧客管理寄り（監査・CMK） / 顧客提供鍵", "saa secure crypto"),
        ("KMS の鍵ポリシーが重要な理由は？", "誰が鍵を使えるかの根本制御。IAMだけでは足りない場合あり", "saa secure crypto"),
        ("Envelope encryption とは？", "データ鍵で暗号化し、データ鍵をKMSマスター鍵で包む方式", "saa secure crypto"),
        ("CloudHSM を選ぶときば？", "専用HSM・鍵の完全管理や準拠要件が必要なとき", "saa secure crypto"),
        ("ACM の主な用途は？", "ALB/CloudFront等のTLS証明書発行・更新自動化", "saa secure crypto"),
        ("S3 Block Public Access の役割は？", "アカウント/バケット単位で公開設定を強制ブロック", "saa secure crypto"),
        ("バケットを非公開にする最低セットは？", "Block Public Access ON + 公開ACLなし + 必要ならポリシーで明示許可のみ", "saa secure crypto"),
        ("Macie は何用？", "S3内のPII等の機密データ発見", "saa secure crypto"),
        ("GuardDuty は何用？", "アカウント/ワークロードの脅威検知（異常API等）", "saa secure crypto"),
        ("Config は何用？", "構成記録・変更追跡・準拠ルール評価", "saa secure crypto"),
        ("CloudTrail は何用？", "API呼び出しの監査ログ（誰が何をしたか）", "saa secure crypto"),
        ("CloudTrail と CloudWatch Logs の違いは？", "Trail=API監査 / CW Logs=アプリ・OS等のログ集約", "saa secure crypto"),
        ("EBS / RDS / S3 の暗号化を有効化する定石は？", "作成時に暗号化ON（後から不可な場合あり。スナップショット経由等）", "saa secure crypto"),
    ],
)
pack(
    "01-secure/06-scenarios.tsv",
    "AWS::SAA::01-セキュア",
    [
        ("「アプリがS3に書く。鍵は埋め込みたくない」→？", "EC2/ECS/LambdaにIAMロール。必要ならSSE-KMS", "saa secure scenario"),
        ("「他アカウントのバケットを読みたい」→？", "バケットポリシー＋相手側ロール/ユーザー権限。必要ならKMS鍵ポリシーも", "saa secure scenario"),
        ("「プライベートSubnetのEC2がS3へ、インターネット経由なし」→？", "S3 Gateway Endpoint（またはInterface）", "saa secure scenario"),
        ("「オンプレからAWSへ閉域接続、安定帯域」→？", "Direct Connect（必要ならDX+VPN冗長）", "saa secure scenario"),
        ("「WebをDDoSとSQLiから守りたい」→？", "CloudFront/ALB + Shield + WAF", "saa secure scenario"),
        ("「社内ADでAWSコンソールにログイン」→？", "IAM Identity Center またはフェデレーション", "saa secure scenario"),
        ("「全アカウントでルート操作を禁止したい」→？", "SCPで制限（管理アカウントは例外扱いに注意）", "saa secure scenario"),
        ("「DBパスワードを自動ローテ」→？", "Secrets Manager + RDS等ローテーション", "saa secure scenario"),
        ("「S3に個人情報が混入していないか調べたい」→？", "Macie", "saa secure scenario"),
        ("「不審なAPI呼び出しを検知」→？", "GuardDuty（調査はDetective等）", "saa secure scenario"),
        ("「構成ドリフトや暗号化未設定を検知」→？", "Config ルール", "saa secure scenario"),
        ("「ALB配下をインターネット非公開にしたい」→？", "内部ALB + プライベートSubnet、または認証付き公開", "saa secure scenario"),
    ],
)

# ========== 02 Resilient ==========
pack(
    "02-resilient/01-decouple-scale.tsv",
    "AWS::SAA::02-レジリエント",
    [
        ("疎結合にする定番サービスは？", "SQS / SNS / EventBridge / Step Functions", "saa resilient decouple"),
        ("SQS と SNS の違いは？", "SQS=キュー（pull・緩衝） / SNS=パブサブ通知（push）", "saa resilient decouple"),
        ("標準キューと FIFO の違いは？", "FIFO=順序・Exactly-once寄り。標準=高スループット・順序ベストエフォート", "saa resilient decouple"),
        ("可視性タイムアウトとは？", "受信後、他コンシューマから見えなくなる時間。処理時間に合わせる", "saa resilient decouple"),
        ("DLQ の用途は？", "処理失敗メッセージの隔離・後で調査", "saa resilient decouple"),
        ("EventBridge の強みは？", "イベントルールで多数ターゲットへルーティング（SaaS連携も）", "saa resilient decouple"),
        ("Step Functions の用途は？", "ワークフローオーケストレーション（リトライ・分岐・可視化）", "saa resilient decouple"),
        ("ALB と NLB の違いは？", "ALB=L7（HTTP） / NLB=L4（超低遅延・静的IP）", "saa resilient decouple"),
        ("CLB は今どう扱う？", "レガシー。新規はALB/NLB", "saa resilient decouple"),
        ("Auto Scaling の目的は？", "需要に合わせた台数増減・可用性維持", "saa resilient decouple"),
        ("ターゲット追跡スケーリングとは？", "CPU等の指標を目標値に保つよう自動調整", "saa resilient decouple"),
        ("マルチティア構成の定石は？", "Web/App/DBを層分離。DBはプライベート", "saa resilient decouple"),
        ("API Gateway + Lambda が向くのは？", "サーバレスAPI・バースト耐性・運用負荷低減", "saa resilient decouple"),
        ("ECS と EKS の使い分けは？", "ECS=AWSネイティブ簡単 / EKS=Kubernetes互換・移植性", "saa resilient decouple"),
        ("Fargate を選ぶ理由は？", "サーバ管理なしでコンテナ実行", "saa resilient decouple"),
    ],
)
pack(
    "02-resilient/02-ha-dr.tsv",
    "AWS::SAA::02-レジリエント",
    [
        ("Multi-AZ の目的は？", "AZ障害に耐える高可用（同期/自動フェイルオーバー系）", "saa resilient ha"),
        ("Multi-Region の目的は？", "リージョン災害対策・グローバル展開・低遅延", "saa resilient ha"),
        ("RPO / RTO とは？", "RPO=許容データ損失量 / RTO=復旧までの許容時間", "saa resilient ha"),
        ("バックアップ＆リストア戦略は？", "最安・RTO/RPO大。定期バックアップから復旧", "saa resilient ha"),
        ("パイロットライトとは？", "核心のみ起動、災害時にスケールアウト。コスト低め", "saa resilient ha"),
        ("ウォームスタンバイとは？", "縮小版を常時稼働、災害時に拡大。パイロットより速い", "saa resilient ha"),
        ("マルチサイト（アクティブ/アクティブ）とは？", "複数拠点で同時稼働。RTO/RPO最小・コスト最大", "saa resilient ha"),
        ("Route 53 フェイルオーバールーティングは？", "ヘルスチェック失敗時に予備へ切替", "saa resilient ha"),
        ("レイテンシルーティングは？", "ユーザーから低遅延なリージョンへ", "saa resilient ha"),
        ("加重ルーティングの用途は？", "カナリア・トラフィック分割", "saa resilient ha"),
        ("RDS Multi-AZ と Read Replica の違いは？", "Multi-AZ=可用性（自動フェイルオーバー） / Replica=読み取りスケール（別用途）", "saa resilient ha"),
        ("Aurora の高可用の特徴は？", "共有ストレージ・複数AZレプリカ・高速フェイルオーバー", "saa resilient ha"),
        ("S3 の耐久性の意味は？", "データ喪失に極めて強い（11 9s）。可用性とは別概念", "saa resilient ha"),
        ("S3 Cross-Region Replication の用途は？", "コンプライアンス・DR・レイテンシ", "saa resilient ha"),
        ("単一障害点（SPOF）を避ける定石は？", "複数AZ・冗長化・オートスケール・マネージドサービス", "saa resilient ha"),
        ("ASG + 複数AZ にする理由は？", "AZ障害時も残存AZでキャパを維持", "saa resilient ha"),
    ],
)
pack(
    "02-resilient/03-scenarios.tsv",
    "AWS::SAA::02-レジリエント",
    [
        ("「スパイクで落ちる同期API」→？", "SQSで緩衝 + ワーカー。必要ならALB+ASG", "saa resilient scenario"),
        ("「注文処理を確実に順番どおり」→？", "SQS FIFO（またはDynamoDB等の設計）", "saa resilient scenario"),
        ("「AZ障害でもWebを止めない」→？", "複数AZにALB+ASG、DBはMulti-AZ", "saa resilient scenario"),
        ("「RPOほぼゼロ・高速切替のDR」→？", "マルチサイト or ウォームスタンバイ寄り", "saa resilient scenario"),
        ("「安くDR、復旧は数時間OK」→？", "バックアップ＆リストア", "saa resilient scenario"),
        ("「DB読み取りがボトルネック」→？", "Read Replica / Aurora Replica / キャッシュ", "saa resilient scenario"),
        ("「リージョン障害に備えたい」→？", "クロスリージョンレプリカ + Route 53フェイルオーバー", "saa resilient scenario"),
        ("「マイクロサービス間を疎結合に」→？", "SNS+SQS または EventBridge", "saa resilient scenario"),
        ("「長時間ワークフローを管理」→？", "Step Functions", "saa resilient scenario"),
        ("「静的IPで極低遅延LB」→？", "NLB", "saa resilient scenario"),
        ("「パス/ホストでルーティング」→？", "ALB", "saa resilient scenario"),
        ("「障害時に待機系サイトへDNS切替」→？", "Route 53フェイルオーバー", "saa resilient scenario"),
    ],
)

# ========== 03 Performance ==========
pack(
    "03-performance/01-storage.tsv",
    "AWS::SAA::03-性能",
    [
        ("S3 / EBS / EFS / FSx の使い分けは？", "S3=オブジェクト / EBS=EC2ブロック / EFS=複数EC2共有NFS / FSx=Windows・Lustre等", "saa perf storage"),
        ("EBS gp3 と io2 の使い分けは？", "gp3=汎用コスパ / io2=超高IOPS・重要DB", "saa perf storage"),
        ("インスタンスストアが向くのは？", "一時・再作成可データ。永続性はEBS/S3", "saa perf storage"),
        ("S3 性能を上げる定石は？", "並列化・プレフィックス分散・Transfer Acceleration等", "saa perf storage"),
        ("EFS と FSx for Lustre の違いは？", "EFS=汎用共有ファイル / Lustre=HPC高スループット", "saa perf storage"),
        ("FSx for Windows を選ぶときば？", "Windowsファイル共有・AD統合が必要", "saa perf storage"),
        ("S3 Intelligent-Tiering は？", "アクセス頻度に応じ自動階層。パターン不明時", "saa perf storage"),
        ("大きなオブジェクトを高速転送したい→？", "マルチパートアップロード / Transfer Acceleration / DataSync", "saa perf storage"),
    ],
)
pack(
    "03-performance/02-compute.tsv",
    "AWS::SAA::03-性能",
    [
        ("EC2 ファミリー選定の観点は？", "CPU/メモリ/GPU/ネットワーク最適化などワークロード適合", "saa perf compute"),
        ("Placement Group（cluster）は？", "低遅延・高スループット（同一AZ密集）", "saa perf compute"),
        ("Lambda の向き不向きは？", "短時間イベント向き。長時間・恒常高負荷はECS/EC2も検討", "saa perf compute"),
        ("Batch の用途は？", "大規模バッチのキューイング・計算資源管理", "saa perf compute"),
        ("CloudFront の主効果は？", "エッジキャッシュでレイテンシ低下・オリジン負荷減", "saa perf compute"),
        ("Global Accelerator と CloudFront の違いは？", "GA=TCP/UDPのAnya経路最適化 / CF=HTTPキャッシュCDN", "saa perf compute"),
        ("Enhanced Networking / EFA が出るときば？", "高ネットワーク性能・HPC通信が必要", "saa perf compute"),
        ("オートスケールで性能を保つ定石は？", "先行スケール・適切なメトリクス・暖機（必要なら）", "saa perf compute"),
    ],
)
pack(
    "03-performance/03-database.tsv",
    "AWS::SAA::03-性能",
    [
        ("RDS / Aurora / DynamoDB の使い分けは？", "RDS=マネージドRDB / Aurora=高可用高パフォーマンス互換 / DDB=超スケールKVS", "saa perf db"),
        ("DynamoDB が向くアクセスは？", "キーが明確・大規模・低レイテンシ。結合多用は不向き", "saa perf db"),
        ("DAX は何用？", "DynamoDB用インメモリキャッシュ（マイクロ秒級）", "saa perf db"),
        ("ElastiCache の用途は？", "RDB等の前段キャッシュ・セッション（Redis/Memcached）", "saa perf db"),
        ("読み取りスケールの定石は？", "Read Replica / Aurora Replica / キャッシュ", "saa perf db"),
        ("書き込みがボトルネックなRDB→？", "シャーディング検討、またはDynamoDB等への適材適所", "saa perf db"),
        ("Aurora Serverless が向くのは？", "変動が大きい・間欠的な負荷", "saa perf db"),
        ("DynamoDB オンデマンドとプロビジョンドの違いは？", "オンデマンド=自動で変動追随 / プロビジョンド=予測可能なら安く安定", "saa perf db"),
        ("パーティションキー設計が重要な理由は？", "偏るとホットパーティションで性能劣化", "saa perf db"),
        ("RDS Proxy の用途は？", "接続プーリング。Lambda等の接続急増対策", "saa perf db"),
    ],
)
pack(
    "03-performance/04-network-ingest.tsv",
    "AWS::SAA::03-性能",
    [
        ("低レイテンシ設計の定石は？", "ユーザーに近いリージョン/エッジ・不要ホップ削減", "saa perf net"),
        ("Kinesis Data Streams の用途は？", "リアルタイムストリーム処理（複数コンシューマ可）", "saa perf net"),
        ("Kinesis Data Firehose の用途は？", "ストリームをS3/Redshift等へ配信（マネージド）", "saa perf net"),
        ("MSK を選ぶときば？", "Kafka互換が必要", "saa perf net"),
        ("DataSync の用途は？", "オンプレ⇔AWS等のファイル高速同期", "saa perf net"),
        ("Transfer Family の用途は？", "SFTP/FTPS等でS3/EFSへ転送", "saa perf net"),
        ("Snow ファミリーを選ぶときば？", "ネットワーク転送が非現実的な大容量", "saa perf net"),
        ("同一AZ配置が効くのは？", "超低遅延（ただしAZ障害リスクとトレードオフ）", "saa perf net"),
    ],
)
pack(
    "03-performance/05-scenarios.tsv",
    "AWS::SAA::03-性能",
    [
        ("「世界中の静的配信を速く」→？", "S3 + CloudFront", "saa perf scenario"),
        ("「ゲームやIoTのTCPを全球最適化」→？", "Global Accelerator", "saa perf scenario"),
        ("「EC2間で共有ファイルシステム」→？", "EFS（WindowsならFSx）", "saa perf scenario"),
        ("「超高IOPSのDBディスク」→？", "io2等のプロビジョンドIOPS EBS", "saa perf scenario"),
        ("「セッションを共有したい」→？", "ElastiCache（またはDDB）", "saa perf scenario"),
        ("「クリックストリームをリアルタイム分析」→？", "Kinesis Data Streams + 処理", "saa perf scenario"),
        ("「ログをS3へほぼリアルタイム保存」→？", "Firehose → S3", "saa perf scenario"),
        ("「オンプレNASをAWSへ高速移行」→？", "DataSync（大量ならSnowも）", "saa perf scenario"),
        ("「キーアクセスの超大規模DB」→？", "DynamoDB（+必要ならDAX）", "saa perf scenario"),
        ("「RDSが接続数で死ぬ（Lambda）」→？", "RDS Proxy", "saa perf scenario"),
        ("「読み取り9割のRDB」→？", "Read Replica / Aurora + キャッシュ", "saa perf scenario"),
        ("「HPCで高速共有ストレージ」→？", "FSx for Lustre", "saa perf scenario"),
    ],
)

# ========== 04 Cost ==========
pack(
    "04-cost/01-compute-pricing.tsv",
    "AWS::SAA::04-コスト",
    [
        ("オンデマンドを選ぶときば？", "短期間・変動・中断不可のベース", "saa cost compute"),
        ("RI と Savings Plans の違いは？", "RI=インスタンス寄り拘束 / SP=$/時間コミットで柔軟（特にCompute SP）", "saa cost compute"),
        ("スポットが向くのは？", "中断耐性あるバッチ・ステートレス。ステートフル本番は注意", "saa cost compute"),
        ("スポット中断への備えは？", "チェックポイント・分散・Diversified・ASG混在", "saa cost compute"),
        ("ライトサイジングとは？", "過剰スペックを実測に合わせて縮小", "saa cost compute"),
        ("Compute Optimizer の用途は？", "EC2/EBS等の適正サイズ推奨", "saa cost compute"),
        ("サーバレスが安くなる条件は？", "アイドルが多い・イベント駆動。常時高負荷は要比較", "saa cost compute"),
        ("Savings Plans の適用範囲イメージは？", "Compute SPはEC2/Fargate/Lambda等に広く効く", "saa cost compute"),
    ],
)
pack(
    "04-cost/02-storage-db-net.tsv",
    "AWS::SAA::04-コスト",
    [
        ("S3 クラス選定の軸は？", "アクセス頻度・取り出し時間・可用性要件", "saa cost storage"),
        ("Standard-IA / Glacier Instant / Deep Archive のイメージは？", "IA=低頻度 / Instant=即時アーカイブ / Deep=最安・取り出し遅い", "saa cost storage"),
        ("ライフサイクルポリシーの用途は？", "日数経過で安価クラスへ自動移行・期限切れ削除", "saa cost storage"),
        ("不完全なマルチパートの掃除は？", "ライフサイクルで.abortを削除（放置コスト防止）", "saa cost storage"),
        ("EBSスナップショットのコスト意識は？", "増分だが世代管理。不要削除・アーカイブ検討", "saa cost storage"),
        ("DynamoDB コストを抑える観点は？", "オンデマンドvsプロビジョン・キャパシティ・TTL・設計", "saa cost storage"),
        ("Aurora Serverless が安いケースは？", "アイドルが多い変動負荷", "saa cost storage"),
        ("データ転送コストの定石は？", "同一AZ・エンドポイント・CloudFrontで外向き削減", "saa cost storage"),
        ("NAT Gateway が高いときの対策は？", "不要外向き削減・エンドポイント活用・設計見直し", "saa cost storage"),
        ("S3へ同じリージョンからEC2で出すコスト感は？", "同一リージョン内の出し入れは比較的安い（詳細は料金表）が、AZ間や外向きに注意", "saa cost storage"),
    ],
)
pack(
    "04-cost/03-tools-scenarios.tsv",
    "AWS::SAA::04-コスト",
    [
        ("Cost Explorer は？", "コスト可視化・分析", "saa cost tools"),
        ("Budgets は？", "予算超過アラート（予測超過も可）", "saa cost tools"),
        ("コスト配分タグの用途は？", "部門・プロジェクト別の集計", "saa cost tools"),
        ("CUR は？", "最詳細の利用明細（S3出力）", "saa cost tools"),
        ("「安定した常時EC2を安く」→？", "Savings Plans または RI", "saa cost scenario"),
        ("「バッチは安く、落ちても再実行可」→？", "スポット", "saa cost scenario"),
        ("「古いログを安く保管、すぐ読む必要薄」→？", "S3 Glacier系 + ライフサイクル", "saa cost scenario"),
        ("「外向き転送が痛い」→？", "CloudFront / 圧縮 / キャッシュ / 不要転送削減", "saa cost scenario"),
        ("「開発環境を夜間止めたい」→？", "スケジュール停止・Instance Scheduler等", "saa cost scenario"),
        ("「過大なEC2が多い」→？", "Compute Optimizer + ライトサイジング", "saa cost scenario"),
        ("「S3アクセスパターン不明」→？", "Intelligent-Tiering", "saa cost scenario"),
        ("「予測不能なスパイクのAPI」→？", "Lambda/Fargate等の従量 + 適切なキャッシュ", "saa cost scenario"),
    ],
)

# ========== 05 High-yield cross ==========
pack(
    "05-mock/01-hy-secure-resilient.tsv",
    "AWS::SAA::05-模試",
    [
        ("「インターネットに出さずS3」定石は？", "Gateway VPC Endpoint", "saa hy"),
        ("「鍵ローテ必須のDBパスワード」定石は？", "Secrets Manager", "saa hy"),
        ("「明示的DenyとAllowがぶつかったら」？", "Deny優先", "saa hy"),
        ("「SGで拒否ルールは？」", "SGに拒否はない（許可のみ）。拒否はNACL", "saa hy"),
        ("「ALBを複数AZに置く理由」？", "AZ障害耐性", "saa hy"),
        ("「RDS Multi-AZは読み取りスケール？」", "基本いいえ（可用性）。読み取りはReplica", "saa hy"),
        ("「SQSで処理失敗を隔離」？", "DLQ", "saa hy"),
        ("「イベント駆動でFan-out」？", "SNS→複数SQS（またはEventBridge）", "saa hy"),
        ("「パイロットライトとウォームの差」？", "常時稼働の大きさ（ウォームの方が厚い）", "saa hy"),
        ("「Route53でヘルスチェック切替」？", "フェイルオーバーポリシー", "saa hy"),
    ],
)
pack(
    "05-mock/02-hy-perf-cost.tsv",
    "AWS::SAA::05-模試",
    [
        ("「静的配信」三点セットは？", "S3 + CloudFront（+OAC/OAI）", "saa hy"),
        ("「共有POSIXファイル」？", "EFS", "saa hy"),
        ("「Windowsファイル共有」？", "FSx for Windows", "saa hy"),
        ("「DynamoDB超低レイテンシ」？", "DAX", "saa hy"),
        ("「RDS接続過多（Lambda）」？", "RDS Proxy", "saa hy"),
        ("「中断可バッチ最安」？", "スポット", "saa hy"),
        ("「1年安定利用の割引」？", "SP または RI", "saa hy"),
        ("「低頻度アクセスのオブジェクト」？", "S3 IA / Intelligent-Tiering / Glacier系", "saa hy"),
        ("「外向き通信を閉域でS3」コスト面も？", "VPCエンドポイント（NAT経由より安いことが多い）", "saa hy"),
        ("「コスト可視化」？", "Cost Explorer / 配分タグ / Budgets", "saa hy"),
    ],
)
pack(
    "05-mock/03-hy-service-pick.tsv",
    "AWS::SAA::05-模試",
    [
        ("「マネージドKafka」？", "MSK", "saa hy"),
        ("「S3へストリームロード簡単」？", "Firehose", "saa hy"),
        ("「複数コンシューマで生ストリーム」？", "Kinesis Data Streams", "saa hy"),
        ("「オンプレファイル同期」？", "DataSync", "saa hy"),
        ("「SFTPでS3」？", "Transfer Family", "saa hy"),
        ("「PB級持ち込み」？", "Snow Family", "saa hy"),
        ("「サーバレスコンテナ」？", "Fargate", "saa hy"),
        ("「K8sが必要」？", "EKS", "saa hy"),
        ("「単純なコンテナオーケスト」？", "ECS", "saa hy"),
        ("「グローバルAnycastでTCP高速化」？", "Global Accelerator", "saa hy"),
        ("「Blue/Greenや加重シフト（DNS）」？", "Route 53 加重", "saa hy"),
        ("「WAFルールを全アカウント統一」？", "Firewall Manager", "saa hy"),
        ("「S3の機密データ検出」？", "Macie", "saa hy"),
        ("「脅威検知」？", "GuardDuty", "saa hy"),
        ("「構成履歴・準拠」？", "Config", "saa hy"),
        ("「API監査ログ」？", "CloudTrail", "saa hy"),
    ],
)


# ========== extra density for ~90% ==========
pack(
    "01-secure/07-more.tsv",
    "AWS::SAA::01-セキュア",
    [
        ("条件キー aws:SourceIp の典型用途は？", "特定IPからのみAPI許可", "saa secure iam"),
        ("MFA必須をIAMで強制する定石は？", "条件キー aws:MultiFactorAuthPresent", "saa secure iam"),
        ("S3 Object Lock の用途は？", "WORM・改ざん防止（コンプライアンス）", "saa secure crypto"),
        ("S3 Versioning の用途は？", "上書き・削除からの復旧", "saa secure crypto"),
        ("KMS キーの自動ローテーションは？", "CMKで有効化可能（年次）。影響範囲を理解して使う", "saa secure crypto"),
        ("クライアント側暗号とサーバ側の違いは？", "クライアント=送る前に暗号化 / サーバ=S3等が保存時に暗号化", "saa secure crypto"),
        ("VPC Flow Logs の用途は？", "ENIのトラフィックメタデータ記録・NW監査", "saa secure vpc"),
        ("Gateway Endpoint にSGは付く？", "付かない（ルートテーブル制御）。InterfaceはSG対象", "saa secure vpc"),
        ("パブリックにS3を出す代わりの定石は？", "CloudFront + OAC（旧OAI）でオリジン非公開", "saa secure edge"),
        ("Inspector と GuardDuty の違いは？", "Inspector=脆弱性スキャン / GuardDuty=脅威検知", "saa secure edge"),
        ("Security Hub の位置づけは？", "検出結果の集約・標準準拠チェックのハブ", "saa secure edge"),
        ("Certificate Manager（プライベートCA）が出るときば？", "内部TLSをAWSで管理したいとき", "saa secure crypto"),
        ("EC2 IMDSv2 を勧める理由は？", "SSRF等による認証情報窃取リスク低減", "saa secure iam"),
        ("SCP でルートユーザーを制限できる？", "管理アカウント以外では一定の制限が可能（設計に注意）", "saa secure orgs"),
        ("Organizations の一括請求の利点は？", "支払い一元化・ボリューム割引の合算", "saa secure orgs"),
        ("クロスアカウントでCloudWatch等を集約する発想は？", "ログ/監視アカウントへ集約（権限はロール）", "saa secure orgs"),
        ("S3 ACL とバケットポリシー、今の推奨は？", "ACL無効化＋ポリシー中心が現行推奨", "saa secure crypto"),
        ("暗号化されたEBSを他アカウント共有するときば？", "スナップショット共有＋KMS鍵の権限も必要", "saa secure crypto"),
        ("WAF のスコープ例は？", "CloudFront / ALB / API Gateway 等", "saa secure edge"),
        ("「社外に一時的にオブジェクト共有」→？", "署名付きURL（または署名付きCookie）", "saa secure scenario"),
    ],
)
pack(
    "02-resilient/04-more.tsv",
    "AWS::SAA::02-レジリエント",
    [
        ("ELB のヘルスチェックが重要な理由は？", "異常インスタンスを外し、健全な方へ振る", "saa resilient decouple"),
        ("接続排出（connection draining）とは？", "登録解除時に既存接続を猶予して切る", "saa resilient decouple"),
        ("SQS ロングポーリングの利点は？", "空応答削減・コストと遅延の改善", "saa resilient decouple"),
        ("SNS フィルターポリシーは？", "購読者が欲しいメッセージだけ受信", "saa resilient decouple"),
        ("EventBridge Scheduler / ルールのイメージは？", "時間またはイベントでターゲット起動", "saa resilient decouple"),
        ("Step Functions 標準と Express の差（大枠）は？", "標準=長時間・監査向き / Express=高頻度短時間", "saa resilient decouple"),
        ("Aurora Global Database の用途は？", "クロスリージョン低遅延読み取り・DR", "saa resilient ha"),
        ("DynamoDB Global Tables の用途は？", "マルチリージョンアクティブ書き込み寄り", "saa resilient ha"),
        ("S3 バージョニング＋MFA Delete の意味は？", "誤削除・悪意ある削除への耐性強化", "saa resilient ha"),
        ("バックアップを別アカウント/リージョンに置く理由は？", "アカウント侵害・リージョン障害からの隔離", "saa resilient ha"),
        ("ASG のクールダウンとは？", "スケール後に連続スケールしすぎない待機", "saa resilient decouple"),
        ("ライフサイクルフックの用途は？", "起動/終了時にカスタム処理（登録待ち等）", "saa resilient decouple"),
        ("NLB のクロスゾーン負荷分散は？", "AZをまたいで均等に振る設定（料金注意）", "saa resilient decouple"),
        ("Route 53 ヘルスチェックの対象例は？", "エンドポイント・他計算済みチェック・CloudWatch警報", "saa resilient ha"),
        ("「ステートレスアプリが耐障害に強い理由」は？", "どのインスタンスでも処理でき、置換しやすい", "saa resilient ha"),
        ("EBS スナップショットの保存先は？", "S3（リージョン内）。必要ならコピーでDR", "saa resilient ha"),
        ("AMI を跨リージョンコピーする用途は？", "DR・マルチリージョン展開", "saa resilient ha"),
        ("RDS の自動バックアップ保持は？", "保持期間内のポイントインタイムリカバリ用", "saa resilient ha"),
        ("「キューが伸びたらスケール」定石は？", "SQSキュー長をASG/ECSスケール指標に", "saa resilient scenario"),
        ("「デプロイ中も止めない」定石は？", "ローリング/Blue-Green、ALB切替、疎結合", "saa resilient scenario"),
    ],
)
pack(
    "03-performance/06-more.tsv",
    "AWS::SAA::03-性能",
    [
        ("S3 Transfer Acceleration は？", "エッジ経由で遠距離アップロード高速化", "saa perf storage"),
        ("EBS スループットと IOPS の違い（ざっくり）は？", "IOPS=IO回数 / スループット=秒あたりデータ量", "saa perf storage"),
        ("インスタンスに複数EBSを付ける狙いば？", "ストライピング等で性能（運用複雑化に注意）", "saa perf storage"),
        ("CloudFront オリジンシールドのイメージは？", "オリジンへのリクエスト集約で負荷減", "saa perf compute"),
        ("Lambda プロビジョニング済み同時実行は？", "コールドスタート低減（コスト増）", "saa perf compute"),
        ("EC2 のバースト性能（T系）注意点は？", "クレジット枯渇で性能低下", "saa perf compute"),
        ("Placement Group spread は？", "別ハードに分散して同時障害リスク低減", "saa perf compute"),
        ("DynamoDB GSIs の用途は？", "別キーでのクエリ。コストと整合性に注意", "saa perf db"),
        ("強い一貫性と結果整合性（DDB）は？", "強い=最新保証（コスト/レイテンシ） / 結果整合=通常読取", "saa perf db"),
        ("ElastiCache Redis と Memcached の差（大枠）は？", "Redis=高機能・永続寄り / Memcached=単純高速", "saa perf db"),
        ("Aurora のストレージ自動拡張の利点は？", "容量計画負担が減り性能もスケール", "saa perf db"),
        ("OpenSearch の典型用途は？", "ログ検索・全文検索", "saa perf net"),
        ("EMR の用途は？", "大規模分散処理（Hadoop/Spark）", "saa perf net"),
        ("Redshift の用途は？", "データウェアハウス分析", "saa perf net"),
        ("Athena の用途は？", "S3へSQL（サーバレス）", "saa perf net"),
        ("「画像をリサイズしてS3へ」定石は？", "S3イベント→Lambda（またはバッチ）", "saa perf scenario"),
        ("「モバイルから世界中アップロードが遅い」→？", "Transfer Acceleration または CloudFront設計", "saa perf scenario"),
        ("「同一ファイルを数千台が読む」→？", "EFS/FSx または S3+CDN（要件次第）", "saa perf scenario"),
        ("「分析用にログを溜めてSQL」→？", "S3 + Athena（必要ならGlue）", "saa perf scenario"),
        ("「低遅延ゲーミングTCP」→？", "Global Accelerator", "saa perf scenario"),
    ],
)
pack(
    "04-cost/04-more.tsv",
    "AWS::SAA::04-コスト",
    [
        ("Dedicated Host を選ぶときば？", "ライセンス・物理占有要件", "saa cost compute"),
        ("キャパシティ予約の用途は？", "必要時に確実にEC2を確保（割引とは別概念）", "saa cost compute"),
        ("S3 取り出し料金が出やすいクラスは？", "IA / Glacier 系（アクセス頻度と相談）", "saa cost storage"),
        ("リクエスト料金が効くサービス例は？", "S3・Lambda・DynamoDB等。無駄なチャットを減らす", "saa cost storage"),
        ("Idle リソースの典型は？", "未使用EBS・Elastic IP・負荷ゼロのEC2/ALB", "saa cost tools"),
        ("Trusted Advisor のコストチェックは？", "未使用・過剰リソースの指摘（サポートプランで範囲差）", "saa cost tools"),
        ("Cost Anomaly Detection は？", "異常なコスト増の検知", "saa cost tools"),
        ("Savings Plans のコミット単位は？", "時間あたりの利用額（$/hour）", "saa cost compute"),
        ("スポットをステートフルDBに使う？", "原則非推奨（中断リスク）", "saa cost compute"),
        ("「開発用RDSを安く」→？", "停止スケジュール・小さいインスタンス・Aurora Serverless等", "saa cost scenario"),
        ("「NAT経由のS3転送が痛い」→？", "S3 Gateway Endpoint", "saa cost scenario"),
        ("「CloudWatchコスト増」対策の発想は？", "ログ保持短縮・フィルタ・メトリクス絞り込み", "saa cost scenario"),
        ("「同じデータをAZ間で大量転送」注意は？", "AZ間転送課金。設計で同居/エンドポイント検討", "saa cost scenario"),
        ("S3 ライフサイクルで Intelligent-Tiering へも？", "可能。パターンに合わせた移行設計", "saa cost storage"),
        ("EBS gp2 と gp3 のコスト感は？", "gp3の方がIOPS/スループットを独立調整できコスパ良いことが多い", "saa cost storage"),
        ("「常時ONのALBが複数」→？", "統合・不要削除・台数見直し", "saa cost scenario"),
        ("Reserved Capacity（DDB等）の発想は？", "安定利用なら予約で割引", "saa cost storage"),
        ("「ログを全部Standardに永久保存」は？", "高い。ライフサイクルで移行", "saa cost scenario"),
        ("Compute Savings Plans が RI より柔軟な点は？", "インスタンスファミリやリージョンをまたぎやすい", "saa cost compute"),
        ("「予算超過で通知」→？", "AWS Budgets", "saa cost tools"),
    ],
)
pack(
    "05-mock/04-hy-trap.tsv",
    "AWS::SAA::05-模試",
    [
        ("「可用性」と「耐久性」を混ぜない。S3の11 9sは？", "耐久性（データ喪失耐性）", "saa hy"),
        ("「Multi-AZ RDS = 読み取り性能UP」は？", "誤り。可用性目的", "saa hy"),
        ("「NACLはステートフル」は？", "誤り。ステートレス", "saa hy"),
        ("「SGにDenyルール」は？", "ない。許可のみ", "saa hy"),
        ("「SCPだけでアプリ権限が付く」は？", "誤り。上限のみ。IAMが必要", "saa hy"),
        ("「スポットは無停止保証」は？", "誤り。中断あり", "saa hy"),
        ("「EBSは複数インスタンスから同時マウントが基本」は？", "原則1台（Multi-Attach対応タイプは例外）", "saa hy"),
        ("「EFSは1AZ限定」は？", "誤り。リージョン内複数AZ（One Zoneタイプ除く）", "saa hy"),
        ("「CloudFrontはTCP任意プロトコル向け」は？", "主にHTTP(S)。任意TCPはGlobal Accelerator寄り", "saa hy"),
        ("「DynamoDBは複雑なJOIN向き」は？", "不向き。キー設計前提", "saa hy"),
        ("「IAMロールは長期鍵と同じ」は？", "違う。一時認証情報", "saa hy"),
        ("「バケット公開=Block Public Access ONのまま」は？", "矛盾。公開するなら設定を理解して外す（非推奨な公開が多い）", "saa hy"),
        ("「Pilot Lightは常時フル稼働」は？", "誤り。核のみ", "saa hy"),
        ("「同じVPCならSG不要」は？", "誤り。層ごとにSGで制御", "saa hy"),
        ("「Kinesis=Firehoseと同じ」は？", "違う。Streamsは処理基盤、Firehoseは配信寄り", "saa hy"),
        ("「コスト最適化=常にスポット」は？", "誤り。要件（中断・安定）次第", "saa hy"),
        ("「AZを1つにまとめると安い＆堅牢」は？", "安く見えるが単一障害点。堅牢ではない", "saa hy"),
        ("「Route53はDNSのみでヘルスは見ない」は？", "誤り。ヘルスチェック連携あり", "saa hy"),
        ("「LambdaにOSパッチは顧客責任」は？", "実行環境はAWS。コードと権限は顧客", "saa hy"),
        ("「S3はファイルシステムとしてEC2にそのままマウントが定石」は？", "非定石。共有FSならEFS/FSx", "saa hy"),
    ],
)


def main() -> int:
    tsv_only = "--tsv-only" in sys.argv
    OUT.mkdir(parents=True, exist_ok=True)
    for d in ["06-review"]:
        (OUT / d).mkdir(parents=True, exist_ok=True)

    total = 0
    written: list[tuple[Path, str]] = []
    for rel, deck, cards in PACKS:
        path = OUT / rel
        write_tsv(path, cards)
        total += len(cards)
        written.append((path, deck))
        print(f"wrote {path.relative_to(ROOT)} ({len(cards)}) -> {deck}")

    if tsv_only:
        print(f"DONE files={len(written)} cards={total} (tsv-only)")
        return 0

    failed = 0
    for path, deck in written:
        r = subprocess.run(
            [sys.executable, str(ADD), "--deck", deck, str(path)],
            cwd=str(ROOT),
        )
        if r.returncode != 0:
            failed += 1

    print(f"DONE files={len(written)} cards={total} failed_uploads={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
