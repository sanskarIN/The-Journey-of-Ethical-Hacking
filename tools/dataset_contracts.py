#!/usr/bin/env python3
"""Validate local synthetic CSV files against repository dataset contracts.

The validator is dependency-free, reads only local files, makes no network
requests, and performs no security-system interaction.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def load_contracts(path: Path) -> dict[str, dict[str, object]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    datasets = data.get("datasets", {})
    if not isinstance(datasets, dict):
        raise ValueError("contracts file must contain a 'datasets' object")
    return datasets


def validate_dataset(csv_path: Path, contract: dict[str, object]) -> list[str]:
    issues: list[str] = []
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        header = list(reader.fieldnames or [])
        rows = list(reader)

    required = [str(value) for value in contract.get("required_columns", [])]
    missing = [column for column in required if column not in header]
    if missing:
        issues.append("missing required columns: " + ", ".join(missing))

    allow_extra = bool(contract.get("allow_extra_columns", True))
    if not allow_extra:
        extra = [column for column in header if column not in required]
        if extra:
            issues.append("unexpected columns: " + ", ".join(extra))

    primary_id = str(contract.get("primary_id", ""))
    if primary_id and primary_id not in header:
        issues.append(f"primary identifier column missing: {primary_id}")
    elif primary_id:
        seen: set[str] = set()
        for row_number, row in enumerate(rows, start=2):
            value = (row.get(primary_id) or "").strip()
            if not value:
                issues.append(f"row {row_number}: primary identifier {primary_id} is empty")
            elif value in seen:
                issues.append(f"row {row_number}: duplicate primary identifier {value}")
            else:
                seen.add(value)

    allowed_values = contract.get("allowed_values", {})
    if isinstance(allowed_values, dict):
        for column, allowed in allowed_values.items():
            if column not in header or not isinstance(allowed, list):
                continue
            allowed_set = {str(value) for value in allowed}
            for row_number, row in enumerate(rows, start=2):
                value = (row.get(str(column)) or "").strip()
                if value not in allowed_set:
                    issues.append(
                        f"row {row_number}: {column} value {value!r} is not allowed"
                    )

    integer_ranges = contract.get("integer_ranges", {})
    if isinstance(integer_ranges, dict):
        for column, bounds in integer_ranges.items():
            if column not in header or not isinstance(bounds, dict):
                continue
            minimum = bounds.get("min")
            maximum = bounds.get("max")
            for row_number, row in enumerate(rows, start=2):
                raw = (row.get(str(column)) or "").strip()
                try:
                    value = int(raw)
                except ValueError:
                    issues.append(f"row {row_number}: {column} value {raw!r} is not an integer")
                    continue
                if isinstance(minimum, int) and value < minimum:
                    issues.append(f"row {row_number}: {column} value {value} is below {minimum}")
                if isinstance(maximum, int) and value > maximum:
                    issues.append(f"row {row_number}: {column} value {value} is above {maximum}")

    return issues


def validate_catalog(contracts_path: Path, datasets_dir: Path) -> list[str]:
    issues: list[str] = []
    contracts = load_contracts(contracts_path)

    for filename, contract in sorted(contracts.items()):
        csv_path = datasets_dir / filename
        if not csv_path.exists():
            issues.append(f"{filename}: dataset file is missing")
            continue
        if not isinstance(contract, dict):
            issues.append(f"{filename}: contract must be an object")
            continue
        for issue in validate_dataset(csv_path, contract):
            issues.append(f"{filename}: {issue}")

    uncontracted = sorted(
        path.name for path in datasets_dir.glob("*.csv") if path.name not in contracts
    )
    for filename in uncontracted:
        issues.append(f"{filename}: no contract defined")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate local synthetic dataset contracts.")
    parser.add_argument("contracts", type=Path)
    parser.add_argument("datasets_dir", type=Path)
    args = parser.parse_args()

    issues = validate_catalog(args.contracts, args.datasets_dir)
    for issue in issues:
        print(f"- {issue}")

    if issues:
        print(f"Dataset contract validation failed with {len(issues)} issue(s).")
        return 1

    print("Dataset contract validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
