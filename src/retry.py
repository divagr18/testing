from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Retry a transient runtime failure exactly once."""
    try:
        return operation()
    except RuntimeError:
        return operation()
