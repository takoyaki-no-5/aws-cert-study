#!/usr/bin/env python3
"""AnkiConnect でカードを閲覧・検索・削除する。

使い方:
  python3 .cursor/hooks/anki-manage.py decks
  python3 .cursor/hooks/anki-manage.py count 'deck:AWS::CLF*'
  python3 .cursor/hooks/anki-manage.py list 'deck:AWS::CLF::01-セキュリティ' --limit 20
  python3 .cursor/hooks/anki-manage.py show 1784897024681
  python3 .cursor/hooks/anki-manage.py search '接続テスト'
  python3 .cursor/hooks/anki-manage.py delete --query '接続テスト' --yes
  python3 .cursor/hooks/anki-manage.py delete --ids 1784897024681 --yes
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
    for c in (
        shutil.which("curl.exe"),
        "/mnt/c/Windows/System32/curl.exe",
        "C:/Windows/System32/curl.exe",
    ):
        if c and os.path.isfile(c):
            return c
    return None


def invoke_direct(url: str, action: str, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    req = urllib.request.Request(
        url, data=payload, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=10) as res:
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
        timeout=60,
    )
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "curl failed").strip())
    body = json.loads(r.stdout.strip())
    if body.get("error"):
        raise RuntimeError(body["error"])
    return body.get("result")


_MODE = None


def invoke(action: str, **params):
    global _MODE
    errors = []
    if on_wsl() or _MODE == "win-curl":
        try:
            result = invoke_via_win_curl(action, **params)
            _MODE = "win-curl"
            return result
        except Exception as e:  # noqa: BLE001
            errors.append(str(e))
            if _MODE == "win-curl":
                raise
    try:
        url = os.environ.get("ANKICONNECT_URL", "http://127.0.0.1:8765")
        result = invoke_direct(url, action, **params)
        _MODE = "direct"
        return result
    except Exception as e:  # noqa: BLE001
        errors.append(str(e))
        raise RuntimeError("; ".join(errors)) from e


def field_map(note: dict) -> dict[str, str]:
    fields = note.get("fields") or {}
    return {k: (v.get("value") if isinstance(v, dict) else str(v)) for k, v in fields.items()}


def front_back(note: dict) -> tuple[str, str]:
    fm = field_map(note)
    for a, b in (("表面", "裏面"), ("Front", "Back"), ("質問", "答え")):
        if a in fm and b in fm:
            return fm[a], fm[b]
    vals = list(fm.values())
    return (vals[0] if vals else "", vals[1] if len(vals) > 1 else "")


def cmd_decks(_: argparse.Namespace) -> int:
    for name in sorted(invoke("deckNames") or []):
        if name.startswith("AWS") or "CLF" in name:
            print(name)
    print("---")
    for name in sorted(invoke("deckNames") or []):
        if not (name.startswith("AWS") or "CLF" in name):
            print(name)
    return 0


def cmd_count(args: argparse.Namespace) -> int:
    ids = invoke("findNotes", query=args.query) or []
    print(f"{len(ids)}\t{args.query}")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    ids = invoke("findNotes", query=args.query) or []
    total = len(ids)
    ids = ids[: args.limit]
    if not ids:
        print("(0 notes)")
        return 0
    notes = invoke("notesInfo", notes=ids) or []
    print(f"showing {len(notes)}/{total}")
    for n in notes:
        front, back = front_back(n)
        front_one = front.replace("\n", " ")[:80]
        print(f"{n['noteId']}\t{front_one}\t tags={n.get('tags')}")
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    notes = invoke("notesInfo", notes=args.ids) or []
    for n in notes:
        front, back = front_back(n)
        print(f"id: {n['noteId']}")
        print(f"model: {n.get('modelName')}")
        print(f"tags: {n.get('tags')}")
        print(f"--- front ---\n{front}")
        print(f"--- back ---\n{back}")
        print()
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    # Anki 検索: 文言はそのまま。デッキ絞りがあれば付ける
    q = args.text
    if args.deck:
        q = f'deck:"{args.deck}" {q}'
    args.query = q
    return cmd_list(args)


def cmd_delete(args: argparse.Namespace) -> int:
    ids: list[int] = []
    if args.ids:
        ids.extend(args.ids)
    if args.query:
        ids.extend(invoke("findNotes", query=args.query) or [])
    # unique
    ids = sorted(set(ids))
    if not ids:
        print("削除対象なし")
        return 0
    notes = invoke("notesInfo", notes=ids[:50]) or []
    print(f"削除予定: {len(ids)} 枚（先頭最大50件を表示）")
    for n in notes:
        front, _ = front_back(n)
        print(f"  {n['noteId']}\t{front.replace(chr(10), ' ')[:70]}")
    if not args.yes:
        print("実行するには --yes を付けてください")
        return 2
    invoke("deleteNotes", notes=ids)
    print(f"deleted {len(ids)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Anki note browse/delete via AnkiConnect")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("decks", help="デッキ一覧")
    p.set_defaults(func=cmd_decks)

    p = sub.add_parser("count", help="検索ヒット数")
    p.add_argument("query")
    p.set_defaults(func=cmd_count)

    p = sub.add_parser("list", help="ノート一覧（IDと表面）")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=30)
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("show", help="ノート詳細")
    p.add_argument("ids", nargs="+", type=int)
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("search", help="文言検索")
    p.add_argument("text")
    p.add_argument("--deck", default="")
    p.add_argument("--limit", type=int, default=30)
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("delete", help="ノート削除（要 --yes）")
    p.add_argument("--ids", nargs="*", type=int, default=[])
    p.add_argument("--query", default="")
    p.add_argument("--yes", action="store_true")
    p.set_defaults(func=cmd_delete)

    args = ap.parse_args()
    try:
        invoke("version")
    except Exception as e:
        print(f"AnkiConnect に接続できません: {e}", file=sys.stderr)
        return 1
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
