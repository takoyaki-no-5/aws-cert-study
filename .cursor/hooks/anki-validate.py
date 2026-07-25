#!/usr/bin/env python3
"""study/anki 配下の TSV が Anki インポート可能な形かを検査する。

使い方:
  python3 .cursor/hooks/anki-validate.py                    # 全部
  python3 .cursor/hooks/anki-validate.py study/anki/clf     # 範囲指定
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


def targets(args: list[str]) -> list[Path]:
    roots = [Path(a) for a in args] or [REPO / "study" / "anki"]
    files: list[Path] = []
    for root in roots:
        root = root if root.is_absolute() else REPO / root
        files.extend(sorted(root.rglob("*.tsv")) if root.is_dir() else [root])
    return files


def check(path: Path) -> list[str]:
    errors: list[str] = []
    fronts: Counter[str] = Counter()
    for i, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            errors.append(f"{i}: 空行")
            continue
        cols = raw.split("\t")
        if len(cols) not in (2, 3):
            errors.append(f"{i}: 列数 {len(cols)}（表面/裏面/タグの2〜3列）")
            continue
        if not cols[0].strip() or not cols[1].strip():
            errors.append(f"{i}: 表面か裏面が空")
        fronts[cols[0]] += 1
    for front, n in fronts.items():
        if n > 1:
            errors.append(f"表面が重複 {n}件: {front[:40]}")
    return errors


def main() -> int:
    failed = 0
    for path in targets(sys.argv[1:]):
        rel = path.relative_to(REPO) if path.is_relative_to(REPO) else path
        errors = check(path)
        count = len([l for l in path.read_text(encoding="utf-8").splitlines() if l.strip()])
        if errors:
            failed += 1
            print(f"NG {rel} ({count}枚)")
            for e in errors:
                print(f"   {e}")
        else:
            print(f"OK {rel} ({count}枚)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
