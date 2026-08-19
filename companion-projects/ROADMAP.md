# Companion Projects Roadmap

The current milestone delivers **20 complete offline defensive projects**. Future additions should deepen defensive engineering without crossing the repository's authorization-first boundary.

## Completed expansion items

- [x] Control Evidence Mapper — map local evidence records to recognized defensive controls.
- [x] Patch Register Summary — summarize an exported patch-status CSV without scanning hosts.
- [x] Recovery Exercise Reporter — summarize local tabletop recovery exercise results.
- [x] Exception Register Validator — validate owner, expiry, rationale, and approval fields in governance exports.
- [x] Suite-level structure validation with a 20-project floor.
- [x] Suite-wide test discovery and CI integration.

## Next project candidates

- **Alert Deduplicator** — group repeated synthetic alert records by stable keys.
- **Policy Expiry Reporter** — flag local policy records approaching review dates.
- **Certificate Inventory Parser** — summarize explicitly supplied certificate metadata files without contacting services.
- **Audit Log Schema Checker** — validate required fields and timestamp consistency in synthetic audit exports.
- **Control Coverage Summary** — summarize recognized controls that have or lack mapped synthetic evidence.
- **Exercise Action Tracker** — summarize follow-up actions from local tabletop exercise exports.
- **Configuration Review Queue** — rank explicit configuration-review records by age and review state.
- **Evidence Naming Validator** — validate safe, deterministic evidence filename conventions without reading file contents.

## Quality roadmap

1. Keep every project standard-library-first.
2. Add at least two tests for each new executable utility.
3. Add project-level synthetic examples only when they cannot be mistaken for real credentials or incidents.
4. Keep suite-level structure checks synchronized with the current minimum project milestone.
5. Keep documentation-link and accessibility checks covering every project README.
6. Track compatibility with the repository's supported Python version.
7. Keep every current project offline unless a reviewed threat-model change explicitly approves otherwise.
8. Continue reviewing recursive filesystem utilities for symlink and scope safety.

## Non-roadmap items

Exploit frameworks, credential-testing tools, malware features, persistence, stealth, destructive actions, unauthorized scanning, and target reconnaissance are intentionally not planned for this suite.
