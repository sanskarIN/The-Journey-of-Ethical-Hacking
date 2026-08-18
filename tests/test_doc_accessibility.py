from pathlib import Path

from tools.doc_accessibility import check_text


def test_accessible_markdown_passes() -> None:
    text = "# Guide\n\n[Authorization checklist](authorization.md)\n\n![Architecture diagram](diagram.png)\n"
    assert check_text(Path("guide.md"), text) == []


def test_missing_h1_is_reported() -> None:
    issues = check_text(Path("guide.md"), "## Secondary heading\n")
    assert "missing level-1 heading" in issues


def test_empty_image_alt_is_reported() -> None:
    issues = check_text(Path("guide.md"), "# Guide\n\n![](diagram.png)\n")
    assert any("empty alt text" in issue for issue in issues)


def test_generic_link_text_is_reported() -> None:
    issues = check_text(Path("guide.md"), "# Guide\n\n[click here](guide.md)\n")
    assert any("generic link text" in issue for issue in issues)


def test_tab_is_reported() -> None:
    issues = check_text(Path("guide.md"), "# Guide\n\nItem\tvalue\n")
    assert any("tab character" in issue for issue in issues)
