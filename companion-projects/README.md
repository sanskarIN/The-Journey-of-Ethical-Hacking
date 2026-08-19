# Defensive Companion Projects

This directory contains small, authorization-first cybersecurity projects that complement **The Journey of Ethical Hacking** without publishing the paid book manuscript.

Every project is designed for local files, synthetic data, owned systems, or explicitly authorized environments. The current suite is intentionally offline and avoids exploit delivery, credential theft, destructive actions, stealth, persistence, or unauthorized scanning.

## Project catalog

1. `log-sifter` — summarize local authentication-style logs.
2. `integrity-manifest` — create and verify SHA-256 file-integrity manifests.
3. `ioc-normalizer` — normalize defensive indicators without network lookups.
4. `incident-timeline` — turn local JSONL events into a sorted incident timeline.
5. `header-safety-report` — inspect saved email headers for authentication signals.
6. `secrets-redactor` — redact common secret-like values from text before sharing logs.
7. `evidence-inventory` — inventory evidence files with metadata and hashes.
8. `access-review-helper` — compare account exports with an approved-role policy.
9. `config-baseline-diff` — compare two local JSON configuration snapshots for drift.
10. `asset-inventory-summary` — summarize an explicit local asset inventory export.
11. `security-checklist-tracker` — measure progress in Markdown defensive checklists.
12. `backup-verify` — compare primary and backup directories with SHA-256 hashes.
13. `jsonl-event-validator` — validate structured defensive event records.
14. `data-retention-planner` — calculate advisory review dates from a local retention register.
15. `change-review-notes` — render local change-control exports as Markdown review notes.
16. `permission-matrix-auditor` — compare local permission assignments with an explicit policy.
17. `control-evidence-mapper` — map local evidence records to recognized defensive controls.
18. `exception-register-validator` — review local governance exceptions for expiry and approval.
19. `patch-register-summary` — summarize an explicit local patch-status export without scanning systems.
20. `recovery-exercise-reporter` — summarize fictional or authorized tabletop recovery exercises.

## Suite documentation

- [`PROJECT_MATRIX.md`](PROJECT_MATRIX.md) — project-by-project feature and test matrix.
- [`PROJECT_STANDARD.md`](PROJECT_STANDARD.md) — required engineering baseline.
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — suite layout and runtime model.
- [`SAFETY.md`](SAFETY.md) — authorization and data-handling boundaries.
- [`THREAT_MODEL.md`](THREAT_MODEL.md) — risks, controls, and non-goals.
- [`SYNTHETIC_DATA_GUIDE.md`](SYNTHETIC_DATA_GUIDE.md) — safe fixture guidance.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution and testing requirements.
- [`MAINTENANCE_CHECKLIST.md`](MAINTENANCE_CHECKLIST.md) — review checklist for future changes.
- [`CHANGELOG.md`](CHANGELOG.md) — dedicated suite history.
- [`ROADMAP.md`](ROADMAP.md) — safe future project ideas and quality work.

## Design rules

- Python standard library only where practical.
- No network access in the current suite.
- Explicit input paths instead of automatic device discovery.
- Deterministic output suitable for tests.
- Clear `--help` output.
- Synthetic examples only.
- Defensive learning outcomes are stated in each project README.

## Quick start

Inspect any project:

```bash
python companion-projects/<project>/<tool>.py --help
```

List every discovered unit-test file:

```bash
python companion-projects/run_tests.py --list
```

Run the complete companion-project test suite:

```bash
python companion-projects/run_tests.py
```

Validate the suite structure:

```bash
python tools/companion_projects_check.py --root .
```

Run only against local data you own or are explicitly authorized to process.
