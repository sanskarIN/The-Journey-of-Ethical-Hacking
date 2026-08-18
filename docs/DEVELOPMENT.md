# Contributor Development Setup

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

This guide provides a repeatable local setup for the public companion repository.

## Environment baseline

- Python: **3.12** via `.python-version`
- Development dependencies: `requirements-dev.txt`
- Current pinned test dependencies:
  - `pytest==9.1.1`
  - `pytest-cov==7.1.0`

## Create a virtual environment

### Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

### Linux/macOS shell

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

## Run the repository checks

```bash
python -m pytest --cov=tools --cov-report=term-missing -q
python tools/repo_health.py --root .
```

Useful focused checks:

```bash
python tools/learning_index_check.py --root .
python tools/release_consistency.py --root .
python tools/docs_toc.py --docs-dir docs --output docs/TOC.md --check
python tools/gumroad_presence.py --root .
```

## Documentation generation

Regenerate the documentation TOC after adding or removing a guide:

```bash
python tools/docs_toc.py --docs-dir docs --output docs/TOC.md
```

Generate the synthetic dataset data dictionary after changing dataset contracts:

```bash
python tools/data_dictionary.py schemas/dataset_contracts.json --output docs/DATA_DICTIONARY.md
```

## Contribution boundaries

- Use fictional/synthetic data only in public examples.
- Do not include credentials, secrets, personal data, private logs, or sensitive production evidence.
- Keep all practical cybersecurity examples defensive, authorized, local/offline, and non-destructive.
- Do not add commercial master DOCX/PDF/EPUB or store-delivery files to the public repository.
- Keep X/Twitter omitted from publication-facing content.
- Do not add an author avatar/photo/person image.

For the requested local Git commit email, see `docs/GIT_COMMIT_IDENTITY.md`.

**Publication storefront:** https://ramsandesh.gumroad.com
