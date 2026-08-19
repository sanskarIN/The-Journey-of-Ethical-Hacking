# Repository Structure

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

```text
.
├── .github/                     # CI, release workflows, issue/PR templates, CODEOWNERS
├── companion-projects/          # 20 offline defensive mini-projects + suite engineering docs
│   ├── <project>/               # README + focused implementation + project-owned tests
│   ├── README.md                # Complete project catalog
│   ├── PROJECT_MATRIX.md        # Skill/input/network/test matrix
│   ├── PROJECT_STANDARD.md      # Engineering baseline
│   ├── ARCHITECTURE.md          # Suite architecture/runtime model
│   ├── CLI_CONTRACT.md          # Shared CLI and exit-code contract
│   ├── TESTING.md               # Complete project test workflow
│   ├── SAFETY.md                # Authorization/safety boundary
│   ├── THREAT_MODEL.md          # Suite risks and non-goals
│   ├── SYNTHETIC_DATA_GUIDE.md  # Safe fixture conventions
│   ├── CONTRIBUTING.md          # Suite contribution rules
│   ├── MAINTENANCE_CHECKLIST.md # Maintenance/review checklist
│   ├── CHANGELOG.md             # Suite-specific history
│   ├── ROADMAP.md               # Safe future work
│   └── run_tests.py             # Project-owned test runner
├── datasets/                    # Synthetic CSV data only
├── docs/                        # Usage, release, maintenance, and repository documentation
├── examples/                    # Safe contributor examples
├── exercises/                   # Fictional discussion-only tabletop packs
├── resources/                   # Defensive checklists, templates, and learning indexes
├── schemas/                     # Machine-readable synthetic dataset contracts
├── tests/                       # Repository unit, validator, release, and CLI smoke tests
├── tools/                       # Local-only analysis and repository-quality helpers
├── .python-version              # Python 3.12 baseline
├── requirements-dev.txt         # Pinned development/test dependencies
├── COMPANION_RELEASE.json       # Active machine-readable candidate metadata
├── CITATION.cff                 # GitHub citation metadata
├── README.md
├── LICENSE
├── NOTICE
├── BOOK_CONTENT_LICENSE.md
├── SECURITY.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SUPPORT.md
├── ERRATA.md
├── ROADMAP.md
├── CHANGELOG.md
└── what_changed.md
```

## Companion suite invariants

`tools/companion_projects_check.py` protects the current suite structure by checking:

- a minimum of 20 project directories;
- required suite documentation;
- README catalog coverage for each project slug;
- one project-matrix row per project;
- current matrix rows marked offline and tested;
- a level-1 heading in every project README;
- at least one implementation and one project-owned test file per project.

## Validation layers

The repository uses separate but overlapping quality layers:

1. Python compilation (`compileall`).
2. Main pytest/coverage and CLI smoke tests.
3. Project-owned companion tests.
4. Companion suite structural/documentation validation.
5. Repository policy and health validation.
6. Release metadata/readiness/tag/manifest validation.
7. Manual review of the frozen release branch and tagged manifest artifact.

The public repository intentionally excludes the paid master manuscript, commercial publication PDF/EPUB, cover, certificates, and store-delivery assets.

The official publication storefront is **https://ramsandesh.gumroad.com**.
