#!/usr/bin/env python3
"""Create and verify local SHA-256 file-integrity manifests."""

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


def inventory(root: Path) -> dict[str, dict[str, object]]:
    if not root.is_dir():
        raise ValueError(f"not a directory: {root}")
    result: dict[str, dict[str, object]] = {}
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        relative = path.relative_to(root).as_posix()
        result[relative] = {
            "size": path.stat().st_size,
            "sha256": sha256_file(path),
        }
    return result


def create_manifest(root: Path, output: Path) -> None:
    payload = {"algorithm": "sha256", "files": inventory(root)}
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def verify_manifest(root: Path, manifest_path: Path) -> dict[str, list[str]]:
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    if payload.get("algorithm") != "sha256" or not isinstance(payload.get("files"), dict):
        raise ValueError("unsupported or invalid manifest")

    expected = payload["files"]
    current = inventory(root)
    expected_paths = set(expected)
    current_paths = set(current)

    missing = sorted(expected_paths - current_paths)
    unexpected = sorted(current_paths - expected_paths)
    changed = sorted(
        path
        for path in expected_paths & current_paths
        if expected[path] != current[path]
    )
    ok = sorted((expected_paths & current_paths) - set(changed))
    return {"ok": ok, "missing": missing, "changed": changed, "unexpected": unexpected}


def main() -> int:
    parser = argparse.ArgumentParser(description="Create or verify a local SHA-256 integrity manifest.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create", help="Create a manifest")
    create_parser.add_argument("root", type=Path)
    create_parser.add_argument("manifest", type=Path)

    verify_parser = subparsers.add_parser("verify", help="Verify a manifest")
    verify_parser.add_argument("root", type=Path)
    verify_parser.add_argument("manifest", type=Path)

    args = parser.parse_args()
    try:
        if args.command == "create":
            create_manifest(args.root, args.manifest)
            return 0
        result = verify_manifest(args.root, args.manifest)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result["missing"] or result["changed"] or result["unexpected"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
