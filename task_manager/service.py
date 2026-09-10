"""
Core service layer containing business logic for managing tasks.
"""

from typing import List, Optional

from task_manager.models import Priority, Status, Task
from task_manager.storage import Storage


class TaskService:
    """Provides CRUD operations and filtering for tasks."""

    def __init__(self, storage: Optional[Storage] = None):
        self.storage = storage or Storage()
        self._tasks: List[Task] = self.storage.load()
        self._next_id: int = self._compute_next_id()

    # ------------------------------------------------------------------ #
    #  Private helpers                                                     #
    # ------------------------------------------------------------------ #

    def _compute_next_id(self) -> int:
        if not self._tasks:
            return 1
        return max(t.id for t in self._tasks) + 1

    def _find_by_id(self, task_id: int) -> Optional[Task]:
        return next((t for t in self._tasks if t.id == task_id), None)

    def _persist(self) -> None:
        self.storage.save(self._tasks)

    # ------------------------------------------------------------------ #
    #  Public API                                                          #
    # ------------------------------------------------------------------ #

    def add(self, title: str, description: str = "", priority: str = "medium") -> Task:
        """Create and persist a new task."""
        task = Task(title=title, description=description, priority=Priority(priority))
        task.id = self._next_id
        self._next_id += 1
        self._tasks.append(task)
        self._persist()
        return task

    def list_all(self) -> List[Task]:
        """Return all tasks."""
        return list(self._tasks)

    def filter_by_status(self, status: str) -> List[Task]:
        """Return tasks matching the given status."""
        target = Status(status)
        return [t for t in self._tasks if t.status == target]

    def filter_by_priority(self, priority: str) -> List[Task]:
        """Return tasks matching the given priority."""
        target = Priority(priority)
        return [t for t in self._tasks if t.priority == target]

    def update_status(self, task_id: int, status: str) -> Optional[Task]:
        """Update the status of a task by ID."""
        task = self._find_by_id(task_id)
        if task is None:
            return None
        if status == Status.IN_PROGRESS.value:
            task.mark_in_progress()
        elif status == Status.DONE.value:
            task.mark_done()
        self._persist()
        return task

    def delete(self, task_id: int) -> bool:
        """Delete a task by ID. Returns True if found and deleted."""
        task = self._find_by_id(task_id)
        if task is None:
            return False
        self._tasks.remove(task)
        self._persist()
        return True

    def clear_all(self) -> None:
        """Remove all tasks."""
        self._tasks.clear()
        self.storage.clear()
        self._next_id = 1
