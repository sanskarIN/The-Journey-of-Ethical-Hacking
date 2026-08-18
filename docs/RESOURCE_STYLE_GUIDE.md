# Companion Resource Style Guide

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This guide keeps public companion contributions consistent, safe, accessible, and easy to review.

## General writing

- Use clear descriptive headings.
- Prefer short paragraphs and explicit assumptions.
- Expand uncommon acronyms at first use when practical.
- Separate facts, assumptions, and fictional exercise data.
- Do not imply that a toy score is a production security or risk model.
- Use the direct Gumroad storefront `https://ramsandesh.gumroad.com` when linking to the commercial publication.

## Safety language

Every practical resource should make its scope clear when needed:

- lawful and authorized use only;
- fictional or synthetic data for public exercises;
- no credentials, secrets, personal data, or third-party target information;
- no destructive, evasive, bypass, malware, or unauthorized-access instructions.

## Synthetic datasets

- Use obviously fictional identifiers such as `EP-001` or `GOV-001`.
- Keep datasets small enough for manual inspection.
- Use one stable primary identifier in the first column.
- Do not include real company/customer names unless they are generic category labels.
- Update `schemas/dataset_contracts.json` when adding a CSV dataset.
- Run CSV quality, contract, summary, and sensitivity checks before committing.

## Markdown resources

- Begin with one level-1 heading.
- Use descriptive link text.
- Give informative images useful alt text.
- Avoid decorative person/avatar imagery in this repository.
- Keep tables small and explain them in surrounding prose.
- Run accessibility, relative-link, and Gumroad-presence checks before committing.

## Python utilities

- Standard library is preferred for small teaching helpers.
- Utilities must remain local/offline unless a future design is explicitly reviewed for authorization and privacy.
- Do not add scanning, exploitation, credential access, evasion, persistence, surveillance, or destructive features.
- Separate reusable functions from CLI entry points so they can be unit tested.
- Add tests for new behavior.

## Commit style

Use concise, scoped commit messages such as:

- `datasets: add fictional privacy control sample`
- `tests: add dataset contract validator tests`
- `docs: clarify errata workflow`

Prefer meaningful atomic commits over empty or artificial commit-count padding.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
