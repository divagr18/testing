def timeout_seconds(value: str | None, default: int = 30) -> int:
    """Read a positive timeout from a text configuration value."""
    if value is None:
        return default
    parsed = int(value)
    if parsed < 1:
        raise ValueError("timeout must be positive")
    return parsed
