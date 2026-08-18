# The Journey of Ethical Hacking — Companion Resources

Official defensive, authorization-first companion repository for **The Journey of Ethical Hacking — 2026 Edition**.

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Author:** Ram Sandesh  
**Repository:** https://github.com/sanskarIN/The-Journey-of-Ethical-Hacking  
**Official Gumroad:** https://ramsandesh.gumroad.com  
**Contact:** sanskarin@outlook.in

## Quick navigation

- [Get the book on Gumroad](https://ramsandesh.gumroad.com)
- [Complete documentation index](docs/INDEX.md)
- [Gumroad storefront and badge guide](docs/GUMROAD.md)
- [Complete 200-part learning index](resources/learning_stage_index.md)
- [Synthetic dataset catalog](datasets/README.md)
- [Dataset contract schemas](schemas/README.md)
- [Fictional tabletop exercises](exercises/README.md)
- [Worked synthetic-dataset contribution example](examples/new_dataset_contribution/README.md)
- [Offline analysis examples](docs/OFFLINE_ANALYSIS_EXAMPLES.md)
- [Documentation accessibility guide](docs/ACCESSIBILITY.md)
- [Companion resource style guide](docs/RESOURCE_STYLE_GUIDE.md)
- [Public release checklist](docs/RELEASE_CHECKLIST.md)
- [Release snapshot](docs/RELEASE_SNAPSHOT.md)
- [Annual edition maintenance](docs/ANNUAL_EDITION_MAINTENANCE.md)
- [Book errata log](ERRATA.md)
- [Safe contribution guide](CONTRIBUTING.md)
- [Responsible-use and security policy](SECURITY.md)
- [Repository roadmap](ROADMAP.md)
- [Detailed change audit](what_changed.md)
- [`COMPANION_RELEASE.json`](COMPANION_RELEASE.json) — machine-readable release metadata

## What this repository contains

This public repository contains safe companion material: synthetic datasets, offline labs, checklists, templates, defensive examples, learning-roadmap files, local analysis helpers, validation tools, unit/CLI tests, fictional tabletop exercises, and contribution/release documentation.

### Learning resources

The series index is split into **20 stages covering Parts 1–200**, with corrected part titles and safe companion-practice guidance for every stage.

### Synthetic datasets

The repository contains small fictional datasets for asset posture, control evidence, risk signals, cloud posture, privacy controls, endpoint fleets, SaaS governance, resilience exercises, governance controls, and workforce capability. Machine-readable contracts under `schemas/` define expected columns.

### Offline utilities

Current local-only Python helpers include:

- `tools/risk_priority.py`
- `tools/evidence_freshness.py`
- `tools/control_review.py`
- `tools/dataset_summary.py`
- `tools/csv_quality.py`
- `tools/dataset_contracts.py`
- `tools/json_metadata.py`
- `tools/synthetic_safety.py`
- `tools/doc_accessibility.py`
- `tools/markdown_links.py`
- `tools/gumroad_presence.py`
- `tools/resource_manifest.py`
- `tools/repo_health.py`

Run the test suite with coverage reporting:

```bash
python -m pytest --cov=tools --cov-report=term-missing -q
```

Run all repository structural checks from one entry point:

```bash
python tools/repo_health.py --root .
```

Generate a machine-readable public-resource manifest:

```bash
python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json
```

## Release integrity

The repository CI and local health tooling validate:

- synthetic CSV structure;
- dataset contracts;
- release/schema JSON metadata;
- sensitive-looking values in public synthetic datasets;
- Markdown accessibility basics;
- relative Markdown links;
- the exact official Gumroad storefront URL on core public-facing pages;
- public-resource manifest generation;
- unit tests, CLI smoke tests, and test coverage.

## Safety boundary

Use these resources only for lawful, authorized, defensive learning. The repository intentionally excludes credential attacks, malware, stealth/evasion, unauthorized scanning, destructive actions, instructions for bypassing security controls, and sensitive real-world target data.

## Licensing

- Companion source code and files explicitly covered by the repository license: **Apache License 2.0**.
- Book manuscript, publication PDF/EPUB, cover, diagrams, certificates, and commercial publishing assets: **Copyright © 2026 Ram Sandesh. All rights reserved**, unless a specific file explicitly states otherwise.

The paid master manuscript and complete commercial eBook files are intentionally **not** stored in this public repository.

## Official book storefront

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Direct link:** https://ramsandesh.gumroad.com

## Publication note

The publication and repository do not use an author avatar/photo/person image. X/Twitter links are intentionally omitted to avoid stale profile information.
