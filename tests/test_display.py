import unittest

from src.display import normalize_display_name


class DisplayNameTests(unittest.TestCase):
    def test_trims_collapses_and_titles_a_name(self):
        self.assertEqual(normalize_display_name("  pull   guard  "), "Pull Guard")


if __name__ == "__main__":
    unittest.main()
