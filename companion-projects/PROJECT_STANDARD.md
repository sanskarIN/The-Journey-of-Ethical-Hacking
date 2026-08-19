# Companion Project Standard

Each companion project must meet this baseline before it is listed as complete.

## Required files

- `README.md` beginning with a level-1 heading and documenting purpose, inputs, outputs, examples, limitations, and safety scope.
- At least one focused executable Python script or library entry point.
- At least one deterministic project-owned test file.

The suite-level validator enforces these minimum files for every current project.

## Engineering requirements

- Prefer Python standard library dependencies.
- Validate inputs and fail with readable messages.
- Keep the current suite offline; do not add network calls or live-target discovery.
- Keep output deterministic where possible.
- Use explicit input paths instead of silently searching a user's device.
- Recursive filesystem tools should avoid following symbolic links outside the explicitly selected tree.
- Never store credentials, tokens, personal data, buyer data, or real incident evidence in fixtures.
- Use synthetic fixtures for tests and examples.

## CLI conventions

Follow `CLI_CONTRACT.md`.

At minimum:

- provide `--help` with successful exit and `usage:` output;
- use clear non-zero status for invalid input or failed verification where appropriate;
- write primary results to stdout and diagnostics to stderr when practical;
- accept explicit local file/directory paths;
- avoid stack traces for ordinary rejected user input when a concise CLI error is sufficient.

The repository pytest suite smoke-tests every discovered companion-project CLI with a timeout.

## Test conventions

Follow `TESTING.md`.

Each project should cover:

1. A normal valid-input path.
2. At least one malformed/invalid-input path.
3. Deterministic results or findings.
4. Relevant boundary behavior such as dates/timezones, recursive path handling, policy validation, or numeric ranges.

The project is not complete until the applicable compilation, pytest, project-owned test, suite structure, and repository-health gates succeed.

## Documentation conventions

Each project README should include:

1. Defensive learning objective.
2. Input format.
3. Output format.
4. Safe example.
5. Limitations.
6. Authorization reminder.

The suite catalog (`README.md`) must list every project slug, and `PROJECT_MATRIX.md` must contain one row per current project. Current matrix rows remain marked network access `No` and tests `Yes`.

## Review checklist

- [ ] No destructive behavior.
- [ ] No credential theft or collection.
- [ ] No stealth or evasion features.
- [ ] No unauthorized discovery or scanning.
- [ ] No network access in the current suite.
- [ ] No paid-book manuscript content.
- [ ] Synthetic examples only.
- [ ] README begins with `# `.
- [ ] Suite README catalog contains the project slug.
- [ ] Project matrix contains exactly one current project row.
- [ ] Tests cover normal and invalid input paths.
- [ ] `python -m compileall -q tools tests companion-projects` succeeds.
- [ ] `python companion-projects/run_tests.py` succeeds.
- [ ] `python tools/companion_projects_check.py --root .` succeeds.
