# Issue Triage Guide

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

Use this guide to classify and respond to public repository issues consistently.

## Triage categories

### Book errata

Use for concise factual, formatting, numbering, or cross-reference corrections. Ask reporters for part/chapter/topic references and a short correction description; do not request long excerpts from the paid book.

### Documentation

Use for README, guide, accessibility, link, or navigation issues. Prefer small fixes with relative links and descriptive text.

### Synthetic datasets and schemas

Use for fictional CSV samples, contracts, validators, or examples. Reject submissions containing personal data, secrets, credentials, real target information, or sensitive production evidence.

### Tools and tests

Use for local-only companion utilities, unit tests, CI validation, and repository-health checks. Keep utilities offline and non-invasive.

### Release maintenance

Use for `COMPANION_RELEASE.json`, release snapshots, changelog consistency, public manifests, dependency/action review, or tagged companion releases.

### Storefront/documentation visibility

Use when the official publication link is missing or incorrect on a public-facing page. The canonical link is **https://ramsandesh.gumroad.com**.

## Safety triage

Close or redirect requests that seek unauthorized access, credential theft, malware, security-control bypass, destructive actions, stealth/evasion, tracking people/devices without consent, or targeting third-party systems.

For a genuine repository security vulnerability, direct the reporter to `SECURITY.md` rather than discussing sensitive details publicly.

## Resolution checklist

- [ ] Category identified.
- [ ] Scope is appropriate for the public companion repository.
- [ ] Safety and privacy boundaries are satisfied.
- [ ] Reproduction/validation steps use local or synthetic data only where applicable.
- [ ] Linked PR or commit uses a clear logical change.
- [ ] Documentation/release records are updated when needed.

**Publication storefront:** https://ramsandesh.gumroad.com
