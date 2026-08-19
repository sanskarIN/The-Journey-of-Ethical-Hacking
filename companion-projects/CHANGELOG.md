# Companion Projects Changelog

This changelog tracks the dedicated `companion-projects/` suite separately from the repository-wide `CHANGELOG.md`.

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
