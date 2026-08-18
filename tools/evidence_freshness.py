#!/usr/bin/env python3
"""Offline evidence-freshness summary for synthetic/local CSV data."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def freshness_bucket(age_days: int) -> str:
    if age_days <= 30:
        return "fresh"
    if age_days <= 60:
        return "aging"
    return "stale"


def summarize(path: Path) -> dict[str, int]:
    counts = {"fresh": 0, "aging": 0, "stale": 0}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            age = int(row.get("evidence_age_days", "0") or 0)
            counts[freshness_bucket(age)] += 1
    return counts


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize local evidence age buckets.")
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()
    counts = summarize(args.csv_file)
    for key in ("fresh", "aging", "stale"):
        print(f"{key}: {counts[key]}")


if __name__ == "__main__":
    main()
