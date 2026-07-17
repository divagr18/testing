def normalize_display_name(value: str) -> str:
    """Turn inconsistent user input into a stable display label."""
    return " ".join(value.strip().split()).title()
