#!/usr/bin/env python3
"""Validate the repository's repeatable local/CI development environment.

The checker reads local configuration files only. It verifies that workflow
Python versions match `.python-version` and that development requirements use
exact `==` pins for deterministic contributor/test environments.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

PYTHON_VERSION_RE = re.compile(r"^\s*python-version:\s*[\"']?([^\"'\s]+)", re.MULTILINE)


def read_baseline(root: Path) -> str:
    return (root / ".python-version").read_text(encoding="utf-8").strip()


def workflow_python_versions(root: Path) -> list[tuple[Path, str]]:
    results: list[tuple[Path, str]] = []
    workflow_dir = root / ".github" / "workflows"
    for path in sorted([*workflow_dir.glob("*.yml"), *workflow_dir.glob("*.yaml")]):
        text = path.read_text(encoding="utf-8")
        for value in PYTHON_VERSION_RE.findall(text):
            results.append((path, value))
    return results


def requirement_lines(root: Path) -> list[str]:
    path = root / "requirements-dev.txt"
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def validate(root: Path) -> list[str]:
    issues: list[str] = []
    version_file = root / ".python-version"
    requirements_file = root / "requirements-dev.txt"

    if not version_file.is_file():
        issues.append("missing .python-version")
    if not requirements_file.is_file():
        issues.append("missing requirements-dev.txt")
    if issues:
        return issues

    baseline = read_baseline(root)
    if not re.fullmatch(r"\d+\.\d+", baseline):
        issues.append(f"invalid .python-version baseline: {baseline}")

    workflow_versions = workflow_python_versions(root)
    if not workflow_versions:
        issues.append("no workflow python-version values found")
    for path, value in workflow_versions:
        if value != baseline:
            issues.append(
                f"{path.relative_to(root)}: python-version {value} does not match .python-version {baseline}"
            )

    requirements = requirement_lines(root)
    if not requirements:
        issues.append("requirements-dev.txt has no dependencies")
    for requirement in requirements:
        if "==" not in requirement:
            issues.append(f"development dependency is not exactly pinned: {requirement}")
        else:
            name, version = requirement.split("==", 1)
            if not name.strip() or not version.strip():
                issues.append(f"invalid pinned development dependency: {requirement}")

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate local/CI development-environment consistency.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    issues = validate(args.root.resolve())
    for issue in issues:
        print(issue)
    if issues:
        raise SystemExit(1)
    print("Development environment consistency check: OK")


if __name__ == "__main__":
    main()
