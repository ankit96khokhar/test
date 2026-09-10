"""
Utility / helper functions used across the project.
"""

import re
from datetime import datetime


def slugify(text: str) -> str:
    """Convert a string to a lowercase, hyphen-separated slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text


def format_datetime(iso_str: str) -> str:
    """Return a human-friendly datetime string from an ISO 8601 string."""
    try:
        dt = datetime.fromisoformat(iso_str)
        return dt.strftime("%d %b %Y, %H:%M")
    except (ValueError, TypeError):
        return iso_str


def truncate(text: str, max_length: int = 50) -> str:
    """Truncate a string and append '…' if it exceeds max_length."""
    if len(text) <= max_length:
        return text
    return text[: max_length - 1] + "…"


def validate_priority(value: str) -> bool:
    """Return True if the priority string is valid."""
    return value in {"low", "medium", "high"}


def validate_status(value: str) -> bool:
    """Return True if the status string is valid."""
    return value in {"pending", "in_progress", "done"}
