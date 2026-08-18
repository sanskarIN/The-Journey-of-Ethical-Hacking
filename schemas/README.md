# Synthetic Dataset Contracts

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This directory contains machine-readable contracts for the fictional CSV datasets used by the public companion repository.

The contracts are intentionally simple. Each dataset entry identifies:

- the expected primary identifier column;
- the required column names;
- whether additional columns are allowed.

They are used only for local validation of repository exercise files. They do not describe production security data models and should not be treated as an enterprise schema standard.

Run the validators with:

```bash
python tools/dataset_contracts.py schemas/dataset_contracts.json datasets
python tools/json_metadata.py COMPANION_RELEASE.json schemas/dataset_contracts.json
```

The validators perform no network access and do not modify the CSV or JSON files.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
