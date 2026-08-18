# Companion Resource Release Checklist

Use this checklist before publishing a new public companion-resource snapshot.

## Content boundary

- [ ] Paid master DOCX/PDF/EPUB is not present.
- [ ] Commercial cover/store assets are not present unless intentionally relicensed.
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
- [ ] New datasets use fictional identifiers and have contracts.

## Documentation

- [ ] `python tools/doc_accessibility.py README.md docs resources schemas` passes.
- [ ] `python tools/markdown_links.py README.md docs resources schemas ERRATA.md ROADMAP.md CHANGELOG.md what_changed.md` passes.
- [ ] README navigation is current.
- [ ] Errata process and correction log are current.

## Code quality

- [ ] `python -m pytest -q` passes.
- [ ] New utilities are local/offline and dependency-light.
- [ ] New behavior has unit tests.

## Release metadata

- [ ] `COMPANION_RELEASE.json` version is updated.
- [ ] `CHANGELOG.md` describes notable changes.
- [ ] `what_changed.md` records the detailed work.
- [ ] `ROADMAP.md` reflects completed and next tasks.

## Git history

- [ ] Commits are atomic and meaningful.
- [ ] Local command-line commits use the intended Git identity configuration.
- [ ] No generated commercial publication files are accidentally tracked.
