#!/usr/bin/env python3
"""Validate repository JSON metadata using local files only.

This helper performs structural checks for companion-release metadata and
synthetic-dataset contracts. It performs no network or system interaction.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

RELEASE_REQUIRED = {
    "project",
    "edition",
    "companion_release",
    "author",
    "repository",
    "official_gumroad",
    "series_parts",
    "companion_projects",
    "companion_projects_offline",
    "public_scope",
    "code_license",
    "commercial_book_rights",
    "commercial_manuscript_in_public_repo",
    "author_avatar_or_photo_used",
    "x_or_twitter_link_included",
    "safety_scope",
}

CONTRACT_REQUIRED = {"version", "datasets"}
DATASET_CONTRACT_REQUIRED = {"primary_id", "required_columns", "allow_extra_columns"}


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_release(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["release metadata must be a JSON object"]

    missing = sorted(RELEASE_REQUIRED - set(data))
    if missing:
        errors.append("missing release keys: " + ", ".join(missing))

    if data.get("series_parts") != 200:
        errors.append("series_parts must equal 200")
    if data.get("companion_projects") != 20:
        errors.append("companion_projects must equal 20")
    if data.get("companion_projects_offline") is not True:
        errors.append("companion_projects_offline must be true")
    if data.get("official_gumroad") != "https://ramsandesh.gumroad.com":
        errors.append("official_gumroad must use the approved direct storefront URL")
    if data.get("commercial_manuscript_in_public_repo") is not False:
        errors.append("commercial_manuscript_in_public_repo must be false")
    if data.get("author_avatar_or_photo_used") is not False:
        errors.append("author_avatar_or_photo_used must be false")
    if data.get("x_or_twitter_link_included") is not False:
        errors.append("x_or_twitter_link_included must be false")

    scope = data.get("public_scope")
    if scope is not None and (
        not isinstance(scope, list)
        or not scope
        or not all(isinstance(item, str) and item.strip() for item in scope)
    ):
        errors.append("public_scope must be a non-empty list of strings")

    return errors


def validate_contracts(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["dataset contracts must be a JSON object"]

    missing = sorted(CONTRACT_REQUIRED - set(data))
    if missing:
        errors.append("missing contract keys: " + ", ".join(missing))
        return errors

    datasets = data.get("datasets")
    if not isinstance(datasets, dict) or not datasets:
        errors.append("datasets must be a non-empty object")
        return errors

    for filename, contract in sorted(datasets.items()):
        if not isinstance(contract, dict):
            errors.append(f"{filename}: contract must be an object")
            continue
        missing_contract = sorted(DATASET_CONTRACT_REQUIRED - set(contract))
        if missing_contract:
            errors.append(f"{filename}: missing keys: {', '.join(missing_contract)}")
        columns = contract.get("required_columns")
        primary_id = contract.get("primary_id")
        if not isinstance(columns, list) or not columns or not all(isinstance(item, str) and item for item in columns):
            errors.append(f"{filename}: required_columns must be a non-empty list of strings")
        elif primary_id not in columns:
            errors.append(f"{filename}: primary_id must appear in required_columns")
        if not isinstance(contract.get("allow_extra_columns"), bool):
            errors.append(f"{filename}: allow_extra_columns must be boolean")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate local companion JSON metadata.")
    parser.add_argument("release_json", type=Path)
    parser.add_argument("contracts_json", type=Path)
    args = parser.parse_args()

    checks = [
        (args.release_json, validate_release),
        (args.contracts_json, validate_contracts),
    ]

    failures = 0
    for path, validator in checks:
        try:
            errors = validator(load_json(path))
        except (OSError, json.JSONDecodeError) as exc:
            errors = [str(exc)]
        if errors:
            failures += len(errors)
            for error in errors:
                print(f"{path}: {error}")
        else:
            print(f"{path}: OK")

    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
