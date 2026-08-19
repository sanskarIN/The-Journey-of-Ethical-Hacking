#!/usr/bin/env python3
"""Summarize an explicit local patch-status export for defensive review."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

REQUIRED_COLUMNS = {"asset", "patch_id", "status", "age_days"}
VALID_STATUS = {"installed", "pending", "failed", "not-applicable"}


def summarize(path: Path) -> dict[str, object]:
    statuses: Counter[str] = Counter()
    pending_age_days: list[int] = []
    total = 0

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames or []))
            raise ValueError(f"missing required CSV columns: {', '.join(missing)}")

        for line_number, row in enumerate(reader, start=2):
            asset = (row.get("asset") or "").strip()
            patch_id = (row.get("patch_id") or "").strip()
            status = (row.get("status") or "").strip().lower()
            if not asset or not patch_id:
                raise ValueError(f"line {line_number}: asset and patch_id must not be empty")
            if status not in VALID_STATUS:
                raise ValueError(f"line {line_number}: invalid status {status!r}")
            try:
                age_days = int((row.get("age_days") or "").strip())
            except ValueError as exc:
                raise ValueError(f"line {line_number}: age_days must be an integer") from exc
            if age_days < 0:
                raise ValueError(f"line {line_number}: age_days must not be negative")

            total += 1
            statuses[status] += 1
            if status in {"pending", "failed"}:
                pending_age_days.append(age_days)

    return {
        "patch_records": total,
        "by_status": dict(sorted(statuses.items())),
        "open_items": statuses["pending"] + statuses["failed"],
        "oldest_open_age_days": max(pending_age_days) if pending_age_days else 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize an explicit local patch register CSV.")
    parser.add_argument("patches_csv", type=Path)
    args = parser.parse_args()

    try:
        result = summarize(args.patches_csv)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result["open_items"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
