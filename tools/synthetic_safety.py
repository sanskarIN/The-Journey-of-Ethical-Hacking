#!/usr/bin/env python3
"""Detect obviously sensitive-looking values in synthetic CSV exercises.

This is a conservative local lint rule for public sample data. It does not
send data anywhere and is not a replacement for a full privacy or secrets
review.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

PATTERNS = {
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    "url": re.compile(r"https?://", re.IGNORECASE),
    "ipv4": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "token_like": re.compile(r"(?:ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16}|\b[A-Fa-f0-9]{32,}\b)"),
}


def scan_value(value: str) -> list[str]:
    return [name for name, pattern in PATTERNS.items() if pattern.search(value)]


def scan_csv(path: Path) -> list[str]:
    findings: list[str] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row_number, row in enumerate(reader, start=2):
            for column, raw in row.items():
                value = raw or ""
                for finding in scan_value(value):
                    findings.append(f"{path}:{row_number}:{column}: {finding}")
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description="Lint synthetic CSV files for sensitive-looking values.")
    parser.add_argument("csv_files", nargs="+", type=Path)
    args = parser.parse_args()

    findings: list[str] = []
    for path in args.csv_files:
        try:
            findings.extend(scan_csv(path))
        except (OSError, csv.Error) as exc:
            print(f"{path}: {exc}")
            raise SystemExit(1) from exc

    for item in findings:
        print(item)
    if findings:
        raise SystemExit(1)
    print("Synthetic-data sensitivity check: OK")


if __name__ == "__main__":
    main()
