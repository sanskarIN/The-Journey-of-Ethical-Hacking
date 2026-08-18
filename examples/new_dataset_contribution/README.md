# Example: Add a New Synthetic Dataset and Contract

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

This worked example shows the repository pattern for contributing a **fictional, offline-only CSV dataset** plus a matching contract entry.

## Example files

- `sample_service_assurance.csv` — fictional service-assurance records.
- `contract_snippet.json` — the matching dataset-contract entry.

## Contribution workflow

1. Choose a narrow defensive learning objective.
2. Use fictional identifiers such as `SV-001`; never copy production identifiers or personal data.
3. Keep columns explainable and non-sensitive.
4. Add the CSV under `datasets/` in a real contribution.
5. Add a matching entry to `schemas/dataset_contracts.json`.
6. Update `datasets/README.md` with a short description.
7. Run:

```bash
python tools/csv_quality.py datasets/*.csv
python tools/dataset_contracts.py schemas/dataset_contracts.json datasets
python tools/dataset_summary.py datasets/*.csv
python -m pytest -q
```

8. Document the defensive learning purpose in the pull request.

## Safety checklist

- No passwords, tokens, keys, secrets, or credentials.
- No real names, email addresses, device IDs, account IDs, or target information.
- No exploit steps, bypass guidance, malware, stealth, or destructive behavior.
- No instructions requiring access to a real system or service.

**Official publication storefront:** https://ramsandesh.gumroad.com
