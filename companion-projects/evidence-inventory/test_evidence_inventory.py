import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("evidence_inventory.py")
SPEC = importlib.util.spec_from_file_location("evidence_inventory", MODULE_PATH)
evidence_inventory = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(evidence_inventory)


class EvidenceInventoryTests(unittest.TestCase):
    def test_collects_relative_paths_and_hashes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "evidence"
            root.mkdir()
            (root / "note.txt").write_text("synthetic evidence", encoding="utf-8")
            rows = evidence_inventory.collect(root)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["path"], "note.txt")
        self.assertEqual(len(rows[0]["sha256"]), 64)

    def test_writes_csv_header(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "inventory.csv"
            evidence_inventory.write_csv([], output)
            with output.open("r", encoding="utf-8", newline="") as handle:
                header = next(csv.reader(handle))

        self.assertEqual(header, evidence_inventory.FIELDNAMES)


if __name__ == "__main__":
    unittest.main()
