import unittest

from src.retry import retry_once


class RetryTests(unittest.TestCase):
    def test_returns_the_operation_value(self):
        self.assertEqual(retry_once(lambda: "ok"), "ok")

    def test_allows_a_second_attempt_after_timeout(self):
        outcomes = iter([TimeoutError("temporary"), "done"])

        def next_outcome():
            outcome = next(outcomes)
            if isinstance(outcome, Exception):
                raise outcome
            return outcome

        self.assertEqual(retry_once(next_outcome), "done")


if __name__ == "__main__":
    unittest.main()
