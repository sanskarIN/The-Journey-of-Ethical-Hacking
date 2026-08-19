#!/usr/bin/env python3
"""Create a CSV inventory of explicitly selected local evidence files."""

from __future__ import annotations

import argparse
import csv
import hashlib
from datetime import datetime, timezone
from pathlib import Path

CHUNK_SIZE = 1024 * 1024
FIELDNAMES = ["path", "size", "modified_utc", "sha256"]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()


def collect(root: Path) -> list[dict[str, str | int]]:
    if not root.is_dir():
        raise ValueError(f"not a directory: {root}")

    rows: list[dict[str, str | int]] = []
    for path in sorted(
        p for p in root.rglob("*") if p.is_file() and not p.is_symlink()
    ):
        stat = path.stat()
        rows.append(
            {
                "path": path.relative_to(root).as_posix(),
                "size": stat.st_size,
                "modified_utc": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                "sha256": sha256_file(path),
            }
        )
    return rows


def write_csv(rows: list[dict[str, str | int]], output: Path) -> None:
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Inventory files in an explicitly selected local directory.")
    parser.add_argument("root", type=Path)
    parser.add_argument("output_csv", type=Path)
    args = parser.parse_args()

    try:
        write_csv(collect(args.root), args.output_csv)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
