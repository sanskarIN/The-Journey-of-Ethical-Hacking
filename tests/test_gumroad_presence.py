import json
from pathlib import Path

from tools.gumroad_presence import (
    EXPECTED_LEARNING_STAGES,
    GUMROAD,
    PUBLIC_MARKDOWN,
    validate,
)


def make_valid_tree(root: Path) -> None:
    for relative in PUBLIC_MARKDOWN:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# Example\n\n{GUMROAD}\n", encoding="utf-8")

    learning = root / "resources" / "learning"
    learning.mkdir(parents=True, exist_ok=True)
    for stage in range(1, EXPECTED_LEARNING_STAGES + 1):
        start = (stage - 1) * 10 + 1
        end = stage * 10
        path = learning / f"stage_{stage:02d}_parts_{start:03d}_{end:03d}.md"
        path.write_text(f"# Stage {stage:02d}\n\n{GUMROAD}\n", encoding="utf-8")

    (root / "CITATION.cff").write_text(
        f'cff-version: 1.2.0\nurl: "{GUMROAD}"\n', encoding="utf-8"
    )
    funding = root / ".github" / "FUNDING.yml"
    funding.parent.mkdir(parents=True, exist_ok=True)
    funding.write_text(f'custom:\n  - "{GUMROAD}"\n', encoding="utf-8")

    (root / "COMPANION_RELEASE.json").write_text(
        json.dumps(
            {
                "official_gumroad": GUMROAD,
                "gumroad_highlighted_in_all_learning_stages": True,
            }
        ),
        encoding="utf-8",
    )


def test_gumroad_presence_accepts_complete_tree(tmp_path: Path):
    make_valid_tree(tmp_path)
    assert validate(tmp_path) == []


def test_gumroad_presence_reports_missing_core_link(tmp_path: Path):
    make_valid_tree(tmp_path)
    target = tmp_path / PUBLIC_MARKDOWN[0]
    target.write_text("# Example\n", encoding="utf-8")
    assert any("missing Gumroad URL" in item for item in validate(tmp_path))


def test_gumroad_presence_reports_missing_learning_stage_link(tmp_path: Path):
    make_valid_tree(tmp_path)
    target = tmp_path / "resources" / "learning" / "stage_20_parts_191_200.md"
    target.write_text("# Stage 20\n", encoding="utf-8")
    errors = validate(tmp_path)
    assert any("stage_20_parts_191_200.md" in item for item in errors)


def test_gumroad_presence_reports_missing_citation_link(tmp_path: Path):
    make_valid_tree(tmp_path)
    (tmp_path / "CITATION.cff").write_text("cff-version: 1.2.0\n", encoding="utf-8")
    errors = validate(tmp_path)
    assert any("CITATION.cff" in item for item in errors)


def test_gumroad_presence_reports_missing_funding_link(tmp_path: Path):
    make_valid_tree(tmp_path)
    (tmp_path / ".github" / "FUNDING.yml").write_text("custom: []\n", encoding="utf-8")
    errors = validate(tmp_path)
    assert any("FUNDING.yml" in item for item in errors)


def test_gumroad_presence_requires_release_metadata_value(tmp_path: Path):
    make_valid_tree(tmp_path)
    (tmp_path / "COMPANION_RELEASE.json").write_text(
        json.dumps(
            {
                "official_gumroad": "https://example.invalid",
                "gumroad_highlighted_in_all_learning_stages": True,
            }
        ),
        encoding="utf-8",
    )
    assert any("official_gumroad" in item for item in validate(tmp_path))


def test_gumroad_presence_requires_learning_stage_flag(tmp_path: Path):
    make_valid_tree(tmp_path)
    (tmp_path / "COMPANION_RELEASE.json").write_text(
        json.dumps({"official_gumroad": GUMROAD}), encoding="utf-8"
    )
    assert any("gumroad_highlighted_in_all_learning_stages" in item for item in validate(tmp_path))
