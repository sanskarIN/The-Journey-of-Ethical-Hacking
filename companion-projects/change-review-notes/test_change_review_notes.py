import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("change_review_notes.py")
SPEC = importlib.util.spec_from_file_location("change_review_notes", MODULE_PATH)
change_review_notes = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(change_review_notes)


class ChangeReviewNotesTests(unittest.TestCase):
    def test_load_and_render(self) -> None:
        csv_text = (
            "change_id,system,owner,summary,risk,approved\n"
            "CHG-001,lab-app,alex,Enable audit logging,low,true\n"
            "CHG-002,lab-db,casey,Review retention,medium,false\n"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "changes.csv"
            path.write_text(csv_text, encoding="utf-8")
            changes = change_review_notes.load(path)
            markdown = change_review_notes.render(changes)

        self.assertEqual(len(changes), 2)
        self.assertIn("CHG-001", markdown)
        self.assertIn("Approved: no", markdown)

    def test_bad_risk_is_rejected(self) -> None:
        csv_text = "change_id,system,owner,summary,risk,approved\nCHG-1,lab,alex,test,urgent,true\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "changes.csv"
            path.write_text(csv_text, encoding="utf-8")
            with self.assertRaises(ValueError):
                change_review_notes.load(path)


if __name__ == "__main__":
    unittest.main()
