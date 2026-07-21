import unittest
from src.taskboard import Task
from src.taskboard.sorting import by_priority


class SortingTests(unittest.TestCase):
    def test_sorts_high_priority_first(self):
        self.assertEqual([t.id for t in by_priority([Task(1, "A", priority="low"), Task(2, "B", priority="high")])], [2, 1])
