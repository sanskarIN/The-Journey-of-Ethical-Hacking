#!/usr/bin/env python3
"""Validate a local exception register for defensive governance review."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path

REQUIRED_COLUMNS = {"exception_id", "owner", "expires_on", "rationale", "approved"}
TRUE_VALUES = {"true", "1", "yes"}
FALSE_VALUES = {"false", "0", "no"}


def parse_bool(value: str, line_number: int) -> bool:
    normalized = value.strip().lower()
    if normalized in TRUE_VALUES:
        return True
    if normalized in FALSE_VALUES:
        return False
    raise ValueError(f"line {line_number}: invalid approved value {value!r}")


def parse_date(value: str, context: str) -> date:
    try:
        return date.fromisoformat(value.strip())
    except ValueError as exc:
        raise ValueError(f"{context}: invalid date {value!r}") from exc


def validate_register(path: Path, as_of: date) -> dict[str, object]:
    findings: list[dict[str, object]] = []
    total = 0

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames or []))
            raise ValueError(f"missing required CSV columns: {', '.join(missing)}")

        for line_number, row in enumerate(reader, start=2):
            exception_id = (row.get("exception_id") or "").strip()
            owner = (row.get("owner") or "").strip()
            rationale = (row.get("rationale") or "").strip()
            if not exception_id or not owner or not rationale:
                raise ValueError(f"line {line_number}: exception_id, owner, and rationale must not be empty")
            expires_on = parse_date(row.get("expires_on") or "", f"line {line_number}")
            approved = parse_bool(row.get("approved") or "", line_number)
            total += 1

            reasons: list[str] = []
            if expires_on < as_of:
                reasons.append("expired")
            if not approved:
                reasons.append("not-approved")
            if reasons:
                findings.append(
                    {
                        "exception_id": exception_id,
                        "owner": owner,
                        "expires_on": expires_on.isoformat(),
                        "reasons": reasons,
                    }
                )

    return {"as_of": as_of.isoformat(), "exceptions": total, "findings": findings}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a local exception register as of an explicit date.")
    parser.add_argument("exceptions_csv", type=Path)
    parser.add_argument("--as-of", required=True, help="Review date in YYYY-MM-DD format")
    args = parser.parse_args()

    try:
        result = validate_register(args.exceptions_csv, parse_date(args.as_of, "--as-of"))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result["findings"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
