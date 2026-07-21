"""Dashboard-specific grouping helpers."""
from .board import Task
from .sorting import by_priority


def group_by_status(tasks: list[Task], *, limit: int | None = None) -> dict[str, list[Task]]:
    """Build sorted workflow columns, optionally capping each visible list.

    This supersedes the unbounded dashboard proposal with a view that is useful
    for a real queue while still retaining the count badges for hidden work.
    """
    if limit is not None and limit < 1:
        raise ValueError("Dashboard limit must be positive.")
    groups = {"todo": [], "doing": [], "done": []}
    for task in tasks:
        groups[task.status].append(task)
    ordered = {status: by_priority(items) for status, items in groups.items()}
    if limit is not None:
        return {status: items[:limit] for status, items in ordered.items()}
    return ordered


def column_totals(tasks: list[Task]) -> dict[str, int]:
    """Return a compact badge count for each workflow column."""
    return {status: len(items) for status, items in group_by_status(tasks).items()}
