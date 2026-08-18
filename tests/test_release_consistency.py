from __future__ import annotations

import json
from pathlib import Path

from tools.release_consistency import validate


def write_fixture(root: Path, version: str = "2026.08.18.6") -> None:
    (root / "docs").mkdir(parents=True)
    (root / "COMPANION_RELEASE.json").write_text(
        json.dumps({"companion_release": version}), encoding="utf-8"
    )
    (root / "CHANGELOG.md").write_text(
        f"# Changelog\n\nRelease `{version}`\n", encoding="utf-8"
    )
    (root / "docs" / "RELEASE_SNAPSHOT.md").write_text(
        f"# Snapshot\n\nCompanion release: **{version}**\n", encoding="utf-8"
    )
    (root / "CITATION.cff").write_text(
        f'cff-version: 1.2.0\nversion: "{version}"\n', encoding="utf-8"
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


def test_validate_reports_citation_version_mismatch(tmp_path: Path) -> None:
    write_fixture(tmp_path)
    (tmp_path / "CITATION.cff").write_text(
        'cff-version: 1.2.0\nversion: "2026.08.18.5"\n', encoding="utf-8"
    )
    errors = validate(tmp_path)
    assert any("CITATION.cff version" in error for error in errors)


def test_validate_reports_missing_citation_file(tmp_path: Path) -> None:
    write_fixture(tmp_path)
    (tmp_path / "CITATION.cff").unlink()
    errors = validate(tmp_path)
    assert any("CITATION.cff" in error for error in errors)
