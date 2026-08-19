import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "tools"
COMPANION_DIR = ROOT / "companion-projects"

TOOLS = sorted(path for path in TOOLS_DIR.glob("*.py") if path.name != "__init__.py")
COMPANION_TOOLS = sorted(
    path
    for path in COMPANION_DIR.glob("*/*.py")
    if not path.name.startswith("test_")
)
CLI_PATHS = TOOLS + COMPANION_TOOLS


def test_tool_discovery_is_not_empty() -> None:
    assert TOOLS, "No local Python tools were discovered"


def test_companion_cli_discovery_matches_project_floor() -> None:
    assert len(COMPANION_TOOLS) >= 20, (
        f"Expected at least 20 companion project CLIs, found {len(COMPANION_TOOLS)}"
    )


@pytest.mark.parametrize(
    "path",
    CLI_PATHS,
    ids=lambda path: path.relative_to(ROOT).as_posix(),
)
def test_cli_help_smoke(path: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(path), "--help"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=10,
    )
    relative = path.relative_to(ROOT).as_posix()
    assert result.returncode == 0, f"{relative}: {result.stderr}"
    assert "usage:" in result.stdout.lower(), relative
