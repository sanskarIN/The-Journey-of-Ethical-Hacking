# Companion Projects Architecture

The companion-project suite uses a deliberately simple architecture so readers can inspect every project without a framework or package manager.

## Layout

```text
companion-projects/
├── README.md
├── PROJECT_MATRIX.md
├── PROJECT_STANDARD.md
├── SAFETY.md
├── THREAT_MODEL.md
├── SYNTHETIC_DATA_GUIDE.md
├── CONTRIBUTING.md
├── run_tests.py
└── <project>/
    ├── README.md
    ├── <tool>.py
    └── test_<tool>.py
```

## Runtime model

Each tool is an independent Python command-line program using the standard library. There is intentionally no shared runtime package between projects: this keeps examples self-contained and reduces coupling for learners.

## Data flow

1. The user explicitly selects one or more local input paths.
2. The tool validates syntax and required fields.
3. The tool performs deterministic local transformation, comparison, hashing, validation, or summarization.
4. Results go to stdout or an explicitly selected output file.
5. Verification-oriented tools return non-zero status when review is needed.

## Dependency policy

Standard-library-only code is preferred. A future external dependency should be introduced only when it provides clear defensive value that cannot reasonably be achieved with the standard library, and it must be documented and pinned.

## Network policy

Current companion projects are offline. A future network-enabled proposal requires a threat-model update, explicit authorization safeguards, privacy review, narrow endpoints, timeouts, and tests proving safe failure behavior.

## Testing model

Every project owns its unit tests. `run_tests.py` discovers `*/test_*.py` and executes each test file in an isolated Python process so one project's imports do not affect another.
