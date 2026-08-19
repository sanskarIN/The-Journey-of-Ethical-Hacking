#!/usr/bin/env python3
"""Generate or validate a deterministic companion release-readiness report.

All checks operate on local repository files only. The tool performs no
network access, Git ref mutation, account action, or production-system access.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.gumroad_presence import GUMROAD
from tools.manifest_verify import validate_manifest
from tools.policy_status import collect as collect_policy, is_current as policy_status_is_current
from tools.resource_manifest import build_manifest
from tools.tag_preflight import expected_tag, validate as validate_tag


def release_version(root: Path) -> str:
    data = json.loads((root / "COMPANION_RELEASE.json").read_text(encoding="utf-8"))
    return str(data.get("companion_release", "unknown"))


def workflow_issues(root: Path) -> list[str]:
    path = root / ".github" / "workflows" / "release-manifest.yml"
    if not path.is_file():
        return ["missing .github/workflows/release-manifest.yml"]
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    required_fragments = {
        '"companion-v*"': "tag trigger companion-v*",
        "requirements-dev.txt": "pinned development dependency install",
        "python -m compileall": "Python compilation step",
        "python -m pytest": "main test suite step",
        "companion-projects/run_tests.py": "project-owned companion tests",
        "tools/companion_projects_check.py": "companion structure validation",
        "tools/tag_preflight.py": "tag preflight step",
        "tools/resource_manifest.py": "manifest generation step",
        "tools/manifest_verify.py": "manifest verification step",
    }
    for fragment, label in required_fragments.items():
        if fragment not in text:
            issues.append(f"release workflow missing {label}")
    return issues


def candidate_workflow_issues(root: Path) -> list[str]:
    path = root / ".github" / "workflows" / "release-candidate.yml"
    if not path.is_file():
        return ["missing .github/workflows/release-candidate.yml"]
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    required_fragments = {
        "workflow_dispatch": "manual dispatch trigger",
        "requirements-dev.txt": "pinned development dependency install",
        "python -m compileall": "Python compilation step",
        "python -m pytest": "main test suite step",
        "companion-projects/run_tests.py": "project-owned companion tests",
        "tools/companion_projects_check.py": "companion structure validation",
        "tools/release_readiness.py": "release readiness step",
        "tools/resource_manifest.py": "manifest generation step",
        "tools/manifest_verify.py": "manifest verification step",
        "actions/upload-artifact@": "candidate evidence upload step",
    }
    for fragment, label in required_fragments.items():
        if fragment not in text:
            issues.append(f"release candidate workflow missing {label}")
    return issues


def collect(root: Path) -> list[tuple[str, bool, list[str]]]:
    checks: list[tuple[str, bool, list[str]]] = []

    policy_failures: list[str] = []
    for name, passed, issues in collect_policy(root):
        if not passed:
            if issues:
                policy_failures.extend(f"{name}: {issue}" for issue in issues)
            else:
                policy_failures.append(f"{name}: failed")
    checks.append(("Repository policy checks", not policy_failures, policy_failures))

    policy_path = root / "docs" / "POLICY_STATUS.md"
    policy_current = policy_status_is_current(root, policy_path)
    checks.append(
        (
            "Generated policy status freshness",
            policy_current,
            [] if policy_current else ["docs/POLICY_STATUS.md is stale or failing"],
        )
    )

    tag = expected_tag(root)
    tag_errors = validate_tag(root, tag)
    checks.append(("Expected companion tag naming", not tag_errors, tag_errors))

    manifest = build_manifest(root)
    manifest_errors = validate_manifest(root, manifest)
    checks.append(("Public resource manifest integrity", not manifest_errors, manifest_errors))

    workflow_errors = workflow_issues(root)
    checks.append(("Tagged release workflow configuration", not workflow_errors, workflow_errors))

    candidate_errors = candidate_workflow_issues(root)
    checks.append(("Release candidate workflow configuration", not candidate_errors, candidate_errors))

    return checks


def render(root: Path) -> str:
    checks = collect(root)
    version = release_version(root)
    tag = expected_tag(root)
    release_branch = f"release/{tag}"
    lines = [
        "# Companion Release Readiness",
        "",
        "[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)",
        "",
        f"**Official Gumroad:** {GUMROAD}",
        "",
        f"**Companion release:** `{version}`",
        f"**Expected tag:** `{tag}`",
        "",
        "This generated report records deterministic local pre-tag checks. It does not create a Git branch, Git tag, or GitHub Release.",
        "",
        "| Release gate | Status |",
        "|---|---|",
    ]
    for name, passed, _ in checks:
        lines.append(f"| {name} | {'PASS' if passed else 'FAIL'} |")

    failures = [(name, issues) for name, passed, issues in checks if not passed]
    overall = "READY" if not failures else "NOT READY"
    lines.extend(["", f"## Result: {overall}", ""])

    if failures:
        for name, issues in failures:
            lines.append(f"### {name}")
            lines.append("")
            for issue in issues:
                lines.append(f"- {issue}")
            lines.append("")
    else:
        lines.append(
            f"The repository-local automated release gate is clean for `{tag}`. Freeze the reviewed snapshot on `{release_branch}` before creating the tag and reviewing the generated manifest artifact."
        )
        lines.append("")

    lines.extend(
        [
            "## Manual GitHub operations",
            "",
            f"1. Freeze the reviewed candidate on branch `{release_branch}`.",
            f"2. Create the lightweight or annotated tag `{tag}` from the reviewed release-branch commit.",
            "3. Confirm the tagged-release workflow completes successfully.",
            "4. Download and review the generated `PUBLIC_RESOURCE_MANIFEST.json` artifact.",
            "5. Apply the documented repository About description, Gumroad website, and topics if those settings have not yet been configured manually.",
            "",
            "This generated report does not mutate Git refs or repository settings, so those remain explicit release operations.",
            "",
            "## Publication boundary",
            "",
            "The public repository remains limited to defensive companion resources. Commercial publication files stay outside GitHub; direct X/Twitter URLs remain excluded; and no author avatar/photo/person image is used for promotion.",
            "",
            f"**Publication storefront:** {GUMROAD}",
            "",
        ]
    )
    return "\n".join(lines)


def is_current(root: Path, output: Path) -> bool:
    return output.is_file() and output.read_text(encoding="utf-8") == render(root)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate or validate release readiness.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, default=Path("docs/RELEASE_READINESS.md"))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output

    if args.check:
        if not is_current(root, output):
            print(f"Release readiness report is stale or failing: {output}")
            raise SystemExit(1)
        print(f"Release readiness report is current: {output}")
        return

    output.write_text(render(root), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
