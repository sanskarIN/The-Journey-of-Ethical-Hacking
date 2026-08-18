#!/usr/bin/env python3
"""Check relative Markdown links without making network requests."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def relative_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split("#", 1)[0].strip()
    if not target or target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return (source.parent / unquote(target)).resolve()


def check_file(path: Path, repo_root: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8")
    for line_no, line in enumerate(text.splitlines(), 1):
        for match in LINK_RE.finditer(line):
            target = relative_target(path, match.group(1))
            if target is None:
                continue
            try:
                target.relative_to(repo_root.resolve())
            except ValueError:
                issues.append(f"line {line_no}: relative link escapes repository: {match.group(1)}")
                continue
            if not target.exists():
                issues.append(f"line {line_no}: missing relative target: {match.group(1)}")
    return issues


def markdown_files(paths: list[Path]) -> list[Path]:
    files: set[Path] = set()
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".md":
            files.add(path)
        elif path.is_dir():
            files.update(p for p in path.rglob("*.md") if ".git" not in p.parts)
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check relative links in local Markdown files.")
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    failures = 0
    for path in markdown_files(args.paths):
        issues = check_file(path.resolve(), args.root.resolve())
        if issues:
            failures += len(issues)
            print(path)
            for issue in issues:
                print(f"  - {issue}")

    if failures:
        print(f"Markdown link check failed with {failures} issue(s).")
        return 1

    print("Markdown relative-link check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
