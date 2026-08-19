# Companion Projects Roadmap

The first milestone delivers 16 complete offline defensive projects. Future additions should deepen defensive engineering without crossing the repository's authorization-first boundary.

## Next project candidates

- **Alert Deduplicator** — group repeated synthetic alert records by stable keys.
- **Control Evidence Mapper** — map local evidence files to a defensive control checklist.
- **Policy Expiry Reporter** — flag local policy records approaching review dates.
- **Patch Register Summary** — summarize an exported patch-status CSV without scanning hosts.
- **Certificate Inventory Parser** — summarize explicitly supplied certificate metadata files without contacting services.
- **Audit Log Schema Checker** — validate required fields and timestamp consistency in synthetic audit exports.
- **Recovery Exercise Reporter** — turn tabletop recovery results into Markdown metrics.
- **Exception Register Validator** — validate owner, expiry, rationale, and approval fields in governance exports.

## Quality roadmap

1. Keep every project standard-library-first.
2. Add at least two tests for each new executable utility.
3. Add project-level synthetic examples only when they cannot be mistaken for real credentials or incidents.
4. Add suite-level discovery checks so the project matrix cannot silently become stale.
5. Add documentation-link checks for every project README.
6. Track compatibility with the repository's supported Python version.
7. Keep every current project offline unless a reviewed threat-model change explicitly approves otherwise.

## Non-roadmap items

Exploit frameworks, credential-testing tools, malware features, persistence, stealth, destructive actions, unauthorized scanning, and target reconnaissance are intentionally not planned for this suite.
