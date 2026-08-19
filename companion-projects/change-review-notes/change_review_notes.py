#!/usr/bin/env python3
"""Render local change-control CSV records as Markdown review notes."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

REQUIRED_COLUMNS = {"change_id", "system", "owner", "summary", "risk", "approved"}
RISKS = {"low", "medium", "high"}
TRUE_VALUES = {"true", "1", "yes"}
FALSE_VALUES = {"false", "0", "no"}


def parse_bool(value: str, line_number: int) -> bool:
    normalized = value.strip().lower()
    if normalized in TRUE_VALUES:
        return True
    if normalized in FALSE_VALUES:
        return False
    raise ValueError(f"line {line_number}: invalid approved value {value!r}")


def load(path: Path) -> list[dict[str, object]]:
    changes: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames or []))
            raise ValueError(f"missing required CSV columns: {', '.join(missing)}")

        for line_number, row in enumerate(reader, start=2):
            values = {key: (row.get(key) or "").strip() for key in REQUIRED_COLUMNS}
            if any(not values[key] for key in REQUIRED_COLUMNS - {"approved"}):
                raise ValueError(f"line {line_number}: required text fields must not be empty")
            risk = values["risk"].lower()
            if risk not in RISKS:
                raise ValueError(f"line {line_number}: invalid risk {values['risk']!r}")
            changes.append(
                {
                    "change_id": values["change_id"],
                    "system": values["system"],
                    "owner": values["owner"],
                    "summary": values["summary"],
                    "risk": risk,
                    "approved": parse_bool(values["approved"], line_number),
                }
            )
    return changes


def render(changes: list[dict[str, object]]) -> str:
    lines = ["# Change Review Notes", ""]
    for change in changes:
        lines.extend(
            [
                f"## {change['change_id']} — {change['system']}",
                "",
                f"- Owner: {change['owner']}",
                f"- Risk: {change['risk']}",
                f"- Approved: {'yes' if change['approved'] else 'no'}",
                f"- Summary: {str(change['summary']).replace(chr(10), ' ')}",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a local change-control CSV as Markdown review notes.")
    parser.add_argument("changes_csv", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        changes = load(args.changes_csv)
        markdown = render(changes)
        if args.output:
            args.output.write_text(markdown, encoding="utf-8")
        else:
            print(markdown, end="")
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    return 1 if any(not change["approved"] for change in changes) else 0


if __name__ == "__main__":
    raise SystemExit(main())
