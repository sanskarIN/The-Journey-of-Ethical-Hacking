#!/usr/bin/env python3
"""Verify a generated public-resource manifest against a local repository tree.

The verifier operates only on local files. It performs no network access and
never reads or publishes commercial book artifacts.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.resource_manifest import EXCLUDED_SUFFIXES, public_files, sha256


def validate_manifest(root: Path, manifest: dict[str, object]) -> list[str]:
    errors: list[str] = []

    if manifest.get("format_version") != 1:
        errors.append("manifest format_version must be 1")

    resources = manifest.get("resources")
    if not isinstance(resources, list):
        return errors + ["manifest resources must be a list"]

    if manifest.get("resource_count") != len(resources):
        errors.append("manifest resource_count does not match resources length")

    seen: set[str] = set()
    manifested_paths: set[str] = set()

    for index, entry in enumerate(resources):
        if not isinstance(entry, dict):
            errors.append(f"resource entry {index} must be an object")
            continue

        path_value = entry.get("path")
        if not isinstance(path_value, str) or not path_value:
            errors.append(f"resource entry {index} has an invalid path")
            continue
        if path_value in seen:
            errors.append(f"duplicate manifest path: {path_value}")
            continue
        seen.add(path_value)
        manifested_paths.add(path_value)

        relative = Path(path_value)
        if relative.is_absolute() or ".." in relative.parts:
            errors.append(f"unsafe manifest path: {path_value}")
            continue
        if relative.suffix.lower() in EXCLUDED_SUFFIXES:
            errors.append(f"commercial/archive format must not be manifested: {path_value}")
            continue

        file_path = root / relative
        if not file_path.is_file():
            errors.append(f"manifested file is missing: {path_value}")
            continue

        expected_bytes = entry.get("bytes")
        if expected_bytes != file_path.stat().st_size:
            errors.append(f"byte-size mismatch: {path_value}")

        expected_hash = entry.get("sha256")
        if expected_hash != sha256(file_path):
            errors.append(f"SHA-256 mismatch: {path_value}")

    expected_paths = {
        path.relative_to(root).as_posix() for path in public_files(root)
    }
    for missing in sorted(expected_paths - manifested_paths):
        errors.append(f"public file missing from manifest: {missing}")
    for extra in sorted(manifested_paths - expected_paths):
        errors.append(f"unexpected manifest path: {extra}")

    return errors


def load_manifest(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("manifest root must be an object")
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify a public-resource manifest.")
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    root = args.root.resolve()
    manifest_path = args.manifest if args.manifest.is_absolute() else root / args.manifest
    try:
        manifest = load_manifest(manifest_path)
    except (json.JSONDecodeError, ValueError) as exc:
        print(exc)
        raise SystemExit(1) from exc

    errors = validate_manifest(root, manifest)
    for error in errors:
        print(error)
    if errors:
        raise SystemExit(1)
    print(f"Public resource manifest verification: OK ({manifest_path})")


if __name__ == "__main__":
    main()
