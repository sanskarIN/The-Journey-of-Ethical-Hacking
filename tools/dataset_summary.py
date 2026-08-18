#!/usr/bin/env python3
"""Summarize local synthetic CSV datasets without external access.

The utility reads only the files supplied on the command line and reports
basic structure useful for defensive learning and repository maintenance.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def summarize(path: Path) -> dict[str, object]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    blank_cells = 0
    for row in rows:
        blank_cells += sum(1 for name in fieldnames if not (row.get(name) or "").strip())

    return {
        "file": path.name,
        "rows": len(rows),
        "columns": len(fieldnames),
        "blank_cells": blank_cells,
        "fields": fieldnames,
    }


def format_summary(result: dict[str, object]) -> str:
    fields = ", ".join(result["fields"])
    return (
        f"{result['file']}: rows={result['rows']} columns={result['columns']} "
        f"blank_cells={result['blank_cells']}\n  fields: {fields}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize local synthetic CSV datasets.")
    parser.add_argument("csv_files", nargs="+", type=Path)
    args = parser.parse_args()

    for path in args.csv_files:
        try:
            print(format_summary(summarize(path)))
        except (OSError, csv.Error) as exc:
            print(f"{path}: {exc}")
            raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
