import unittest

from src.names import normalize_name


class NameTests(unittest.TestCase):
    def test_trims_and_lowercases_names(self):
        self.assertEqual(normalize_name("  Ada  "), "ada")


if __name__ == "__main__":
    unittest.main()
