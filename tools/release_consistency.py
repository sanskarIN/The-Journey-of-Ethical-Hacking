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
CITATION_DATE_RE = re.compile(r'^date-released:\s*["\']?(\d{4}-\d{2}-\d{2})', re.MULTILINE)


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


def load_citation_date(citation_path: Path) -> str:
    text = citation_path.read_text(encoding="utf-8")
    match = CITATION_DATE_RE.search(text)
    if not match:
        raise ValueError("CITATION.cff is missing a date-released value")
    return match.group(1)


def expected_release_date(version: str) -> str:
    year, month, day, _ = version.split(".", 3)
    return f"{year}-{month}-{day}"


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    release_path = root / "COMPANION_RELEASE.json"
    changelog_path = root / "CHANGELOG.md"
    snapshot_path = root / "docs" / "RELEASE_SNAPSHOT.md"
    candidate_path = root / "docs" / "RELEASE_CANDIDATE.md"
    readiness_path = root / "docs" / "RELEASE_READINESS.md"
    branch_path = root / "docs" / "RELEASE_BRANCH.md"
    citation_path = root / "CITATION.cff"

    required_paths = (
        release_path,
        changelog_path,
        snapshot_path,
        candidate_path,
        readiness_path,
        branch_path,
        citation_path,
    )
    for path in required_paths:
        if not path.is_file():
            errors.append(f"missing release consistency file: {path.relative_to(root)}")
    if errors:
        return errors

    try:
        version = load_release_version(release_path)
    except (json.JSONDecodeError, ValueError) as exc:
        return [str(exc)]

    expected_tag = f"companion-v{version}"
    text_checks = (
        (changelog_path, "CHANGELOG.md", version),
        (snapshot_path, "docs/RELEASE_SNAPSHOT.md", version),
        (candidate_path, "docs/RELEASE_CANDIDATE.md", version),
        (candidate_path, "docs/RELEASE_CANDIDATE.md", expected_tag),
        (readiness_path, "docs/RELEASE_READINESS.md", version),
        (readiness_path, "docs/RELEASE_READINESS.md", expected_tag),
        (branch_path, "docs/RELEASE_BRANCH.md", version),
        (branch_path, "docs/RELEASE_BRANCH.md", expected_tag),
    )
    for path, label, expected in text_checks:
        text = path.read_text(encoding="utf-8")
        if expected not in text:
            errors.append(f"{label} does not mention current release value {expected}")

    try:
        citation_version = load_citation_version(citation_path)
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if citation_version != version:
            errors.append(
                f"CITATION.cff version {citation_version} does not match companion release {version}"
            )

    try:
        citation_date = load_citation_date(citation_path)
    except ValueError as exc:
        errors.append(str(exc))
    else:
        expected_date = expected_release_date(version)
        if citation_date != expected_date:
            errors.append(
                f"CITATION.cff date-released {citation_date} does not match release date {expected_date}"
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
