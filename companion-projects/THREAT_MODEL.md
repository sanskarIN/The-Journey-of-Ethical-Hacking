# Companion Projects Threat Model

This threat model defines risks the companion-project suite should actively avoid.

## Assets to protect

- User files supplied as explicit inputs.
- Private incident data.
- Credentials and secrets.
- Paid book content.
- Repository integrity and contributor trust.

## Trust boundaries

The tools should treat every input file as untrusted data. They should not assume CSV, JSON, JSONL, Markdown, or saved header files are well formed.

## Primary risks

### Accidental disclosure

A user may publish real logs or secrets while demonstrating a tool.

**Controls:** synthetic-data guidance, redaction tooling, public-repository boundary policy, documentation reminders.

### Unexpected filesystem access

A utility could read more of a device than the user intended.

**Controls:** explicit path arguments, no implicit home-directory crawling, no automatic discovery, clear scope documentation.

### Network side effects

A parser could evolve into a tool that contacts external services or live targets.

**Controls:** offline-by-default project standard and matrix-level `Network access: No` requirement.

### Unsafe feature drift

A defensive project could gain exploit, stealth, persistence, credential-collection, or unauthorized scanning features.

**Controls:** contribution rules, safety boundary, review checklist, and narrow project purposes.

### Untrusted input crashes

Malformed data could make tools fail unpredictably.

**Controls:** validation, readable errors, deterministic tests, and non-zero exit codes for failed verification.

## Non-goals

The companion suite is not a penetration-testing framework, exploit collection, malware toolkit, credential-testing system, network scanner, or live target reconnaissance suite.

## Review trigger

Update this threat model whenever a project proposes network access, automatic discovery, external integrations, write access to user data, or a new data type with materially different privacy risk.
