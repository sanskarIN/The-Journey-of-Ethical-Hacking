import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("patch_register_summary.py")
SPEC = importlib.util.spec_from_file_location("patch_register_summary", MODULE_PATH)
patch_register_summary = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(patch_register_summary)


class PatchRegisterSummaryTests(unittest.TestCase):
    def test_open_patch_summary(self) -> None:
        csv_text = (
            "asset,patch_id,status,age_days\n"
            "lab-1,KB-001,installed,2\n"
            "lab-2,KB-002,pending,12\n"
            "lab-3,KB-003,failed,20\n"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "patches.csv"
            path.write_text(csv_text, encoding="utf-8")
            result = patch_register_summary.summarize(path)

        self.assertEqual(result["patch_records"], 3)
        self.assertEqual(result["open_items"], 2)
        self.assertEqual(result["oldest_open_age_days"], 20)

    def test_negative_age_is_rejected(self) -> None:
        csv_text = "asset,patch_id,status,age_days\nlab,KB-001,pending,-1\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "patches.csv"
            path.write_text(csv_text, encoding="utf-8")
            with self.assertRaises(ValueError):
                patch_register_summary.summarize(path)


if __name__ == "__main__":
    unittest.main()
