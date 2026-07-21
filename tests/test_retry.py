import unittest

from src.retry import retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_propagates_operation_failures(self):
        def failing_operation():
            raise RuntimeError("temporary failure")

        with self.assertRaisesRegex(RuntimeError, "temporary failure"):
            retry_once(failing_operation)


if __name__ == "__main__":
    unittest.main()
