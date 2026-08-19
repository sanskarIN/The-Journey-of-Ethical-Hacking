#!/usr/bin/env python3
"""Validate the structure of the offline defensive companion-project suite."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

REQUIRED_SUITE_FILES = {
    "README.md",
    "PROJECT_MATRIX.md",
    "PROJECT_STANDARD.md",
    "ARCHITECTURE.md",
    "SAFETY.md",
    "THREAT_MODEL.md",
    "SYNTHETIC_DATA_GUIDE.md",
    "CONTRIBUTING.md",
    "ROADMAP.md",
    "CHANGELOG.md",
    "MAINTENANCE_CHECKLIST.md",
    "run_tests.py",
}


@dataclass(frozen=True)
class ProjectStatus:
    name: str
    implementations: tuple[str, ...]
    tests: tuple[str, ...]


def discover_projects(suite_dir: Path) -> list[Path]:
    if not suite_dir.is_dir():
        raise ValueError(f"companion project directory not found: {suite_dir}")
    return sorted(
        path
        for path in suite_dir.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )


def validate(suite_dir: Path, minimum_projects: int = 16) -> tuple[list[ProjectStatus], list[str]]:
    errors: list[str] = []

    missing_suite_files = sorted(
        name for name in REQUIRED_SUITE_FILES if not (suite_dir / name).is_file()
    )
    for name in missing_suite_files:
        errors.append(f"missing suite file: {name}")

    projects = discover_projects(suite_dir)
    if len(projects) < minimum_projects:
        errors.append(
            f"expected at least {minimum_projects} companion projects, found {len(projects)}"
        )

    statuses: list[ProjectStatus] = []
    for project in projects:
        if not (project / "README.md").is_file():
            errors.append(f"{project.name}: missing README.md")

        implementations = tuple(
            path.name
            for path in sorted(project.glob("*.py"))
            if not path.name.startswith("test_")
        )
        tests = tuple(path.name for path in sorted(project.glob("test_*.py")))

        if not implementations:
            errors.append(f"{project.name}: no Python implementation found")
        if not tests:
            errors.append(f"{project.name}: no unit test file found")

        statuses.append(
            ProjectStatus(
                name=project.name,
                implementations=implementations,
                tests=tests,
            )
        )

    return statuses, errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the defensive companion-project suite structure."
    )
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--minimum-projects", type=int, default=16)
    args = parser.parse_args()

    if args.minimum_projects < 1:
        parser.error("--minimum-projects must be at least 1")

    suite_dir = args.root / "companion-projects"
    try:
        statuses, errors = validate(suite_dir, args.minimum_projects)
    except ValueError as exc:
        parser.error(str(exc))

    for status in statuses:
        print(
            f"PASS {status.name}: "
            f"implementations={len(status.implementations)} tests={len(status.tests)}"
        )

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1

    print(f"Companion project structure valid: {len(statuses)} projects")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
