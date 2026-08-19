# Contributing to Companion Projects

Contributions are welcome when they strengthen defensive learning and preserve the repository's authorization-first boundary.

## Good contributions

- Input validation improvements.
- Better deterministic tests.
- Accessibility and documentation improvements.
- Safer synthetic fixtures.
- Local parsers for defensive data formats.
- Read-only governance and audit helpers.
- Reliability, portability, and error-message improvements.

## Contributions that do not fit this directory

Do not add code for unauthorized discovery, credential collection, exploit delivery, malware behavior, persistence, evasion, destructive actions, stealth, or scanning third-party systems.

## Project proposal checklist

Before adding a new project, document:

1. Defensive learning objective.
2. Exact local input format.
3. Exact output format.
4. Why network access is unnecessary, or a strong defensive justification if a future design proposes it.
5. Synthetic test strategy.
6. Privacy and authorization limitations.

## Testing

Run:

```bash
python companion-projects/run_tests.py
```

Every new executable project should add at least one normal-path test and one validation/error-path test.

## Public repository boundary

Never commit paid manuscript files, buyer information, credentials, tokens, private incident evidence, or real target data.
