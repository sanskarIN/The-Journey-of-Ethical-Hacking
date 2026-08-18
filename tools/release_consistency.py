#!/usr/bin/env python3
"""Validate companion-release version consistency across public release records.

This utility reads local repository files only. It performs no network access
and no security-system interaction.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

VERSION_RE = re.compile(r"\b\d{4}\.\d{2}\.\d{2}\.\d+\b")
CITATION_VERSION_RE = re.compile(r'^version:\s*["\']?([^"\'\n]+)', re.MULTILINE)


def load_release_version(release_path: Path) -> str:
    data = json.loads(release_path.read_text(encoding="utf-8"))
    value = data.get("companion_release")
    if not isinstance(value, str) or not VERSION_RE.fullmatch(value):
        raise ValueError("COMPANION_RELEASE.json has an invalid companion_release value")
    return value


def load_citation_version(citation_path: Path) -> str:
    text = citation_path.read_text(encoding="utf-8")
    match = CITATION_VERSION_RE.search(text)
    if not match:
        raise ValueError("CITATION.cff is missing a top-level version value")
    value = match.group(1).strip()
    if not VERSION_RE.fullmatch(value):
        raise ValueError("CITATION.cff has an invalid version value")
    return value


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    release_path = root / "COMPANION_RELEASE.json"
    changelog_path = root / "CHANGELOG.md"
    snapshot_path = root / "docs" / "RELEASE_SNAPSHOT.md"
    citation_path = root / "CITATION.cff"

    for path in (release_path, changelog_path, snapshot_path, citation_path):
        if not path.is_file():
            errors.append(f"missing release consistency file: {path.relative_to(root)}")
    if errors:
        return errors

    try:
        version = load_release_version(release_path)
    except (json.JSONDecodeError, ValueError) as exc:
        return [str(exc)]

    changelog = changelog_path.read_text(encoding="utf-8")
    snapshot = snapshot_path.read_text(encoding="utf-8")

    if version not in changelog:
        errors.append(f"CHANGELOG.md does not mention current companion release {version}")
    if version not in snapshot:
        errors.append(f"docs/RELEASE_SNAPSHOT.md does not mention current companion release {version}")

    try:
        citation_version = load_citation_version(citation_path)
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if citation_version != version:
            errors.append(
                f"CITATION.cff version {citation_version} does not match companion release {version}"
            )

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Check companion release-version consistency.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    errors = validate(args.root.resolve())
    for error in errors:
        print(error)
    if errors:
        raise SystemExit(1)
    version = load_release_version(args.root.resolve() / "COMPANION_RELEASE.json")
    print(f"Release consistency check: OK ({version})")


if __name__ == "__main__":
    main()
