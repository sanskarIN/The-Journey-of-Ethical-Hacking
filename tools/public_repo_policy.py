#!/usr/bin/env python3
"""Validate public companion-repository governance and publication boundaries.

The checker operates only on local repository files. It requires core
community/governance files, rejects commercial publication file formats, and
rejects direct X/Twitter URLs from text files.
"""

from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED_FILES = (
    "README.md",
    "LICENSE",
    "BOOK_CONTENT_LICENSE.md",
    "NOTICE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "SUPPORT.md",
    "CITATION.cff",
    "COMPANION_RELEASE.json",
    ".github/CODEOWNERS",
    ".github/FUNDING.yml",
    ".github/dependabot.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
)

FORBIDDEN_PUBLICATION_SUFFIXES = {
    ".pdf",
    ".epub",
    ".docx",
    ".mobi",
    ".azw",
    ".azw3",
    ".zip",
}

TEXT_SUFFIXES = {
    "",
    ".md",
    ".txt",
    ".py",
    ".json",
    ".yml",
    ".yaml",
    ".cff",
    ".csv",
}

# Build the disallowed URL markers in memory so this policy source file does
# not itself contain a direct publication-facing X/Twitter URL literal.
_X_HOST = "x" + ".com/"
_TWITTER_HOST = "twitter" + ".com/"
_WWW_TWITTER_HOST = "www." + _TWITTER_HOST
FORBIDDEN_SOCIAL_URL_MARKERS = tuple(
    scheme + host
    for scheme in ("https://", "http://")
    for host in (_X_HOST, _TWITTER_HOST, _WWW_TWITTER_HOST)
)


def iter_public_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if ".git" in relative.parts or ".venv" in relative.parts or "__pycache__" in relative.parts:
            continue
        files.append(path)
    return sorted(files)


def validate(root: Path) -> list[str]:
    issues: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            issues.append(f"missing required repository file: {relative}")

    for path in iter_public_files(root):
        relative = path.relative_to(root)
        suffix = path.suffix.lower()
        if suffix in FORBIDDEN_PUBLICATION_SUFFIXES:
            issues.append(f"commercial/publication file type is not allowed publicly: {relative}")
            continue

        if suffix not in TEXT_SUFFIXES:
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        lower = text.lower()
        for marker in FORBIDDEN_SOCIAL_URL_MARKERS:
            if marker in lower:
                issues.append(f"X/Twitter URL is not allowed in public repository text: {relative}")
                break

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate public companion-repository boundaries.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    issues = validate(args.root.resolve())
    for issue in issues:
        print(issue)
    if issues:
        raise SystemExit(1)
    print("Public repository policy check: OK")


if __name__ == "__main__":
    main()
