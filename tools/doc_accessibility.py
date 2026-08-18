#!/usr/bin/env python3
"""Conservative accessibility checks for public Markdown documentation.

The checker is intentionally dependency-free and only inspects local files.
It performs no network requests and does not modify repository content.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

GENERIC_LINK_TEXT = {"click here", "here", "link", "more", "read more"}
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\([^)]*\)")


def check_text(path: Path, text: str) -> list[str]:
    issues: list[str] = []
    lines = text.splitlines()

    if not any(line.startswith("# ") for line in lines):
        issues.append("missing level-1 heading")

    for line_no, line in enumerate(lines, 1):
        for match in IMAGE_RE.finditer(line):
            if not match.group(1).strip():
                issues.append(f"line {line_no}: image has empty alt text")
        for match in LINK_RE.finditer(line):
            label = match.group(1).strip().lower()
            if label in GENERIC_LINK_TEXT:
                issues.append(f"line {line_no}: generic link text '{match.group(1)}'")
        if "\t" in line:
            issues.append(f"line {line_no}: tab character may reduce Markdown portability")

    return issues


def markdown_files(paths: list[Path]) -> list[Path]:
    found: set[Path] = set()
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".md":
            found.add(path)
        elif path.is_dir():
            found.update(p for p in path.rglob("*.md") if ".git" not in p.parts)
    return sorted(found)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check local Markdown accessibility basics.")
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    failures = 0
    for path in markdown_files(args.paths):
        issues = check_text(path, path.read_text(encoding="utf-8"))
        if issues:
            failures += len(issues)
            print(path)
            for issue in issues:
                print(f"  - {issue}")

    if failures:
        print(f"Accessibility check failed with {failures} issue(s).")
        return 1

    print("Accessibility check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
