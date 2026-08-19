#!/usr/bin/env python3
"""Audit explicit local permission assignments against a JSON policy."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

REQUIRED_COLUMNS = {"principal", "resource", "permission"}


def load_policy(path: Path) -> dict[str, set[str]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not payload:
        raise ValueError("policy must be a non-empty object mapping resources to permission lists")
    policy: dict[str, set[str]] = {}
    for resource, permissions in payload.items():
        if not isinstance(resource, str) or not resource.strip():
            raise ValueError("policy resource names must be non-empty strings")
        if not isinstance(permissions, list) or not permissions:
            raise ValueError(f"policy resource {resource!r} must have a non-empty permission list")
        if not all(isinstance(permission, str) and permission.strip() for permission in permissions):
            raise ValueError(f"policy resource {resource!r} contains an invalid permission")
        policy[resource.strip()] = {permission.strip().lower() for permission in permissions}
    return policy


def audit(assignments: Path, policy: dict[str, set[str]]) -> dict[str, object]:
    violations: list[dict[str, str]] = []
    total = 0

    with assignments.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
            missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames or []))
            raise ValueError(f"missing required CSV columns: {', '.join(missing)}")

        for line_number, row in enumerate(reader, start=2):
            principal = (row.get("principal") or "").strip()
            resource = (row.get("resource") or "").strip()
            permission = (row.get("permission") or "").strip().lower()
            if not principal or not resource or not permission:
                raise ValueError(f"line {line_number}: fields must not be empty")
            total += 1
            allowed = policy.get(resource)
            if allowed is None:
                violations.append(
                    {"principal": principal, "resource": resource, "permission": permission, "reason": "unknown-resource"}
                )
            elif permission not in allowed:
                violations.append(
                    {"principal": principal, "resource": resource, "permission": permission, "reason": "unapproved-permission"}
                )

    return {"assignments": total, "violations": violations}


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit local permission assignments against an explicit JSON policy.")
    parser.add_argument("assignments_csv", type=Path)
    parser.add_argument("policy_json", type=Path)
    args = parser.parse_args()

    try:
        result = audit(args.assignments_csv, load_policy(args.policy_json))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result["violations"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
