from pathlib import Path

from tools.learning_index_check import validate


def write_stage(root: Path, stage: int, start: int, end: int) -> None:
    path = root / "resources" / "learning" / f"stage_{stage:02d}_parts_{start:03d}_{end:03d}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# Stage {stage:02d} — Parts {start}–{end}", ""]
    for index, part in enumerate(range(start, end + 1), start=1):
        lines.append(f"{index}. **Part {part} — Example title {part}**")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def make_valid_index(root: Path) -> None:
    for stage in range(1, 21):
        start = (stage - 1) * 10 + 1
        write_stage(root, stage, start, start + 9)


def test_complete_index_passes(tmp_path: Path) -> None:
    make_valid_index(tmp_path)
    assert validate(tmp_path) == []


def test_missing_part_is_reported(tmp_path: Path) -> None:
    make_valid_index(tmp_path)
    path = tmp_path / "resources" / "learning" / "stage_20_parts_191_200.md"
    text = path.read_text(encoding="utf-8").replace(
        "10. **Part 200 — Example title 200**\n", ""
    )
    path.write_text(text, encoding="utf-8")
    issues = validate(tmp_path)
    assert any("expected 10 parts" in issue for issue in issues)
    assert any("missing parts: 200" in issue for issue in issues)


def test_duplicate_part_is_reported(tmp_path: Path) -> None:
    make_valid_index(tmp_path)
    path = tmp_path / "resources" / "learning" / "stage_20_parts_191_200.md"
    text = path.read_text(encoding="utf-8").replace(
        "10. **Part 200 — Example title 200**",
        "10. **Part 199 — Example title 199 duplicate**",
    )
    path.write_text(text, encoding="utf-8")
    issues = validate(tmp_path)
    assert any("duplicate parts: 199" in issue for issue in issues)
    assert any("missing parts: 200" in issue for issue in issues)
