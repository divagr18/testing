from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Run one operation without retrying it yet."""
    return operation()


def retry_diagnostic_fields(error: Exception, attempts: int) -> dict[str, object]:
    """Expose retry diagnostics as simple log-friendly fields."""
    return {
        "attempts": attempts,
        "error_type": type(error).__name__,
        "message": str(error),
        "retryable": isinstance(error, TimeoutError),
    }
