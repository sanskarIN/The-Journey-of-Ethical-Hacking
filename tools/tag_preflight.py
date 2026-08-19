#!/usr/bin/env python3
"""Validate the expected companion-release tag name from local release metadata.

This utility reads local repository files only. It performs no network access,
account operations, or Git ref mutations.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

VERSION_RE = re.compile(r"\d{4}\.\d{2}\.\d{2}\.\d+")
TAG_RE = re.compile(r"companion-v(\d{4}\.\d{2}\.\d{2}\.\d+)")


def release_version(root: Path) -> str:
    data = json.loads((root / "COMPANION_RELEASE.json").read_text(encoding="utf-8"))
    version = data.get("companion_release")
    if not isinstance(version, str) or not VERSION_RE.fullmatch(version):
        raise ValueError("COMPANION_RELEASE.json has an invalid companion_release value")
    return version


def expected_tag(root: Path) -> str:
    return f"companion-v{release_version(root)}"


def validate(root: Path, tag: str) -> list[str]:
    errors: list[str] = []
    match = TAG_RE.fullmatch(tag)
    if not match:
        return ["tag must match companion-vYYYY.MM.DD.N"]

    expected = expected_tag(root)
    if tag != expected:
        errors.append(f"tag {tag} does not match expected release tag {expected}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate companion release tag naming.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--tag", help="Tag to validate; omit to print the expected tag")
    args = parser.parse_args()

    root = args.root.resolve()
    if not args.tag:
        print(expected_tag(root))
        return

    errors = validate(root, args.tag)
    for error in errors:
        print(error)
    if errors:
        raise SystemExit(1)
    print(f"Tag preflight: OK ({args.tag})")


if __name__ == "__main__":
    main()
