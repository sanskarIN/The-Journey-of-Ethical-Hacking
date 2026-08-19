#!/usr/bin/env python3
"""Offline validator and normalizer for defensive indicators."""

from __future__ import annotations

import argparse
import ipaddress
import json
import re
from pathlib import Path

DOMAIN_RE = re.compile(r"^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$", re.IGNORECASE)
HEX_RE = re.compile(r"^[0-9a-fA-F]+$")
HASH_LENGTHS = {32: "md5", 40: "sha1", 64: "sha256"}


def classify(value: str) -> tuple[str, str] | None:
    candidate = value.strip()
    if not candidate:
        return None

    try:
        address = ipaddress.ip_address(candidate)
        return ("ipv4" if address.version == 4 else "ipv6", address.compressed.lower())
    except ValueError:
        pass

    lowered = candidate.rstrip(".").lower()
    if DOMAIN_RE.fullmatch(lowered):
        return "domain", lowered

    if len(candidate) in HASH_LENGTHS and HEX_RE.fullmatch(candidate):
        return HASH_LENGTHS[len(candidate)], candidate.lower()

    return None


def normalize_lines(lines: list[str]) -> dict[str, object]:
    entries: set[tuple[str, str]] = set()
    rejected: list[str] = []

    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        result = classify(stripped)
        if result is None:
            rejected.append(stripped)
        else:
            entries.add(result)

    normalized = [
        {"type": indicator_type, "value": value}
        for indicator_type, value in sorted(entries)
    ]
    return {"indicators": normalized, "rejected": rejected}


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize defensive indicators from a local text file.")
    parser.add_argument("input_file", type=Path)
    args = parser.parse_args()

    try:
        lines = args.input_file.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        parser.error(str(exc))

    print(json.dumps(normalize_lines(lines), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
