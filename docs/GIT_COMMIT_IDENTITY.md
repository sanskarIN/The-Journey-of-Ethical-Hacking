# Git Commit Identity

For local development on this repository, configure the requested commit email as:

```bash
git config user.email "sanskarin@outlook.in"
```

Optionally set it globally for repositories on the same development machine:

```bash
git config --global user.email "sanskarin@outlook.in"
```

Set the desired local Git author name separately, for example:

```bash
git config user.name "Sanskar"
```

Verify the active identity with:

```bash
git config user.name
git config user.email
```

## Connector note

The GitHub connector used to create the repository files in the initial companion build does not expose an `author` or `author_email` field for content commits. Those API-created commits are therefore attributed by GitHub through the connected account rather than by a manually supplied email value.
