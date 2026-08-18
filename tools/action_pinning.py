#!/usr/bin/env python3
"""Validate immutable external GitHub Actions references in local workflows.

The validator reads repository workflow YAML as text. External `uses:` entries
must be pinned to a full 40-character hexadecimal commit SHA. Local actions
(`./...`) and Docker references are not treated as external GitHub actions.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

USES_RE = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)", re.MULTILINE)
PINNED_RE = re.compile(r"^[^@\s]+@[0-9a-fA-F]{40}$")


def workflow_files(root: Path) -> list[Path]:
    workflow_dir = root / ".github" / "workflows"
    return sorted([*workflow_dir.glob("*.yml"), *workflow_dir.glob("*.yaml")])


def validate_reference(reference: str) -> str | None:
    if reference.startswith("./") or reference.startswith("docker://"):
        return None
    if "@" not in reference:
        return f"external action reference is missing @ref: {reference}"
    if not PINNED_RE.fullmatch(reference):
        return f"external action is not pinned to a full commit SHA: {reference}"
    return None


def validate(root: Path) -> list[str]:
    issues: list[str] = []
    files = workflow_files(root)
    if not files:
        return ["no GitHub Actions workflow files found"]

    for path in files:
        text = path.read_text(encoding="utf-8")
        for reference in USES_RE.findall(text):
            issue = validate_reference(reference)
            if issue:
                issues.append(f"{path.relative_to(root)}: {issue}")
    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate full-SHA GitHub Actions pinning.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    issues = validate(args.root.resolve())
    for issue in issues:
        print(issue)
    if issues:
        raise SystemExit(1)
    print("GitHub Actions pinning check: OK (external actions use full SHAs)")


if __name__ == "__main__":
    main()
