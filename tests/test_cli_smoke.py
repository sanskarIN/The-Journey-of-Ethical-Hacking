import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

TOOLS = [
    "risk_priority.py",
    "evidence_freshness.py",
    "control_review.py",
    "csv_quality.py",
    "dataset_contracts.py",
    "doc_accessibility.py",
    "markdown_links.py",
    "json_metadata.py",
    "dataset_summary.py",
    "repo_health.py",
    "resource_manifest.py",
    "synthetic_safety.py",
    "gumroad_presence.py",
]


@pytest.mark.parametrize("filename", TOOLS)
def test_tool_help_smoke(filename: str):
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / filename), "--help"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "usage:" in result.stdout.lower()
