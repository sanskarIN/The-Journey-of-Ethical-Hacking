from pathlib import Path

from tools.resource_manifest import build_manifest, public_files


def test_manifest_includes_public_files_and_excludes_commercial_formats(tmp_path: Path):
    (tmp_path / "docs").mkdir()
    (tmp_path / "README.md").write_text("# Example\n", encoding="utf-8")
    (tmp_path / "docs" / "guide.md").write_text("# Guide\n", encoding="utf-8")
    (tmp_path / "docs" / "book.pdf").write_bytes(b"not-public")

    paths = [path.relative_to(tmp_path).as_posix() for path in public_files(tmp_path)]

    assert "README.md" in paths
    assert "docs/guide.md" in paths
    assert "docs/book.pdf" not in paths


def test_manifest_reports_count_size_and_sha(tmp_path: Path):
    (tmp_path / "README.md").write_text("# Example\n", encoding="utf-8")

    manifest = build_manifest(tmp_path)

    assert manifest["format_version"] == 1
    assert manifest["resource_count"] == 1
    entry = manifest["resources"][0]
    assert entry["path"] == "README.md"
    assert entry["bytes"] > 0
    assert len(entry["sha256"]) == 64
