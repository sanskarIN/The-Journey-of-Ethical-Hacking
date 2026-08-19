# Synthetic Data Guide

Use synthetic data for examples, tests, screenshots, bug reports, and documentation in the companion-project suite.

## Synthetic data principles

- Use reserved documentation IP ranges such as `192.0.2.0/24`, `198.51.100.0/24`, and `203.0.113.0/24` when an example needs an IPv4 address.
- Use `.example` or `.test` domains for illustrative names.
- Use obvious labels such as `lab-host-1`, `synthetic-user`, and `training-dataset`.
- Use fake hashes only when the hash itself is the data being tested; never paste a credential or secret and hash it for a fixture.
- Use dates and timestamps that are clearly part of a training scenario.
- Do not copy real private email headers, account exports, incident logs, or configuration files into fixtures.

## Secrets

Fixtures must never contain working API keys, passwords, session tokens, private keys, recovery codes, or credentials. Use strings such as `synthetic-value` when a parser needs placeholder content.

## Personal information

Avoid real names, email addresses, phone numbers, account identifiers, buyer records, or other personal data. Prefer neutral fictional labels.

## Incident examples

Keep examples defensive and non-operational. Describe events at the level needed to test parsing, validation, reporting, and governance behavior without publishing attack instructions.

## Review before commit

Before committing fixture data, verify that it is synthetic, contains no secrets, contains no paid manuscript text, and contains no private incident evidence.
