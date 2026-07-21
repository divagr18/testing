import unittest

from src.taskboard import Board, TaskNotFoundError


class BoardTests(unittest.TestCase):
    def test_adds_and_lists_tasks(self):
        board = Board()
        task = board.add("Record the demo", priority="high")

        self.assertEqual(task.id, 1)
        self.assertEqual(board.list(), [task])

    def test_rejects_blank_title(self):
        with self.assertRaises(ValueError):
            Board().add("  ")

    def test_moves_a_task(self):
        board = Board()
        task = board.add("Review queue")

        self.assertEqual(board.move(task.id, "done").status, "done")

    def test_missing_task_is_explicit(self):
        with self.assertRaises(TaskNotFoundError):
            Board().get(99)
