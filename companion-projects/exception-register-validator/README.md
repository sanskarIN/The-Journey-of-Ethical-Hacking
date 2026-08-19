# Exception Register Validator

Validate a local governance/security exception register and identify expired or unapproved records as of an explicit date.

## Input format

```text
exception_id,owner,expires_on,rationale,approved
EX-001,alex,2026-09-30,Training exception,true
```

Dates use `YYYY-MM-DD`. Approval accepts common true/false values.

## Usage

```bash
python companion-projects/exception-register-validator/exception_register_validator.py exceptions.csv --as-of 2026-08-19
```

## Learning objective

Practice exception-governance hygiene, expiry review, ownership validation, and explicit approval tracking.

## Scope

This utility is read-only and advisory. It does not connect to ticketing systems, modify exceptions, or change security controls.

Use synthetic records or exports you are authorized to review.
