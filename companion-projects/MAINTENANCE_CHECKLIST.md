# Companion Projects Maintenance Checklist

Use this checklist when adding, changing, or reviewing a companion project.

## Before changing code

- [ ] Confirm the learning objective is defensive and authorization-first.
- [ ] Confirm the project can remain local/offline.
- [ ] Use synthetic data for examples and tests.
- [ ] Avoid credentials, private incident data, buyer information, and paid manuscript content.

## Project structure

- [ ] Keep a project-specific `README.md` beginning with a level-1 heading.
- [ ] Keep at least one focused Python implementation.
- [ ] Keep at least one deterministic unit-test file.
- [ ] Document input format and output format.
- [ ] Document limitations and authorization scope.
- [ ] Keep the project slug listed in `README.md`.
- [ ] Keep exactly one corresponding row in `PROJECT_MATRIX.md`.
- [ ] Keep current matrix rows marked network access `No` and tests `Yes`.

## CLI contract

- [ ] Follow `CLI_CONTRACT.md` for explicit local inputs, help behavior, deterministic output, and exit status conventions.
- [ ] Ensure `--help` exits successfully and includes `usage:`.
- [ ] Use readable `argparse` errors for ordinary invalid input when appropriate.
- [ ] Keep output ordering deterministic where practical.
- [ ] Do not add implicit device discovery or network access to the current suite.

## Implementation review

- [ ] Validate all externally supplied fields.
- [ ] Use explicit local paths rather than automatic discovery.
- [ ] Avoid following symbolic links when recursively reading user-selected directories.
- [ ] Return non-zero status for failed verification or review findings where the project contract calls for it.
- [ ] Keep output deterministic where practical.
- [ ] Remove unused imports and dead code.

## Tests

- [ ] Add or update a normal valid-input test.
- [ ] Add or update at least one malformed/invalid-input test.
- [ ] Add boundary regression tests for dates, timezones, recursive paths, policies, or similar project-specific constraints when relevant.
- [ ] Keep fixtures synthetic and free of secrets/private evidence.
- [ ] Review `TESTING.md` when changing the suite-level test model.

## Documentation review

- [ ] Update `README.md` when behavior changes.
- [ ] Update `PROJECT_MATRIX.md` when adding/removing a project.
- [ ] Update `CLI_CONTRACT.md` if shared CLI behavior changes.
- [ ] Update `TESTING.md` if validation commands change.
- [ ] Update `CHANGELOG.md` for meaningful suite changes.
- [ ] Update `ROADMAP.md` when a planned item is completed or replaced.
- [ ] Keep Markdown links relative when linking repository files.

## Validation

Run the full local sequence:

```bash
python -m compileall -q tools tests companion-projects
python -m pytest --cov=tools --cov-report=term-missing -q
python companion-projects/run_tests.py
python tools/companion_projects_check.py --root .
python tools/repo_health.py --root .
```

Then confirm:

- [ ] Compilation succeeds.
- [ ] Main pytest/coverage and CLI smoke tests succeed.
- [ ] All project-owned tests succeed.
- [ ] The suite validator reports at least 20 valid projects.
- [ ] Main CI includes compilation, project tests, and suite validation.
- [ ] Release-candidate CI includes the same core quality gates.
- [ ] Tagged-release CI includes the same core quality gates.

## Release boundary

- [ ] `COMPANION_RELEASE.json` continues to record `companion_projects: 20` unless a deliberate future milestone updates the project floor and all synchronized documentation/tests.
- [ ] `companion_projects_offline` remains `true` for the current suite.
- [ ] Do not add commercial manuscript or publication-delivery files.
- [ ] Do not add real secrets, tokens, credentials, or private evidence.
- [ ] Do not add exploit, persistence, evasion, destructive, or unauthorized scanning behavior.
