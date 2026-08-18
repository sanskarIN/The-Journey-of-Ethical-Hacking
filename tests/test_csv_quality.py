from pathlib import Path

from tools.csv_quality import inspect_csv


def test_valid_csv_has_no_issues(tmp_path: Path) -> None:
    csv_path = tmp_path / "valid.csv"
    csv_path.write_text("id,status\nA-1,Current\nA-2,Review-Due\n", encoding="utf-8")
    assert inspect_csv(csv_path) == []


def test_duplicate_identifier_is_reported(tmp_path: Path) -> None:
    csv_path = tmp_path / "duplicate.csv"
    csv_path.write_text("id,status\nA-1,Current\nA-1,Review-Due\n", encoding="utf-8")
    issues = inspect_csv(csv_path)
    assert any("duplicate primary identifier" in issue for issue in issues)


def test_inconsistent_width_is_reported(tmp_path: Path) -> None:
    csv_path = tmp_path / "width.csv"
    csv_path.write_text("id,status\nA-1,Current,Extra\n", encoding="utf-8")
    issues = inspect_csv(csv_path)
    assert any("expected 2 columns" in issue for issue in issues)
