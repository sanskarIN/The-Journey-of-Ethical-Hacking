#!/usr/bin/env python3
"""Validate local synthetic CSV headers against repository dataset contracts.

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
        reader = csv.reader(handle)
        header = next(reader, [])

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
