#!/usr/bin/env python3
"""CLF ロードマップに沿い、階層 TSV を生成して AnkiConnect へ投入する。"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "study" / "anki" / "clf"
ADD = ROOT / ".cursor" / "hooks" / "anki-add.py"

# (相対パス, デッキ, [(Front, Back, tags), ...])
# tags はスペース区切り文字列
PACKS: list[tuple[str, str, list[tuple[str, str, str]]]] = []


def pack(rel: str, deck: str, cards: list[tuple[str, str, str]]) -> None:
    PACKS.append((rel, deck, cards))


# --- 1. セキュリティ ---
pack(
    "01-security/01-shared-responsibility.tsv",
    "AWS::CLF::01-セキュリティ",
    [
        ("責任共有モデルで AWS の責任は？", "クラウド「の」セキュリティ（HW・AZ・ハイパーバイザ・マネージドサービスの基盤）", "clf security shared"),
        ("責任共有モデルで顧客の責任は？", "クラウド「内」のセキュリティ（データ・IAM・OSパッチ・NW設定・暗号化）", "clf security shared"),
        ("EC2 の責任境界は？", "AWS=物理〜ハイパーバイザ / 顧客=ゲストOS・パッチ・SG・データ", "clf security shared"),
        ("RDS の責任境界は？", "AWS=OS〜DBエンジンのパッチ / 顧客=データ・ユーザー管理・暗号化設定", "clf security shared"),
        ("Lambda の責任境界は？", "AWS=実行環境全体 / 顧客=コード・権限・依存関係", "clf security shared"),
        ("S3 の責任境界は？", "AWS=基盤・耐久性 / 顧客=バケットポリシー・公開設定・暗号化・バージョニング", "clf security shared"),
    ],
)
pack(
    "01-security/02-iam.tsv",
    "AWS::CLF::01-セキュリティ",
    [
        ("IAM ユーザー / グループ / ロール / ポリシーの役割は？", "ユーザー=人・アプリの永続ID / グループ=ユーザー集合 / ロール=一時権限 / ポリシー=権限の文書", "clf security iam"),
        ("EC2 に AWS API 権限を付ける正しい方法は？", "インスタンスプロファイル（IAM ロール）。アクセスキーを埋め込まない", "clf security iam"),
        ("ルートユーザーでやるべきでないことは？", "日常運用。MFA必須・用途はアカウント設定・サポート等の限定操作のみ", "clf security iam"),
        ("IAM のベストプラクティス（頻出）は？", "最小権限・MFA・ロール優先・ルート封印・定期ローテート", "clf security iam"),
        ("IAM Identity Center（旧SSO）は何用？", "複数アカウント／アプリへのシングルサインオン・中央での権限管理", "clf security iam"),
        ("フェデレーションとは？", "社内IdP等の外部IDで AWS に一時認証する仕組み", "clf security iam"),
        ("Access Analyzer の用途は？", "外部共有されているリソース（S3等）を検出して過剰公開を見つける", "clf security iam"),
        ("認証情報レポートは何を見る？", "アカウント内の全IAMユーザーの認証情報状態（MFA・キー経過等）", "clf security iam"),
    ],
)
pack(
    "01-security/03-multi-account.tsv",
    "AWS::CLF::01-セキュリティ",
    [
        ("AWS Organizations の主な用途は？", "複数アカウントの統合管理・一括請求・SCP", "clf security orgs"),
        ("SCP（Service Control Policy）は何をする？", "OU/アカウントに使えるサービスの上限を強制（IAMより強いガードレール）", "clf security orgs"),
        ("Control Tower は何用？", "マルチアカウント環境のランディングゾーンを自動セットアップ・ガバナンス", "clf security orgs"),
    ],
)
pack(
    "01-security/04-detect-protect.tsv",
    "AWS::CLF::01-セキュリティ",
    [
        ("GuardDuty は？", "脅威検知（異常なAPI・マルウェア等）。マネージドIDS的", "clf security detect"),
        ("Inspector は？", "EC2/コンテナイメージ等の脆弱性スキャン", "clf security detect"),
        ("Macie は？", "S3内の機密データ（PII等）をMLで発見", "clf security detect"),
        ("Detective は？", "セキュリティ調査のための関係可視化・根本分析支援", "clf security detect"),
        ("Security Hub は？", "複数セキュリティサービスの検出結果を集約・準拠チェック", "clf security detect"),
        ("Shield と WAF の違いは？", "Shield=DDoS防護（Standard無料/Advanced有料） / WAF=L7ルール（SQLインジェ等）", "clf security protect"),
        ("Firewall Manager は？", "Organizations全体にWAF/Shield等のルールを中央配布", "clf security protect"),
        ("Config は？", "リソース構成の記録・変更追跡・準拠ルール評価", "clf security detect"),
        ("CloudTrail は？", "アカウントのAPI呼び出しログ（誰が何をしたか）", "clf security detect"),
        ("Trusted Advisor は？", "コスト・性能・セキュリティ・耐障害性・サービスの制限のベストプラクティス検査", "clf security detect"),
    ],
)
pack(
    "01-security/05-data-protection.tsv",
    "AWS::CLF::01-セキュリティ",
    [
        ("KMS と CloudHSM の違いは？", "KMS=マネージド鍵管理 / CloudHSM=専用HSM（顧客が完全制御・準拠要件向け）", "clf security crypto"),
        ("Secrets Manager と Parameter Store の違いは？", "Secrets=秘密の自動ローテ向け有料寄り / Parameter=設定値中心（SecureString可）", "clf security crypto"),
        ("ACM は？", "TLS証明書の発行・管理（主にAWSサービス向け無料パブリック証明書）", "clf security crypto"),
        ("転送時と保存時の暗号化の意味は？", "転送時=通信中（TLS） / 保存時=ディスク上（SSE等）", "clf security crypto"),
    ],
)
pack(
    "01-security/06-network-security.tsv",
    "AWS::CLF::01-セキュリティ",
    [
        ("セキュリティグループの特徴は？", "ステートフル・インスタンス/ENI単位・許可のみ", "clf security nacl"),
        ("ネットワークACLの特徴は？", "ステートレス・サブネット単位・許可と拒否両方", "clf security nacl"),
    ],
)
pack(
    "01-security/07-compliance.tsv",
    "AWS::CLF::01-セキュリティ",
    [
        ("Artifact は？", "AWSのコンプライアンスレポート（SOC等）をダウンロードするポータル", "clf security compliance"),
        ("Audit Manager は？", "監査証拠の継続収集を自動化し評価を支援", "clf security compliance"),
    ],
)

# --- 2. 請求 ---
pack(
    "02-billing/01-pricing-models.tsv",
    "AWS::CLF::02-請求",
    [
        ("オンデマンド料金は？", "使った分だけ。コミットなし。変動ワークロード向き", "clf billing pricing"),
        ("RI（予約インスタンス）は？", "1/3年のキャパシティ予約で割引。特定インスタンス系にコミット", "clf billing pricing"),
        ("Savings Plans は？", "1/3年の利用額コミットで割引。RIより柔軟（コンピュート横断可）", "clf billing pricing"),
        ("スポットインスタンスは？", "余った容量を大幅割引。中断されうる。耐障害なバッチ向き", "clf billing pricing"),
        ("Dedicated Hosts は？", "物理サーバまるごと専有。ライセンス・規制向け", "clf billing pricing"),
        ("Dedicated Instances は？", "他テナントとハード共有しないインスタンス。Hostほど物理固定ではない", "clf billing pricing"),
        ("無料枠の3種類は？", "常時無料 / 12か月無料 / 短期トライアル", "clf billing pricing"),
        ("データ転送の基本ルールは？", "多くの場合「入り」は無料寄り、「AZ/リージョンを出ていく」と課金", "clf billing pricing"),
    ],
)
pack(
    "02-billing/02-cost-management.tsv",
    "AWS::CLF::02-請求",
    [
        ("Cost Explorer は？", "過去・予測のコスト可視化・分析UI", "clf billing tools"),
        ("Budgets は？", "予算閾値でアラート（コスト/使用量）", "clf billing tools"),
        ("CUR（Cost and Usage Report）は？", "最も詳細な利用明細をS3へ出力", "clf billing tools"),
        ("Pricing Calculator は？", "導入前の見積もりツール", "clf billing tools"),
        ("コスト配分タグは？", "リソースにタグ付けして部門・PJ別にコスト按分", "clf billing tools"),
        ("Compute Optimizer は？", "過剰/不足なコンピュート構成の推奨を出す", "clf billing tools"),
    ],
)
pack(
    "02-billing/03-consolidated-billing.tsv",
    "AWS::CLF::02-請求",
    [
        ("一括請求（Consolidated Billing）の利点は？", "1請求書・ボリュームディスカウントの合算適用・アカウント横断のコスト把握", "clf billing orgs"),
    ],
)
pack(
    "02-billing/04-support-plans.tsv",
    "AWS::CLF::02-請求",
    [
        ("Basic サポートは？", "無料。アカウント/請求のサポートとTrusted Advisorのコアチェック等", "clf billing support"),
        ("Developer サポートは？", "開発向け。一般的なガイダンス。ビジネス時間帯のメール等", "clf billing support"),
        ("Business サポートは？", "本番向け。24時間電話・Trusted Advisor全項目・短めの応答目標", "clf billing support"),
        ("Enterprise / On-Ramp は？", "大企業向け。TAM等。最高レベルの応答とアーキテクチャ支援", "clf billing support"),
        ("本番障害で24/365サポートが必要な最低プランは？", "Business 以上", "clf billing support"),
    ],
)
pack(
    "02-billing/05-other.tsv",
    "AWS::CLF::02-請求",
    [
        ("AWS Marketplace は？", "サードパーティのソフト/AMI/SaaSを調達・課金する場", "clf billing other"),
        ("AWS IQ は？", "認定エキスパートに短期間の支援を依頼できるマーケット", "clf billing other"),
        ("re:Post は？", "AWSのコミュニティQ&A（旧フォーラム後継）", "clf billing other"),
    ],
)

# --- 3. 概念 ---
pack(
    "03-concepts/01-value-proposition.tsv",
    "AWS::CLF::03-概念",
    [
        ("クラウドの主なメリット（代表）は？", "固定費→変動費、規模の経済、キャパシティ予想不要、速度と俊敏性、データセンター運用から解放、数分で世界展開", "clf concepts value"),
        ("CapEx と OpEx の違いは？", "CapEx=先行設備投資 / OpEx=運用費（従量）。クラウドはOpEx寄り", "clf concepts value"),
        ("弾力性（Elasticity）とは？", "需要に合わせて自動で伸縮すること", "clf concepts value"),
        ("スケーラビリティとは？", "負荷増大に対応して規模を拡大できること（垂直/水平）", "clf concepts value"),
        ("高可用性と耐障害性の違いは？", "高可用性=稼働率を高く保つ / 耐障害性=障害時も動き続ける設計", "clf concepts value"),
    ],
)
pack(
    "03-concepts/02-cloud-models.tsv",
    "AWS::CLF::03-概念",
    [
        ("パブリック / ハイブリッド / オンプレミスは？", "パブリック=AWS等共有 / オンプレ=自前 / ハイブリッド=併用", "clf concepts model"),
        ("IaaS / PaaS / SaaS の違いは？", "IaaS=基盤貸し（EC2） / PaaS=実行基盤（Beanstalk等） / SaaS=完成アプリ", "clf concepts model"),
    ],
)
pack(
    "03-concepts/03-well-architected.tsv",
    "AWS::CLF::03-概念",
    [
        ("Well-Architected の6本柱は？", "運用上の優秀性・セキュリティ・信頼性・パフォーマンス効率・コスト最適化・サステナビリティ", "clf concepts wa"),
        ("「障害から自動復旧」はどの柱？", "信頼性", "clf concepts wa"),
        ("「最小権限・暗号化」はどの柱？", "セキュリティ", "clf concepts wa"),
        ("「実験を高速に回す運用プロセス」はどの柱？", "運用上の優秀性", "clf concepts wa"),
    ],
)
pack(
    "03-concepts/04-migration.tsv",
    "AWS::CLF::03-概念",
    [
        ("CAF の目的は？", "クラウド導入の組織的準備（ビジネス/人材/ガバナンス/プラットフォーム/セキュリティ/運用）", "clf concepts caf"),
        ("移行戦略 7R を列挙すると？", "Rehost/Replatform/Refactor/Repurchase/Retain/Retire/Relocate", "clf concepts 7r"),
        ("Migration Evaluator は？", "移行のコスト評価・ビジネスケース作成支援", "clf concepts migrate"),
        ("Migration Hub は？", "移行プロジェクトの進捗を中央で追跡", "clf concepts migrate"),
    ],
)
pack(
    "03-concepts/05-global-infrastructure.tsv",
    "AWS::CLF::03-概念",
    [
        ("リージョンとは？", "地理的に独立したAWSの領域。複数AZを含む", "clf concepts global"),
        ("AZ（Availability Zone）とは？", "リージョン内の独立したデータセンター群。障害分離単位", "clf concepts global"),
        ("エッジロケーションは？", "CloudFront等を置くPOP。ユーザー近くでキャッシュ", "clf concepts global"),
        ("マルチAZ と マルチリージョンの違いは？", "AZ=同一リージョン内の高可用 / リージョン=広域DR・低遅延の地理分散", "clf concepts global"),
        ("CloudFront と Global Accelerator の違いは？", "CloudFront=コンテンツキャッシュCDN / GA=エニーキャストで最適経路（非キャッシュ用途も）", "clf concepts global"),
        ("Outposts / Local Zones / Wavelength の違いは？", "Outposts=オンプレにAWSラック / Local Zones=大都市近傍AZ / Wavelength=通信キャリア拠点に超低遅延", "clf concepts global"),
    ],
)

# --- 4. サービス ---
pack(
    "04-services/01-compute.tsv",
    "AWS::CLF::04-サービス",
    [
        ("EC2 は？", "仮想サーバ（IaaS）。OSまで顧客管理", "clf services compute"),
        ("Lambda は？", "サーバレス関数。イベント駆動・実行時間課金", "clf services compute"),
        ("ECS / EKS / Fargate の関係は？", "ECS=AWSコンテナオーケスト / EKS=マネージドKubernetes / Fargate=サーバレス容器実行", "clf services compute"),
        ("Elastic Beanstalk は？", "アプリを上げると環境を自動構築するPaaS的サービス", "clf services compute"),
        ("Lightsail は？", "簡易VPS。予測可能な低価格パッケージ", "clf services compute"),
        ("Auto Scaling の目的は？", "需要に合わせてEC2等の数を自動増減", "clf services compute"),
        ("ALB / NLB / GLB の違いは？", "ALB=L7 HTTP / NLB=L4 超高性能 / GLB=L3/L4 Gateway（アプライアンス等）", "clf services compute"),
    ],
)
pack(
    "04-services/02-storage.tsv",
    "AWS::CLF::04-サービス",
    [
        ("S3 標準の特徴は？", "高耐久オブジェクトストレージ。頻繁アクセス向き", "clf services storage"),
        ("S3 標準IA / Glacier の使い分けは？", "IA=低頻度アクセス / Glacier系=長期アーカイブ（取り出しに時間・料金）", "clf services storage"),
        ("S3 の耐久性の意味は？", "オブジェクトが失われにくい設計（通称11ナイン）。可用性とは別", "clf services storage"),
        ("バージョニングとライフサイクルは？", "バージョニング=旧版保持 / ライフサイクル=日数でクラス移行・削除を自動化", "clf services storage"),
        ("EBS / EFS / FSx の違いは？", "EBS=AZ内ブロック（1インスタンス） / EFS=NFS共有 / FSx=マネージドファイル（Windows等）", "clf services storage"),
        ("Storage Gateway は？", "オンプレからクラウドストレージを使うハイブリッド接続", "clf services storage"),
        ("AWS Backup は？", "複数サービスのバックアップを中央管理", "clf services storage"),
    ],
)
pack(
    "04-services/03-database.tsv",
    "AWS::CLF::04-サービス",
    [
        ("RDS は？", "マネージドリレーショナルDB（MySQL/PG等）", "clf services db"),
        ("Aurora は？", "AWS独自の高可用・高性能互換RDSエンジン", "clf services db"),
        ("DynamoDB は？", "サーバレスNoSQLキーバリュー/ドキュメント。超低レイテンシ", "clf services db"),
        ("ElastiCache は？", "マネージドRedis/Memcachedキャッシュ", "clf services db"),
        ("Redshift は？", "データウェアハウス（分析用列指向）", "clf services db"),
        ("Neptune / DocumentDB / QLDB は？", "Neptune=グラフ / DocumentDB=Mongo互換 / QLDB=台帳", "clf services db"),
    ],
)
pack(
    "04-services/04-networking.tsv",
    "AWS::CLF::04-サービス",
    [
        ("VPC の基本部品は？", "サブネット・ルートテーブル・IGW・NAT・SG/NACL", "clf services net"),
        ("IGW と NAT の違いは？", "IGW=パブリック双方向インターネット / NAT=プライベートから外向きのみ", "clf services net"),
        ("VPN と Direct Connect の違いは？", "VPN=インターネット上の暗号トンネル / DX=専用線相当の安定接続", "clf services net"),
        ("ピアリングと Transit Gateway の違いは？", "ピアリング=1対1 / TGW=ハブで多数VPC接続", "clf services net"),
        ("Route 53 は？", "DNS・ヘルスチェック・ドメイン登録", "clf services net"),
        ("API Gateway は？", "APIの受付・認可・スロットリング等を担うフロントドア", "clf services net"),
    ],
)
pack(
    "04-services/05-analytics.tsv",
    "AWS::CLF::04-サービス",
    [
        ("Athena は？", "S3データにSQLでクエリ（サーバレス）", "clf services analytics"),
        ("Glue は？", "ETL・データカタログ", "clf services analytics"),
        ("Kinesis Data Streams と Firehose の違いは？", "Streams=リアルタイム処理用ストリーム / Firehose=S3等へほぼ準備なしで配信", "clf services analytics"),
        ("QuickSight は？", "BIダッシュボード", "clf services analytics"),
        ("EMR / OpenSearch は？", "EMR=ビッグデータ（Spark等） / OpenSearch=検索・ログ分析", "clf services analytics"),
    ],
)
pack(
    "04-services/06-ml-ai.tsv",
    "AWS::CLF::04-サービス",
    [
        ("SageMaker は？", "MLの構築・学習・デプロイ基盤", "clf services ml"),
        ("Rekognition は？", "画像・動画の物体/顔分析", "clf services ml"),
        ("Textract は？", "文書からテキスト・表を抽出（OCR超）", "clf services ml"),
        ("Polly / Transcribe / Translate は？", "Polly=音声合成 / Transcribe=音声→文字 / Translate=翻訳", "clf services ml"),
        ("Lex / Comprehend は？", "Lex=チャットボット / Comprehend=テキストの感情・エンティティ分析", "clf services ml"),
        ("Kendra / Personalize / Forecast は？", "Kendra=企業検索 / Personalize=レコメンド / Forecast=時系列予測", "clf services ml"),
    ],
)
pack(
    "04-services/07-integration.tsv",
    "AWS::CLF::04-サービス",
    [
        ("SQS は？", "キュー（非同期・疎結合）。プル型", "clf services integration"),
        ("SNS は？", "パブサブ通知。プッシュ型（メール/HTTP/SQS等）", "clf services integration"),
        ("EventBridge は？", "イベントバス。SaaS/AWSイベントをルールでルーティング", "clf services integration"),
        ("Step Functions は？", "複数AWSサービスを状態機械でオーケストレーション", "clf services integration"),
    ],
)
pack(
    "04-services/08-migration-transfer.tsv",
    "AWS::CLF::04-サービス",
    [
        ("DMS は？", "DB移行（均一/異種）。継続レプリケーション可", "clf services migrate"),
        ("Snow ファミリーは？", "物理デバイスで大容量データを配送移行（Snowball等）", "clf services migrate"),
        ("DataSync は？", "オンラインでNAS等↔AWS間の高速データ転送", "clf services migrate"),
        ("Transfer Family は？", "SFTP/FTPS/FTPでS3/EFSへアクセスさせる", "clf services migrate"),
        ("MGN（Application Migration Service）は？", "リホスト（リフト&シフト）移行を自動化", "clf services migrate"),
    ],
)
pack(
    "04-services/09-devtools-iac.tsv",
    "AWS::CLF::04-サービス",
    [
        ("CloudFormation と CDK の違いは？", "CFN=JSON/YAMLテンプレ / CDK=慣れた言語でCFNを生成", "clf services devops"),
        ("CodePipeline の役割は？", "CI/CDのパイプラインオーケストレーション", "clf services devops"),
        ("CodeCommit / CodeBuild / CodeDeploy は？", "Commit=Gitリポ / Build=ビルド / Deploy=デプロイ自動化", "clf services devops"),
        ("CLI / SDK / CloudShell は？", "CLI=コマンド / SDK=コードからAPI / CloudShell=ブラウザの用意されたシェル", "clf services devops"),
    ],
)
pack(
    "04-services/10-management.tsv",
    "AWS::CLF::04-サービス",
    [
        ("CloudWatch は？", "メトリクス・ログ・アラーム・ダッシュボード", "clf services mgmt"),
        ("CloudTrail と Config の違いは？（再確認）", "Trail=操作ログ / Config=構成履歴と準拠", "clf services mgmt"),
        ("Systems Manager は？", "運用ハブ（パッチ・セッションマネージャ・パラメータ等）", "clf services mgmt"),
        ("Health Dashboard は？", "AWS側の障害・メンテが自アカウントに与える影響を表示", "clf services mgmt"),
        ("Service Catalog は？", "承認済み製品をユーザーにセルフサービス提供", "clf services mgmt"),
        ("X-Ray は？", "分散トレーシング（リクエストの遅れ箇所を可視化）", "clf services mgmt"),
    ],
)

# --- 5/6 はプロセス用プレースホルダ（カードなしでもフォルダは作る）---


def write_tsv(path: Path, cards: list[tuple[str, str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    for front, back, tags in cards:
        # タブをフィールドに入れない
        front = front.replace("\t", " ").replace("\n", "<br>")
        back = back.replace("\t", " ").replace("\n", "<br>")
        tags = tags.replace("\t", " ")
        lines.append(f"{front}\t{back}\t{tags}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    # プロセス用空フォルダ
    for d in ["05-mock", "06-review"]:
        (OUT / d).mkdir(parents=True, exist_ok=True)
        readme = OUT / d / "README.md"
        if not readme.exists():
            readme.write_text(
                "# 後から追加\n\n模試の間違い・弱点カードをここに置く。\n",
                encoding="utf-8",
            )

    total_cards = 0
    written: list[tuple[Path, str]] = []
    for rel, deck, cards in PACKS:
        path = OUT / rel
        write_tsv(path, cards)
        total_cards += len(cards)
        written.append((path, deck))
        print(f"wrote {path.relative_to(ROOT)} ({len(cards)} cards) -> {deck}")

    # Anki 投入
    failed = 0
    for path, deck in written:
        r = subprocess.run(
            [sys.executable, str(ADD), "--deck", deck, str(path)],
            cwd=str(ROOT),
        )
        if r.returncode != 0:
            failed += 1

    print(f"DONE files={len(written)} cards={total_cards} failed_uploads={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
