# Companion Projects Architecture

The 20-project companion suite uses a deliberately simple architecture so readers can inspect every project without a framework or runtime package manager.

## Layout

```text
companion-projects/
├── README.md
├── PROJECT_MATRIX.md
├── PROJECT_STANDARD.md
├── ARCHITECTURE.md
├── CLI_CONTRACT.md
├── TESTING.md
├── SAFETY.md
├── THREAT_MODEL.md
├── SYNTHETIC_DATA_GUIDE.md
├── CONTRIBUTING.md
├── MAINTENANCE_CHECKLIST.md
├── CHANGELOG.md
├── ROADMAP.md
├── run_tests.py
└── <project>/
    ├── README.md
    ├── <tool>.py
    └── test_<tool>.py
```

## Runtime model

Each project is an independent Python command-line program using the standard library where practical. There is intentionally no shared runtime package between project directories: this keeps examples self-contained, minimizes dependency coupling, and lets each project be read independently.

The repository baseline is Python 3.12. `requirements-dev.txt` is for repository testing/quality tooling rather than a runtime dependency bundle for the companion utilities.

## Data flow

1. The user explicitly selects one or more local input paths.
2. The tool treats input as untrusted and validates syntax, required fields, categorical values, dates, ranges, or other project-specific constraints.
3. The tool performs deterministic local transformation, comparison, hashing, validation, or summarization.
4. Results go to stdout or an explicitly selected output file.
5. Verification/review-oriented tools return a non-zero status when the project contract defines a finding/failure condition.

See `CLI_CONTRACT.md` for the shared command-line behavior.

## Filesystem scope

Tools do not silently search a user's device. Recursive utilities receive an explicit directory path. Current recursive hashing/inventory utilities avoid following symbolic links so a selected tree does not silently expand into linked files outside the intended scope.

## Dependency policy

Standard-library-only code is preferred. A future external runtime dependency should be introduced only when it provides clear defensive value that cannot reasonably be achieved with the standard library, and it must be documented, reviewed, and pinned where appropriate.

## Network policy

All current companion projects are offline. They do not perform live-target discovery, DNS/HTTP/reputation lookups, authentication attempts, remote collection, or system scanning.

Changing that current invariant would require an explicit architectural decision, a threat-model update, authorization/privacy safeguards, narrow endpoints, timeouts, failure-mode tests, machine-readable release metadata changes, project-matrix changes, and review of the repository safety boundary.

## Testing model

Testing is layered:

1. `python -m compileall -q tools tests companion-projects` catches syntax/bytecode-compilation errors.
2. The main pytest suite tests repository utilities and smoke-tests `--help` for every discovered repository/companion CLI.
3. `run_tests.py` discovers `*/test_*.py` and executes each project-owned test file in an isolated Python process.
4. `tools/companion_projects_check.py` validates suite structure and documentation synchronization.
5. `tools/repo_health.py` runs the consolidated structural/policy gate.
6. Release-candidate and tagged-release workflows repeat the core quality gates before accepting release evidence.

See `TESTING.md` for the complete command sequence.

## Suite integrity model

The repository currently treats these as invariants:

- at least 20 project directories;
- one catalog entry per project slug;
- one project-matrix row per project;
- current matrix rows marked offline and tested;
- a level-1 README plus implementation and project-owned tests for every project;
- required suite-level engineering/safety/maintenance documentation.

These invariants are automated rather than relying only on reviewer memory.
