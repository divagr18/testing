import unittest

from src.retry import retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_retries_a_timeout_once(self):
        calls = 0

        def operation():
            nonlocal calls
            calls += 1
            if calls == 1:
                raise TimeoutError("first")
            return "recovered"

        self.assertEqual(retry_once(operation), "recovered")

    def test_keeps_the_first_timeout_as_context(self):
        with self.assertRaisesRegex(TimeoutError, "two timeout") as captured:
            retry_once(lambda: (_ for _ in ()).throw(TimeoutError("first")))
        self.assertIsInstance(captured.exception.__cause__, TimeoutError)


if __name__ == "__main__":
    unittest.main()
