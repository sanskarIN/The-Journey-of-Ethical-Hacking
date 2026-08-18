#!/usr/bin/env python3
"""Generate a compact Markdown index for repository documentation.

This utility reads local Markdown files only and performs no network access.
"""

from __future__ import annotations

import argparse
from pathlib import Path

GUMROAD = "https://ramsandesh.gumroad.com"


def first_heading(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("_", " ").replace("-", " ").title()


def collect_docs(docs_dir: Path, output_name: str = "TOC.md") -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    for path in sorted(docs_dir.glob("*.md")):
        if path.name == output_name:
            continue
        entries.append((path.name, first_heading(path)))
    return entries


def render(entries: list[tuple[str, str]]) -> str:
    lines = [
        "# Documentation Table of Contents",
        "",
        "[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)",
        "",
        f"**Official Gumroad:** {GUMROAD}",
        "",
        "Generated from the level-1 headings of Markdown files in `docs/`.",
        "",
    ]
    for filename, title in entries:
        lines.append(f"- [{title}]({filename})")
    lines.extend(["", f"**Publication storefront:** {GUMROAD}", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate docs/TOC.md from local documentation.")
    parser.add_argument("--docs-dir", type=Path, default=Path("docs"))
    parser.add_argument("--output", type=Path, default=Path("docs/TOC.md"))
    args = parser.parse_args()

    entries = collect_docs(args.docs_dir, args.output.name)
    args.output.write_text(render(entries), encoding="utf-8")
    print(f"Documentation TOC generated: {args.output} ({len(entries)} entries)")


if __name__ == "__main__":
    main()
