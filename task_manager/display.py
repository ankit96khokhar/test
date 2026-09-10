"""
Display helpers for rendering tasks in the terminal.
"""

from typing import List

from task_manager.models import Priority, Status, Task

# ANSI colours
_RESET = "\033[0m"
_BOLD = "\033[1m"
_RED = "\033[31m"
_YELLOW = "\033[33m"
_GREEN = "\033[32m"
_CYAN = "\033[36m"
_GREY = "\033[90m"


def _priority_color(priority: Priority) -> str:
    return {
        Priority.HIGH: _RED,
        Priority.MEDIUM: _YELLOW,
        Priority.LOW: _GREEN,
    }.get(priority, _RESET)


def _status_color(status: Status) -> str:
    return {
        Status.PENDING: _GREY,
        Status.IN_PROGRESS: _CYAN,
        Status.DONE: _GREEN,
    }.get(status, _RESET)


def print_task(task: Task) -> None:
    """Print a single task in a human-readable format."""
    pc = _priority_color(task.priority)
    sc = _status_color(task.status)

    print(
        f"{_BOLD}[{task.id}]{_RESET} {task.title} "
        f"| Priority: {pc}{task.priority.value.upper()}{_RESET} "
        f"| Status: {sc}{task.status.value.replace('_', ' ').upper()}{_RESET}"
    )
    if task.description:
        print(f"     {_GREY}{task.description}{_RESET}")


def print_task_list(tasks: List[Task]) -> None:
    """Print a list of tasks with a header."""
    if not tasks:
        print("No tasks found.")
        return

    print(f"\n{'─' * 60}")
    for task in tasks:
        print_task(task)
    print(f"{'─' * 60}")
    print(f"Total: {len(tasks)} task(s)\n")


def print_success(message: str) -> None:
    print(f"{_GREEN}✔ {message}{_RESET}")


def print_error(message: str) -> None:
    print(f"{_RED}✖ {message}{_RESET}")


def print_info(message: str) -> None:
    print(f"{_CYAN}ℹ {message}{_RESET}")
