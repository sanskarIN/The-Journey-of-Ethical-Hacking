#!/usr/bin/env python3
"""Create a local defensive report from saved email headers."""

from __future__ import annotations

import argparse
import json
import re
from email import policy
from email.parser import Parser
from email.utils import parseaddr
from pathlib import Path

AUTH_RESULTS = {"spf", "dkim", "dmarc"}


def address_domain(value: str | None) -> str | None:
    if not value:
        return None
    _, address = parseaddr(value)
    if "@" not in address:
        return None
    return address.rsplit("@", 1)[1].lower()


def auth_status(message, mechanism: str) -> str:
    statuses: list[str] = []
    pattern = re.compile(rf"\b{re.escape(mechanism)}\s*=\s*([a-zA-Z0-9_-]+)", re.IGNORECASE)
    for header in message.get_all("Authentication-Results", []):
        statuses.extend(match.group(1).lower() for match in pattern.finditer(str(header)))
    if not statuses:
        return "not-found"
    if "fail" in statuses:
        return "fail"
    if "pass" in statuses:
        return "pass"
    return statuses[0]


def analyze(text: str) -> dict[str, object]:
    message = Parser(policy=policy.default).parsestr(text, headersonly=True)
    from_value = message.get("From")
    reply_to = message.get("Reply-To")
    return_path = message.get("Return-Path")

    from_domain = address_domain(str(from_value) if from_value else None)
    reply_domain = address_domain(str(reply_to) if reply_to else None)

    return {
        "from": str(from_value) if from_value else None,
        "reply_to": str(reply_to) if reply_to else None,
        "return_path": str(return_path) if return_path else None,
        "received_hops": len(message.get_all("Received", [])),
        "authentication": {name: auth_status(message, name) for name in sorted(AUTH_RESULTS)},
        "from_reply_domain_mismatch": bool(from_domain and reply_domain and from_domain != reply_domain),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze a saved email header file locally.")
    parser.add_argument("header_file", type=Path)
    args = parser.parse_args()

    try:
        text = args.header_file.read_text(encoding="utf-8")
    except OSError as exc:
        parser.error(str(exc))

    print(json.dumps(analyze(text), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
