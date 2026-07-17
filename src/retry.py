from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Run one operation without retrying it yet."""
    return operation()


def timeout_error_name(error: BaseException) -> str:
    """Return the concrete error type name for retry diagnostics."""
    return type(error).__name__
