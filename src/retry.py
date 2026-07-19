from collections.abc import Callable
from dataclasses import dataclass


def retry_once(operation: Callable[[], object]) -> object:
    """Run one operation without retrying it yet."""
    return operation()


@dataclass(frozen=True)
class RetryDiagnostic:
    attempts: int
    error_type: str
    message: str


def build_retry_diagnostic(error: Exception, attempts: int) -> RetryDiagnostic:
    """Capture structured retry diagnostics for callers that log failures."""
    return RetryDiagnostic(attempts=attempts, error_type=type(error).__name__, message=str(error))
