#!/usr/bin/env python3
"""CLF 高頻度カード増強 — 全部できたら約90点水準。低頻度は入れない。"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "study" / "anki" / "clf"
ADD = ROOT / ".cursor" / "hooks" / "anki-add.py"
PACKS: list[tuple[str, str, list[tuple[str, str, str]]]] = []


def p(rel: str, deck: str, cards: list[tuple[str, str, str]]) -> None:
    PACKS.append((rel, deck, cards))


def c(front: str, back: str, *tags: str) -> tuple[str, str, str]:
    return (front, back, " ".join(tags) if tags else "clf")


# ========== 1 セキュリティ（高頻度）==========
p(
    "01-security/09-hy-shared.tsv",
    "AWS::CLF::01-セキュリティ",
    [
        c("責任共有で「物理DC・ラック・電源」は誰？", "AWS", "clf", "security", "hy"),
        c("責任共有で「ハイパーバイザ」は誰？", "AWS", "clf", "security", "hy"),
        c("責任共有で「ゲストOSのパッチ」は誰？（EC2）", "顧客", "clf", "security", "hy"),
        c("責任共有で「セキュリティグループ設定」は誰？", "顧客", "clf", "security", "hy"),
        c("責任共有で「S3バケットを公開にするか」は誰？", "顧客", "clf", "security", "hy"),
        c("責任共有で「RDSの自動バックアップ基盤」は誰寄り？", "AWS（マネージド）。データの中身と権限は顧客", "clf", "security", "hy"),
        c("責任共有で「Lambdaのランタイムパッチ」は誰？", "AWS。コードとIAMは顧客", "clf", "security", "hy"),
        c("責任共有で「データの分類・暗号化の選択」は誰？", "顧客", "clf", "security", "hy"),
        c("責任共有で「IAMユーザー作成」は誰？", "顧客", "clf", "security", "hy"),
        c("「クラウドのセキュリティ」と「クラウド内のセキュリティ」どっちが顧客？", "クラウド内＝顧客 / クラウドの＝AWS", "clf", "security", "hy"),
        c("抽象度が上がるほど（IaaS→SaaS）顧客の責任は？", "減る（AWSがより多く担う）", "clf", "security", "hy"),
        c("EC2とLambdaで顧客がパッチする範囲の差は？", "EC2はOSまで顧客。Lambdaはコード層のみ", "clf", "security", "hy"),
    ],
)

p(
    "01-security/10-hy-iam.tsv",
    "AWS::CLF::01-セキュリティ",
    [
        c("IAMポリシーで明示的DenyとAllowがぶつかると？", "Denyが勝つ", "clf", "security", "hy"),
        c("アイデンティティベースポリシーとリソースベースの違いは？", "前者=誰に何を / 後者=このリソースへ誰が（S3バケットポリシー等）", "clf", "security", "hy"),
        c("アクセスキーをコードに書くのはなぜダメ？", "漏洩リスク。ロールや一時認証を使う", "clf", "security", "hy"),
        c("長期認証情報より推奨されるのは？", "IAMロールによる一時認証情報", "clf", "security", "hy"),
        c("ルートユーザーでやる操作の例は？", "アカウント解約、一部の税務/サポート設定、ルートの変更など限定的", "clf", "security", "hy"),
        c("ルートにMFAを付けないリスクは？", "アカウント乗っ取りで全破壊されうる", "clf", "security", "hy"),
        c("パスワードポリシーで設定できるものの例は？", "長さ・複雑さ・有効期限・再利用禁止など", "clf", "security", "hy"),
        c("IAMグループにポリシーを付ける利点は？", "ユーザー個別ではなく集合で権限管理できる", "clf", "security", "hy"),
        c("クロスアカウントアクセスの基本手段は？", "相手アカウントのロールをAssumeRole", "clf", "security", "hy"),
        c("アプリケーションがAWS外から呼ぶときもキー直書きは避ける？", "はい。可能な限りロール/フェデレーション/Secrets", "clf", "security", "hy"),
        c("最小権限の意味は？", "必要最小限のアクション・リソースだけ許可", "clf", "security", "hy"),
        c("権限が広すぎると何が起きやすい？", "漏洩時の被害拡大・誤操作", "clf", "security", "hy"),
        c("IAM Identity Centerが向くケースは？", "多数アカウント/多数ユーザーへのSSO", "clf", "security", "hy"),
        c("社内Active Directory連携のキーワードは？", "フェデレーション / Identity Center / IdP", "clf", "security", "hy"),
        c("アクセスキーのローテーションとは？", "古いキーを無効化し新しいキーへ定期的に替える", "clf", "security", "hy"),
        c("「権限はあるが実際に使われたか」を見る材料の一例は？", "CloudTrail / Access Advisor（最終アクセス）系", "clf", "security", "hy"),
        c("EC2からDynamoDBへ権限を渡す正しい形は？", "EC2ロールにDynamoDB許可ポリシー", "clf", "security", "hy"),
        c("コンソールログイン用とAPI用の認証の違いは？", "コンソール=ユーザー名+パス(+MFA) / API=キーまたは一時クレデンシャル", "clf", "security", "hy"),
    ],
)

p(
    "01-security/11-hy-detect-protect.tsv",
    "AWS::CLF::01-セキュリティ",
    [
        c("GuardDutyの入力の代表は？", "CloudTrail・VPCフロー・DNSログ等（マネージドで解析）", "clf", "security", "hy"),
        c("GuardDutyは脆弱性スキャンか？", "いいえ。脅威検知。脆弱性はInspector", "clf", "security", "hy"),
        c("Inspectorが見るものの例は？", "CVE・ネットワーク到達性など", "clf", "security", "hy"),
        c("Macieが主に見る場所は？", "S3", "clf", "security", "hy"),
        c("Security HubとGuardDutyの関係は？", "GuardDuty等の検出をSecurity Hubが集約・標準化できる", "clf", "security", "hy"),
        c("Shield Standardの料金は？", "追加料金なし（自動有効）", "clf", "security", "hy"),
        c("Shield Advancedが欲しいとき（CLFレベル）は？", "高度なDDoS対策・支援が必要なとき（有料）", "clf", "security", "hy"),
        c("WAFを置く典型的な前面は？", "CloudFront / ALB / API Gateway 等", "clf", "security", "hy"),
        c("Firewall Managerの前提になりやすいものは？", "Organizationsでの中央管理", "clf", "security", "hy"),
        c("CloudTrailは何を残す？", "誰が・いつ・どのAPIを呼んだか", "clf", "security", "hy"),
        c("Configは何を残す？", "リソースがどんな構成だったか・準拠していたか", "clf", "security", "hy"),
        c("CloudTrailとConfigを一言で区別すると？", "Trail=操作 / Config=状態", "clf", "security", "hy"),
        c("Trusted Advisorのカテゴリ例は？", "コスト・性能・セキュリティ・耐障害性・サービス制限", "clf", "security", "hy"),
        c("Trusted Advisor全チェックが見られるプラン帯は？", "Business以上（Basicは限定）", "clf", "security", "hy"),
        c("Detectiveが向く作業は？", "インシデントの調査・関係性の深掘り", "clf", "security", "hy"),
        c("「暗号化されていないEBSがないか」継続チェック向きは？", "Configルール", "clf", "security", "hy"),
        c("「ルートにMFAがない」を指摘しがちなのは？", "Trusted Advisor（セキュリティ）", "clf", "security", "hy"),
        c("「公開バケット」を見つけたい第一候補は？", "Access Analyzer / Trusted Advisor / MacieやSecurity Hub連携も", "clf", "security", "hy"),
        c("WAFで防ぎやすい攻撃の例は？", "SQLインジェクション・XSSなどL7", "clf", "security", "hy"),
        c("DDoSの大量通信量攻撃にまず効くのは？", "Shield（+必要ならAdvanced）", "clf", "security", "hy"),
    ],
)

p(
    "01-security/12-hy-crypto-nacl.tsv",
    "AWS::CLF::01-セキュリティ",
    [
        c("KMSの顧客管理キーとAWS管理キーの違い（CLF）は？", "顧客管理=ポリシーやローテをより制御 / AWS管理=サービス任せで簡単", "clf", "security", "hy"),
        c("CloudHSMが選ばれる理由の典型は？", "専用HSM・厳しいコンプライアンスで鍵を自分で握りたい", "clf", "security", "hy"),
        c("Secrets Managerの売りの一つは？", "秘密の自動ローテーション連携", "clf", "security", "hy"),
        c("Parameter Storeの向きは？", "設定値・階層パラメータ（秘密もSecureString可）", "clf", "security", "hy"),
        c("ACM証明書の典型的な利用先は？", "ALB・CloudFrontなどのAWS終端", "clf", "security", "hy"),
        c("転送時暗号化の代表手段は？", "TLS/HTTPS", "clf", "security", "hy"),
        c("保存時暗号化の代表手段は？", "SSE（S3/EBS等）やKMS", "clf", "security", "hy"),
        c("SGのデフォルト送信は？（典型理解）", "多くの場合、作成時は外向き許可が付く設計が多い（問題文の前提に注意）", "clf", "security", "hy"),
        c("SGは拒否ルールを書ける？", "書けない（許可のみ）。拒否はNACL", "clf", "security", "hy"),
        c("NACLはステートフル？", "いいえ。ステートレス（往復を明示）", "clf", "security", "hy"),
        c("SGはステートフル？", "はい。戻り通信は自動許可", "clf", "security", "hy"),
        c("評価の単位: SGは？ NACLは？", "SG=ENI/インスタンス側 / NACL=サブネット", "clf", "security", "hy"),
        c("Artifactで手に入るものの例は？", "SOC・ISOなどの監査レポートPDF", "clf", "security", "hy"),
        c("Audit Managerの価値は？", "監査用エビデンス収集の自動化", "clf", "security", "hy"),
        c("暗号化していてもIAM権限が甘いと？", "権限があれば読める。暗号化は鍵と権限管理とセット", "clf", "security", "hy"),
    ],
)

p(
    "01-security/13-hy-orgs.tsv",
    "AWS::CLF::01-セキュリティ",
    [
        c("Organizationsの管理アカウントの役割は？", "組織の作成・一括請求の支払い側など", "clf", "security", "hy"),
        c("OU（Organizational Unit）は何？", "アカウントをグループ化する入れ物。SCPを付けられる", "clf", "security", "hy"),
        c("SCPでAllowしてもIAMでDenyなら？", "結局使えない。SCPは上限、IAMは実際の許可", "clf", "security", "hy"),
        c("SCPだけでログインユーザーに権限を与えられる？", "いいえ。SCPは制限。許可はIAM等が必要", "clf", "security", "hy"),
        c("Control Towerのランディングゾーンとは？", "推奨される初期マルチアカウント構成の土台", "clf", "security", "hy"),
        c("勘定を環境ごと（開発/本番）に分ける利点は？", "爆破半径の縮小・請求と権限の分離", "clf", "security", "hy"),
    ],
)

# ========== 2 請求（超高頻度）==========
p(
    "02-billing/07-hy-support.tsv",
    "AWS::CLF::02-請求",
    [
        c("Basicで使えるサポート範囲の中心は？", "アカウントと請求、＋Trusted Advisorの限定チェック等", "clf", "billing", "hy"),
        c("Developerの想定利用者は？", "実験・開発中（本番クリティカル向けではない）", "clf", "billing", "hy"),
        c("Businessで初めて得られる代表的なものと言えば？", "24/365の技術サポート、Trusted Advisor全項目、短い応答目標", "clf", "billing", "hy"),
        c("Enterpriseの象徴的な付加は？", "TAM（テクニカルアカウントマネージャ）等の専任支援", "clf", "billing", "hy"),
        c("インフラ障害で電話したい → 最低どのプラン？", "Business", "clf", "billing", "hy"),
        c("アーキテクチャの深いレビューを継続的に受けたい帯は？", "Enterprise寄り", "clf", "billing", "hy"),
        c("Trusted Advisorが一部しか見えないプランは？", "Basic（と条件により限定）", "clf", "billing", "hy"),
        c("サポートプランはアカウント単位で選ぶ理解でよいか（CLF）？", "はい（Organizationsでも扱いは問題文に従う）", "clf", "billing", "hy"),
        c("「請求額の問い合わせ」だけならBasicで足りる？", "足りる（アカウント/請求サポート）", "clf", "billing", "hy"),
        c("DeveloperとBusinessの決定的差を一言で？", "本番向けの緊急度・チャネル・Trusted Advisor範囲", "clf", "billing", "hy"),
        c("Enterprise On-Rampの位置づけ（CLF）は？", "Enterpriseへの入門的な上位プラン帯（詳細は選択肢の文言に合わせる）", "clf", "billing", "hy"),
        c("サポートケースの緊急度が選べるプラン帯は？", "Business以上で本格的", "clf", "billing", "hy"),
        c("「週末の夜に本番が落ちた」Basicで電話できる？", "できない想定。Business以上", "clf", "billing", "hy"),
        c("Well-Architectedレビュー支援が手厚い帯は？", "上位（Enterprise）", "clf", "billing", "hy"),
        c("料金はおおむねどう決まる？（CLFイメージ）", "月額の利用率に応じた割合＋下限など（暗記はプラン差優先）", "clf", "billing", "hy"),
    ],
)

p(
    "02-billing/08-hy-pricing.tsv",
    "AWS::CLF::02-請求",
    [
        c("オンデマンドが向くワークロードは？", "短命・予測不能・コミットしたくない", "clf", "billing", "hy"),
        c("RIの支払いオプション例は？", "全額前払い / 一部 / 前払いなし（割引率が変わる）", "clf", "billing", "hy"),
        c("Compute Savings Plansの柔軟性は？", "インスタンスファミリーやリージョン等をまたいで適用しやすい", "clf", "billing", "hy"),
        c("EC2 Instance Savings Plansは？", "特定ファミリー等に寄せる代わりにより高い割引になりやすい", "clf", "billing", "hy"),
        c("スポットが向かないもの？", "ステートフルで中断不可の本番DBなど", "clf", "billing", "hy"),
        c("スポットの中断は何が起きる？", "AWS都合で回収されうる。アプリ側で耐える", "clf", "billing", "hy"),
        c("Dedicated Hostが必要な典型理由は？", "既存ソケット/コア課金ライセンス、規制で物理専有", "clf", "billing", "hy"),
        c("無料枠「常時無料」の例のイメージは？", "一定量までずっと無料のサービス枠", "clf", "billing", "hy"),
        c("無料枠「12か月」のイメージは？", "新規アカウントから1年だけ付く枠", "clf", "billing", "hy"),
        c("無料枠「トライアル」のイメージは？", "短期だけ試せる枠", "clf", "billing", "hy"),
        c("同じAZ内の私有IP通信の課金イメージは？", "無料または相対的に安い（問題の前提に注意）", "clf", "billing", "hy"),
        c("インターネットへ出るデータ転送は？", "一般に課金対象になりやすい", "clf", "billing", "hy"),
        c("CloudFrontを使うと転送コストで得することがある理由は？", "エッジ経由の方が安くなるケースがある", "clf", "billing", "hy"),
        c("AZをまたぐデータ転送は？", "課金されやすい（設計で意識）", "clf", "billing", "hy"),
        c("S3からインターネットへの取り出しは？", "転送料が発生しうる", "clf", "billing", "hy"),
        c("RIを使い切れないリスクは？", "コミット分が無駄になりうる", "clf", "billing", "hy"),
        c("Savings Plansのコミット単位のイメージは？", "時間あたりの利用額（$/hour）を約束", "clf", "billing", "hy"),
        c("「とりあえず試す」最初の課金モデルは？", "オンデマンド", "clf", "billing", "hy"),
        c("バッチで落としてもよい分散処理向きは？", "スポット", "clf", "billing", "hy"),
        c("1年確実に同じサイズを使うなら？", "RIまたはSavings Plansを検討", "clf", "billing", "hy"),
    ],
)

p(
    "02-billing/09-hy-tools.tsv",
    "AWS::CLF::02-請求",
    [
        c("Cost Explorerでできることの中心は？", "可視化・フィルタ・予測の確認", "clf", "billing", "hy"),
        c("Budgetsの通知先の例は？", "メールやSNS", "clf", "billing", "hy"),
        c("Budgetsで監視できるものの例は？", "実コスト・使用量・RI/SPの利用率など", "clf", "billing", "hy"),
        c("CURの保存先の典型は？", "S3バケット", "clf", "billing", "hy"),
        c("Pricing Calculatorはアカウント作成後専用？", "いいえ。見積もりは事前にも使える", "clf", "billing", "hy"),
        c("コスト配分タグを使う手順の要点は？", "タグ付け→請求設定で活性化→レポートに出す", "clf", "billing", "hy"),
        c("Compute Optimizerの対象イメージは？", "EC2やAuto Scaling、Lambda等の権利サイズ", "clf", "billing", "hy"),
        c("一括請求で割引が効きやすくなる理由は？", "使用量が合算されボリュームディスカウントの段に届きやすい", "clf", "billing", "hy"),
        c("一括請求でもアカウントの分離は保てる？", "はい。請求はまとめてもリソース/権限はアカウント単位", "clf", "billing", "hy"),
        c("請求アラートを「まだ小さいうちから」仕込むなら？", "Budgets", "clf", "billing", "hy"),
        c("「サービス別の内訳を毎月深掘り」向きは？", "Cost Explorer（詳細ならCUR）", "clf", "billing", "hy"),
        c("Marketplaceの請求のイメージは？", "AWSの請求にサードパーティ分が載ることがある", "clf", "billing", "hy"),
        c("Professional Servicesとは？", "AWS公式の有償コンサル支援", "clf", "billing", "hy"),
        c("re:Postとサポートケースの違いは？", "re:Post=コミュニティ / サポート=契約プランに基づく公式支援", "clf", "billing", "hy"),
        c("無料枠を超えそうな監視に使うのは？", "BudgetsやCost Explorer", "clf", "billing", "hy"),
    ],
)

# ========== 3 概念 ==========
p(
    "03-concepts/07-hy-wa.tsv",
    "AWS::CLF::03-概念",
    [
        c("WA: 「ランブック・自動化・小さな変更」→柱は？", "運用上の優秀性", "clf", "concepts", "hy"),
        c("WA: 「検知・IAM・データ保護」→柱は？", "セキュリティ", "clf", "concepts", "hy"),
        c("WA: 「バックアップ・マルチAZ・故障の分離」→柱は？", "信頼性", "clf", "concepts", "hy"),
        c("WA: 「適切なリソースタイプ・キャッシュ・CDN」→柱は？", "パフォーマンス効率", "clf", "concepts", "hy"),
        c("WA: 「使った分だけ・不要リソース削除」→柱は？", "コスト最適化", "clf", "concepts", "hy"),
        c("WA: 「利用率向上・環境影響」→柱は？", "サステナビリティ", "clf", "concepts", "hy"),
        c("柱はいくつ？（現行CLF）", "6", "clf", "concepts", "hy"),
        c("信頼性でよく出る設計は？", "単一障害点をなくす・マルチAZ", "clf", "concepts", "hy"),
        c("セキュリティでよく出る設計は？", "最小権限・暗号化・監視", "clf", "concepts", "hy"),
        c("コスト最適化でやりがちな失敗は？", "常時最大構成のつけっぱなし", "clf", "concepts", "hy"),
        c("パフォーマンス効率でやりがちな失敗は？", "監視せず勘でインスタンスタイプを上げる", "clf", "concepts", "hy"),
        c("運用優秀性で重視することの一例は？", "障害対応の手順化と改善の反復", "clf", "concepts", "hy"),
        c("サステナビリティとコストが同時に良くなる例は？", "過大なアイドル資源を減らす", "clf", "concepts", "hy"),
        c("「すべてを信頼せず検証する」はどの柱の思想？", "セキュリティ", "clf", "concepts", "hy"),
        c("「故障は起きる前提」はどの柱？", "信頼性", "clf", "concepts", "hy"),
    ],
)

p(
    "03-concepts/08-hy-basics-7r.tsv",
    "AWS::CLF::03-概念",
    [
        c("クラウドメリット: 規模の経済とは？", "AWSの巨大量購入で単価が下がる恩恵を受ける", "clf", "concepts", "hy"),
        c("クラウドメリット: キャパシティ予想が不要とは？", "ピークに合わせて買いすぎなくてよい", "clf", "concepts", "hy"),
        c("クラウドメリット: 速度と俊敏性とは？", "数分でリソースを調達し実験できる", "clf", "concepts", "hy"),
        c("クラウドメリット: データセンター運用から解放とは？", "電源・冷却・ラック作業から離れられる", "clf", "concepts", "hy"),
        c("クラウドメリット: 数分で世界展開とは？", "リージョンを選んですぐ海外にも置ける", "clf", "concepts", "hy"),
        c("弾力性 vs スケーラビリティを一言で？", "弾力=自動伸縮 / スケール=拡大できる能力", "clf", "concepts", "hy"),
        c("水平スケールと垂直スケールは？", "水平=台数 / 垂直=1台のスペック", "clf", "concepts", "hy"),
        c("高可用性の指標でよく出る考え方は？", "稼働率（例: 99.x%）を上げる設計", "clf", "concepts", "hy"),
        c("IaaSの例は？", "EC2 / VPC", "clf", "concepts", "hy"),
        c("PaaSの例は？", "Elastic Beanstalk 等", "clf", "concepts", "hy"),
        c("SaaSの例は？", "完成したWebアプリサービス全般（AWS外も含め概念）", "clf", "concepts", "hy"),
        c("ハイブリッドの例は？", "オンプレDB＋AWS分析、Outposts等", "clf", "concepts", "hy"),
        c("7R Relocateとは？", "例えばVMwareをクラウドへ移すような再配置", "clf", "concepts", "hy"),
        c("CAFを使うタイミングは？", "組織としてクラウド導入の準備・変革を進めるとき", "clf", "concepts", "hy"),
        c("Migration Hubの価値は？", "複数移行ツールの進捗を一箇所で追う", "clf", "concepts", "hy"),
        c("Migration Evaluatorの価値は？", "コスト試算で移行の正当化材料を作る", "clf", "concepts", "hy"),
        c("リージョン選択の理由例は？", "レイテンシ・法令・サービス有無・コスト", "clf", "concepts", "hy"),
        c("AZが分かれている意味は？", "電源や障害の影響を分離", "clf", "concepts", "hy"),
        c("エッジロケーションが多い理由は？", "ユーザー近くで配信し遅延と負荷を減らす", "clf", "concepts", "hy"),
        c("CloudFrontのキャッシュの利点は？", "オリジン負荷低減＋低遅延", "clf", "concepts", "hy"),
        c("Global Acceleratorが効くケースは？", "TCP/UDPアプリの入口を最適化（非キャッシュ中心）", "clf", "concepts", "hy"),
        c("Outpostsの一言は？", "AWSを自社DCに延長", "clf", "concepts", "hy"),
        c("Local Zonesの一言は？", "大都市近くの低遅延ゾーン", "clf", "concepts", "hy"),
        c("Wavelengthの一言は？", "通信キャリア網のすぐそば", "clf", "concepts", "hy"),
    ],
)

# ========== 4 サービス（シナリオ大量）==========
p(
    "04-services/12-hy-compute-storage.tsv",
    "AWS::CLF::04-サービス",
    [
        c("「OSを自由に選びたい」何？", "EC2", "clf", "services", "hy"),
        c("「リクエストのたびに起動、ゼロまで縮む」何？", "Lambda", "clf", "services", "hy"),
        c("「Dockerはある。オーケストはAWS寄せ」何？", "ECS", "clf", "services", "hy"),
        c("「既存のK8sスキルを活かす」何？", "EKS", "clf", "services", "hy"),
        c("「コンテナのサーバ管理をしたくない」何？", "Fargate", "clf", "services", "hy"),
        c("「コードをzipで上げるとURLが欲しい」Paas的？", "Elastic Beanstalk", "clf", "services", "hy"),
        c("「個人ブログを安く簡単に」何？", "Lightsail（または静的ならS3+CloudFront）", "clf", "services", "hy"),
        c("「昼だけEC2を増やす」何？", "Auto Scaling", "clf", "services", "hy"),
        c("「ホストヘッダで振り分け」LBは？", "ALB", "clf", "services", "hy"),
        c("「極低遅延で数百万接続」LBは？", "NLB", "clf", "services", "hy"),
        c("S3 Standard向きは？", "頻繁にアクセスするデータ", "clf", "services", "hy"),
        c("S3 Standard-IA向きは？", "アクセスは少ないがすぐ取りたい", "clf", "services", "hy"),
        c("S3 Glacier Instant Retrieval向きは？", "アーカイブだがミリ秒で取り出したい", "clf", "services", "hy"),
        c("S3 Glacier Flexible / Deep Archive向きは？", "取り出しが遅くてよい超長期保管", "clf", "services", "hy"),
        c("S3 One Zone-IAの注意は？", "単一AZ。AZ障害で失われうる", "clf", "services", "hy"),
        c("S3のバージョニングの効果は？", "誤削除・上書きから復旧しやすい", "clf", "services", "hy"),
        c("ライフサイクルポリシーの例は？", "30日後にIA、90日後にGlacier", "clf", "services", "hy"),
        c("EBSスナップショットの保存先イメージは？", "S3に保管（リージョン内）", "clf", "services", "hy"),
        c("インスタンスストアの特徴は？", "一時的。停止で消えることが多い", "clf", "services", "hy"),
        c("「Windowsファイル共有をマネージドで」何？", "FSx for Windows 等", "clf", "services", "hy"),
        c("「オンプレアプリがファイル共有のままS3を使いたい」入口は？", "Storage Gateway", "clf", "services", "hy"),
        c("「RDSもEBSもまとめてバックアップ方針」何？", "AWS Backup", "clf", "services", "hy"),
        c("S3のオブジェクトとは？", "データ本体＋キー＋メタデータ", "clf", "services", "hy"),
        c("バケット名の制約イメージは？", "グローバルで一意など", "clf", "services", "hy"),
        c("「静的サイトをS3で」足りないものになりがちなのは？", "独自ドメインHTTPSならCloudFront+ACM等", "clf", "services", "hy"),
    ],
)

p(
    "04-services/13-hy-db-net.tsv",
    "AWS::CLF::04-サービス",
    [
        c("「結合クエリが必要・リレーショナル」何？", "RDS/Aurora", "clf", "services", "hy"),
        c("「超高トラフィックのキーバリュー」何？", "DynamoDB", "clf", "services", "hy"),
        c("「セッションを高速キャッシュ」何？", "ElastiCache", "clf", "services", "hy"),
        c("「BI用に列指向で集計」何？", "Redshift", "clf", "services", "hy"),
        c("AuroraがRDSより選ばれる理由（CLF）は？", "性能・可用性・ストレージ自動拡張などAWS最適化", "clf", "services", "hy"),
        c("DynamoDBの運用で楽な点は？", "サーバレスでスケール管理が軽い", "clf", "services", "hy"),
        c("「マルチAZ DB」が欲しいとき（RDS）は？", "スタンバイを別AZに置く構成を選ぶ", "clf", "services", "hy"),
        c("読み込み負荷を分散するRDSの仕組みは？", "リードレプリカ", "clf", "services", "hy"),
        c("パブリックサブネットの典型用途は？", "ALBやNAT、踏み台など", "clf", "services", "hy"),
        c("プライベートサブネットの典型用途は？", "アプリサーバ・DB", "clf", "services", "hy"),
        c("ルートテーブルの役割は？", "どこ向けの通信をどこへ送るか", "clf", "services", "hy"),
        c("IGWがないとできないことは？", "サブネットから直接インターネット双方向（構成依存）", "clf", "services", "hy"),
        c("NAT Gatewayの目的は？", "プライベートから外への更新通信を許す", "clf", "services", "hy"),
        c("VPCピアリングの制限のイメージは？", "推移的ルーティングができない等（ハブが要るならTGW）", "clf", "services", "hy"),
        c("Direct Connectの利点は？", "安定帯域・低揺らぎ・閉域寄り接続", "clf", "services", "hy"),
        c("Site-to-Site VPNの利点は？", "すぐ作れる暗号化トンネル", "clf", "services", "hy"),
        c("Route 53のルーティング例は？", "単純・フェイルオーバ・レイテンシ・地理など", "clf", "services", "hy"),
        c("API Gatewayの後ろに置く定番は？", "Lambda や HTTPサービス", "clf", "services", "hy"),
        c("「DNSでプライマリ死んだらセカンダリ」何？", "Route 53フェイルオーバ", "clf", "services", "hy"),
        c("「世界のユーザーを近いリージョンへ」DNSは？", "レイテンシベース等", "clf", "services", "hy"),
    ],
)

p(
    "04-services/14-hy-integration-analytics-ml.tsv",
    "AWS::CLF::04-サービス",
    [
        c("SQS標準とFIFOの差（CLF）は？", "FIFO=順序と正確に一度の処理に強い / 標準=高スループット", "clf", "services", "hy"),
        c("SQSで消費者は何をする？", "キューからメッセージを取得（プル）", "clf", "services", "hy"),
        c("SNSの購読者の例は？", "メール、SQS、Lambda、HTTP", "clf", "services", "hy"),
        c("ファンアウト構成とは？", "SNS→複数SQSなどへ同時配信", "clf", "services", "hy"),
        c("EventBridgeのルールとは？", "イベントパターンにマッチしたらターゲットへ送る", "clf", "services", "hy"),
        c("Step Functionsが向くのは？", "複数ステップの業務フロー可視化・リトライ", "clf", "services", "hy"),
        c("Athenaの課金イメージは？", "スキャンしたデータ量など", "clf", "services", "hy"),
        c("Glue Data Catalogの役割は？", "テーブル定義のメタデータ置き場", "clf", "services", "hy"),
        c("Firehoseが楽な理由は？", "配信先へのバッファリングや変換を任せやすい", "clf", "services", "hy"),
        c("QuickSightのユーザーは誰？", "ビジネスユーザー・分析者向けBI", "clf", "services", "hy"),
        c("EMRが使うエンジンの例は？", "Spark / Hadoop 等", "clf", "services", "hy"),
        c("OpenSearchの典型用途は？", "ログ検索・全文検索", "clf", "services", "hy"),
        c("SageMakerの範囲は？", "学習データ準備〜学習〜デプロイ", "clf", "services", "hy"),
        c("Rekognitionでできる例は？", "物体検出・顔分析・不適切コンテンツ検知", "clf", "services", "hy"),
        c("Textractでできる例は？", "請求書やフォームから項目抽出", "clf", "services", "hy"),
        c("Pollyの入力と出力は？", "テキスト→音声", "clf", "services", "hy"),
        c("Transcribeの入力と出力は？", "音声→テキスト", "clf", "services", "hy"),
        c("Translateは？", "テキストの言語変換", "clf", "services", "hy"),
        c("Comprehendは？", "テキストの洞察（感情・キーフレーズ等）", "clf", "services", "hy"),
        c("Lexは？", "音声/テキストの会話インターフェース構築", "clf", "services", "hy"),
        c("Kendraは？", "社内文書のエンタープライズ検索", "clf", "services", "hy"),
        c("「どのMLサービスか迷ったら」CLFの戦術は？", "入出力のメディア（画像/音声/テキスト）で当てる", "clf", "services", "hy"),
    ],
)

p(
    "04-services/15-hy-migrate-devops-mgmt.tsv",
    "AWS::CLF::04-サービス",
    [
        c("DMSの均一移行とは？", "同じエンジン同士（例: Oracle→Oracle）", "clf", "services", "hy"),
        c("DMSの異種移行とは？", "エンジンが違う（例: Oracle→Aurora PostgreSQL）", "clf", "services", "hy"),
        c("Snowballのイメージは？", "ペタ未満〜大容量を物理搬送", "clf", "services", "hy"),
        c("DataSyncが効くのは？", "オンラインで大量ファイルを繰り返し同期", "clf", "services", "hy"),
        c("Transfer Familyが効くのは？", "既存SFTPクライアントを変えずにS3へ", "clf", "services", "hy"),
        c("MGNの移行スタイルは？", "リホスト（ほぼそのまま移す）", "clf", "services", "hy"),
        c("CloudFormationのスタックとは？", "テンプレから作ったリソースのまとまり", "clf", "services", "hy"),
        c("CDKの利点は？", "TypeScript等でインフラを書きCFNに変換", "clf", "services", "hy"),
        c("CodeCommitは何の代替？", "マネージドGitリポジトリ", "clf", "services", "hy"),
        c("CodeBuildは何をする？", "コンパイル・テストを実行", "clf", "services", "hy"),
        c("CodeDeployは何をする？", "EC2/Lambda等へのデプロイ自動化", "clf", "services", "hy"),
        c("CodePipelineのステージ例は？", "Source→Build→Deploy", "clf", "services", "hy"),
        c("CloudShellの利点は？", "ブラウザですぐCLI、認証済み", "clf", "services", "hy"),
        c("CloudWatch Logsは？", "アプリ/OSログの集約", "clf", "services", "hy"),
        c("CloudWatch Metricsは？", "CPU等の数値時系列", "clf", "services", "hy"),
        c("アラームの定番アクションは？", "SNS通知、Auto Scaling操作など", "clf", "services", "hy"),
        c("Systems Manager Parameter StoreとSecretsの使い分け再確認は？", "設定=Parameter寄り / 秘密ローテ=Secrets寄り", "clf", "services", "hy"),
        c("Session Managerの利点は？", "SSHポートを開けずにシェル", "clf", "services", "hy"),
        c("Health Dashboardでわかることの例は？", "AWS側障害が自分のリソースに関係するか", "clf", "services", "hy"),
        c("X-Rayが欲しくなる症状は？", "マイクロサービス間で遅い箇所がわからない", "clf", "services", "hy"),
        c("Service Catalogの利用者メリットは？", "承認済み構成だけをポータルから起動", "clf", "services", "hy"),
        c("「誰がいつセキュリティグループを変えた」一次情報は？", "CloudTrail", "clf", "services", "hy"),
        c("「今のSG設定が先週と違う」一次情報は？", "Config", "clf", "services", "hy"),
        c("コンソールとCLIの使い分けは？", "コンソール=視覚操作 / CLI=自動化・再現", "clf", "services", "hy"),
        c("SDKを使う理由は？", "アプリコードからAWS APIを呼ぶ", "clf", "services", "hy"),
    ],
)


def write_tsv(path: Path, cards: list[tuple[str, str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    for front, back, tags in cards:
        front = front.replace("\t", " ").replace("\n", "<br>")
        back = back.replace("\t", " ").replace("\n", "<br>")
        tags = tags.replace("\t", " ")
        lines.append(f"{front}\t{back}\t{tags}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    written: list[tuple[Path, str]] = []
    total = 0
    for rel, deck, cards in PACKS:
        path = OUT / rel
        write_tsv(path, cards)
        total += len(cards)
        written.append((path, deck))
        print(f"wrote {path.relative_to(ROOT)} ({len(cards)})")

    failed = 0
    for path, deck in written:
        r = subprocess.run([sys.executable, str(ADD), "--deck", deck, str(path)], cwd=str(ROOT))
        if r.returncode != 0:
            failed += 1
            print(f"FAIL {path}")

    print(f"DONE new_cards={total} files={len(written)} failed={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
