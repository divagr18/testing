import unittest
from src.taskboard import Task
from src.taskboard.report import progress_line


class ReportTests(unittest.TestCase):
    def test_summarises_progress(self):
        self.assertEqual(progress_line([Task(1, "A", "done"), Task(2, "B", "doing")]), "1/2 complete · 1 in progress")
