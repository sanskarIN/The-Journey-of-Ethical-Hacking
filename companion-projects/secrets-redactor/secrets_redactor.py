#!/usr/bin/env python3
"""Redact common secret-like values from local text before sharing."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REPLACEMENT = "[REDACTED]"

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    (
        "bearer",
        re.compile(r"(?i)(\bAuthorization\s*:\s*Bearer\s+)[A-Za-z0-9._~+/=-]+"),
    ),
    (
        "assignment",
        re.compile(
            r"(?im)(\b(?:api[_-]?key|token|secret|password)\b\s*[:=]\s*)(?:['\"]?)[^\s'\";,]+(?:['\"]?)"
        ),
    ),
    (
        "private_key",
        re.compile(
            r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----.*?-----END [A-Z0-9 ]*PRIVATE KEY-----",
            re.DOTALL,
        ),
    ),
]


def redact(text: str) -> tuple[str, dict[str, int]]:
    counts: dict[str, int] = {}
    sanitized = text

    for name, pattern in PATTERNS:
        if name in {"bearer", "assignment"}:
            sanitized, count = pattern.subn(lambda match: match.group(1) + REPLACEMENT, sanitized)
        else:
            sanitized, count = pattern.subn(REPLACEMENT, sanitized)
        counts[name] = count

    return sanitized, counts


def main() -> int:
    parser = argparse.ArgumentParser(description="Redact common secret-like values from a local text file.")
    parser.add_argument("input_file", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        text = args.input_file.read_text(encoding="utf-8")
        sanitized, counts = redact(text)
        if args.output:
            args.output.write_text(sanitized, encoding="utf-8")
        else:
            print(sanitized, end="" if sanitized.endswith("\n") else "\n")
    except OSError as exc:
        parser.error(str(exc))

    total = sum(counts.values())
    print(f"redactions={total}", file=__import__("sys").stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
