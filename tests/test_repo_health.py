from pathlib import Path

from tools.repo_health import build_checks


def test_build_checks_contains_expected_validators(tmp_path: Path):
    datasets = tmp_path / "datasets"
    datasets.mkdir()
    (datasets / "sample.csv").write_text("id,status\nA-1,Ready\n", encoding="utf-8")

    commands = build_checks(tmp_path)
    text = "\n".join(" ".join(command) for command in commands)

    assert "tools/csv_quality.py" in text
    assert "tools/dataset_contracts.py" in text
    assert "tools/json_metadata.py" in text
    assert "tools/doc_accessibility.py" in text
    assert "tools/markdown_links.py" in text
    assert "sample.csv" in text


def test_build_checks_uses_current_python(tmp_path: Path):
    (tmp_path / "datasets").mkdir()
    commands = build_checks(tmp_path)
    assert commands
    assert all(command[0] for command in commands)
