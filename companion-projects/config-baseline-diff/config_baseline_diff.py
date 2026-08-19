#!/usr/bin/env python3
"""Compare two local JSON configuration snapshots for defensive drift review."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def flatten(value: object, prefix: str = "") -> dict[str, object]:
    if isinstance(value, dict):
        result: dict[str, object] = {}
        for key in sorted(value):
            path = f"{prefix}.{key}" if prefix else str(key)
            result.update(flatten(value[key], path))
        return result
    return {prefix or "$": value}


def compare(baseline: object, current: object) -> dict[str, list[str]]:
    before = flatten(baseline)
    after = flatten(current)
    before_keys = set(before)
    after_keys = set(after)
    changed = sorted(key for key in before_keys & after_keys if before[key] != after[key])
    return {
        "added": sorted(after_keys - before_keys),
        "removed": sorted(before_keys - after_keys),
        "changed": changed,
    }


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare two local JSON configuration snapshots.")
    parser.add_argument("baseline", type=Path)
    parser.add_argument("current", type=Path)
    args = parser.parse_args()

    try:
        result = compare(load_json(args.baseline), load_json(args.current))
    except (OSError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if any(result.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
