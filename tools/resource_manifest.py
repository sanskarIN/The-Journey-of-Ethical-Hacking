#!/usr/bin/env python3
"""Generate a machine-readable manifest of public companion resources.

The generator hashes local repository files only. It excludes Git metadata,
cache files, and commercial publication formats by design.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

PUBLIC_DIRS = ("docs", "resources", "datasets", "schemas", "exercises", "examples", "tools", "tests", ".github")
PUBLIC_TOP_LEVEL = (
    "README.md",
    "ROADMAP.md",
    "CHANGELOG.md",
    "ERRATA.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SUPPORT.md",
    "NOTICE",
    "LICENSE",
    "BOOK_CONTENT_LICENSE.md",
    "COMPANION_RELEASE.json",
    "what_changed.md",
)
EXCLUDED_SUFFIXES = {".pdf", ".epub", ".docx", ".zip"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def public_files(root: Path) -> list[Path]:
    files: set[Path] = set()
    for name in PUBLIC_TOP_LEVEL:
        path = root / name
        if path.is_file():
            files.add(path)
    for dirname in PUBLIC_DIRS:
        base = root / dirname
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            if "__pycache__" in path.parts or path.suffix in EXCLUDED_SUFFIXES:
                continue
            files.add(path)
    return sorted(files, key=lambda item: item.relative_to(root).as_posix())


def build_manifest(root: Path) -> dict[str, object]:
    entries = []
    for path in public_files(root):
        entries.append(
            {
                "path": path.relative_to(root).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    return {
        "format_version": 1,
        "resource_count": len(entries),
        "resources": entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate local public-resource manifest JSON.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, help="Write JSON to this path instead of stdout")
    args = parser.parse_args()

    root = args.root.resolve()
    text = json.dumps(build_manifest(root), indent=2, ensure_ascii=False) + "\n"
    if args.output:
        output = args.output if args.output.is_absolute() else root / args.output
        output.write_text(text, encoding="utf-8")
        print(output)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
