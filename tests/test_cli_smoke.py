import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "tools"
TOOLS = sorted(path.name for path in TOOLS_DIR.glob("*.py") if path.name != "__init__.py")


def test_tool_discovery_is_not_empty() -> None:
    assert TOOLS, "No local Python tools were discovered"


@pytest.mark.parametrize("filename", TOOLS)
def test_tool_help_smoke(filename: str):
    result = subprocess.run(
        [sys.executable, str(TOOLS_DIR / filename), "--help"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, f"{filename}: {result.stderr}"
    assert "usage:" in result.stdout.lower(), filename
