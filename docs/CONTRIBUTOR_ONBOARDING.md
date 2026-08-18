# First-Time Contributor Onboarding

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This checklist helps first-time contributors make small, safe, reviewable changes to the public companion repository.

## Before you edit

- [ ] Read `README.md`, `CONTRIBUTING.md`, and `SECURITY.md`.
- [ ] Confirm the change belongs in the public companion repository rather than the commercial manuscript.
- [ ] Use only fictional/synthetic data in public examples.
- [ ] Do not add credentials, secrets, personal data, real target details, or sensitive production evidence.
- [ ] Keep practical cybersecurity material lawful, authorized, defensive, and non-destructive.
- [ ] Keep X/Twitter links omitted from publication-facing content.
- [ ] Do not add an author avatar/photo/person image.

## For synthetic dataset contributions

- [ ] Follow `examples/new_dataset_contribution/README.md`.
- [ ] Add or update the corresponding contract in `schemas/dataset_contracts.json`.
- [ ] Use stable fictional identifiers.
- [ ] Prefer explicit categorical values and bounded non-negative integer fields where useful.

## Before opening a pull request

Run:

```bash
python -m pytest --cov=tools --cov-report=term-missing -q
python tools/repo_health.py --root .
python tools/release_consistency.py --root .
```

Then check:

- [ ] Documentation links are relative where practical.
- [ ] Public-facing Markdown keeps the official Gumroad URL where required.
- [ ] New docs use descriptive headings and accessible link text.
- [ ] Commit messages explain one logical change at a time.
- [ ] The PR description explains what changed, why, and how it was validated.

## Storefront boundary

The Gumroad link is for purchasing/current publication listings. Paid manuscript/PDF/EPUB/store-delivery files do not belong in this public repository.

**Publication storefront:** https://ramsandesh.gumroad.com
