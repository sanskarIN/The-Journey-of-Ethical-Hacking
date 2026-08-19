#!/usr/bin/env python3
"""Validate local JSONL security-event records for defensive labs."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

REQUIRED = {"timestamp", "severity", "category", "summary", "asset"}
SEVERITIES = {"low", "medium", "high", "critical"}


def parse_timestamp(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValueError(f"invalid timestamp {value!r}") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"timestamp must include timezone: {value!r}")
    return parsed


def validate_lines(lines: list[str]) -> dict[str, object]:
    errors: list[str] = []
    valid = 0

    for line_number, raw in enumerate(lines, start=1):
        if not raw.strip():
            continue
        try:
            item = json.loads(raw)
            if not isinstance(item, dict):
                raise ValueError("event must be a JSON object")
            missing = REQUIRED - set(item)
            if missing:
                raise ValueError(f"missing fields: {', '.join(sorted(missing))}")
            for key in {"timestamp", "severity", "category", "summary", "asset"}:
                if not isinstance(item[key], str) or not item[key].strip():
                    raise ValueError(f"{key} must be non-empty text")
            parse_timestamp(item["timestamp"])
            if item["severity"].strip().lower() not in SEVERITIES:
                raise ValueError(f"invalid severity {item['severity']!r}")
        except (json.JSONDecodeError, ValueError) as exc:
            errors.append(f"line {line_number}: {exc}")
        else:
            valid += 1

    return {"valid_events": valid, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a local JSONL defensive event file.")
    parser.add_argument("events_file", type=Path)
    args = parser.parse_args()

    try:
        result = validate_lines(args.events_file.read_text(encoding="utf-8").splitlines())
    except OSError as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
