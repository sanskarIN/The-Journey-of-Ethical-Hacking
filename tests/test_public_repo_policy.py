from pathlib import Path

from tools.public_repo_policy import REQUIRED_FILES, validate


def make_required_files(root: Path) -> None:
    for relative in REQUIRED_FILES:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("safe placeholder\n", encoding="utf-8")


def test_valid_public_tree_passes(tmp_path: Path) -> None:
    make_required_files(tmp_path)
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "guide.md").write_text(
        "# Guide\n\nhttps://ramsandesh.gumroad.com\n",
        encoding="utf-8",
    )
    assert validate(tmp_path) == []


def test_missing_required_file_is_reported(tmp_path: Path) -> None:
    make_required_files(tmp_path)
    (tmp_path / "SECURITY.md").unlink()
    assert any("SECURITY.md" in item for item in validate(tmp_path))


def test_commercial_publication_format_is_rejected(tmp_path: Path) -> None:
    make_required_files(tmp_path)
    (tmp_path / "book.pdf").write_bytes(b"not-a-real-pdf")
    assert any("book.pdf" in item for item in validate(tmp_path))


def test_x_url_is_rejected(tmp_path: Path) -> None:
    make_required_files(tmp_path)
    (tmp_path / "README.md").write_text(
        "https://x.com/example\n",
        encoding="utf-8",
    )
    assert any("X/Twitter URL" in item for item in validate(tmp_path))


def test_plain_x_twitter_words_without_url_are_allowed(tmp_path: Path) -> None:
    make_required_files(tmp_path)
    (tmp_path / "README.md").write_text(
        "X/Twitter links are intentionally omitted.\n",
        encoding="utf-8",
    )
    assert validate(tmp_path) == []
