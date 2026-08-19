import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("asset_inventory_summary.py")
SPEC = importlib.util.spec_from_file_location("asset_inventory_summary", MODULE_PATH)
asset_inventory_summary = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(asset_inventory_summary)


class AssetInventorySummaryTests(unittest.TestCase):
    def test_summary_and_review_flags(self) -> None:
        csv_text = (
            "asset,type,owner,status\n"
            "lab-host-1,workstation,alex,active\n"
            "lab-db-1,database,,unknown\n"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "assets.csv"
            path.write_text(csv_text, encoding="utf-8")
            result = asset_inventory_summary.summarize(path)

        self.assertEqual(result["assets"], 2)
        self.assertEqual(result["by_type"], {"database": 1, "workstation": 1})
        self.assertEqual(len(result["needs_review"]), 1)

    def test_invalid_status_is_rejected(self) -> None:
        csv_text = "asset,type,owner,status\nlab,server,alex,invalid\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "assets.csv"
            path.write_text(csv_text, encoding="utf-8")
            with self.assertRaises(ValueError):
                asset_inventory_summary.summarize(path)


if __name__ == "__main__":
    unittest.main()
