import unittest
from src.taskboard import Task
from src.taskboard.filters import matching


class FilterTests(unittest.TestCase):
    def test_matches_title_without_case_sensitivity(self):
        tasks = [Task(1, "Record demo"), Task(2, "Write docs")]
        self.assertEqual(matching(tasks, "DEMO"), [tasks[0]])
