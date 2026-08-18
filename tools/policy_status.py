#!/usr/bin/env python3
"""Generate or validate a deterministic repository policy-status report.

The report executes local repository validators only. It performs no network,
account, device, scanning, authentication, or production-system interaction.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.action_pinning import validate as validate_actions
from tools.data_dictionary import is_current as data_dictionary_is_current
from tools.dev_environment import validate as validate_dev_environment
from tools.docs_toc import is_current as docs_toc_is_current
from tools.gumroad_presence import GUMROAD, validate as validate_gumroad
from tools.learning_index_check import validate as validate_learning_index
from tools.public_repo_policy import validate as validate_public_repo
from tools.release_consistency import validate as validate_release


def release_version(root: Path) -> str:
    data = json.loads((root / "COMPANION_RELEASE.json").read_text(encoding="utf-8"))
    return str(data.get("companion_release", "unknown"))


def collect(root: Path) -> list[tuple[str, bool, list[str]]]:
    checks: list[tuple[str, bool, list[str]]] = []

    def add(name: str, issues: list[str]) -> None:
        checks.append((name, not issues, issues))

    add("Immutable GitHub Actions references", validate_actions(root))
    add("Development environment consistency", validate_dev_environment(root))
    add("Public repository boundary", validate_public_repo(root))
    add("Release and citation version consistency", validate_release(root))
    add("Parts 1–200 learning index integrity", validate_learning_index(root))
    add("Official Gumroad storefront presence", validate_gumroad(root))

    data_dictionary_current = data_dictionary_is_current(
        root / "schemas" / "dataset_contracts.json",
        root / "docs" / "DATA_DICTIONARY.md",
    )
    add(
        "Generated dataset data dictionary freshness",
        [] if data_dictionary_current else ["docs/DATA_DICTIONARY.md is stale"],
    )

    toc_current = docs_toc_is_current(root / "docs", root / "docs" / "TOC.md")
    add(
        "Generated documentation TOC freshness",
        [] if toc_current else ["docs/TOC.md is stale"],
    )

    return checks


def render(root: Path) -> str:
    checks = collect(root)
    lines = [
        "# Repository Policy Status",
        "",
        "[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)",
        "",
        f"**Official Gumroad:** {GUMROAD}",
        "",
        f"**Companion release:** `{release_version(root)}`",
        "",
        "This generated report summarizes deterministic local repository-policy checks used for release review.",
        "",
        "| Policy check | Status |",
        "|---|---|",
    ]

    for name, passed, _ in checks:
        lines.append(f"| {name} | {'PASS' if passed else 'FAIL'} |")

    failures = [(name, issues) for name, passed, issues in checks if not passed]
    lines.extend(["", "## Policy boundary", ""])
    lines.append(
        "The public repository is limited to defensive companion resources. Commercial publication files remain outside GitHub; direct X/Twitter URLs are excluded; and no author avatar/photo/person image is required or used for publication promotion."
    )

    if failures:
        lines.extend(["", "## Current failures", ""])
        for name, issues in failures:
            lines.append(f"### {name}")
            lines.append("")
            for issue in issues:
                lines.append(f"- {issue}")
            lines.append("")

    lines.extend(["", f"**Publication storefront:** {GUMROAD}", ""])
    return "\n".join(lines)


def is_current(root: Path, output: Path) -> bool:
    if not output.is_file():
        return False
    return output.read_text(encoding="utf-8") == render(root)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate or validate repository policy status.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, default=Path("docs/POLICY_STATUS.md"))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output

    if args.check:
        if not is_current(root, output):
            print(f"Repository policy status is stale or failing: {output}")
            raise SystemExit(1)
        print(f"Repository policy status is current: {output}")
        return

    output.write_text(render(root), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
