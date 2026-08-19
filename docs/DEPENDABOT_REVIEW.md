# Dependabot Review Procedure

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

Dependabot is configured to check GitHub Actions and development dependencies periodically. Dependency updates should be reviewed rather than merged automatically without validation.

## Current status

At the time this release-candidate pass was prepared, the repository had no open pull requests or issues requiring review.

## GitHub Actions updates

For an Actions update:

1. Confirm the upstream action/release is the intended project and version.
2. Review release notes for breaking changes or permission changes.
3. Preserve full-length immutable commit-SHA pinning in workflow files.
4. Keep the readable release-version comment next to the SHA pin.
5. Run `python tools/action_pinning.py --root .`.
6. Run the complete repository health/test gate.
7. Update `docs/DEPENDENCY_ACTION_REVIEW.md` when the accepted version changes.

## Python development dependency updates

For a `requirements-dev.txt` update:

1. Review the package source and release notes.
2. Keep exact pins for the development/test dependencies.
3. Confirm `.python-version` and CI Python remain aligned.
4. Run `python tools/dev_environment.py --root .`.
5. Run the complete test and repository-health gate.

## Do not auto-merge when

- CI or repository-health checks fail;
- the update weakens immutable action pinning;
- the source or package identity is unclear;
- the update adds unnecessary runtime/network/security-system access;
- the change conflicts with the defensive/publication boundary;
- the change would publish commercial book/store-delivery files.

## Publication boundary

Dependency maintenance applies only to the public companion repository. The commercial book remains distributed through **https://ramsandesh.gumroad.com** and is not committed here.
