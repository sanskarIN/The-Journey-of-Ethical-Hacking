import json
from pathlib import Path

from tools.gumroad_presence import GUMROAD, PUBLIC_MARKDOWN, validate


def make_valid_tree(root: Path) -> None:
    for relative in PUBLIC_MARKDOWN:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# Example\n\n{GUMROAD}\n", encoding="utf-8")
    (root / "COMPANION_RELEASE.json").write_text(
        json.dumps({"official_gumroad": GUMROAD}), encoding="utf-8"
    )


def test_gumroad_presence_accepts_complete_tree(tmp_path: Path):
    make_valid_tree(tmp_path)
    assert validate(tmp_path) == []


def test_gumroad_presence_reports_missing_link(tmp_path: Path):
    make_valid_tree(tmp_path)
    target = tmp_path / PUBLIC_MARKDOWN[0]
    target.write_text("# Example\n", encoding="utf-8")
    assert any("missing Gumroad URL" in item for item in validate(tmp_path))


def test_gumroad_presence_requires_release_metadata_value(tmp_path: Path):
    make_valid_tree(tmp_path)
    (tmp_path / "COMPANION_RELEASE.json").write_text(
        json.dumps({"official_gumroad": "https://example.invalid"}), encoding="utf-8"
    )
    assert any("official_gumroad" in item for item in validate(tmp_path))
