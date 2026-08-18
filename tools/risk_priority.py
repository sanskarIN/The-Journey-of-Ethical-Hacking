#!/usr/bin/env python3
"""Offline prioritization helper for fictional/synthetic risk records.

This tool reads a local CSV file only. It performs no network, account,
device, API, scanning, authentication, or security-control interaction.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

CRITICALITY_SCORE = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}


def score(row: dict[str, str]) -> int:
    value = CRITICALITY_SCORE.get(row.get("criticality", "Medium"), 2) * 10
    value += min(int(row.get("age_days", "0") or 0), 90) // 10
    value += 8 if row.get("open_exception", "No").lower() == "yes" else 0
    value += 6 if row.get("telemetry_gap", "No").lower() == "yes" else 0
    value += 6 if row.get("recovery_gap", "No").lower() == "yes" else 0
    return value


def rank_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return sorted(rows, key=score, reverse=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank local synthetic risk signals.")
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()

    for row in rank_rows(args.csv_file):
        print(f"{row.get('signal_id','?'):8} score={score(row):2} domain={row.get('domain','Unknown')}")


if __name__ == "__main__":
    main()
