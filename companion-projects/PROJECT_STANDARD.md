# Companion Project Standard

Each companion project should meet this baseline before it is listed as complete.

## Required files

- `README.md` with purpose, inputs, outputs, examples, and safety notes.
- One focused executable script or library entry point.
- A deterministic test file when executable logic exists.

## Engineering requirements

- Prefer Python standard library dependencies.
- Validate inputs and fail with readable messages.
- Avoid network calls unless a future project explicitly documents an authorized defensive need.
- Keep output deterministic where possible.
- Never store credentials, tokens, personal data, or real incident evidence in fixtures.
- Use synthetic fixtures for tests and examples.

## CLI conventions

- Provide `--help`.
- Use non-zero exit status for invalid input or failed verification.
- Write primary results to stdout and diagnostics to stderr when practical.
- Accept explicit file paths instead of silently searching a user's device.

## Documentation conventions

Each README must include:

1. Defensive learning objective.
2. Input format.
3. Output format.
4. Safe example.
5. Limitations.
6. Authorization reminder.

## Review checklist

- [ ] No destructive behavior.
- [ ] No credential theft or collection.
- [ ] No stealth or evasion features.
- [ ] No unauthorized discovery or scanning.
- [ ] No paid-book manuscript content.
- [ ] Synthetic examples only.
- [ ] Tests cover normal and invalid input paths.
