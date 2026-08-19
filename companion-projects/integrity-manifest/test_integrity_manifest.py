import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("integrity_manifest.py")
SPEC = importlib.util.spec_from_file_location("integrity_manifest", MODULE_PATH)
integrity_manifest = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(integrity_manifest)


class IntegrityManifestTests(unittest.TestCase):
    def test_create_and_verify(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            root = base / "data"
            root.mkdir()
            (root / "a.txt").write_text("alpha", encoding="utf-8")
            manifest = base / "manifest.json"

            integrity_manifest.create_manifest(root, manifest)
            result = integrity_manifest.verify_manifest(root, manifest)

        self.assertEqual(result["changed"], [])
        self.assertEqual(result["missing"], [])
        self.assertEqual(result["unexpected"], [])
        self.assertEqual(result["ok"], ["a.txt"])

    def test_changed_file_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            root = base / "data"
            root.mkdir()
            path = root / "a.txt"
            path.write_text("alpha", encoding="utf-8")
            manifest = base / "manifest.json"
            integrity_manifest.create_manifest(root, manifest)
            path.write_text("beta", encoding="utf-8")
            result = integrity_manifest.verify_manifest(root, manifest)

        self.assertEqual(result["changed"], ["a.txt"])


if __name__ == "__main__":
    unittest.main()
