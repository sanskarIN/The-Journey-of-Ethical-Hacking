from pathlib import Path

from tools.release_readiness import workflow_issues


def write_workflow(root: Path, text: str) -> None:
    path = root / ".github" / "workflows" / "release-manifest.yml"
    path.parent.mkdir(parents=True)
    path.write_text(text, encoding="utf-8")


def test_release_workflow_with_required_steps_passes(tmp_path: Path) -> None:
    write_workflow(
        tmp_path,
        '\n'.join(
            [
                'tags:',
                '  - "companion-v*"',
                'run: python tools/tag_preflight.py --tag "$GITHUB_REF_NAME"',
                'run: python tools/resource_manifest.py --output PUBLIC_RESOURCE_MANIFEST.json',
                'run: python tools/manifest_verify.py PUBLIC_RESOURCE_MANIFEST.json',
            ]
        ),
    )
    assert workflow_issues(tmp_path) == []


def test_release_workflow_missing_manifest_verification_is_reported(tmp_path: Path) -> None:
    write_workflow(
        tmp_path,
        '\n'.join(
            [
                'tags:',
                '  - "companion-v*"',
                'run: python tools/tag_preflight.py --tag "$GITHUB_REF_NAME"',
                'run: python tools/resource_manifest.py --output PUBLIC_RESOURCE_MANIFEST.json',
            ]
        ),
    )
    issues = workflow_issues(tmp_path)
    assert any("manifest verification step" in item for item in issues)


def test_missing_release_workflow_is_reported(tmp_path: Path) -> None:
    assert workflow_issues(tmp_path) == [
        "missing .github/workflows/release-manifest.yml"
    ]
