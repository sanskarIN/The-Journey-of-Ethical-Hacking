#!/usr/bin/env python3
"""Compare local account exports with an approved-role policy."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

REQUIRED_COLUMNS = {"account", "role", "enabled"}
TRUE_VALUES = {"true", "1", "yes"}
FALSE_VALUES = {"false", "0", "no"}


def load_policy(path: Path) -> set[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    roles = payload.get("approved_roles") if isinstance(payload, dict) else None
    if (
        not isinstance(roles, list)
        or not roles
        or not all(isinstance(role, str) and role.strip() for role in roles)
    ):
        raise ValueError("policy must contain a non-empty string list named approved_roles")
    return {role.strip().lower() for role in roles}


def parse_enabled(value: str, line_number: int) -> bool:
    normalized = value.strip().lower()
    if normalized in TRUE_VALUES:
        return True
    if normalized in FALSE_VALUES:
        return False
    raise ValueError(f"line {line_number}: invalid enabled value {value!r}")


def review(accounts_path: Path, approved_roles: set[str]) -> dict[str, object]:
    violations: list[dict[str, object]] = []
    total = 0
    enabled_count = 0

    with accounts_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames or []))
            raise ValueError(f"missing required CSV columns: {', '.join(missing)}")

        for line_number, row in enumerate(reader, start=2):
            account = (row.get("account") or "").strip()
            role = (row.get("role") or "").strip().lower()
            if not account or not role:
                raise ValueError(f"line {line_number}: account and role must not be empty")
            enabled = parse_enabled(row.get("enabled") or "", line_number)
            total += 1
            enabled_count += int(enabled)
            if role not in approved_roles:
                violations.append({"account": account, "role": role, "enabled": enabled, "reason": "unapproved-role"})

    return {
        "accounts": total,
        "enabled_accounts": enabled_count,
        "violations": violations,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Review a local account CSV against an approved-role policy.")
    parser.add_argument("accounts_csv", type=Path)
    parser.add_argument("policy_json", type=Path)
    args = parser.parse_args()

    try:
        result = review(args.accounts_csv, load_policy(args.policy_json))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result["violations"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
