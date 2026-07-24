#!/usr/bin/env python3
"""AnkiConnect 経由でカードを追加する（Anki Desktop 起動 + AnkiConnect 必須）。

WSL からは Windows の localhost:8765 に届かないため、Windows の curl.exe 経由で中継する。

使い方:
  python3 .cursor/hooks/anki-add.py --deck 'AWS::CLF' study/anki/clf_2026-07-24_billing.tsv
  python3 .cursor/hooks/anki-add.py --deck 'AWS::CLF' --front 'Q' --back 'A' --tags 'clf billing'
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import urllib.request


def on_wsl() -> bool:
    if os.environ.get("WSL_DISTRO_NAME"):
        return True
    try:
        return "microsoft" in open("/proc/version", encoding="utf-8").read().lower()
    except OSError:
        return False


def find_win_curl() -> str | None:
    candidates = [
        shutil.which("curl.exe"),
        "/mnt/c/Windows/System32/curl.exe",
        "C:/Windows/System32/curl.exe",
    ]
    for c in candidates:
        if c and os.path.isfile(c):
            return c
    return None


def invoke_direct(url: str, action: str, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    req = urllib.request.Request(
        url, data=payload, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=5) as res:
        body = json.loads(res.read().decode())
    if body.get("error"):
        raise RuntimeError(body["error"])
    return body.get("result")


def invoke_via_win_curl(action: str, **params):
    curl = find_win_curl()
    if not curl:
        raise RuntimeError("Windows curl.exe が見つかりません")
    payload = json.dumps({"action": action, "version": 6, "params": params})
    r = subprocess.run(
        [
            curl,
            "-sS",
            "--connect-timeout",
            "5",
            "http://127.0.0.1:8765",
            "-H",
            "Content-Type: application/json",
            "-d",
            payload,
        ],
        capture_output=True,
        text=True,
        timeout=20,
    )
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "curl failed").strip())
    out = r.stdout.strip()
    if not out:
        raise RuntimeError("empty response from AnkiConnect")
    body = json.loads(out)
    if body.get("error"):
        raise RuntimeError(body["error"])
    return body.get("result")


_MODE: str | None = None


def invoke(action: str, **params):
    global _MODE
    errors: list[str] = []

    # WSL では先に Windows curl 経由を試す
    if on_wsl() or _MODE == "win-curl":
        try:
            result = invoke_via_win_curl(action, **params)
            _MODE = "win-curl"
            return result
        except Exception as e:  # noqa: BLE001
            errors.append(f"win-curl: {e}")
            if _MODE == "win-curl":
                raise RuntimeError("; ".join(errors)) from e

    try:
        url = os.environ.get("ANKICONNECT_URL", "http://127.0.0.1:8765")
        result = invoke_direct(url, action, **params)
        _MODE = "direct"
        return result
    except Exception as e:  # noqa: BLE001
        errors.append(f"direct: {e}")
        raise RuntimeError("; ".join(errors)) from e


def ensure_deck(name: str) -> None:
    invoke("createDeck", deck=name)


def resolve_model(preferred: str | None = None) -> tuple[str, str, str]:
    """ノートタイプと表裏フィールド名を決める。日本語版は『基本』/表面/裏面。"""
    models = invoke("modelNames") or []
    candidates = []
    if preferred:
        candidates.append(preferred)
    candidates.extend(["Basic", "基本", "Modern Q&A [v2] [ja]"])
    model = next((m for m in candidates if m in models), None)
    if not model:
        raise RuntimeError(f"ノートタイプが見つかりません: {models}")
    fields = invoke("modelFieldNames", modelName=model) or []
    if model in ("Basic", "基本") and len(fields) >= 2:
        return model, fields[0], fields[1]
    if "Front" in fields and "Back" in fields:
        return model, "Front", "Back"
    if "表面" in fields and "裏面" in fields:
        return model, "表面", "裏面"
    if "質問" in fields and "答え" in fields:
        return model, "質問", "答え"
    if len(fields) >= 2:
        return model, fields[0], fields[1]
    raise RuntimeError(f"フィールドが足りません: {model} -> {fields}")


def add_note(
    deck: str,
    front: str,
    back: str,
    tags: list[str],
    model: str,
    front_field: str,
    back_field: str,
) -> int:
    return invoke(
        "addNote",
        note={
            "deckName": deck,
            "modelName": model,
            "fields": {front_field: front, back_field: back},
            "tags": tags,
            "options": {"allowDuplicate": False},
        },
    )


def parse_tsv(path: str):
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                raise ValueError(f"{path}:{line_no}: need Front\\tBack")
            front, back = parts[0], parts[1]
            tags = parts[2].split() if len(parts) > 2 and parts[2].strip() else []
            yield front, back, tags


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--deck", required=True)
    ap.add_argument("--front")
    ap.add_argument("--back")
    ap.add_argument("--tags", default="")
    ap.add_argument("--model", help="ノートタイプ名（省略時は Basic / 基本 を自動選択）")
    ap.add_argument("tsv", nargs="?")
    args = ap.parse_args()

    try:
        ver = invoke("version")
    except Exception as e:
        print(
            "AnkiConnect に接続できません。Anki を起動し、アドオン 2055492159 を入れてください。",
            file=sys.stderr,
        )
        print(f"詳細: {e}", file=sys.stderr)
        return 1

    print(f"connected via {_MODE} (api v{ver})")
    ensure_deck(args.deck)
    model, front_field, back_field = resolve_model(args.model)
    print(f"model={model} fields={front_field}/{back_field}")
    added = 0
    skipped = 0

    notes = []
    if args.tsv:
        notes.extend(parse_tsv(args.tsv))
    if args.front is not None:
        if args.back is None:
            print("--front には --back が必要です", file=sys.stderr)
            return 1
        notes.append((args.front, args.back, args.tags.split()))

    if not notes:
        print("追加するカードがありません", file=sys.stderr)
        return 1

    for front, back, tags in notes:
        try:
            add_note(args.deck, front, back, tags, model, front_field, back_field)
            added += 1
        except RuntimeError as e:
            if "duplicate" in str(e).lower():
                skipped += 1
            else:
                raise

    print(f"OK: added={added} skipped_duplicate={skipped} deck={args.deck}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
