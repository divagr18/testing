def normalize_name(value: str) -> str:
    """Normalize display names supplied by a request."""
    return value.strip().lower()
