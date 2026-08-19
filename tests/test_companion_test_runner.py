import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = ROOT / "companion-projects" / "run_tests.py"
SPEC = importlib.util.spec_from_file_location("companion_test_runner", RUNNER_PATH)
runner = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(runner)


def make_test(suite: Path, project: str, name: str, source: str) -> Path:
    project_dir = suite / project
    project_dir.mkdir(parents=True, exist_ok=True)
    path = project_dir / name
    path.write_text(source, encoding="utf-8")
    return path


def test_run_test_files_accepts_success(tmp_path: Path, monkeypatch) -> None:
    suite = tmp_path / "companion-projects"
    test_file = make_test(suite, "sample", "test_ok.py", "raise SystemExit(0)\n")
    monkeypatch.setattr(runner, "ROOT", suite)

    assert runner.run_test_files([test_file], timeout_seconds=1) == []


def test_run_test_files_reports_nonzero_exit(tmp_path: Path, monkeypatch) -> None:
    suite = tmp_path / "companion-projects"
    test_file = make_test(suite, "sample", "test_fail.py", "raise SystemExit(3)\n")
    monkeypatch.setattr(runner, "ROOT", suite)

    assert runner.run_test_files([test_file], timeout_seconds=1) == [
        "sample/test_fail.py"
    ]


def test_run_test_files_reports_timeout(tmp_path: Path, monkeypatch) -> None:
    suite = tmp_path / "companion-projects"
    test_file = make_test(
        suite,
        "sample",
        "test_slow.py",
        "import time\ntime.sleep(2)\n",
    )
    monkeypatch.setattr(runner, "ROOT", suite)

    assert runner.run_test_files([test_file], timeout_seconds=0.05) == [
        "sample/test_slow.py"
    ]


def test_fail_fast_does_not_run_later_test(tmp_path: Path, monkeypatch) -> None:
    suite = tmp_path / "companion-projects"
    marker = tmp_path / "marker.txt"
    failing = make_test(suite, "a", "test_fail.py", "raise SystemExit(1)\n")
    later = make_test(
        suite,
        "b",
        "test_later.py",
        f"from pathlib import Path\nPath({str(marker)!r}).write_text('ran')\n",
    )
    monkeypatch.setattr(runner, "ROOT", suite)

    failures = runner.run_test_files(
        [failing, later],
        timeout_seconds=1,
        fail_fast=True,
    )

    assert failures == ["a/test_fail.py"]
    assert not marker.exists()


def test_run_test_files_rejects_nonpositive_timeout(tmp_path: Path, monkeypatch) -> None:
    suite = tmp_path / "companion-projects"
    monkeypatch.setattr(runner, "ROOT", suite)

    with pytest.raises(ValueError):
        runner.run_test_files([], timeout_seconds=0)
