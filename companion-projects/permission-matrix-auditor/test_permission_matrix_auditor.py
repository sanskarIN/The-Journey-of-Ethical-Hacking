import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("permission_matrix_auditor.py")
SPEC = importlib.util.spec_from_file_location("permission_matrix_auditor", MODULE_PATH)
permission_matrix_auditor = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(permission_matrix_auditor)


class PermissionMatrixAuditorTests(unittest.TestCase):
    def test_unapproved_permission_and_unknown_resource(self) -> None:
        csv_text = (
            "principal,resource,permission\n"
            "alex,reports,read\n"
            "casey,reports,delete\n"
            "jordan,unknown,read\n"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "assignments.csv"
            path.write_text(csv_text, encoding="utf-8")
            result = permission_matrix_auditor.audit(path, {"reports": {"read", "write"}})

        self.assertEqual(result["assignments"], 3)
        self.assertEqual(len(result["violations"]), 2)
        self.assertEqual(result["violations"][0]["reason"], "unapproved-permission")
        self.assertEqual(result["violations"][1]["reason"], "unknown-resource")

    def test_empty_field_is_rejected(self) -> None:
        csv_text = "principal,resource,permission\nalex,reports,\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "assignments.csv"
            path.write_text(csv_text, encoding="utf-8")
            with self.assertRaises(ValueError):
                permission_matrix_auditor.audit(path, {"reports": {"read"}})


if __name__ == "__main__":
    unittest.main()
