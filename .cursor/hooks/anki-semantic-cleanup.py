#!/usr/bin/env python3
"""意味的重複として消す表面（完全一致）を TSV と Anki から削除。残す側は残す。"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path("study/anki/clf")

# 消す表面（残すカードの方が情報量・試験向き）
DELETE_FRONTS = [
    "Trusted Advisorのカテゴリ例は？",  # 「Trusted Advisor は？」にカテゴリ含む
    "CloudTrail と Config の違いは？（再確認）",  # 一言区別と同一
    "Systems Manager Parameter StoreとSecretsの使い分け再確認は？",  # 違いカードと同一
    "「最も詳細な利用内訳CSVが欲しい」何？",  # CUR定義と同一知識
    "「DNSフェイルオーバ」何？",  # プライマリ/セカンダリと同一
    "本番障害で24/365サポートが必要な最低プランは？",  # 電話サポート要ると同一
    "DeveloperとBusinessの決定的差を一言で？",  # 最大の差と同一
    "Basicで使えるサポート範囲の中心は？",  # Basicサポートは？と同一
    "「コンテナのサーバ管理をしたくない」何？",  # ほぼ同文シナリオ重複
    "「公開バケット」を見つけたい第一候補は？",  # 外部公開S3と同一
    "「超高トラフィックのキーバリュー」何？",  # ミリ秒サーバレスDBと同一
    "「導入前に月額を概算したい」何？",  # Pricing Calculatorは？と同一
    "Migration Evaluatorの価値は？",  # Migration Evaluatorは？と同一
    "「コードをzipで上げるとURLが欲しい」Paas的？",  # Beanstalkは？/PaaS例と重複
    "EC2 に AWS API 権限を付ける正しい方法は？",  # EC2→S3シナリオと同一知識
    "「無料のTrusted Advisorは全部使える？」",  # 全チェックが見られるプラン帯と同一
    "「マルチアカウントの初期セットアップを標準化」何？",  # Control Towerは何用と同一
    "「秘密鍵を自動ローテさせたい」Secrets Manager と Parameter Store どちら？",  # 違いカードで十分（ローテは裏面に含む）
]


def find_win_curl():
    for c in (
        shutil.which("curl.exe"),
        "/mnt/c/Windows/System32/curl.exe",
        "C:/Windows/System32/curl.exe",
    ):
        if c and os.path.isfile(c):
            return c
    return None


def on_wsl() -> bool:
    return bool(os.environ.get("WSL_DISTRO_NAME")) or (
        Path("/proc/version").exists()
        and "microsoft" in Path("/proc/version").read_text().lower()
    )


def invoke(action: str, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params})
    if on_wsl():
        curl = find_win_curl()
        r = subprocess.run(
            [
                curl,
                "-sS",
                "http://127.0.0.1:8765",
                "-H",
                "Content-Type: application/json",
                "-d",
                payload,
            ],
            capture_output=True,
            text=True,
            timeout=60,
        )
        body = json.loads(r.stdout.strip())
    else:
        import urllib.request

        req = urllib.request.Request(
            "http://127.0.0.1:8765",
            data=payload.encode(),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=30) as res:
            body = json.loads(res.read().decode())
    if body.get("error"):
        raise RuntimeError(body["error"])
    return body.get("result")


def scrub_tsv() -> int:
    removed = 0
    delete_set = set(DELETE_FRONTS)
    for p in ROOT.rglob("*.tsv"):
        lines = p.read_text(encoding="utf-8").splitlines()
        keep = []
        changed = False
        for line in lines:
            if not line.strip():
                continue
            front = line.split("\t")[0]
            if front in delete_set:
                removed += 1
                changed = True
                print(f"TSV- {p}: {front}")
            else:
                keep.append(line)
        if changed:
            p.write_text("\n".join(keep) + ("\n" if keep else ""), encoding="utf-8")
    return removed


def scrub_anki() -> int:
    invoke("version")
    all_ids = []
    for front in DELETE_FRONTS:
        # 表面完全一致に近い検索
        q = f'deck:AWS::CLF* "{front}"'
        ids = invoke("findNotes", query=q) or []
        # フィルタ: notesInfoで表面一致のみ
        if not ids:
            continue
        for chunk_start in range(0, len(ids), 50):
            chunk = ids[chunk_start : chunk_start + 50]
            for n in invoke("notesInfo", notes=chunk) or []:
                fields = n.get("fields") or {}
                val = ""
                for k in ("表面", "Front", "質問"):
                    if k in fields:
                        v = fields[k]
                        val = v.get("value") if isinstance(v, dict) else str(v)
                        break
                if val.strip() == front.strip():
                    all_ids.append(n["noteId"])
                    print(f"ANKI- {n['noteId']}: {front}")
    all_ids = sorted(set(all_ids))
    if all_ids:
        invoke("deleteNotes", notes=all_ids)
    return len(all_ids)


def main() -> int:
    t = scrub_tsv()
    a = scrub_anki()
    left_tsv = sum(
        1
        for p in ROOT.rglob("*.tsv")
        for line in p.read_text(encoding="utf-8").splitlines()
        if line.strip() and "06-review" not in p.parts
    )
    left_anki = len(invoke("findNotes", query="deck:AWS::CLF*") or [])
    print(f"removed_tsv_lines={t} removed_anki_notes={a}")
    print(f"remaining_tsv≈{left_tsv} remaining_anki={left_anki}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
