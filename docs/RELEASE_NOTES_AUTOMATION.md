# Release Notes Automation Guidance

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

This repository keeps release notes focused on the **public companion resources**, not the paid manuscript or commercial publication files.

## Recommended release-note inputs

Use these repository files as the source of truth:

- `CHANGELOG.md` — human-readable notable changes.
- `what_changed.md` — detailed implementation audit.
- `COMPANION_RELEASE.json` — machine-readable release metadata.
- `ROADMAP.md` — completed and upcoming repository work.
- `docs/RELEASE_CHECKLIST.md` — release gate.

## Suggested automation flow

1. Complete a logical companion-resource milestone.
2. Run the full CI/local validation suite.
3. Update `CHANGELOG.md` and `what_changed.md`.
4. Increment `companion_release` in `COMPANION_RELEASE.json`.
5. Confirm the official Gumroad storefront remains `https://ramsandesh.gumroad.com`.
6. Confirm the public repository still excludes the commercial manuscript, PDF/EPUB, cover, certificate, and store-delivery files.
7. Create a GitHub release or tag using a concise summary derived from the changelog.
8. Link back to the repository and Gumroad storefront in the release description.

## Suggested release-note structure

```text
Companion Resources <version>

Added
- ...

Changed
- ...

Validation
- tests
- dataset contracts
- accessibility
- relative links
- JSON metadata

Publication
- Book/storefront: https://ramsandesh.gumroad.com
```

## Guardrails

- Do not attach the paid master manuscript or commercial eBook files to a public GitHub release.
- Do not include secrets, credentials, personal data, or real target information.
- Do not reintroduce X/Twitter links.
- Do not add an author avatar/photo/person image as part of release promotion.

**Official publication storefront:** https://ramsandesh.gumroad.com
