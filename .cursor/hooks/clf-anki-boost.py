#!/usr/bin/env python3
"""CLF カード増強（シナリオ・対比・誤答切り）。既存と正面が違うので重複しにくい。"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "study" / "anki" / "clf"
ADD = ROOT / ".cursor" / "hooks" / "anki-add.py"

PACKS: list[tuple[str, str, list[tuple[str, str, str]]]] = []


def pack(rel: str, deck: str, cards: list[tuple[str, str, str]]) -> None:
    PACKS.append((rel, deck, cards))


pack(
    "01-security/08-scenarios.tsv",
    "AWS::CLF::01-セキュリティ",
    [
        ("「EC2上のアプリがS3にアクセス」正しい権限の付け方は？", "EC2にIAMロール（インスタンスプロファイル）。キーを埋め込まない", "clf security scenario"),
        ("「社員が退職した。権限をすぐ止めたい」最初に見るのは？", "IAMユーザーの無効化/削除、アクセスキー無効、フェデレーションならIdP側も", "clf security scenario"),
        ("「全アカウントで特定サービスを禁止したい」何を使う？", "Organizations の SCP", "clf security scenario"),
        ("「S3にクレジットカード番号がありそう」何で探す？", "Macie", "clf security scenario"),
        ("「怪しいAPI呼び出しが増えた」何で検知？", "GuardDuty（CloudTrail等を解析）", "clf security scenario"),
        ("「EC2のCVEを調べたい」何を使う？", "Inspector", "clf security scenario"),
        ("「誰がいつIAMを変えたか知りたい」何を見る？", "CloudTrail", "clf security scenario"),
        ("「リソースがルールから外れてないか継続監視」何？", "Config", "clf security scenario"),
        ("「DDoSが来た」標準で付く防護は？", "Shield Standard（無料・自動）", "clf security scenario"),
        ("「SQLインジェクションをHTTPで防ぎたい」何？", "WAF", "clf security scenario"),
        ("「TLS証明書をALBに付けたい」何？", "ACM", "clf security scenario"),
        ("「秘密鍵を自動ローテさせたい」Secrets Manager と Parameter Store どちら？", "Secrets Manager", "clf security scenario"),
        ("「オンプレの監査人がAWSのSOCレポートが欲しい」どこ？", "Artifact", "clf security scenario"),
        ("「サブネット全体で特定ポートを明示拒否したい」SGとNACLどちら？", "NACL（拒否ルールが書ける）", "clf security scenario"),
        ("「同じアカウント内で権限を一時的に借りる」何？", "IAMロールの引き受け（AssumeRole）", "clf security scenario"),
        ("ルートユーザーに必須の対策は？", "MFA。日常作業では使わない", "clf security scenario"),
        ("「外部に公開されているS3がないか」何で点検？", "IAM Access Analyzer（またはTrusted Advisor/Security Hub）", "clf security scenario"),
        ("「マルチアカウントの初期セットアップを標準化」何？", "Control Tower", "clf security scenario"),
        ("「保存データも通信も暗号化したい」キーワードは？", "保存時（SSE等）と転送時（TLS）の両方", "clf security scenario"),
        ("「セキュリティ検出結果を1画面に集めたい」何？", "Security Hub", "clf security scenario"),
    ],
)

pack(
    "02-billing/06-scenarios.tsv",
    "AWS::CLF::02-請求",
    [
        ("「いつ止まるかわからないバッチ」一番安いコンピュートは？", "スポット（中断耐性がある前提）", "clf billing scenario"),
        ("「安定した24/365本番、1年は使う」割引の第一候補は？", "Savings Plans または RI", "clf billing scenario"),
        ("「リージョンをまたぐ構成変更が多く柔軟さが欲しい割引」どっち？", "Savings Plans（RIより柔軟）", "clf billing scenario"),
        ("「来月の請求が跳ねたらメールしたい」何？", "Budgets", "clf billing scenario"),
        ("「部門別にコストを分けたい」何が必要？", "コスト配分タグ（＋激活）", "clf billing scenario"),
        ("「導入前に月額を概算したい」何？", "Pricing Calculator", "clf billing scenario"),
        ("「最も詳細な利用内訳CSVが欲しい」何？", "CUR（Cost and Usage Report）", "clf billing scenario"),
        ("「画面で先月比のグラフを見たい」何？", "Cost Explorer", "clf billing scenario"),
        ("「大きすぎるEC2を勧めてほしい」何？", "Compute Optimizer", "clf billing scenario"),
        ("「本番障害で電話サポートが要る」最低プランは？", "Business", "clf billing scenario"),
        ("「TAMが欲しい」どの帯？", "Enterprise（または同等の上位）", "clf billing scenario"),
        ("「無料のTrusted Advisorは全部使える？」", "いいえ。Basicはコアチェック限定。全項目はBusiness以上", "clf billing scenario"),
        ("「アカウントを増やしても請求書は1枚にしたい」何？", "Organizations 一括請求", "clf billing scenario"),
        ("「インターネットからS3へ入れる転送」課金イメージは？", "多くの場合、入向きは無料寄り。出向き・AZ間は注意", "clf billing scenario"),
        ("「BYOLで物理ソケットが必要」何？", "Dedicated Hosts", "clf billing scenario"),
        ("「サードパーティのAMIを課金付きで買いたい」どこ？", "Marketplace", "clf billing scenario"),
        ("「短期間だけAWSに詳しい人を雇いたい」何？", "IQ", "clf billing scenario"),
        ("Developer と Business の最大の差は？", "本番向け24/365と応答目標・Trusted Advisor全項目はBusiness側", "clf billing scenario"),
        ("「12か月無料枠が切れたあと」どうなる？", "対象外は通常課金。常時無料枠だけ残るものもある", "clf billing scenario"),
        ("「請求の問い合わせだけ」どのプランでもできる？", "Basicでもアカウント/請求のサポートは受けられる", "clf billing scenario"),
    ],
)

pack(
    "03-concepts/06-scenarios.tsv",
    "AWS::CLF::03-概念",
    [
        ("「サーバを買わずに使った分だけ払う」どのメリット？", "固定費→変動費（CapEx→OpEx）", "clf concepts scenario"),
        ("「ブラックフライデーで自動増減」何の性質？", "弾力性", "clf concepts scenario"),
        ("「障害が起きてもサービス継続」設計の柱は？", "信頼性（耐障害性の話にもつながる）", "clf concepts scenario"),
        ("「電力効率や環境負荷も設計に入れる」柱は？", "サステナビリティ", "clf concepts scenario"),
        ("「暗号化と検知を徹底」柱は？", "セキュリティ", "clf concepts scenario"),
        ("「ムダなオーバープロビジョニングをやめる」柱は？", "コスト最適化", "clf concepts scenario"),
        ("「レイテンシを下げるため世界に分散」柱は？", "パフォーマンス効率", "clf concepts scenario"),
        ("「デプロイ手順をコード化して改善し続ける」柱は？", "運用上の優秀性", "clf concepts scenario"),
        ("「VMをほぼそのままAWSへ」7Rはどれ？", "Rehost（リフト&シフト）", "clf concepts scenario"),
        ("「少し改修してマネージドを使う」7Rは？", "Replatform", "clf concepts scenario"),
        ("「アプリを作り直してサーバレス化」7Rは？", "Refactor / Re-architect", "clf concepts scenario"),
        ("「SaaSに乗り換える」7Rは？", "Repurchase", "clf concepts scenario"),
        ("「まだ移さない」7Rは？", "Retain", "clf concepts scenario"),
        ("「捨てる」7Rは？", "Retire", "clf concepts scenario"),
        ("「東京の障害に備え大阪にも」何？", "マルチリージョン", "clf concepts scenario"),
        ("「同じリージョンでDC障害に耐える」最低限は？", "マルチAZ", "clf concepts scenario"),
        ("「静的サイトを世界中で速く」何？", "CloudFront（エッジ）", "clf concepts scenario"),
        ("「自社DCでAWSのAPIを使いたい」何？", "Outposts", "clf concepts scenario"),
        ("「5G基地局のすぐ近くで超低遅延」何？", "Wavelength", "clf concepts scenario"),
        ("「EC2はどのクラウドモデル？」", "IaaS", "clf concepts scenario"),
    ],
)

pack(
    "04-services/11-scenarios.tsv",
    "AWS::CLF::04-サービス",
    [
        ("「イベントでコードを短時間実行、サーバ管理したくない」何？", "Lambda", "clf services scenario"),
        ("「コンテナはあるがサーバは管理したくない」何？", "Fargate（ECS/EKSの起動タイプ）", "clf services scenario"),
        ("「KubernetesをAWSで」何？", "EKS", "clf services scenario"),
        ("「HTTPのパスで振り分け」LBはどれ？", "ALB", "clf services scenario"),
        ("「超高速・TCPで極低遅延LB」どれ？", "NLB", "clf services scenario"),
        ("「オブジェクトを安く長期保管、すぐ読まなくてよい」S3は？", "Glacier / Glacier Deep Archive 系", "clf services scenario"),
        ("「複数EC2で同じファイルをNFS共有」何？", "EFS", "clf services scenario"),
        ("「1台のEC2にディスク」何？", "EBS", "clf services scenario"),
        ("「キーバリューでミリ秒、サーバレスDB」何？", "DynamoDB", "clf services scenario"),
        ("「MySQL互換でマネージド、接合クエリ」何？", "RDS（またはAurora）", "clf services scenario"),
        ("「ペタバイト分析DWH」何？", "Redshift", "clf services scenario"),
        ("「S3のCSVにSQL」何？", "Athena", "clf services scenario"),
        ("「ログをほぼ自動でS3へストリーム」何？", "Kinesis Data Firehose", "clf services scenario"),
        ("「リアルタイムに自分で消費者を書くストリーム」何？", "Kinesis Data Streams", "clf services scenario"),
        ("「非同期で疎結合、引き取る側がペース制御」何？", "SQS", "clf services scenario"),
        ("「1つのイベントをメールとLambdaに同時通知」何？", "SNS", "clf services scenario"),
        ("「S3イベントやCronで複数サービス連携」何？", "EventBridge", "clf services scenario"),
        ("「オンプレDBをAWSへ継続レプリケ」何？", "DMS", "clf services scenario"),
        ("「100TBを回線が細くて送れない」何？", "Snow ファミリー", "clf services scenario"),
        ("「顔写真の人物判定」何？", "Rekognition", "clf services scenario"),
        ("「音声を字幕に」何？", "Transcribe", "clf services scenario"),
        ("「チャットボットの対話」何？", "Lex", "clf services scenario"),
        ("「IaCをYAMLで」何？", "CloudFormation", "clf services scenario"),
        ("「ビルド→テスト→デプロイを自動連結」何？", "CodePipeline", "clf services scenario"),
        ("「CPUアラームで通知」何？", "CloudWatch Alarm（+SNS等）", "clf services scenario"),
        ("「誰がStopInstancesしたか」何？", "CloudTrail", "clf services scenario"),
        ("「プライベートサブネットからパッチ適用したいがSSH鍵は嫌」何？", "Systems Manager Session Manager 等", "clf services scenario"),
        ("「DNSフェイルオーバ」何？", "Route 53", "clf services scenario"),
        ("「オンプレとAWSを専用線」何？", "Direct Connect", "clf services scenario"),
        ("「VPCを多数ハブ接続」何？", "Transit Gateway", "clf services scenario"),
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
        print(f"wrote {path.relative_to(ROOT)} ({len(cards)}) -> {deck}")

    failed = 0
    for path, deck in written:
        r = subprocess.run([sys.executable, str(ADD), "--deck", deck, str(path)], cwd=str(ROOT))
        if r.returncode != 0:
            failed += 1
    print(f"DONE cards={total} files={len(written)} failed={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
