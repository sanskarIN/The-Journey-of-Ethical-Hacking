# Errata Review Process

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

The public repository tracks correction reports without exposing the commercial manuscript.

## 1. Submit a concise report

Use the **Book errata** issue template. Include:

- edition (for example, 2026 Edition);
- part number;
- visible section or topic heading;
- issue type: typo, formatting, broken cross-reference, technical clarification, accessibility, or other;
- concise description of the problem;
- proposed correction, if known.

Do not paste long copyrighted passages from the paid book. A short phrase needed to identify the location is enough.

## 2. Triage

A maintainer checks whether the report is reproducible against the maintained publication source and whether it concerns the book or only the public companion repository.

## 3. Classification

A report may be marked conceptually as:

- **Confirmed** — a real correction is needed;
- **Not an error** — the existing wording is intentional/correct;
- **Companion issue** — the problem belongs to this repository rather than the book;
- **Needs more detail** — the location or issue cannot yet be verified.

## 4. Correction

For confirmed book issues, the commercial source is corrected outside the public repository. The public `ERRATA.md` records only the minimal correction metadata needed by readers.

For companion-repository issues, the fix can be made directly through a pull request or maintainer commit.

## 5. Verification

Before an errata item is marked corrected:

1. verify the updated source;
2. confirm the correction did not create a new cross-reference or formatting problem;
3. regenerate affected publication files when appropriate;
4. record the correction status in `ERRATA.md`;
5. mention the correction in `CHANGELOG.md` for a publication refresh.

## Privacy and safety

Do not submit credentials, private customer information, personal data, confidential screenshots, exploit evidence from third-party systems, or other sensitive material in public errata reports.

For the current commercial publication listing, use **https://ramsandesh.gumroad.com**.
