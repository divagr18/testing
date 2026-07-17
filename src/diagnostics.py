def describe_retry_failure(operation: str, attempts: int, error: Exception) -> dict[str, object]:
    """Return retry context in a form callers can log or serialize."""
    return {
        "operation": operation,
        "attempts": attempts,
        "error_type": type(error).__name__,
        "message": str(error),
    }
