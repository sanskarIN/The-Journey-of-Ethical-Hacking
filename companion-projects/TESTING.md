# Companion Projects Testing Guide

The companion-project suite is designed to be tested entirely offline with Python 3.12 and synthetic/local fixtures.

## Test layers

### 1. Python syntax compilation

Compile every repository Python source before deeper tests:

```bash
python -m compileall -q tools tests companion-projects
```

This catches syntax and bytecode-compilation errors early.

### 2. Repository pytest suite

Run the main repository tests with coverage for `tools/`:

```bash
python -m pytest --cov=tools --cov-report=term-missing -q
```

The main suite also smoke-tests `--help` for every repository tool and every discovered companion-project CLI. CLI smoke tests use a timeout so a broken help path cannot block CI indefinitely.

### 3. Project-owned unit tests

Run every test file under the 20 companion-project directories:

```bash
python companion-projects/run_tests.py
```

Each test file runs in its own Python process. The runner applies a default **30-second per-file timeout** so a stalled future test cannot block the suite indefinitely.

List the discovered project test files without executing them:

```bash
python companion-projects/run_tests.py --list
```

Override the per-file timeout when needed:

```bash
python companion-projects/run_tests.py --timeout 60
```

Stop after the first failure or timeout:

```bash
python companion-projects/run_tests.py --fail-fast
```

The timeout must be greater than zero.

### 4. Suite structure validation

Validate the project floor, catalog, matrix, suite documentation, and per-project file requirements:

```bash
python tools/companion_projects_check.py --root .
```

The validator also checks that the catalog and project matrix stay synchronized with the actual project directories and that current projects remain marked offline and tested.

### 5. Complete repository health gate

Run the consolidated local structural/policy gate:

```bash
python tools/repo_health.py --root .
```

## Required test characteristics

Each executable companion project should include tests for:

- a normal valid-input path;
- at least one malformed or invalid-input path;
- deterministic output or deterministic findings;
- project-specific boundary behavior where relevant.

Recursive filesystem tools should include scope-safety coverage when their behavior changes. Date/time tools should include boundary-date or timezone coverage when applicable.

The repository test suite also covers the companion test runner itself, including successful execution, non-zero failures, per-file timeouts, fail-fast behavior, and invalid timeout rejection.

## Test fixtures

Use only synthetic or explicitly authorized fixture data. Do not commit:

- working credentials or tokens;
- private keys or recovery codes;
- real private email headers;
- private incident evidence;
- buyer/customer records;
- paid manuscript content;
- real target reconnaissance data.

See `SYNTHETIC_DATA_GUIDE.md` for fixture conventions.

## Before merging a project change

Run, in order:

```bash
python -m compileall -q tools tests companion-projects
python -m pytest --cov=tools --cov-report=term-missing -q
python companion-projects/run_tests.py
python tools/companion_projects_check.py --root .
python tools/repo_health.py --root .
```

A change should not be considered complete until all applicable local checks are clean.
