#!/usr/bin/env python3
"""Offline review-priority helper for fictional control-evidence records.

This utility reads only a local CSV file. It does not connect to networks,
accounts, devices, APIs, or security platforms, and it performs no changes.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

CRITICALITY_WEIGHT = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}


def review_score(row: dict[str, str]) -> int:
    score = CRITICALITY_WEIGHT.get(row.get("criticality", "Medium"), 2) * 10
    score += min(int(row.get("evidence_age_days", "0") or 0), 180) // 15
    if row.get("exception_open", "No").lower() == "yes":
        score += 8
    if row.get("recovery_tested", "Yes").lower() != "yes":
        score += 6
    return score


def rank_evidence(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return sorted(rows, key=review_score, reverse=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank local fictional control evidence for review.")
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()

    for row in rank_evidence(args.csv_file):
        print(
            f"{row.get('evidence_id','?'):8} "
            f"score={review_score(row):2} "
            f"area={row.get('control_area','Unknown')}"
        )


if __name__ == "__main__":
    main()
