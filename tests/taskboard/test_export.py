import unittest
from src.taskboard import Task
from src.taskboard.export import to_json


class ExportTests(unittest.TestCase):
    def test_exports_stable_json(self):
        self.assertIn('"title": "Record demo"', to_json([Task(1, "Record demo")]))
