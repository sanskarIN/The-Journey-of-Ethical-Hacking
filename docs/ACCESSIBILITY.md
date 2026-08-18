# Documentation Accessibility Guide

[![Get the Book on Gumroad](https://img.shields.io/badge/Get%20the%20Book-Gumroad-FF90E8?logo=gumroad&logoColor=000000)](https://ramsandesh.gumroad.com)

**Official Gumroad:** https://ramsandesh.gumroad.com

Public companion documentation should remain readable with keyboard navigation, screen readers, zoom, high-contrast settings, and plain-text Markdown renderers.

## Authoring rules

- Start each Markdown file with one clear level-1 heading.
- Use descriptive link text instead of labels such as “click here”.
- Add meaningful alt text to informative images.
- If an image is purely decorative, prefer omitting it from technical documentation rather than relying on decoration for meaning.
- Do not encode meaning through color alone.
- Keep tables small and provide surrounding explanatory text.
- Use ordered headings rather than simulated headings made from bold text.
- Prefer short paragraphs and descriptive section names.
- Put commands and code in fenced code blocks.
- Avoid tabs in prose and tables because rendering differs across tools.
- Expand uncommon acronyms at first use when practical.
- Keep storefront links descriptive; the official direct publication URL is `https://ramsandesh.gumroad.com`.

## Automated check

Run:

```bash
python tools/doc_accessibility.py README.md docs resources schemas exercises examples
```

The local checker currently verifies:

- presence of a level-1 heading;
- non-empty alt text on Markdown images;
- avoidance of generic link labels;
- avoidance of tab characters.

These checks are deliberately conservative and do not replace human accessibility review.

## Human review checklist

1. Can the document be understood without seeing color or decorative imagery?
2. Are headings meaningful when read as a list?
3. Do links make sense when read out of surrounding context?
4. Are diagrams explained in nearby text?
5. Are tables understandable when read row by row?
6. Does zooming or narrow-screen reading preserve the logical order?

Accessibility improvements are welcome through pull requests and documentation issues.

For the complete publication and current listings, use **https://ramsandesh.gumroad.com**.
