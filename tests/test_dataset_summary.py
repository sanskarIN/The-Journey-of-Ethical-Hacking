from pathlib import Path

from tools.dataset_summary import format_summary, summarize


def test_dataset_summary_counts_rows_columns_and_blanks(tmp_path: Path):
    path = tmp_path / "sample.csv"
    path.write_text("id,status,owner\nA-1,Ready,Team A\nA-2,,Team B\n", encoding="utf-8")

    result = summarize(path)

    assert result["file"] == "sample.csv"
    assert result["rows"] == 2
    assert result["columns"] == 3
    assert result["blank_cells"] == 1
    assert result["fields"] == ["id", "status", "owner"]


def test_dataset_summary_formats_readable_output(tmp_path: Path):
    path = tmp_path / "sample.csv"
    path.write_text("id,status\nA-1,Ready\n", encoding="utf-8")

    text = format_summary(summarize(path))

    assert "rows=1" in text
    assert "columns=2" in text
    assert "fields: id, status" in text
