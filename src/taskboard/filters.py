"""Query helpers for task lists."""
from .board import Task


def matching(tasks: list[Task], text: str) -> list[Task]:
    needle = text.casefold().strip()
    return [task for task in tasks if needle in task.title.casefold()]
