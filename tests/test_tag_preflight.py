import json
from pathlib import Path

from tools.tag_preflight import expected_tag, validate


def make_release(root: Path, version: str = "2026.08.18.6") -> None:
    (root / "COMPANION_RELEASE.json").write_text(
        json.dumps({"companion_release": version}), encoding="utf-8"
    )


def test_expected_tag_matches_release_metadata(tmp_path: Path) -> None:
    make_release(tmp_path)
    assert expected_tag(tmp_path) == "companion-v2026.08.18.6"


def test_matching_tag_passes(tmp_path: Path) -> None:
    make_release(tmp_path)
    assert validate(tmp_path, "companion-v2026.08.18.6") == []


def test_wrong_release_tag_fails(tmp_path: Path) -> None:
    make_release(tmp_path)
    issues = validate(tmp_path, "companion-v2026.08.18.5")
    assert any("does not match expected release tag" in item for item in issues)


def test_invalid_tag_format_fails(tmp_path: Path) -> None:
    make_release(tmp_path)
    assert validate(tmp_path, "v2026.08.18.6") == [
        "tag must match companion-vYYYY.MM.DD.N"
    ]
