# Defensive Companion Projects

This directory contains small, authorization-first cybersecurity projects that complement **The Journey of Ethical Hacking** without publishing the paid book manuscript.

Every project is designed for local files, synthetic data, owned systems, or explicitly authorized environments. The projects intentionally avoid exploit delivery, credential theft, destructive actions, stealth, persistence, or unauthorized scanning.

## Project catalog

1. `log-sifter` — summarize local authentication-style logs.
2. `integrity-manifest` — create and verify SHA-256 file-integrity manifests.
3. `ioc-normalizer` — normalize defensive indicators without network lookups.
4. `incident-timeline` — turn local JSONL events into a sorted incident timeline.
5. `header-safety-report` — inspect saved email headers for authentication signals.
6. `secrets-redactor` — redact common secret-like values from text before sharing logs.
7. `evidence-inventory` — inventory evidence files with metadata and hashes.
8. `access-review-helper` — compare account exports with an approved-role policy.

## Design rules

- Python standard library only where practical.
- No network access by default.
- Deterministic output suitable for tests.
- Clear `--help` output.
- Synthetic examples only.
- Defensive learning outcomes are stated in each project README.

## Quick start

```bash
python companion-projects/<project>/<tool>.py --help
```

Run only against data you own or are authorized to process.
