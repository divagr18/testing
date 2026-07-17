from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Run an operation once more after its first failure."""
    try:
        return operation()
    except Exception:
        return operation()
