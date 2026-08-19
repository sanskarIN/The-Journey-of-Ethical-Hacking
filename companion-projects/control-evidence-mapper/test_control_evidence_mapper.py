import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("control_evidence_mapper.py")
SPEC = importlib.util.spec_from_file_location("control_evidence_mapper", MODULE_PATH)
control_evidence_mapper = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(control_evidence_mapper)


class ControlEvidenceMapperTests(unittest.TestCase):
    def test_unknown_control_is_reported(self) -> None:
        csv_text = (
            "evidence_id,control,status,owner\n"
            "EV-001,CTRL-LOGGING,current,alex\n"
            "EV-002,CTRL-UNKNOWN,stale,casey\n"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "evidence.csv"
            path.write_text(csv_text, encoding="utf-8")
            result = control_evidence_mapper.map_evidence(path, {"CTRL-LOGGING"})

        self.assertEqual(result["evidence_records"], 2)
        self.assertEqual(result["by_status"], {"current": 1, "stale": 1})
        self.assertEqual(len(result["unknown_controls"]), 1)

    def test_empty_control_policy_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "controls.json"
            path.write_text('{"controls": []}', encoding="utf-8")
            with self.assertRaises(ValueError):
                control_evidence_mapper.load_controls(path)


if __name__ == "__main__":
    unittest.main()
