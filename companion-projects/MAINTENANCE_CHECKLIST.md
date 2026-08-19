# Companion Projects Maintenance Checklist

Use this checklist when adding, changing, or reviewing a companion project.

## Before changing code

- [ ] Confirm the learning objective is defensive and authorization-first.
- [ ] Confirm the project can remain local/offline.
- [ ] Use synthetic data for examples and tests.
- [ ] Avoid credentials, private incident data, buyer information, and paid manuscript content.

## Project structure

- [ ] Keep a project-specific `README.md`.
- [ ] Keep at least one focused Python implementation.
- [ ] Keep at least one deterministic unit-test file.
- [ ] Document input format and output format.
- [ ] Document limitations and authorization scope.

## Implementation review

- [ ] Validate all externally supplied fields.
- [ ] Use explicit local paths rather than automatic discovery.
- [ ] Avoid following symbolic links when recursively reading user-selected directories.
- [ ] Return non-zero status for failed verification or invalid input where appropriate.
- [ ] Keep output deterministic where practical.
- [ ] Remove unused imports and dead code.

## Documentation review

- [ ] Update `README.md` when behavior changes.
- [ ] Update `PROJECT_MATRIX.md` when adding a project.
- [ ] Update `CHANGELOG.md` for meaningful suite changes.
- [ ] Update `ROADMAP.md` when a planned item is completed or replaced.
- [ ] Keep Markdown links relative when linking repository files.

## Validation

- [ ] Run `python companion-projects/run_tests.py`.
- [ ] Run `python tools/companion_projects_check.py --root .`.
- [ ] Run `python tools/repo_health.py --root .`.
- [ ] Confirm the main CI workflow includes the suite.

## Release boundary

- [ ] Do not add commercial manuscript or publication-delivery files.
- [ ] Do not add real secrets, tokens, credentials, or private evidence.
- [ ] Do not add exploit, persistence, evasion, destructive, or unauthorized scanning behavior.
