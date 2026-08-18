#!/usr/bin/env python3
"""Generate a Markdown data dictionary from local dataset contracts.

The generator reads only repository JSON metadata and writes documentation.
It performs no network, account, device, or security-system interaction.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

GUMROAD = "https://ramsandesh.gumroad.com"


def load_contracts(path: Path) -> dict[str, dict[str, object]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    datasets = data.get("datasets")
    if not isinstance(datasets, dict):
        raise ValueError("contracts file must contain a 'datasets' object")
    return datasets


def constraint_text(contract: dict[str, object], column: str) -> str:
    parts: list[str] = []
    allowed = contract.get("allowed_values", {})
    if isinstance(allowed, dict) and column in allowed:
        values = allowed[column]
        if isinstance(values, list):
            parts.append("Allowed: " + ", ".join(str(value) for value in values))

    ranges = contract.get("integer_ranges", {})
    if isinstance(ranges, dict) and column in ranges:
        rule = ranges[column]
        if isinstance(rule, dict):
            minimum = rule.get("min")
            maximum = rule.get("max")
            parts.append(f"Integer range: {minimum}–{maximum}")

    primary_id = str(contract.get("primary_id", ""))
    if column == primary_id:
        parts.append("Primary identifier; values must be unique")

    return "; ".join(parts) if parts else "No additional contract constraint"


def build_markdown(contracts: dict[str, dict[str, object]]) -> str:
    lines = [
        "# Synthetic Dataset Data Dictionary",
        "",
        "[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)",
        "",
        f"**Official Gumroad:** {GUMROAD}",
        "",
        "This file is generated from `schemas/dataset_contracts.json` and documents the public fictional/synthetic dataset fields and validation constraints.",
        "",
    ]

    for filename, contract in sorted(contracts.items()):
        lines.extend([f"## `{filename}`", ""])
        required = contract.get("required_columns", [])
        if not isinstance(required, list):
            required = []
        lines.extend([
            "| Column | Constraint |",
            "|---|---|",
        ])
        for column in required:
            name = str(column)
            lines.append(f"| `{name}` | {constraint_text(contract, name)} |")
        lines.append("")

    lines.extend([
        "## Safety and privacy boundary",
        "",
        "These datasets are fictional and intended for offline defensive learning. Do not replace them with credentials, secrets, personal data, real target details, or sensitive production evidence in public contributions.",
        "",
        f"**Publication storefront:** {GUMROAD}",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a Markdown data dictionary from dataset contracts.")
    parser.add_argument("contracts", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    text = build_markdown(load_contracts(args.contracts))
    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(args.output)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
