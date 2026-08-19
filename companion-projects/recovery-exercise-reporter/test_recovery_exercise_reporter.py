import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("recovery_exercise_reporter.py")
SPEC = importlib.util.spec_from_file_location("recovery_exercise_reporter", MODULE_PATH)
recovery_exercise_reporter = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(recovery_exercise_reporter)


class RecoveryExerciseReporterTests(unittest.TestCase):
    def test_summary_and_follow_up_count(self) -> None:
        csv_text = (
            "exercise_id,objective,result,duration_minutes,observations\n"
            "REC-001,Restore training service,pass,30,Synthetic exercise completed\n"
            "REC-002,Review alternate process,partial,60,Follow-up item recorded\n"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "exercises.csv"
            path.write_text(csv_text, encoding="utf-8")
            result = recovery_exercise_reporter.summarize(path)

        self.assertEqual(result["exercises"], 2)
        self.assertEqual(result["average_duration_minutes"], 45.0)
        self.assertEqual(result["needs_follow_up"], 1)

    def test_negative_duration_is_rejected(self) -> None:
        csv_text = "exercise_id,objective,result,duration_minutes,observations\nREC-1,Training,pass,-1,Test\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "exercises.csv"
            path.write_text(csv_text, encoding="utf-8")
            with self.assertRaises(ValueError):
                recovery_exercise_reporter.summarize(path)


if __name__ == "__main__":
    unittest.main()
