from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Retry a transient value failure exactly once."""
    try:
        return operation()
    except ValueError:
        return operation()
