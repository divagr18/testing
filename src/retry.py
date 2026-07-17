from collections.abc import Callable


def retry_once(operation: Callable[[], object]) -> object:
    """Attempt the operation twice, returning the first successful result."""
    last_error: Exception | None = None
    for _ in range(2):
        try:
            return operation()
        except Exception as error:
            last_error = error
    assert last_error is not None
    raise last_error
