from pathlib import Path

from tools.manifest_verify import validate_manifest
from tools.resource_manifest import build_manifest


def make_tree(root: Path) -> None:
    (root / "README.md").write_text("# Example\n", encoding="utf-8")
    (root / "docs").mkdir()
    (root / "docs" / "GUIDE.md").write_text("# Guide\n", encoding="utf-8")


def test_generated_manifest_verifies(tmp_path: Path) -> None:
    make_tree(tmp_path)
    manifest = build_manifest(tmp_path)
    assert validate_manifest(tmp_path, manifest) == []


def test_tampered_hash_is_reported(tmp_path: Path) -> None:
    make_tree(tmp_path)
    manifest = build_manifest(tmp_path)
    manifest["resources"][0]["sha256"] = "0" * 64
    issues = validate_manifest(tmp_path, manifest)
    assert any("SHA-256 mismatch" in item for item in issues)


def test_missing_manifest_entry_is_reported(tmp_path: Path) -> None:
    make_tree(tmp_path)
    manifest = build_manifest(tmp_path)
    manifest["resources"].pop()
    manifest["resource_count"] = len(manifest["resources"])
    issues = validate_manifest(tmp_path, manifest)
    assert any("public file missing from manifest" in item for item in issues)


def test_duplicate_manifest_path_is_reported(tmp_path: Path) -> None:
    make_tree(tmp_path)
    manifest = build_manifest(tmp_path)
    manifest["resources"].append(dict(manifest["resources"][0]))
    manifest["resource_count"] = len(manifest["resources"])
    issues = validate_manifest(tmp_path, manifest)
    assert any("duplicate manifest path" in item for item in issues)
