#!/usr/bin/env python3
"""Run the repository's local structural health checks from one command.

All checks operate on repository files only. No network access, scanning,
authentication, device access, or production-system interaction is performed.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def build_checks(root: Path) -> list[list[str]]:
    py = sys.executable
    datasets = [str(path) for path in sorted((root / "datasets").glob("*.csv"))]
    return [
        [py, "tools/action_pinning.py", "--root", str(root)],
        [py, "tools/dev_environment.py", "--root", str(root)],
        [py, "tools/csv_quality.py", *datasets],
        [py, "tools/dataset_contracts.py", "schemas/dataset_contracts.json", "datasets"],
        [py, "tools/data_dictionary.py", "schemas/dataset_contracts.json", "--output", "docs/DATA_DICTIONARY.md", "--check"],
        [py, "tools/json_metadata.py", "COMPANION_RELEASE.json", "schemas/dataset_contracts.json"],
        [py, "tools/release_consistency.py", "--root", str(root)],
        [py, "tools/learning_index_check.py", "--root", str(root)],
        [py, "tools/docs_toc.py", "--docs-dir", "docs", "--output", "docs/TOC.md", "--check"],
        [py, "tools/synthetic_safety.py", *datasets],
        [py, "tools/doc_accessibility.py", "README.md", "docs", "resources", "schemas", "exercises", "examples"],
        [py, "tools/markdown_links.py", "README.md", "docs", "resources", "schemas", "exercises", "examples", "ERRATA.md", "ROADMAP.md", "CHANGELOG.md", "what_changed.md"],
        [py, "tools/gumroad_presence.py", "--root", str(root)],
    ]


def run_checks(root: Path) -> int:
    for command in build_checks(root):
        printable = " ".join(command)
        print(f"==> {printable}")
        result = subprocess.run(command, cwd=root, check=False)
        if result.returncode:
            print(f"FAILED: {printable}")
            return result.returncode
    print("Repository structural checks: OK")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Run local companion-repository health checks.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root (default: current directory)",
    )
    args = parser.parse_args()
    raise SystemExit(run_checks(args.root.resolve()))


if __name__ == "__main__":
    main()
