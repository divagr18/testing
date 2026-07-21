import unittest
from src.taskboard.seed import demo_board


class SeedTests(unittest.TestCase):
    def test_provides_an_interesting_demo_state(self):
        self.assertEqual([task.status for task in demo_board().list()], ["doing", "todo", "todo"])
