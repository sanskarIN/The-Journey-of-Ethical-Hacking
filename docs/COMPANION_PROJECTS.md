# Defensive Companion Project Suite

The repository includes a dedicated `companion-projects/` collection of small, offline, authorization-first Python projects that extend the learning experience without publishing the paid manuscript.

## Current milestone

**16 complete projects**, each with:

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

### Integrity and resilience

- Integrity Manifest
- Backup Verify
- Configuration Baseline Diff

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

## Run all companion tests

```bash
python companion-projects/run_tests.py
```

List discovered companion tests without executing them:

```bash
python companion-projects/run_tests.py --list
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
- `companion-projects/ROADMAP.md`

## Public/commercial boundary

The companion suite is open companion code and documentation under the repository's applicable license. The paid complete book manuscript and commercial publication files remain outside the public repository.

## Official book storefront

[Get **The Journey of Ethical Hacking** on Gumroad](https://ramsandesh.gumroad.com)
