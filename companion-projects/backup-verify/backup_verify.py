#!/usr/bin/env python3
"""Compare two explicit local directories for backup verification."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

CHUNK_SIZE = 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()


def snapshot(root: Path) -> dict[str, str]:
    if not root.is_dir():
        raise ValueError(f"not a directory: {root}")
    return {
        path.relative_to(root).as_posix(): sha256_file(path)
        for path in sorted(p for p in root.rglob("*") if p.is_file())
    }


def compare(primary: Path, backup: Path) -> dict[str, list[str]]:
    expected = snapshot(primary)
    actual = snapshot(backup)
    expected_paths = set(expected)
    actual_paths = set(actual)
    common = expected_paths & actual_paths
    changed = sorted(path for path in common if expected[path] != actual[path])
    matching = sorted(common - set(changed))
    return {
        "matching": matching,
        "missing_from_backup": sorted(expected_paths - actual_paths),
        "unexpected_in_backup": sorted(actual_paths - expected_paths),
        "changed": changed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a local backup directory against a primary directory.")
    parser.add_argument("primary", type=Path)
    parser.add_argument("backup", type=Path)
    args = parser.parse_args()

    try:
        result = compare(args.primary, args.backup)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    failed = result["missing_from_backup"] or result["unexpected_in_backup"] or result["changed"]
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
