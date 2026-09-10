"""
Unit tests for task_manager.utils
"""

from task_manager.utils import format_datetime, slugify, truncate, validate_priority, validate_status


class TestSlugify:
    def test_basic(self):
        assert slugify("Hello World") == "hello-world"

    def test_special_chars(self):
        assert slugify("Buy milk & eggs!") == "buy-milk-eggs"

    def test_extra_spaces(self):
        assert slugify("  multiple   spaces  ") == "multiple-spaces"


class TestTruncate:
    def test_short_string(self):
        assert truncate("hi", 10) == "hi"

    def test_long_string(self):
        result = truncate("A" * 60, 50)
        assert len(result) == 50
        assert result.endswith("…")


class TestValidators:
    def test_valid_priority(self):
        assert validate_priority("low") is True
        assert validate_priority("medium") is True
        assert validate_priority("high") is True

    def test_invalid_priority(self):
        assert validate_priority("critical") is False

    def test_valid_status(self):
        assert validate_status("pending") is True
        assert validate_status("in_progress") is True
        assert validate_status("done") is True

    def test_invalid_status(self):
        assert validate_status("cancelled") is False


class TestFormatDatetime:
    def test_valid_iso(self):
        result = format_datetime("2024-03-15T09:30:00")
        assert "2024" in result or "Mar" in result  # locale-safe check

    def test_invalid_iso(self):
        raw = "not-a-date"
        assert format_datetime(raw) == raw
