#!/usr/bin/env python3
"""Discord Webhook 通知（Cloud Secret `discord_daily_bot`）。

Usage:
  python3 .cursor/hooks/discord-notify.py "メッセージ"
  echo "メッセージ" | python3 .cursor/hooks/discord-notify.py
  python3 .cursor/hooks/discord-notify.py --file path.md

Env:
  discord_daily_bot  Discord Incoming Webhook URL（必須）
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

SECRET_ENV = "discord_daily_bot"
MAX_CONTENT = 1900  # Discord limit 2000; leave headroom
DEFAULT_USERNAME = "aws-cert-study"


def load_webhook() -> str:
    url = (os.environ.get(SECRET_ENV) or "").strip()
    if not url:
        raise SystemExit(
            f"missing env {SECRET_ENV} "
            "(Cloud Agent Secrets に Webhook URL を設定)"
        )
    if not url.startswith("https://discord.com/api/webhooks/") and not url.startswith(
        "https://discordapp.com/api/webhooks/"
    ):
        raise SystemExit(f"{SECRET_ENV} does not look like a Discord webhook URL")
    return url


def post(content: str, *, username: str = DEFAULT_USERNAME) -> int:
    content = content.strip()
    if not content:
        raise SystemExit("empty message")
    if len(content) > MAX_CONTENT:
        content = content[: MAX_CONTENT - 20] + "\n…(省略)"

    url = load_webhook()
    payload = json.dumps(
        {"content": content, "username": username},
        ensure_ascii=False,
    ).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "aws-cert-study-discord-notify/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            # 204 No Content is normal for webhooks
            print(f"ok status={resp.status}")
            return 0
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:300]
        print(f"HTTPError status={e.code} body={body}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"ERROR {type(e).__name__}: {e}", file=sys.stderr)
        return 1


def main() -> int:
    p = argparse.ArgumentParser(description="Post a Discord webhook message")
    p.add_argument("message", nargs="?", help="Message text")
    p.add_argument("--file", "-f", help="Read message from file")
    p.add_argument("--username", "-u", default=DEFAULT_USERNAME)
    args = p.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            content = f.read()
    elif args.message:
        content = args.message
    elif not sys.stdin.isatty():
        content = sys.stdin.read()
    else:
        p.error("provide message, --file, or stdin")

    return post(content, username=args.username)


if __name__ == "__main__":
    raise SystemExit(main())
