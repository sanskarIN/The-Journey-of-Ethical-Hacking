#!/usr/bin/env python3
"""Build a local Markdown incident timeline from JSONL events."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

REQUIRED = {"timestamp", "category", "summary", "asset"}


def parse_timestamp(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        return datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValueError(f"invalid ISO 8601 timestamp: {value!r}") from exc


def load_events(path: Path) -> list[dict[str, str]]:
    events: list[dict[str, str]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            item = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"line {line_number}: invalid JSON") from exc
        if not isinstance(item, dict) or not REQUIRED.issubset(item):
            raise ValueError(f"line {line_number}: missing required fields")
        event = {key: str(item[key]).strip() for key in REQUIRED}
        if any(not value for value in event.values()):
            raise ValueError(f"line {line_number}: fields must not be empty")
        parse_timestamp(event["timestamp"])
        events.append(event)
    return sorted(events, key=lambda event: parse_timestamp(event["timestamp"]))


def render_markdown(events: list[dict[str, str]]) -> str:
    lines = ["# Incident Timeline", "", "| Timestamp | Category | Asset | Summary |", "|---|---|---|---|"]
    for event in events:
        safe = {key: value.replace("|", "\\|").replace("\n", " ") for key, value in event.items()}
        lines.append(
            f"| {safe['timestamp']} | {safe['category']} | {safe['asset']} | {safe['summary']} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a Markdown timeline from local JSONL incident events.")
    parser.add_argument("events_file", type=Path)
    parser.add_argument("--output", type=Path, help="Optional output Markdown path")
    args = parser.parse_args()

    try:
        markdown = render_markdown(load_events(args.events_file))
        if args.output:
            args.output.write_text(markdown, encoding="utf-8")
        else:
            print(markdown, end="")
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
