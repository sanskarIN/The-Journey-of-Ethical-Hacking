import tempfile
import unittest
from pathlib import Path

from tools.companion_projects_check import REQUIRED_SUITE_FILES, validate


class CompanionProjectsCheckTests(unittest.TestCase):
    def make_suite(self, root: Path) -> Path:
        suite = root / "companion-projects"
        suite.mkdir()
        for name in REQUIRED_SUITE_FILES:
            (suite / name).write_text("# Placeholder\n", encoding="utf-8")
        self.write_catalog(suite, [])
        return suite

    def write_catalog(self, suite: Path, names: list[str], *, offline: bool = True) -> None:
        catalog = "# Defensive Companion Projects\n\n" + "\n".join(
            f"- `{name}`" for name in names
        )
        (suite / "README.md").write_text(catalog + "\n", encoding="utf-8")

        network = "No" if offline else "Yes"
        rows = "\n".join(
            f"| {name} | Defensive review | CSV | {network} | Yes |" for name in names
        )
        matrix = (
            "# Companion Project Matrix\n\n"
            "| Project | Primary defensive skill | Input | Network access | Tests |\n"
            "|---|---|---|---|---|\n"
            f"{rows}\n"
        )
        (suite / "PROJECT_MATRIX.md").write_text(matrix, encoding="utf-8")

    def add_project(self, suite: Path, name: str) -> Path:
        project = suite / name
        project.mkdir()
        (project / "README.md").write_text("# Sample\n", encoding="utf-8")
        (project / "sample.py").write_text("print('sample')\n", encoding="utf-8")
        (project / "test_sample.py").write_text("pass\n", encoding="utf-8")
        self.write_catalog(suite, [path.name for path in sorted(suite.iterdir()) if path.is_dir()])
        return project

    def test_complete_project_is_valid(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            suite = self.make_suite(Path(temp_dir))
            self.add_project(suite, "sample-project")

            statuses, errors = validate(suite, minimum_projects=1)

        self.assertEqual(errors, [])
        self.assertEqual(len(statuses), 1)
        self.assertEqual(statuses[0].name, "sample-project")

    def test_missing_readme_and_tests_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            suite = self.make_suite(Path(temp_dir))
            project = suite / "incomplete-project"
            project.mkdir()
            (project / "tool.py").write_text("pass\n", encoding="utf-8")
            self.write_catalog(suite, ["incomplete-project"])

            _, errors = validate(suite, minimum_projects=1)

        self.assertIn("incomplete-project: missing README.md", errors)
        self.assertIn("incomplete-project: no unit test file found", errors)

    def test_project_floor_prevents_silent_deletion(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            suite = self.make_suite(Path(temp_dir))
            _, errors = validate(suite, minimum_projects=20)

        self.assertIn("expected at least 20 companion projects, found 0", errors)

    def test_missing_catalog_entry_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            suite = self.make_suite(Path(temp_dir))
            self.add_project(suite, "sample-project")
            (suite / "README.md").write_text("# Defensive Companion Projects\n", encoding="utf-8")

            _, errors = validate(suite, minimum_projects=1)

        self.assertIn(
            "sample-project: missing from companion-projects/README.md catalog",
            errors,
        )

    def test_matrix_row_count_drift_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            suite = self.make_suite(Path(temp_dir))
            self.add_project(suite, "sample-project")
            self.write_catalog(suite, [])
            (suite / "README.md").write_text(
                "# Defensive Companion Projects\n\n- `sample-project`\n",
                encoding="utf-8",
            )

            _, errors = validate(suite, minimum_projects=1)

        self.assertTrue(any("PROJECT_MATRIX.md project row count" in error for error in errors))

    def test_network_enabled_matrix_row_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            suite = self.make_suite(Path(temp_dir))
            self.add_project(suite, "sample-project")
            self.write_catalog(suite, ["sample-project"], offline=False)

            _, errors = validate(suite, minimum_projects=1)

        self.assertTrue(any("must keep current projects offline" in error for error in errors))

    def test_project_readme_requires_h1(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            suite = self.make_suite(Path(temp_dir))
            project = self.add_project(suite, "sample-project")
            (project / "README.md").write_text("Sample\n", encoding="utf-8")

            _, errors = validate(suite, minimum_projects=1)

        self.assertIn(
            "sample-project: README.md must start with a level-1 heading",
            errors,
        )


if __name__ == "__main__":
    unittest.main()
