from pathlib import Path

from tools.dev_environment import validate


def make_valid_tree(root: Path) -> None:
    (root / ".python-version").write_text("3.12\n", encoding="utf-8")
    (root / "requirements-dev.txt").write_text(
        "pytest==9.1.1\npytest-cov==7.1.0\n",
        encoding="utf-8",
    )
    workflows = root / ".github" / "workflows"
    workflows.mkdir(parents=True)
    (workflows / "ci.yml").write_text(
        'steps:\n  - name: Set up Python\n    with:\n      python-version: "3.12"\n',
        encoding="utf-8",
    )


def test_valid_environment_passes(tmp_path: Path) -> None:
    make_valid_tree(tmp_path)
    assert validate(tmp_path) == []


def test_workflow_python_mismatch_is_reported(tmp_path: Path) -> None:
    make_valid_tree(tmp_path)
    path = tmp_path / ".github" / "workflows" / "ci.yml"
    path.write_text(
        'steps:\n  - name: Set up Python\n    with:\n      python-version: "3.13"\n',
        encoding="utf-8",
    )
    issues = validate(tmp_path)
    assert any("does not match .python-version" in issue for issue in issues)


def test_unpinned_requirement_is_reported(tmp_path: Path) -> None:
    make_valid_tree(tmp_path)
    (tmp_path / "requirements-dev.txt").write_text("pytest>=9\n", encoding="utf-8")
    issues = validate(tmp_path)
    assert any("not exactly pinned" in issue for issue in issues)


def test_missing_version_file_is_reported(tmp_path: Path) -> None:
    make_valid_tree(tmp_path)
    (tmp_path / ".python-version").unlink()
    assert "missing .python-version" in validate(tmp_path)
