# Access Review Helper

Compare a local account export against an approved-role policy to support defensive identity and access-management exercises.

## Learning objective

Practice least-privilege review, deterministic policy checks, and structured reporting.

## Accounts CSV

```text
account,role,enabled
alex,reader,true
casey,admin,false
```

## Policy JSON

```json
{"approved_roles":["reader","analyst","admin"]}
```

## Usage

```bash
python companion-projects/access-review-helper/access_review_helper.py accounts.csv policy.json
```

The report identifies rows with roles that are not listed in the approved policy and validates boolean account status values.

## Scope

This tool only processes explicit local exports. It does not connect to identity providers, change permissions, authenticate as users, or discover accounts.

Use synthetic data or exports you are authorized to review.
