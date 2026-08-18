from pathlib import Path

from tools.markdown_links import check_file


def test_existing_relative_link_passes(tmp_path: Path) -> None:
    target = tmp_path / "target.md"
    target.write_text("# Target\n", encoding="utf-8")
    source = tmp_path / "source.md"
    source.write_text("# Source\n\n[Target](target.md)\n", encoding="utf-8")
    assert check_file(source, tmp_path) == []


def test_missing_relative_link_is_reported(tmp_path: Path) -> None:
    source = tmp_path / "source.md"
    source.write_text("# Source\n\n[Missing](missing.md)\n", encoding="utf-8")
    issues = check_file(source, tmp_path)
    assert any("missing relative target" in issue for issue in issues)


def test_external_link_is_ignored(tmp_path: Path) -> None:
    source = tmp_path / "source.md"
    source.write_text("# Source\n\n[GitHub](https://github.com/)\n", encoding="utf-8")
    assert check_file(source, tmp_path) == []


def test_escape_from_repository_is_reported(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    source = repo / "source.md"
    source.write_text("# Source\n\n[Outside](../outside.md)\n", encoding="utf-8")
    issues = check_file(source, repo)
    assert any("escapes repository" in issue for issue in issues)
