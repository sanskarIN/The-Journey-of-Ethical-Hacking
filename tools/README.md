# Offline Defensive Tools

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

The utilities in this directory operate only on local repository files.

## Analysis helpers

- `risk_priority.py` — ranks fictional/synthetic risk-signal rows for review-priority exercises.
- `evidence_freshness.py` — groups fictional/local control evidence into freshness buckets.
- `control_review.py` — ranks fictional control-evidence records for assurance review.
- `dataset_summary.py` — reports CSV row/column counts, blank cells, and field names.

## Data and metadata validation

- `csv_quality.py` — checks structural quality of synthetic CSV files.
- `dataset_contracts.py` — validates datasets against machine-readable contracts, including required columns, duplicate IDs, approved categorical values, and bounded integer ranges.
- `json_metadata.py` — validates release and dataset-contract JSON structure.
- `synthetic_safety.py` — flags sensitive-looking values such as email, URL, IP, or token-like strings in public synthetic CSV files.
- `data_dictionary.py` — generates `docs/DATA_DICTIONARY.md` and can fail when the committed dictionary is stale.

## Documentation and storefront validation

- `doc_accessibility.py` — checks basic Markdown accessibility expectations.
- `markdown_links.py` — checks relative Markdown links.
- `gumroad_presence.py` — enforces the direct official Gumroad URL across core public-facing docs, all 20 learning-stage pages, citation/funding metadata, and release metadata.
- `docs_toc.py` — generates the documentation TOC and can fail when the committed TOC is stale.

## Repository policy and release integrity

- `action_pinning.py` — rejects movable external GitHub Actions references and requires full 40-character SHAs.
- `dev_environment.py` — checks `.python-version`, workflow Python versions, and exact development dependency pins.
- `public_repo_policy.py` — requires core community/governance files and blocks commercial publication formats and direct X/Twitter URLs from the public repository.
- `companion_projects_check.py` — validates the companion-suite project floor, required suite files, per-project README, implementation, and test presence.
- `policy_status.py` — generates/checks `docs/POLICY_STATUS.md` from deterministic local repository-policy results.
- `release_consistency.py` — verifies the companion release version matches `COMPANION_RELEASE.json`, the changelog, release snapshot, and `CITATION.cff`.
- `learning_index_check.py` — verifies the 20 stage files cover Parts 1–200 exactly once with ten parts per stage.
- `tag_preflight.py` — derives and validates the exact `companion-vYYYY.MM.DD.N` tag expected by release metadata.
- `resource_manifest.py` — generates SHA-256 metadata for public companion resources while excluding commercial publication formats.
- `manifest_verify.py` — verifies a generated public-resource manifest against the exact local repository snapshot.
- `release_readiness.py` — generates/checks the deterministic pre-tag release-readiness report.
- `repo_health.py` — runs the repository's structural and policy validation checks from one command, including companion-project structure and documentation checks.

## Common commands

```bash
python tools/action_pinning.py --root .
python tools/dev_environment.py --root .
python tools/public_repo_policy.py --root .
python tools/companion_projects_check.py --root .
python companion-projects/run_tests.py
python tools/policy_status.py --root . --output docs/POLICY_STATUS.md --check
python tools/dataset_summary.py datasets/*.csv
python tools/data_dictionary.py schemas/dataset_contracts.json --output docs/DATA_DICTIONARY.md --check
python tools/learning_index_check.py --root .
python tools/release_consistency.py --root .
python tools/tag_preflight.py --root . --tag companion-v2026.08.18.6
python tools/docs_toc.py --docs-dir docs --output docs/TOC.md --check
python tools/repo_health.py --root .
python tools/release_readiness.py --root . --output docs/RELEASE_READINESS.md --check
python tools/resource_manifest.py --root . --output PUBLIC_RESOURCE_MANIFEST.json
python tools/manifest_verify.py --root . PUBLIC_RESOURCE_MANIFEST.json
```

## Safety design

These tools intentionally do not include networking, scanning, authentication, account access, device control, exploitation, malware, evasion, persistence, credential extraction, surveillance, or security-control bypass logic.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
