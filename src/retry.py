from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Retry one TimeoutError exactly once."""
    try:
        return operation()
    except TimeoutError:
        return operation()
