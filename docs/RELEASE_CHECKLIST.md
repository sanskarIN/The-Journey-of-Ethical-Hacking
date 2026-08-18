# Companion Resource Release Checklist

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

Use this checklist before publishing a new public companion-resource snapshot.

## Content boundary

- [ ] Paid master DOCX/PDF/EPUB is not present.
- [ ] Commercial cover/store-delivery assets are not present unless intentionally relicensed.
- [ ] X/Twitter links remain omitted.
- [ ] No author avatar/photo/person image has been introduced.
- [ ] No credentials, secrets, tokens, private personal data, or confidential third-party data is present.
- [ ] Public practical material remains defensive, authorized, fictional/offline where appropriate.

## Learning resources

- [ ] Part/stage indexes reflect the maintained 200-part series.
- [ ] Part 200 remains the formal series completion.
- [ ] Safety boundaries remain visible in practical resources.

## Datasets

- [ ] `python tools/csv_quality.py datasets/*.csv` passes.
- [ ] `python tools/dataset_contracts.py schemas/dataset_contracts.json datasets` passes.
- [ ] `python tools/synthetic_safety.py datasets/*.csv` passes.
- [ ] `python tools/dataset_summary.py datasets/*.csv` produces expected summaries.
- [ ] New datasets use fictional identifiers and have contracts.

## Documentation and metadata

- [ ] `python tools/json_metadata.py COMPANION_RELEASE.json schemas/dataset_contracts.json` passes.
- [ ] `python tools/doc_accessibility.py README.md docs resources schemas exercises examples` passes.
- [ ] `python tools/markdown_links.py README.md docs resources schemas exercises examples ERRATA.md ROADMAP.md CHANGELOG.md what_changed.md` passes.
- [ ] `python tools/gumroad_presence.py --root .` passes.
- [ ] README and `docs/INDEX.md` navigation are current.
- [ ] Errata process and correction log are current.
- [ ] Official Gumroad URL is exactly `https://ramsandesh.gumroad.com`.

## Code quality

- [ ] `python -m pytest --cov=tools --cov-report=term-missing -q` passes.
- [ ] `python tools/repo_health.py --root .` passes.
- [ ] CLI smoke tests cover every public local tool.
- [ ] New utilities are local/offline and dependency-light.
- [ ] New behavior has unit tests.

## Release metadata and integrity

- [ ] `COMPANION_RELEASE.json` version is updated.
- [ ] `CHANGELOG.md` describes notable changes.
- [ ] `what_changed.md` records the detailed work.
- [ ] `ROADMAP.md` reflects completed and next tasks.
- [ ] `python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json` generates a reviewable manifest.
- [ ] `docs/RELEASE_SNAPSHOT.md` reflects the intended release gate.

## Git history

- [ ] Commits are atomic and meaningful.
- [ ] Local command-line commits use the intended Git identity configuration.
- [ ] No generated commercial publication files are accidentally tracked.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
