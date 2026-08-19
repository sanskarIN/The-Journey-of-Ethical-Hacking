from __future__ import annotations

import json
from pathlib import Path

from tools.release_consistency import validate


def release_date(version: str) -> str:
    year, month, day, _ = version.split(".", 3)
    return f"{year}-{month}-{day}"


def write_fixture(root: Path, version: str = "2026.08.18.6") -> None:
    (root / "docs").mkdir(parents=True)
    tag = f"companion-v{version}"
    (root / "COMPANION_RELEASE.json").write_text(
        json.dumps({"companion_release": version}), encoding="utf-8"
    )
    (root / "CHANGELOG.md").write_text(
        f"# Changelog\n\nRelease `{version}`\n", encoding="utf-8"
    )
    for filename, title in (
        ("RELEASE_SNAPSHOT.md", "Snapshot"),
        ("RELEASE_CANDIDATE.md", "Candidate"),
        ("RELEASE_READINESS.md", "Readiness"),
        ("RELEASE_BRANCH.md", "Branch"),
    ):
        (root / "docs" / filename).write_text(
            f"# {title}\n\nCompanion release: **{version}**\nExpected tag: `{tag}`\n",
            encoding="utf-8",
        )
    (root / "CITATION.cff").write_text(
        (
            "cff-version: 1.2.0\n"
            f'version: "{version}"\n'
            f'date-released: "{release_date(version)}"\n'
        ),
        encoding="utf-8",
    )


def test_validate_accepts_matching_release_records(tmp_path: Path) -> None:
    write_fixture(tmp_path)
    assert validate(tmp_path) == []


def test_validate_reports_missing_changelog_version(tmp_path: Path) -> None:
    write_fixture(tmp_path)
    (tmp_path / "CHANGELOG.md").write_text("# Changelog\n", encoding="utf-8")
    errors = validate(tmp_path)
    assert any("CHANGELOG.md" in error for error in errors)


def test_validate_reports_missing_snapshot_version(tmp_path: Path) -> None:
    write_fixture(tmp_path)
    (tmp_path / "docs" / "RELEASE_SNAPSHOT.md").write_text("# Snapshot\n", encoding="utf-8")
    errors = validate(tmp_path)
    assert any("RELEASE_SNAPSHOT.md" in error for error in errors)


def test_validate_reports_candidate_tag_mismatch(tmp_path: Path) -> None:
    write_fixture(tmp_path)
    (tmp_path / "docs" / "RELEASE_CANDIDATE.md").write_text(
        "# Candidate\n\nCompanion release: **2026.08.18.6**\nExpected tag: `companion-v2026.08.18.5`\n",
        encoding="utf-8",
    )
    errors = validate(tmp_path)
    assert any("RELEASE_CANDIDATE.md" in error and "companion-v" in error for error in errors)


def test_validate_reports_readiness_version_mismatch(tmp_path: Path) -> None:
    write_fixture(tmp_path)
    (tmp_path / "docs" / "RELEASE_READINESS.md").write_text(
        "# Readiness\n\nCompanion release: **2026.08.18.5**\nExpected tag: `companion-v2026.08.18.5`\n",
        encoding="utf-8",
    )
    errors = validate(tmp_path)
    assert any("RELEASE_READINESS.md" in error for error in errors)


def test_validate_reports_branch_version_mismatch(tmp_path: Path) -> None:
    write_fixture(tmp_path)
    (tmp_path / "docs" / "RELEASE_BRANCH.md").write_text(
        "# Branch\n\nRelease 2026.08.18.5 tag companion-v2026.08.18.5\n",
        encoding="utf-8",
    )
    errors = validate(tmp_path)
    assert any("RELEASE_BRANCH.md" in error for error in errors)


def test_validate_reports_citation_version_mismatch(tmp_path: Path) -> None:
    write_fixture(tmp_path)
    (tmp_path / "CITATION.cff").write_text(
        (
            'cff-version: 1.2.0\nversion: "2026.08.18.5"\n'
            'date-released: "2026-08-18"\n'
        ),
        encoding="utf-8",
    )
    errors = validate(tmp_path)
    assert any("CITATION.cff version" in error for error in errors)


def test_validate_reports_citation_date_mismatch(tmp_path: Path) -> None:
    write_fixture(tmp_path)
    (tmp_path / "CITATION.cff").write_text(
        (
            'cff-version: 1.2.0\nversion: "2026.08.18.6"\n'
            'date-released: "2026-08-17"\n'
        ),
        encoding="utf-8",
    )
    errors = validate(tmp_path)
    assert any("date-released" in error for error in errors)


def test_validate_reports_missing_citation_file(tmp_path: Path) -> None:
    write_fixture(tmp_path)
    (tmp_path / "CITATION.cff").unlink()
    errors = validate(tmp_path)
    assert any("CITATION.cff" in error for error in errors)
