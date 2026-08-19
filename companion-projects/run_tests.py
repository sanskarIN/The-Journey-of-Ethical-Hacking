#!/usr/bin/env python3
"""Run every companion-project unit test as an isolated Python process."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_TIMEOUT_SECONDS = 30.0


def discover() -> list[Path]:
    return sorted(ROOT.glob("*/test_*.py"))


def run_test_files(
    tests: list[Path],
    *,
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
    fail_fast: bool = False,
) -> list[str]:
    """Run test files and return relative paths that failed or timed out."""
    if timeout_seconds <= 0:
        raise ValueError("timeout_seconds must be greater than zero")

    failures: list[str] = []
    for test in tests:
        relative = test.relative_to(ROOT).as_posix()
        print(f"==> {relative}")
        try:
            completed = subprocess.run(
                [sys.executable, str(test)],
                check=False,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            print(
                f"TIMEOUT {relative} after {timeout_seconds:g}s",
                file=sys.stderr,
            )
            failures.append(relative)
        else:
            if completed.returncode != 0:
                failures.append(relative)

        if failures and fail_fast:
            break

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Run all defensive companion-project unit tests.")
    parser.add_argument("--list", action="store_true", help="List discovered test files without running them")
    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT_SECONDS,
        help=f"Per-test-file timeout in seconds (default: {DEFAULT_TIMEOUT_SECONDS:g})",
    )
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="Stop after the first failed or timed-out test file",
    )
    args = parser.parse_args()

    if args.timeout <= 0:
        parser.error("--timeout must be greater than zero")

    tests = discover()
    if not tests:
        print("No companion project tests discovered.", file=sys.stderr)
        return 1

    if args.list:
        for test in tests:
            print(test.relative_to(ROOT).as_posix())
        return 0

    failures = run_test_files(
        tests,
        timeout_seconds=args.timeout,
        fail_fast=args.fail_fast,
    )

    if failures:
        print("\nFailed companion tests:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"\nAll {len(tests)} companion project test files passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
