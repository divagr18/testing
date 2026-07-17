from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Retry a failed operation once."""
    try:
        return operation()
    except Exception:
        return operation()
