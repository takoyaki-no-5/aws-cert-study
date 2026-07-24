#!/usr/bin/env python3
"""CLF デッキ内で表面が同一のノートを検出し、重複を削除（1枚残す）。"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
from collections import defaultdict


def on_wsl() -> bool:
    if os.environ.get("WSL_DISTRO_NAME"):
        return True
    try:
        return "microsoft" in open("/proc/version", encoding="utf-8").read().lower()
    except OSError:
        return False


def find_win_curl():
    for c in (
        shutil.which("curl.exe"),
        "/mnt/c/Windows/System32/curl.exe",
        "C:/Windows/System32/curl.exe",
    ):
        if c and os.path.isfile(c):
            return c
    return None


def invoke_via_win_curl(action: str, **params):
    curl = find_win_curl()
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
        timeout=120,
    )
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "curl failed").strip())
    body = json.loads(r.stdout.strip())
    if body.get("error"):
        raise RuntimeError(body["error"])
    return body.get("result")


def invoke_direct(action: str, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    req = urllib.request.Request(
        "http://127.0.0.1:8765",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as res:
        body = json.loads(res.read().decode())
    if body.get("error"):
        raise RuntimeError(body["error"])
    return body.get("result")


def invoke(action: str, **params):
    if on_wsl():
        return invoke_via_win_curl(action, **params)
    return invoke_direct(action, **params)


def normalize(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text or "")
    text = text.replace("\u3000", " ")
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text


def front_of(note: dict) -> str:
    fields = note.get("fields") or {}
    for key in ("表面", "Front", "質問"):
        if key in fields:
            v = fields[key]
            return v.get("value") if isinstance(v, dict) else str(v)
    vals = list(fields.values())
    if not vals:
        return ""
    v = vals[0]
    return v.get("value") if isinstance(v, dict) else str(v)


def batched(xs, n=50):
    for i in range(0, len(xs), n):
        yield xs[i : i + n]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", default="deck:AWS::CLF*")
    ap.add_argument("--yes", action="store_true")
    args = ap.parse_args()

    invoke("version")
    ids = invoke("findNotes", query=args.query) or []
    print(f"notes in scope: {len(ids)}")

    notes = []
    for chunk in batched(ids, 100):
        notes.extend(invoke("notesInfo", notes=chunk) or [])

    groups: dict[str, list[dict]] = defaultdict(list)
    for n in notes:
        key = normalize(front_of(n))
        if not key:
            continue
        groups[key].append(n)

    dup_groups = {k: v for k, v in groups.items() if len(v) > 1}
    to_delete: list[int] = []
    print(f"duplicate front groups: {len(dup_groups)}")
    for key, group in sorted(dup_groups.items(), key=lambda x: -len(x[1])):
        # 最も古い noteId を残す
        group_sorted = sorted(group, key=lambda n: n["noteId"])
        keep = group_sorted[0]
        drop = group_sorted[1:]
        to_delete.extend(n["noteId"] for n in drop)
        front = front_of(keep).replace("\n", " ")[:70]
        print(f"  x{len(group)} keep={keep['noteId']} drop={[n['noteId'] for n in drop]} | {front}")

    print(f"would delete: {len(to_delete)}")
    if not to_delete:
        print("重複なし")
        return 0
    if not args.yes:
        print("実行するには --yes")
        return 2

    for chunk in batched(to_delete, 100):
        invoke("deleteNotes", notes=chunk)
    left = invoke("findNotes", query=args.query) or []
    print(f"deleted: {len(to_delete)}; remaining: {len(left)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
