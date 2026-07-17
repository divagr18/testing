import unittest

from src.diagnostics import RetryDiagnostic


class RetryDiagnosticTests(unittest.TestCase):
    def test_summary_names_operation_attempts_and_error(self):
        diagnostic = RetryDiagnostic("fetch profile", 2, "timeout")
        self.assertEqual(
            diagnostic.summary(),
            "fetch profile failed after 2 attempts: timeout",
        )


if __name__ == "__main__":
    unittest.main()
