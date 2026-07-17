def describe_retry_failure(operation: str, attempts: int, error: Exception) -> dict[str, object]:
    """Return a compact, structured account of a retry failure for callers to log."""
    return {
        "operation": operation,
        "attempts": attempts,
        "error_type": type(error).__name__,
        "message": str(error),
        "retryable": True,
    }
