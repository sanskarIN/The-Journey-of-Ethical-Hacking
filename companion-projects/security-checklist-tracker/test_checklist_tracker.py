import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("checklist_tracker.py")
SPEC = importlib.util.spec_from_file_location("checklist_tracker", MODULE_PATH)
checklist_tracker = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(checklist_tracker)


class ChecklistTrackerTests(unittest.TestCase):
    def test_summary(self) -> None:
        text = "- [x] Verify backups\n- [ ] Review access\n- [X] Update inventory\n"
        result = checklist_tracker.summarize(text)
        self.assertEqual(result["total"], 3)
        self.assertEqual(result["completed"], 2)
        self.assertEqual(result["pending"], 1)
        self.assertEqual(result["pending_items"], ["Review access"])

    def test_empty_checklist(self) -> None:
        result = checklist_tracker.summarize("# Notes\nNo tasks here.\n")
        self.assertEqual(result["total"], 0)
        self.assertEqual(result["completion_percent"], 0.0)


if __name__ == "__main__":
    unittest.main()
