"""Human-friendly task board rendering."""
from .board import Task


def render_task(task: Task) -> str:
    return f"#{task.id} [{task.status}] ({task.priority}) {task.title}"


def render_tasks(tasks: list[Task]) -> str:
    return "\n".join(render_task(task) for task in tasks) or "No tasks yet."
