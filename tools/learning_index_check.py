#!/usr/bin/env python3
"""Validate the public Parts 1–200 learning-stage index.

The checker reads local Markdown files only. It verifies that the 20 stage
files cover every Part 1 through 200 exactly once, with ten parts per stage.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

PART_RE = re.compile(r"^\d+\. \*\*Part (\d+) — ", re.MULTILINE)
STAGE_RE = re.compile(r"^# Stage (\d{2}) — Parts (\d+)–(\d+)$", re.MULTILINE)


def stage_files(root: Path) -> list[Path]:
    return sorted((root / "resources" / "learning").glob("stage_*_parts_*.md"))


def validate(root: Path) -> list[str]:
    issues: list[str] = []
    files = stage_files(root)
    if len(files) != 20:
        issues.append(f"expected 20 learning-stage files, found {len(files)}")

    all_parts: list[int] = []
    for expected_stage, path in enumerate(files, start=1):
        text = path.read_text(encoding="utf-8")
        heading = STAGE_RE.search(text)
        if not heading:
            issues.append(f"{path.name}: missing or malformed stage heading")
            continue

        stage_no, start, end = map(int, heading.groups())
        if stage_no != expected_stage:
            issues.append(
                f"{path.name}: expected stage {expected_stage:02d}, found {stage_no:02d}"
            )

        parts = [int(value) for value in PART_RE.findall(text)]
        expected_parts = list(range(start, end + 1))
        if len(parts) != 10:
            issues.append(f"{path.name}: expected 10 parts, found {len(parts)}")
        if parts != expected_parts:
            issues.append(
                f"{path.name}: part sequence {parts} does not match heading range {start}-{end}"
            )
        all_parts.extend(parts)

    expected_all = list(range(1, 201))
    if sorted(all_parts) != expected_all:
        missing = sorted(set(expected_all) - set(all_parts))
        duplicates = sorted({part for part in all_parts if all_parts.count(part) > 1})
        if missing:
            issues.append("missing parts: " + ", ".join(map(str, missing)))
        if duplicates:
            issues.append("duplicate parts: " + ", ".join(map(str, duplicates)))
        unexpected = sorted(set(all_parts) - set(expected_all))
        if unexpected:
            issues.append("unexpected parts: " + ", ".join(map(str, unexpected)))

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Parts 1–200 learning-stage coverage.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    issues = validate(args.root.resolve())
    for issue in issues:
        print(issue)
    if issues:
        raise SystemExit(1)
    print("Learning index integrity check: OK (Parts 1–200 exactly once)")


if __name__ == "__main__":
    main()
