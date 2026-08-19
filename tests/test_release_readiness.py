from pathlib import Path

import tools.release_readiness as release_readiness
from tools.release_readiness import candidate_workflow_issues, workflow_issues


def write_workflow(root: Path, name: str, text: str) -> None:
    path = root / ".github" / "workflows" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def full_quality_steps() -> list[str]:
    return [
        'run: python -m pip install -r requirements-dev.txt',
        'run: python -m compileall -q tools tests companion-projects',
        'run: python -m pytest --cov=tools -q',
        'run: python companion-projects/run_tests.py',
        'run: python tools/companion_projects_check.py --root .',
    ]


def test_release_workflow_with_required_steps_passes(tmp_path: Path) -> None:
    write_workflow(
        tmp_path,
        "release-manifest.yml",
        '\n'.join(
            [
                'tags:',
                '  - "companion-v*"',
                *full_quality_steps(),
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
                *full_quality_steps(),
                'run: python tools/tag_preflight.py --tag "$GITHUB_REF_NAME"',
                'run: python tools/resource_manifest.py --output PUBLIC_RESOURCE_MANIFEST.json',
            ]
        ),
    )
    issues = workflow_issues(tmp_path)
    assert any("manifest verification step" in item for item in issues)


def test_release_workflow_missing_companion_tests_is_reported(tmp_path: Path) -> None:
    steps = [step for step in full_quality_steps() if "run_tests.py" not in step]
    write_workflow(
        tmp_path,
        "release-manifest.yml",
        '\n'.join(
            [
                'tags:',
                '  - "companion-v*"',
                *steps,
                'run: python tools/tag_preflight.py --tag "$GITHUB_REF_NAME"',
                'run: python tools/resource_manifest.py --output PUBLIC_RESOURCE_MANIFEST.json',
                'run: python tools/manifest_verify.py PUBLIC_RESOURCE_MANIFEST.json',
            ]
        ),
    )
    issues = workflow_issues(tmp_path)
    assert any("project-owned companion tests" in item for item in issues)


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
                *full_quality_steps(),
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
                *full_quality_steps(),
                'run: python tools/resource_manifest.py --output PUBLIC_RESOURCE_MANIFEST.json',
                'run: python tools/manifest_verify.py PUBLIC_RESOURCE_MANIFEST.json',
                'uses: actions/upload-artifact@0123456789012345678901234567890123456789',
            ]
        ),
    )
    issues = candidate_workflow_issues(tmp_path)
    assert any("release readiness step" in item for item in issues)


def test_candidate_workflow_missing_compilation_is_reported(tmp_path: Path) -> None:
    steps = [step for step in full_quality_steps() if "compileall" not in step]
    write_workflow(
        tmp_path,
        "release-candidate.yml",
        '\n'.join(
            [
                'workflow_dispatch:',
                *steps,
                'run: python tools/release_readiness.py --check',
                'run: python tools/resource_manifest.py --output PUBLIC_RESOURCE_MANIFEST.json',
                'run: python tools/manifest_verify.py PUBLIC_RESOURCE_MANIFEST.json',
                'uses: actions/upload-artifact@0123456789012345678901234567890123456789',
            ]
        ),
    )
    issues = candidate_workflow_issues(tmp_path)
    assert any("Python compilation step" in item for item in issues)


def test_render_uses_release_branch_for_ready_candidate(tmp_path: Path, monkeypatch) -> None:
    (tmp_path / "COMPANION_RELEASE.json").write_text(
        '{"companion_release":"2026.08.19.1"}', encoding="utf-8"
    )
    monkeypatch.setattr(release_readiness, "collect", lambda root: [])
    monkeypatch.setattr(
        release_readiness,
        "expected_tag",
        lambda root: "companion-v2026.08.19.1",
    )

    text = release_readiness.render(tmp_path)

    assert "release/companion-v2026.08.19.1" in text
    assert "reviewed release-branch commit" in text
    assert "does not create a Git branch, Git tag" in text
