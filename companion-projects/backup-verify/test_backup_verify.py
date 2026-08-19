import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("backup_verify.py")
SPEC = importlib.util.spec_from_file_location("backup_verify", MODULE_PATH)
backup_verify = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(backup_verify)


class BackupVerifyTests(unittest.TestCase):
    def test_matching_directories(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            primary = base / "primary"
            backup = base / "backup"
            primary.mkdir()
            backup.mkdir()
            (primary / "a.txt").write_text("same", encoding="utf-8")
            (backup / "a.txt").write_text("same", encoding="utf-8")
            result = backup_verify.compare(primary, backup)

        self.assertEqual(result["matching"], ["a.txt"])
        self.assertEqual(result["changed"], [])

    def test_changed_and_missing_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            primary = base / "primary"
            backup = base / "backup"
            primary.mkdir()
            backup.mkdir()
            (primary / "a.txt").write_text("new", encoding="utf-8")
            (backup / "a.txt").write_text("old", encoding="utf-8")
            (primary / "b.txt").write_text("only primary", encoding="utf-8")
            result = backup_verify.compare(primary, backup)

        self.assertEqual(result["changed"], ["a.txt"])
        self.assertEqual(result["missing_from_backup"], ["b.txt"])


if __name__ == "__main__":
    unittest.main()
