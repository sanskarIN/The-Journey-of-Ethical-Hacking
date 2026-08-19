import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("incident_timeline.py")
SPEC = importlib.util.spec_from_file_location("incident_timeline", MODULE_PATH)
incident_timeline = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(incident_timeline)


class IncidentTimelineTests(unittest.TestCase):
    def test_events_are_sorted(self) -> None:
        data = (
            '{"timestamp":"2026-08-19T01:02:00Z","category":"auth","summary":"Second","asset":"lab-1"}\n'
            '{"timestamp":"2026-08-19T01:01:00Z","category":"system","summary":"First","asset":"lab-2"}\n'
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "events.jsonl"
            path.write_text(data, encoding="utf-8")
            events = incident_timeline.load_events(path)

        self.assertEqual(events[0]["summary"], "First")
        self.assertEqual(events[1]["summary"], "Second")

    def test_markdown_escapes_pipes(self) -> None:
        markdown = incident_timeline.render_markdown([
            {"timestamp": "2026-08-19T01:00:00Z", "category": "note", "summary": "a|b", "asset": "lab"}
        ])
        self.assertIn("a\\|b", markdown)


if __name__ == "__main__":
    unittest.main()
