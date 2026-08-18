# The Journey of Ethical Hacking — Companion Resources

Official defensive, authorization-first companion repository for **The Journey of Ethical Hacking — 2026 Edition**.

**Author:** Ram Sandesh  
**Repository:** https://github.com/sanskarIN/The-Journey-of-Ethical-Hacking  
**Contact:** sanskarin@outlook.in

## Quick navigation

- [Complete 200-part learning index](resources/learning_stage_index.md)
- [Synthetic dataset catalog](datasets/README.md)
- [Offline analysis examples](docs/OFFLINE_ANALYSIS_EXAMPLES.md)
- [Documentation accessibility guide](docs/ACCESSIBILITY.md)
- [Book errata log](ERRATA.md)
- [Errata review process](docs/ERRATA_PROCESS.md)
- [Safe contribution guide](CONTRIBUTING.md)
- [Responsible-use and security policy](SECURITY.md)
- [Repository roadmap](ROADMAP.md)
- [Detailed change audit](what_changed.md)

## What this repository contains

This public repository is for safe companion material: synthetic datasets, offline labs, checklists, templates, defensive examples, learning-roadmap files, local analysis helpers, unit tests, and contribution documentation.

### Learning resources

The series index is split into **20 stages covering Parts 1–200**, with exact corrected part titles and safe companion-practice guidance for every stage.

### Synthetic datasets

The repository contains small fictional datasets for asset posture, control evidence, risk signals, cloud posture, privacy controls, endpoint fleets, SaaS governance, resilience exercises, governance controls, and workforce capability.

### Offline utilities

Current Python helpers are intentionally local-only:

- `tools/risk_priority.py`
- `tools/evidence_freshness.py`
- `tools/control_review.py`
- `tools/csv_quality.py`
- `tools/doc_accessibility.py`

Run the test suite with:

```bash
python -m pytest -q
```

Run the repository data/documentation checks with:

```bash
python tools/csv_quality.py datasets/*.csv
python tools/doc_accessibility.py README.md docs resources
```

## Safety boundary

Use these resources only for lawful, authorized, defensive learning. The repository intentionally excludes credential attacks, malware, stealth/evasion, unauthorized scanning, destructive actions, instructions for bypassing security controls, and sensitive real-world target data.

## Licensing

- Companion source code and files explicitly covered by the repository license: **Apache License 2.0**.
- Book manuscript, publication PDF/EPUB, cover, diagrams, and commercial publishing assets: **Copyright © 2026 Ram Sandesh. All rights reserved**, unless a specific file explicitly states otherwise.

The paid master manuscript and complete commercial eBook files are intentionally **not** stored in this public repository.

## Publication note

The publication and repository do not use an author avatar/photo. X/Twitter links are intentionally omitted to avoid stale profile information.
