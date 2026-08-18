#!/usr/bin/env python3
"""Dependency-free quality checks for local synthetic CSV exercise files.

The utility checks structure only: headers, blank identifiers, duplicate IDs,
and inconsistent row widths. It does not connect to any external service.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def inspect_csv(path: Path) -> list[str]:
    issues: list[str] = []
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.reader(handle))

    if not rows:
        return ["file is empty"]

    header = rows[0]
    if not header or any(not cell.strip() for cell in header):
        issues.append("header contains a blank column name")
    if len(set(header)) != len(header):
        issues.append("header contains duplicate column names")

    expected_width = len(header)
    identifiers: set[str] = set()
    for line_no, row in enumerate(rows[1:], 2):
        if len(row) != expected_width:
            issues.append(f"line {line_no}: expected {expected_width} columns, found {len(row)}")
            continue
        if row and not row[0].strip():
            issues.append(f"line {line_no}: blank primary identifier")
        elif row:
            identifier = row[0].strip()
            if identifier in identifiers:
                issues.append(f"line {line_no}: duplicate primary identifier '{identifier}'")
            identifiers.add(identifier)

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Check local synthetic CSV structure.")
    parser.add_argument("csv_files", nargs="+", type=Path)
    args = parser.parse_args()

    failures = 0
    for path in args.csv_files:
        issues = inspect_csv(path)
        if issues:
            failures += len(issues)
            print(path)
            for issue in issues:
                print(f"  - {issue}")

    if failures:
        print(f"CSV quality check failed with {failures} issue(s).")
        return 1

    print("CSV quality check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
