import json
from pathlib import Path

import tools.policy_status as policy_status


def configure_passing_checks(monkeypatch) -> None:
    monkeypatch.setattr(policy_status, "validate_actions", lambda root: [])
    monkeypatch.setattr(policy_status, "validate_dev_environment", lambda root: [])
    monkeypatch.setattr(policy_status, "validate_public_repo", lambda root: [])
    monkeypatch.setattr(policy_status, "validate_release", lambda root: [])
    monkeypatch.setattr(policy_status, "validate_learning_index", lambda root: [])
    monkeypatch.setattr(policy_status, "validate_gumroad", lambda root: [])
    monkeypatch.setattr(policy_status, "data_dictionary_is_current", lambda contracts, output: True)
    monkeypatch.setattr(policy_status, "docs_toc_is_current", lambda docs, output: True)


def test_render_reports_passing_policies(tmp_path: Path, monkeypatch) -> None:
    configure_passing_checks(monkeypatch)
    (tmp_path / "COMPANION_RELEASE.json").write_text(
        json.dumps({"companion_release": "2026.08.18.6"}),
        encoding="utf-8",
    )
    text = policy_status.render(tmp_path)
    assert "# Repository Policy Status" in text
    assert "`2026.08.18.6`" in text
    assert "| Immutable GitHub Actions references | PASS |" in text
    assert "https://ramsandesh.gumroad.com" in text


def test_render_includes_failure_details(tmp_path: Path, monkeypatch) -> None:
    configure_passing_checks(monkeypatch)
    monkeypatch.setattr(
        policy_status,
        "validate_actions",
        lambda root: ["workflow uses a movable tag"],
    )
    (tmp_path / "COMPANION_RELEASE.json").write_text(
        json.dumps({"companion_release": "2026.08.18.6"}),
        encoding="utf-8",
    )
    text = policy_status.render(tmp_path)
    assert "| Immutable GitHub Actions references | FAIL |" in text
    assert "workflow uses a movable tag" in text


def test_is_current_detects_stale_report(tmp_path: Path, monkeypatch) -> None:
    configure_passing_checks(monkeypatch)
    (tmp_path / "COMPANION_RELEASE.json").write_text(
        json.dumps({"companion_release": "2026.08.18.6"}),
        encoding="utf-8",
    )
    output = tmp_path / "POLICY_STATUS.md"
    output.write_text("# stale\n", encoding="utf-8")
    assert policy_status.is_current(tmp_path, output) is False
