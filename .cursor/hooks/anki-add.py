#!/usr/bin/env python3
"""AnkiConnect 経由でカードを追加する（Anki Desktop 起動 + AnkiConnect 必須）。

使い方:
  # TSV（Front\\tBack\\tTags）を投入
  python3 .cursor/hooks/anki-add.py --deck 'AWS::CLF' study/anki/clf_2026-07-24_billing.tsv

  # 1枚だけ
  python3 .cursor/hooks/anki-add.py --deck 'AWS::CLF' --front 'Q' --back 'A' --tags 'clf billing'
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request


def invoke(action: str, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    req = urllib.request.Request(
        "http://127.0.0.1:8765",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=10) as res:
        body = json.loads(res.read().decode())
    if body.get("error"):
        raise RuntimeError(body["error"])
    return body.get("result")


def ensure_deck(name: str) -> None:
    invoke("createDeck", deck=name)


def add_note(deck: str, front: str, back: str, tags: list[str]) -> int:
    return invoke(
        "addNote",
        note={
            "deckName": deck,
            "modelName": "Basic",
            "fields": {"Front": front, "Back": back},
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
    ap.add_argument("tsv", nargs="?")
    args = ap.parse_args()

    try:
        invoke("version")
    except Exception as e:
        print(
            "AnkiConnect に接続できません。Anki を起動し、アドオン 2055492159 (AnkiConnect) を入れてください。",
            file=sys.stderr,
        )
        print(f"詳細: {e}", file=sys.stderr)
        return 1

    ensure_deck(args.deck)
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
            add_note(args.deck, front, back, tags)
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
