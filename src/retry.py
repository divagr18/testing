from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Make at most two attempts, preserving the final timeout."""
    last_timeout: TimeoutError | None = None
    for _attempt in range(2):
        try:
            return operation()
        except TimeoutError as error:
            last_timeout = error
    raise last_timeout
