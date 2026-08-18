from pathlib import Path

from tools.action_pinning import validate, validate_reference


FULL_SHA = "3d3c42e5aac5ba805825da76410c181273ba90b1"


def test_full_sha_reference_passes() -> None:
    assert validate_reference(f"actions/checkout@{FULL_SHA}") is None


def test_tag_reference_is_rejected() -> None:
    issue = validate_reference("actions/checkout@v7")
    assert issue is not None
    assert "full commit SHA" in issue


def test_local_action_is_allowed() -> None:
    assert validate_reference("./.github/actions/example") is None


def test_repository_workflows_are_scanned(tmp_path: Path) -> None:
    workflows = tmp_path / ".github" / "workflows"
    workflows.mkdir(parents=True)
    (workflows / "ci.yml").write_text(
        "steps:\n  - uses: actions/checkout@v7\n",
        encoding="utf-8",
    )
    issues = validate(tmp_path)
    assert any("actions/checkout@v7" in item for item in issues)


def test_repository_workflows_accept_full_sha(tmp_path: Path) -> None:
    workflows = tmp_path / ".github" / "workflows"
    workflows.mkdir(parents=True)
    (workflows / "ci.yml").write_text(
        f"steps:\n  - uses: actions/checkout@{FULL_SHA} # v7.0.1\n",
        encoding="utf-8",
    )
    assert validate(tmp_path) == []
