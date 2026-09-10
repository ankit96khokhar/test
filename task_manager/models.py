"""
Task model representing a single task item.
"""

from datetime import datetime
from enum import Enum


class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Status(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task:
    """Represents a single task."""

    def __init__(self, title: str, description: str = "", priority: Priority = Priority.MEDIUM):
        self.id: int = 0
        self.title = title
        self.description = description
        self.priority = priority
        self.status = Status.PENDING
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def mark_in_progress(self):
        """Mark the task as in-progress."""
        self.status = Status.IN_PROGRESS
        self.updated_at = datetime.now().isoformat()

    def mark_done(self):
        """Mark the task as done."""
        self.status = Status.DONE
        self.updated_at = datetime.now().isoformat()

    def to_dict(self) -> dict:
        """Serialize the task to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority.value,
            "status": self.status.value,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Deserialize a task from a dictionary."""
        task = cls(
            title=data["title"],
            description=data.get("description", ""),
            priority=Priority(data.get("priority", "medium")),
        )
        task.id = data["id"]
        task.status = Status(data.get("status", "pending"))
        task.created_at = data.get("created_at", datetime.now().isoformat())
        task.updated_at = data.get("updated_at", task.created_at)
        return task

    def __repr__(self) -> str:
        return f"Task(id={self.id}, title='{self.title}', status={self.status.value})"
