import unittest
from unittest.mock import patch
from src.taskboard.cli import main


class CliTests(unittest.TestCase):
    def test_filters_the_demo_board(self):
        with patch("builtins.print") as output:
            self.assertEqual(main(["--status", "doing"]), 0)
        self.assertIn("Record Pull Guard", output.call_args.args[0])
