from pathlib import Path

from tools.release_readiness import candidate_workflow_issues, workflow_issues


def write_workflow(root: Path, name: str, text: str) -> None:
    path = root / ".github" / "workflows" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_release_workflow_with_required_steps_passes(tmp_path: Path) -> None:
    write_workflow(
        tmp_path,
        "release-manifest.yml",
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
        "release-manifest.yml",
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


def test_candidate_workflow_with_required_steps_passes(tmp_path: Path) -> None:
    write_workflow(
        tmp_path,
        "release-candidate.yml",
        '\n'.join(
            [
                'workflow_dispatch:',
                'run: python tools/release_readiness.py --check',
                'run: python tools/resource_manifest.py --output PUBLIC_RESOURCE_MANIFEST.json',
                'run: python tools/manifest_verify.py PUBLIC_RESOURCE_MANIFEST.json',
                'uses: actions/upload-artifact@0123456789012345678901234567890123456789',
            ]
        ),
    )
    assert candidate_workflow_issues(tmp_path) == []


def test_candidate_workflow_missing_readiness_is_reported(tmp_path: Path) -> None:
    write_workflow(
        tmp_path,
        "release-candidate.yml",
        '\n'.join(
            [
                'workflow_dispatch:',
                'run: python tools/resource_manifest.py --output PUBLIC_RESOURCE_MANIFEST.json',
                'run: python tools/manifest_verify.py PUBLIC_RESOURCE_MANIFEST.json',
                'uses: actions/upload-artifact@0123456789012345678901234567890123456789',
            ]
        ),
    )
    issues = candidate_workflow_issues(tmp_path)
    assert any("release readiness step" in item for item in issues)
