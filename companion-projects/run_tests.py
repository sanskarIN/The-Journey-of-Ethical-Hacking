#!/usr/bin/env python3
"""Run every companion-project unit test as an isolated Python process."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def discover() -> list[Path]:
    return sorted(ROOT.glob("*/test_*.py"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Run all defensive companion-project unit tests.")
    parser.add_argument("--list", action="store_true", help="List discovered test files without running them")
    args = parser.parse_args()

    tests = discover()
    if not tests:
        print("No companion project tests discovered.", file=sys.stderr)
        return 1

    if args.list:
        for test in tests:
            print(test.relative_to(ROOT).as_posix())
        return 0

    failures: list[str] = []
    for test in tests:
        relative = test.relative_to(ROOT).as_posix()
        print(f"==> {relative}")
        completed = subprocess.run([sys.executable, str(test)], check=False)
        if completed.returncode != 0:
            failures.append(relative)

    if failures:
        print("\nFailed companion tests:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"\nAll {len(tests)} companion project test files passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
