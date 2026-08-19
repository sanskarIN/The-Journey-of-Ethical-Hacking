#!/usr/bin/env python3
"""Summarize an explicit local asset inventory CSV."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

REQUIRED_COLUMNS = {"asset", "type", "owner", "status"}
VALID_STATUS = {"active", "retired", "maintenance", "unknown"}


def summarize(path: Path) -> dict[str, object]:
    type_counts: Counter[str] = Counter()
    status_counts: Counter[str] = Counter()
    incomplete: list[dict[str, str]] = []
    total = 0

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames or []))
            raise ValueError(f"missing required CSV columns: {', '.join(missing)}")

        for line_number, row in enumerate(reader, start=2):
            asset = (row.get("asset") or "").strip()
            asset_type = (row.get("type") or "").strip().lower()
            owner = (row.get("owner") or "").strip()
            status = (row.get("status") or "").strip().lower()
            if not asset or not asset_type:
                raise ValueError(f"line {line_number}: asset and type must not be empty")
            if status not in VALID_STATUS:
                raise ValueError(f"line {line_number}: invalid status {status!r}")

            total += 1
            type_counts[asset_type] += 1
            status_counts[status] += 1
            if not owner or status == "unknown":
                incomplete.append({"asset": asset, "owner": owner, "status": status})

    return {
        "assets": total,
        "by_type": dict(sorted(type_counts.items())),
        "by_status": dict(sorted(status_counts.items())),
        "needs_review": incomplete,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize a local asset inventory CSV without network discovery.")
    parser.add_argument("assets_csv", type=Path)
    args = parser.parse_args()

    try:
        result = summarize(args.assets_csv)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result["needs_review"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
