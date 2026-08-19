# Companion Projects Changelog

This changelog tracks the dedicated `companion-projects/` suite separately from the repository-wide `CHANGELOG.md`.

## 2026-08-19 — Final engineering hardening

### Added

- `CLI_CONTRACT.md` with shared input, output, exit-status, validation, determinism, privacy, and safety conventions.
- `TESTING.md` with compilation, pytest, project-owned test, suite validation, and repository-health commands.

### Improved

- The structure validator now checks the README catalog against actual project directories.
- The validator checks that the project matrix has exactly one row per current project.
- Current matrix rows must remain marked offline (`No`) and tested (`Yes`).
- Every project README must begin with a level-1 heading.
- Python source compilation is part of normal CI and repository health.
- Main CLI smoke tests now cover every discovered companion-project implementation with a timeout.
- Generated policy status now includes companion-project suite integrity.
- Machine-readable release metadata records 20 current companion projects and offline scope.
- Manual release-candidate and tagged-release workflows run compilation, pytest, project-owned tests, and suite validation.
- Release-readiness validation requires those workflow quality gates to remain present.
- Active release metadata moved to `2026.08.19.1`; the earlier `2026.08.18.6` release branch remains historical evidence.

## 2026-08-19 — Expanded to 20 projects

### Added projects

17. Control Evidence Mapper
18. Exception Register Validator
19. Patch Register Summary
20. Recovery Exercise Reporter

### Improved

- Raised the repository structure-validator floor from 16 to 20 projects.
- Expanded the project matrix and reader-facing catalogs to the 20-project milestone.
- Kept all four new projects read-only/offline and based on explicit local exports or fictional tabletop data.

## 2026-08-19 — Initial 16-project suite

### Added projects

1. Log Sifter
2. Integrity Manifest
3. IOC Normalizer
4. Incident Timeline Builder
5. Header Safety Report
6. Secrets Redactor
7. Evidence Inventory
8. Access Review Helper
9. Configuration Baseline Diff
10. Asset Inventory Summary
11. Security Checklist Tracker
12. Backup Verify
13. JSONL Event Validator
14. Data Retention Planner
15. Change Review Notes
16. Permission Matrix Auditor

Each project includes a project README, focused Python implementation, and deterministic unit tests.

### Added suite engineering

- `PROJECT_MATRIX.md`
- `PROJECT_STANDARD.md`
- `ARCHITECTURE.md`
- `SAFETY.md`
- `THREAT_MODEL.md`
- `SYNTHETIC_DATA_GUIDE.md`
- `CONTRIBUTING.md`
- `ROADMAP.md`
- `CHANGELOG.md`
- `MAINTENANCE_CHECKLIST.md`
- `run_tests.py`

### Repository integration

- Added a repository-level companion project structure validator.
- Added companion-project tests and structure validation to CI.
- Added companion-project accessibility and relative-link checks.
- Added companion-suite checks to the consolidated repository-health command.
- Added suite navigation to the repository README and documentation index.

### Hardening

- Incident timeline timestamps must include timezone information.
- Access-review policies reject an empty approved-role list.
- Integrity Manifest ignores symbolic links when walking explicit local directories.
- Evidence Inventory ignores symbolic links when walking explicit local directories.
- Backup Verify ignores symbolic links when walking explicit local directories.
- Removed an unused import from IOC Normalizer.

### Safety boundary

The suite remains local/offline and authorization-first. It intentionally excludes exploit delivery, credential theft, malware behavior, persistence, evasion, destructive actions, live-target discovery, and unauthorized scanning.

The commercial book manuscript and paid publication files remain outside the public companion repository.
