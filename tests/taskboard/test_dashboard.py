import unittest
from src.taskboard import Task
from src.taskboard.dashboard import group_by_status


class DashboardTests(unittest.TestCase):
    def test_places_tasks_in_workflow_columns(self):
        groups = group_by_status([Task(1, "A"), Task(2, "B", "done")])
        self.assertEqual([task.id for task in groups["done"]], [2])
