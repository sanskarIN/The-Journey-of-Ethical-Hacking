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

## Run all companion tests

```bash
python companion-projects/run_tests.py
```

List discovered companion tests without executing them:

```bash
python companion-projects/run_tests.py --list
```

Validate project structure and the 20-project floor:

```bash
python tools/companion_projects_check.py --root .
```

## Suite documentation

- `companion-projects/README.md`
- `companion-projects/PROJECT_MATRIX.md`
- `companion-projects/PROJECT_STANDARD.md`
- `companion-projects/ARCHITECTURE.md`
- `companion-projects/SAFETY.md`
- `companion-projects/THREAT_MODEL.md`
- `companion-projects/SYNTHETIC_DATA_GUIDE.md`
- `companion-projects/CONTRIBUTING.md`
- `companion-projects/MAINTENANCE_CHECKLIST.md`
- `companion-projects/CHANGELOG.md`
- `companion-projects/ROADMAP.md`

## Public/commercial boundary

The companion suite is open companion code and documentation under the repository's applicable license. The paid complete book manuscript and commercial publication files remain outside the public repository.

## Official book storefront

[Get **The Journey of Ethical Hacking** on Gumroad](https://ramsandesh.gumroad.com)
