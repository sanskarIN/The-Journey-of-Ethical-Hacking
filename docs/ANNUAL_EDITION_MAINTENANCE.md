# Annual Edition Maintenance Checklist

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

Use this checklist when preparing a yearly refresh of the public companion repository and the corresponding commercial book edition.

## Repository integrity

- [ ] Confirm all public files still fit the defensive, authorization-first scope.
- [ ] Run the full unit-test suite with coverage.
- [ ] Validate all synthetic CSV structure and contracts.
- [ ] Validate JSON metadata.
- [ ] Run Markdown accessibility checks.
- [ ] Run relative-link checks.
- [ ] Review open errata and close verified corrections.

## Learning content alignment

- [ ] Verify the 20-stage index still maps cleanly to Parts 1–200 for this edition.
- [ ] Review terminology for consistency with the current publication.
- [ ] Refresh synthetic examples when fields or learning objectives change.
- [ ] Confirm no paid manuscript text has been copied into the public repository.

## Publication and storefront

- [ ] Confirm the official Gumroad URL is exactly `https://ramsandesh.gumroad.com`.
- [ ] Confirm highlighted Gumroad badges still resolve to the direct storefront.
- [ ] Keep X/Twitter links omitted.
- [ ] Keep the no-avatar/no-author-photo publication rule.
- [ ] Verify book-rights and Apache-2.0 companion-resource boundaries.

## Maintenance and dependencies

- [ ] Review GitHub Actions versions used by CI.
- [ ] Review Python/test dependencies and document upgrade decisions.
- [ ] Review supported Python version.
- [ ] Review repository templates, issue forms, and release guidance.
- [ ] Remove obsolete files only after confirming no public documentation links depend on them.

## Release preparation

- [ ] Update `CHANGELOG.md`.
- [ ] Update `what_changed.md`.
- [ ] Update `ROADMAP.md`.
- [ ] Increment `companion_release` in `COMPANION_RELEASE.json`.
- [ ] Complete `docs/RELEASE_CHECKLIST.md`.

**Official publication storefront:** https://ramsandesh.gumroad.com
