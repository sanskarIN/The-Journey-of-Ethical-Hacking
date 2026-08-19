#!/usr/bin/env python3
"""Summarize local tabletop recovery-exercise results."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

REQUIRED_COLUMNS = {"exercise_id", "objective", "result", "duration_minutes", "observations"}
VALID_RESULTS = {"pass", "partial", "fail"}


def summarize(path: Path) -> dict[str, object]:
    result_counts: Counter[str] = Counter()
    durations: list[int] = []
    total = 0

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames or []))
            raise ValueError(f"missing required CSV columns: {', '.join(missing)}")

        for line_number, row in enumerate(reader, start=2):
            exercise_id = (row.get("exercise_id") or "").strip()
            objective = (row.get("objective") or "").strip()
            observations = (row.get("observations") or "").strip()
            result = (row.get("result") or "").strip().lower()
            if not exercise_id or not objective or not observations:
                raise ValueError(f"line {line_number}: exercise_id, objective, and observations must not be empty")
            if result not in VALID_RESULTS:
                raise ValueError(f"line {line_number}: invalid result {result!r}")
            try:
                duration = int((row.get("duration_minutes") or "").strip())
            except ValueError as exc:
                raise ValueError(f"line {line_number}: duration_minutes must be an integer") from exc
            if duration < 0:
                raise ValueError(f"line {line_number}: duration_minutes must not be negative")

            total += 1
            result_counts[result] += 1
            durations.append(duration)

    average = round(sum(durations) / len(durations), 2) if durations else 0.0
    return {
        "exercises": total,
        "by_result": dict(sorted(result_counts.items())),
        "average_duration_minutes": average,
        "needs_follow_up": result_counts["partial"] + result_counts["fail"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize a local tabletop recovery-exercise CSV.")
    parser.add_argument("exercises_csv", type=Path)
    args = parser.parse_args()

    try:
        result = summarize(args.exercises_csv)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result["needs_follow_up"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
