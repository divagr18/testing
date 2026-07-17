def describe_retry_failure(error: Exception) -> str:
    """Make a retry failure easier to spot in logs."""
    return f"retry failed: {error}"
