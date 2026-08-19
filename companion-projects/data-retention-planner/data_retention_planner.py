#!/usr/bin/env python3
"""Calculate advisory review due dates from a local retention register."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import date, timedelta
from pathlib import Path

REQUIRED_COLUMNS = {"dataset", "classification", "last_review", "review_interval_days"}


def parse_date(value: str, context: str) -> date:
    try:
        return date.fromisoformat(value.strip())
    except ValueError as exc:
        raise ValueError(f"{context}: invalid date {value!r}") from exc


def review(path: Path, as_of: date) -> dict[str, object]:
    items: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames or []))
            raise ValueError(f"missing required CSV columns: {', '.join(missing)}")

        for line_number, row in enumerate(reader, start=2):
            dataset = (row.get("dataset") or "").strip()
            classification = (row.get("classification") or "").strip()
            if not dataset or not classification:
                raise ValueError(f"line {line_number}: dataset and classification must not be empty")
            last_review = parse_date(row.get("last_review") or "", f"line {line_number}")
            try:
                interval = int((row.get("review_interval_days") or "").strip())
            except ValueError as exc:
                raise ValueError(f"line {line_number}: review_interval_days must be an integer") from exc
            if interval <= 0:
                raise ValueError(f"line {line_number}: review_interval_days must be positive")
            due = last_review + timedelta(days=interval)
            items.append(
                {
                    "dataset": dataset,
                    "classification": classification,
                    "next_review": due.isoformat(),
                    "due": due <= as_of,
                }
            )

    due_count = sum(1 for item in items if item["due"])
    return {"as_of": as_of.isoformat(), "datasets": items, "due_count": due_count}


def main() -> int:
    parser = argparse.ArgumentParser(description="Calculate advisory review dates from a local retention register.")
    parser.add_argument("register_csv", type=Path)
    parser.add_argument("--as-of", required=True, help="Review date in YYYY-MM-DD format")
    args = parser.parse_args()

    try:
        result = review(args.register_csv, parse_date(args.as_of, "--as-of"))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result["due_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
