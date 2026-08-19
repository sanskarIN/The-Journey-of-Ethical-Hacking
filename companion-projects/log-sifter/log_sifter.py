#!/usr/bin/env python3
"""Summarize local authentication-style CSV logs for defensive learning."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

REQUIRED_COLUMNS = {"timestamp", "status", "user", "source"}
VALID_STATUS = {"success", "failure"}


def summarize(path: Path) -> dict[str, object]:
    total = 0
    statuses: Counter[str] = Counter()
    failures_by_user: Counter[str] = Counter()

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames or []))
            raise ValueError(f"missing required CSV columns: {', '.join(missing)}")

        for line_number, row in enumerate(reader, start=2):
            status = (row.get("status") or "").strip().lower()
            user = (row.get("user") or "").strip()
            if status not in VALID_STATUS:
                raise ValueError(f"line {line_number}: invalid status {status!r}")
            if not user:
                raise ValueError(f"line {line_number}: user must not be empty")
            total += 1
            statuses[status] += 1
            if status == "failure":
                failures_by_user[user] += 1

    return {
        "events": total,
        "successes": statuses["success"],
        "failures": statuses["failure"],
        "failures_by_user": dict(sorted(failures_by_user.items())),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Summarize a local authentication-style CSV log."
    )
    parser.add_argument("csv_file", type=Path, help="Path to the local CSV file")
    args = parser.parse_args()

    try:
        result = summarize(args.csv_file)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
