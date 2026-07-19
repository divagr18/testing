import unittest

from src.retry import retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_returns_the_second_attempt_value(self):
        attempts = iter((TimeoutError("first"), "ok"))

        def operation():
            result = next(attempts)
            if isinstance(result, Exception):
                raise result
            return result

        self.assertEqual(retry_once(operation), "ok")

    def test_raises_the_final_timeout(self):
        with self.assertRaisesRegex(TimeoutError, "second"):
            retry_once(lambda: (_ for _ in ()).throw(TimeoutError("second")))


if __name__ == "__main__":
    unittest.main()
