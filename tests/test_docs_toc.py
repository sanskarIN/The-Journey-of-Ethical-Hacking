from pathlib import Path

from tools.docs_toc import collect_docs, first_heading, render


def test_first_heading_reads_level_one_title(tmp_path: Path) -> None:
    path = tmp_path / "guide.md"
    path.write_text("# Guide Title\n\nBody\n", encoding="utf-8")
    assert first_heading(path) == "Guide Title"


def test_collect_docs_skips_generated_toc(tmp_path: Path) -> None:
    (tmp_path / "A.md").write_text("# Alpha\n", encoding="utf-8")
    (tmp_path / "B.md").write_text("# Beta\n", encoding="utf-8")
    (tmp_path / "TOC.md").write_text("# Existing TOC\n", encoding="utf-8")
    entries = collect_docs(tmp_path)
    assert entries == [("A.md", "Alpha"), ("B.md", "Beta")]


def test_render_includes_gumroad_and_links() -> None:
    text = render([("A.md", "Alpha")])
    assert "https://ramsandesh.gumroad.com" in text
    assert "[Alpha](A.md)" in text
