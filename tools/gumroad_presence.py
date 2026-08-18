#!/usr/bin/env python3
"""Verify the official Gumroad storefront is present in public-facing docs.

The check is local-only and enforces the repository's direct storefront URL.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

GUMROAD = "https://ramsandesh.gumroad.com"
LEARNING_STAGE_GLOB = "resources/learning/stage_*_parts_*.md"
EXPECTED_LEARNING_STAGES = 20
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
    "docs/CONTRIBUTOR_ONBOARDING.md",
    "docs/DATA_DICTIONARY.md",
    "docs/DEVELOPMENT.md",
    "docs/DEPENDENCY_ACTION_REVIEW.md",
    "docs/ERRATA_PROCESS.md",
    "docs/GIT_COMMIT_IDENTITY.md",
    "docs/GUMROAD.md",
    "docs/INDEX.md",
    "docs/ISSUE_TRIAGE.md",
    "docs/OFFLINE_ANALYSIS_EXAMPLES.md",
    "docs/POLICY_STATUS.md",
    "docs/PUBLIC_RESOURCE_MANIFEST.md",
    "docs/RELEASE_CHECKLIST.md",
    "docs/RELEASE_NOTES_AUTOMATION.md",
    "docs/RELEASE_SNAPSHOT.md",
    "docs/REPOSITORY_METADATA.md",
    "docs/REPOSITORY_STRUCTURE.md",
    "docs/RESOURCE_STYLE_GUIDE.md",
    "docs/TAGGED_RELEASES.md",
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

    learning_stages = sorted(root.glob(LEARNING_STAGE_GLOB))
    if len(learning_stages) != EXPECTED_LEARNING_STAGES:
        errors.append(
            f"expected {EXPECTED_LEARNING_STAGES} learning-stage pages, found {len(learning_stages)}"
        )
    for path in learning_stages:
        if GUMROAD not in path.read_text(encoding="utf-8"):
            errors.append(f"missing Gumroad URL: {path.relative_to(root)}")

    citation_path = root / "CITATION.cff"
    if not citation_path.is_file():
        errors.append("missing CITATION.cff")
    elif GUMROAD not in citation_path.read_text(encoding="utf-8"):
        errors.append("missing Gumroad URL: CITATION.cff")

    funding_path = root / ".github" / "FUNDING.yml"
    if not funding_path.is_file():
        errors.append("missing .github/FUNDING.yml")
    elif GUMROAD not in funding_path.read_text(encoding="utf-8"):
        errors.append("missing Gumroad URL: .github/FUNDING.yml")

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
            if release.get("gumroad_highlighted_in_all_learning_stages") is not True:
                errors.append(
                    "COMPANION_RELEASE.json must confirm gumroad_highlighted_in_all_learning_stages"
                )
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
    print(
        f"Gumroad presence check: OK ({GUMROAD}; {EXPECTED_LEARNING_STAGES} learning stages)"
    )


if __name__ == "__main__":
    main()
