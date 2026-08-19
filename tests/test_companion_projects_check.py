import tempfile
import unittest
from pathlib import Path

from tools.companion_projects_check import REQUIRED_SUITE_FILES, validate


class CompanionProjectsCheckTests(unittest.TestCase):
    def make_suite(self, root: Path) -> Path:
        suite = root / "companion-projects"
        suite.mkdir()
        for name in REQUIRED_SUITE_FILES:
            (suite / name).write_text("placeholder\n", encoding="utf-8")
        return suite

    def test_complete_project_is_valid(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            suite = self.make_suite(Path(temp_dir))
            project = suite / "sample-project"
            project.mkdir()
            (project / "README.md").write_text("# Sample\n", encoding="utf-8")
            (project / "sample.py").write_text("print('sample')\n", encoding="utf-8")
            (project / "test_sample.py").write_text("pass\n", encoding="utf-8")

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

            _, errors = validate(suite, minimum_projects=1)

        self.assertIn("incomplete-project: missing README.md", errors)
        self.assertIn("incomplete-project: no unit test file found", errors)

    def test_project_floor_prevents_silent_deletion(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            suite = self.make_suite(Path(temp_dir))
            _, errors = validate(suite, minimum_projects=20)

        self.assertIn("expected at least 20 companion projects, found 0", errors)


if __name__ == "__main__":
    unittest.main()
