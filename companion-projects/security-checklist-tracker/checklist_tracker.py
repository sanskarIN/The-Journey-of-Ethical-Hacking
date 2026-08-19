#!/usr/bin/env python3
"""Summarize local Markdown task checklists for defensive workflows."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TASK_RE = re.compile(r"^\s*[-*]\s+\[([ xX])\]\s+(.+?)\s*$")


def summarize(text: str) -> dict[str, object]:
    completed = 0
    pending_items: list[str] = []

    for line in text.splitlines():
        match = TASK_RE.match(line)
        if not match:
            continue
        if match.group(1).lower() == "x":
            completed += 1
        else:
            pending_items.append(match.group(2))

    total = completed + len(pending_items)
    percentage = round((completed / total) * 100, 2) if total else 0.0
    return {
        "total": total,
        "completed": completed,
        "pending": len(pending_items),
        "completion_percent": percentage,
        "pending_items": pending_items,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize a local Markdown security checklist.")
    parser.add_argument("markdown_file", type=Path)
    args = parser.parse_args()

    try:
        result = summarize(args.markdown_file.read_text(encoding="utf-8"))
    except OSError as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result["pending"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
