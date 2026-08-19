# Defensive Companion Project Suite

The repository includes a dedicated `companion-projects/` collection of small, offline, authorization-first Python projects that extend the learning experience without publishing the paid manuscript.

## Current milestone

**20 complete projects**, each with:

- project-specific README;
- focused Python implementation;
- deterministic unit tests;
- local/offline operation;
- synthetic or explicitly authorized inputs;
- no exploit, credential-collection, persistence, evasion, destructive, or unauthorized scanning behavior.

The machine-readable release metadata also records `companion_projects: 20` and `companion_projects_offline: true`.

## Project families

### Incident and evidence handling

- Log Sifter
- Incident Timeline Builder
- Evidence Inventory
- JSONL Event Validator
- Control Evidence Mapper

### Integrity and resilience

- Integrity Manifest
- Backup Verify
- Configuration Baseline Diff
- Recovery Exercise Reporter

### Data hygiene and privacy

- IOC Normalizer
- Secrets Redactor
- Header Safety Report

### Governance and access review

- Access Review Helper
- Asset Inventory Summary
- Security Checklist Tracker
- Data Retention Planner
- Change Review Notes
- Permission Matrix Auditor
- Exception Register Validator
- Patch Register Summary

## Validation workflow

Compile all Python sources first:

```bash
python -m compileall -q tools tests companion-projects
```

Run the repository pytest suite, including CLI smoke tests:

```bash
python -m pytest --cov=tools --cov-report=term-missing -q
```

Run all project-owned tests:

```bash
python companion-projects/run_tests.py
```

List discovered companion tests without executing them:

```bash
python companion-projects/run_tests.py --list
```

Validate project structure, the 20-project floor, catalog/matrix synchronization, and offline/tested project status:

```bash
python tools/companion_projects_check.py --root .
```

Run the complete structural/policy gate:

```bash
python tools/repo_health.py --root .
```

## Suite documentation

- `companion-projects/README.md`
- `companion-projects/PROJECT_MATRIX.md`
- `companion-projects/PROJECT_STANDARD.md`
- `companion-projects/ARCHITECTURE.md`
- `companion-projects/CLI_CONTRACT.md`
- `companion-projects/TESTING.md`
- `companion-projects/SAFETY.md`
- `companion-projects/THREAT_MODEL.md`
- `companion-projects/SYNTHETIC_DATA_GUIDE.md`
- `companion-projects/CONTRIBUTING.md`
- `companion-projects/MAINTENANCE_CHECKLIST.md`
- `companion-projects/CHANGELOG.md`
- `companion-projects/ROADMAP.md`

## Automated integrity rules

The suite validator requires:

- at least 20 project directories;
- all required suite-level documentation;
- a README catalog entry for every project slug;
- exactly one project-matrix row per current project directory;
- current matrix rows to remain marked `Network access: No` and `Tests: Yes`;
- a level-1 heading in every project README;
- at least one implementation and one project-owned test file for every project.

Normal CI, manual release-candidate CI, and tagged-release CI all compile the Python sources and run the strengthened project/test gates.

## Public/commercial boundary

The companion suite is open companion code and documentation under the repository's applicable license. The paid complete book manuscript and commercial publication files remain outside the public repository.

## Official book storefront

[Get **The Journey of Ethical Hacking** on Gumroad](https://ramsandesh.gumroad.com)
