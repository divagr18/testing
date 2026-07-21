import unittest
from src.taskboard import Task
from src.taskboard.stats import status_counts


class StatsTests(unittest.TestCase):
    def test_counts_each_workflow_status(self):
        tasks = [Task(1, "A"), Task(2, "B", "done"), Task(3, "C", "done")]
        self.assertEqual(status_counts(tasks), {"todo": 1, "doing": 0, "done": 2})
