#!/usr/bin/env python3
"""CLF Anki の意味的重複（同じ知識を問うカード）を検出する。依存なし。"""
from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("study/anki/clf")
OUT = Path("study/anki/clf/06-review/semantic-dupes.md")
THRESHOLD = 0.42
CLUSTER_TH = 0.50


def tokenize(text: str) -> Counter:
    text = re.sub(r"<[^>]+>", "", text or "")
    text = text.lower()
    # 文字 bigram/trigram + 簡易単語
    grams: list[str] = []
    compact = re.sub(r"\s+", "", text)
    for n in (2, 3):
        for i in range(max(0, len(compact) - n + 1)):
            grams.append(compact[i : i + n])
    for w in re.findall(r"[a-z0-9]{2,}|[\u3040-\u30ff\u4e00-\u9fff]{1,}", text):
        grams.append(f"w:{w}")
    return Counter(grams)


def cosine(a: Counter, b: Counter) -> float:
    if not a or not b:
        return 0.0
    keys = set(a) | set(b)
    dot = sum(a[k] * b[k] for k in keys)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def load_cards():
    cards = []
    for p in sorted(ROOT.rglob("*.tsv")):
        if "06-review" in p.parts:
            continue
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            front, back = parts[0], parts[1]
            cards.append(
                {
                    "file": str(p).replace("\\", "/"),
                    "line": i,
                    "front": front,
                    "back": back,
                    "text": f"{front} {back}",
                    "vec": tokenize(f"{front} {back}"),
                }
            )
    return cards


def main() -> int:
    cards = load_cards()
    n = len(cards)
    print(f"cards={n}")

    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            # 裏面だけ同じ・表面だけ同じも拾うため text 全体
            s = cosine(cards[i]["vec"], cards[j]["vec"])
            if s >= THRESHOLD:
                pairs.append((s, i, j))
    pairs.sort(reverse=True)
    print(f"pairs>={THRESHOLD}: {len(pairs)}")

    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for s, i, j in pairs:
        if s >= CLUSTER_TH:
            union(i, j)

    clusters: dict[int, list[int]] = defaultdict(list)
    for i in range(n):
        clusters[find(i)].append(i)
    multi = [m for m in clusters.values() if len(m) >= 2]
    multi.sort(key=len, reverse=True)

    lines = [
        "# CLF Anki 意味的重複レポート",
        "",
        f"- 対象: {n} 枚",
        f"- 類似ペア（cosine≥{THRESHOLD}）: {len(pairs)}",
        f"- まとめクラスタ（≥{CLUSTER_TH}）: {len(multi)}",
        "",
        "自動判定。文言が似ていても「対比の別側面」なら残す価値あり。",
        "消す候補はクラスタ内で1枚残せば十分なもの。",
        "",
        "## 強い重複候補（上位）",
        "",
    ]
    for s, i, j in pairs[:100]:
        a, b = cards[i], cards[j]
        lines += [
            f"### {s:.2f}",
            f"- A: {a['front']}",
            f"  - {a['back'][:140]}",
            f"  - `{a['file']}:{a['line']}`",
            f"- B: {b['front']}",
            f"  - {b['back'][:140]}",
            f"  - `{b['file']}:{b['line']}`",
            "",
        ]

    lines += ["## クラスタ（同じ知識塊の可能性）", ""]
    for members in multi[:50]:
        lines.append(f"### {len(members)}枚")
        for idx in members:
            c = cards[idx]
            lines.append(f"- {c['front']} → `{c['file']}:{c['line']}`")
        lines.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")

    print("\n=== TOP 30 ===")
    for s, i, j in pairs[:30]:
        print(f"{s:.2f} | {cards[i]['front'][:50]}")
        print(f"     | {cards[j]['front'][:50]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
