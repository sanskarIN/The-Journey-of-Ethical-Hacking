#!/usr/bin/env python3
"""Map local defensive evidence records to recognized control identifiers."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

REQUIRED_COLUMNS = {"evidence_id", "control", "status", "owner"}
VALID_STATUS = {"current", "stale", "missing"}


def load_controls(path: Path) -> set[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    controls = payload.get("controls") if isinstance(payload, dict) else None
    if (
        not isinstance(controls, list)
        or not controls
        or not all(isinstance(control, str) and control.strip() for control in controls)
    ):
        raise ValueError("policy must contain a non-empty string list named controls")
    return {control.strip() for control in controls}


def map_evidence(path: Path, controls: set[str]) -> dict[str, object]:
    status_counts: Counter[str] = Counter()
    unknown_controls: list[dict[str, str]] = []
    total = 0

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames or []))
            raise ValueError(f"missing required CSV columns: {', '.join(missing)}")

        for line_number, row in enumerate(reader, start=2):
            evidence_id = (row.get("evidence_id") or "").strip()
            control = (row.get("control") or "").strip()
            status = (row.get("status") or "").strip().lower()
            owner = (row.get("owner") or "").strip()
            if not evidence_id or not control or not owner:
                raise ValueError(f"line {line_number}: evidence_id, control, and owner must not be empty")
            if status not in VALID_STATUS:
                raise ValueError(f"line {line_number}: invalid status {status!r}")

            total += 1
            status_counts[status] += 1
            if control not in controls:
                unknown_controls.append(
                    {"evidence_id": evidence_id, "control": control, "owner": owner}
                )

    return {
        "evidence_records": total,
        "by_status": dict(sorted(status_counts.items())),
        "unknown_controls": unknown_controls,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Map local evidence records to explicit control identifiers.")
    parser.add_argument("evidence_csv", type=Path)
    parser.add_argument("controls_json", type=Path)
    args = parser.parse_args()

    try:
        result = map_evidence(args.evidence_csv, load_controls(args.controls_json))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result["unknown_controls"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
