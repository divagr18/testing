import unittest
from src.taskboard import Task
from src.taskboard.formatting import render_task, render_tasks


class FormattingTests(unittest.TestCase):
    def test_renders_a_task(self):
        self.assertEqual(render_task(Task(1, "Ship demo", "doing", "high")), "#1 [doing] (high) Ship demo")

    def test_renders_empty_collection(self):
        self.assertEqual(render_tasks([]), "No tasks yet.")
