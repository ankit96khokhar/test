# Task Manager 📋

A simple command-line task manager written in Python. Tasks are persisted to a local JSON file.

## Project Structure

```
task-manager/
├── task_manager/
│   ├── __init__.py     # Package metadata
│   ├── models.py       # Task, Priority, Status data models
│   ├── storage.py      # JSON file persistence
│   ├── service.py      # Business logic / CRUD operations
│   ├── display.py      # Terminal display helpers (ANSI colours)
│   ├── cli.py          # argparse CLI entry point
│   └── utils.py        # Shared utility functions
├── tests/
│   ├── test_models.py  # Model unit tests
│   ├── test_service.py # Service unit tests
│   └── test_utils.py   # Utility unit tests
├── pyproject.toml
└── README.md
```

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Add a task
task-manager add "Buy groceries" -d "Milk, eggs, bread" -p high

# List all tasks
task-manager list

# Filter by status
task-manager list --status pending

# Filter by priority
task-manager list --priority high

# Mark a task as in-progress
task-manager update 1 in_progress

# Mark a task as done
task-manager update 1 done

# Delete a task
task-manager delete 1

# Clear all tasks
task-manager clear
```

## Running Tests

```bash
pip install pytest
pytest
```

## License

MIT
