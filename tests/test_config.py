import unittest

from src.config import timeout_seconds


class ConfigTests(unittest.TestCase):
    def test_uses_default_and_explicit_timeout(self):
        self.assertEqual(timeout_seconds(None), 30)
        self.assertEqual(timeout_seconds("45"), 45)

    def test_rejects_non_positive_timeout(self):
        with self.assertRaises(ValueError):
            timeout_seconds("0")


if __name__ == "__main__":
    unittest.main()
