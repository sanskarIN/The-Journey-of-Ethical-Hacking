#!/usr/bin/env python3
"""Verify the official Gumroad storefront is present in public-facing docs.

The check is local-only and enforces the repository's direct storefront URL.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

GUMROAD = "https://ramsandesh.gumroad.com"
PUBLIC_MARKDOWN = (
    "README.md",
    "SUPPORT.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "ERRATA.md",
    "ROADMAP.md",
    "CHANGELOG.md",
    "docs/ACCESSIBILITY.md",
    "docs/ANNUAL_EDITION_MAINTENANCE.md",
    "docs/DEPENDENCY_ACTION_REVIEW.md",
    "docs/ERRATA_PROCESS.md",
    "docs/GIT_COMMIT_IDENTITY.md",
    "docs/GUMROAD.md",
    "docs/INDEX.md",
    "docs/OFFLINE_ANALYSIS_EXAMPLES.md",
    "docs/RELEASE_CHECKLIST.md",
    "docs/RELEASE_NOTES_AUTOMATION.md",
    "docs/RELEASE_SNAPSHOT.md",
    "docs/REPOSITORY_STRUCTURE.md",
    "docs/RESOURCE_STYLE_GUIDE.md",
    "docs/USAGE.md",
    "resources/README.md",
    "resources/learning_stage_index.md",
    "datasets/README.md",
    "schemas/README.md",
    "tools/README.md",
    "tests/README.md",
    "exercises/README.md",
    "examples/new_dataset_contribution/README.md",
)


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    for relative in PUBLIC_MARKDOWN:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing public file: {relative}")
            continue
        if GUMROAD not in path.read_text(encoding="utf-8"):
            errors.append(f"missing Gumroad URL: {relative}")

    release_path = root / "COMPANION_RELEASE.json"
    if not release_path.is_file():
        errors.append("missing COMPANION_RELEASE.json")
    else:
        try:
            release = json.loads(release_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid COMPANION_RELEASE.json: {exc}")
        else:
            if release.get("official_gumroad") != GUMROAD:
                errors.append("COMPANION_RELEASE.json official_gumroad is missing or incorrect")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Check official Gumroad presence in public repository pages.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    errors = validate(args.root.resolve())
    for error in errors:
        print(error)
    if errors:
        raise SystemExit(1)
    print(f"Gumroad presence check: OK ({GUMROAD})")


if __name__ == "__main__":
    main()
