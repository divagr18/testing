from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Retry one transient timeout and preserve every other failure."""
    try:
        return operation()
    except TimeoutError:
        return operation()
