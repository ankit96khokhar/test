"""
CLI entry point — parses arguments and dispatches to the TaskService.
"""

import argparse
import sys

from task_manager.display import print_error, print_info, print_success, print_task_list
from task_manager.service import TaskService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="task-manager",
        description="A simple CLI task manager",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # add
    add_p = sub.add_parser("add", help="Add a new task")
    add_p.add_argument("title", help="Task title")
    add_p.add_argument("-d", "--description", default="", help="Task description")
    add_p.add_argument(
        "-p", "--priority",
        choices=["low", "medium", "high"],
        default="medium",
        help="Task priority (default: medium)",
    )

    # list
    list_p = sub.add_parser("list", help="List tasks")
    list_p.add_argument(
        "-s", "--status",
        choices=["pending", "in_progress", "done"],
        help="Filter by status",
    )
    list_p.add_argument(
        "-p", "--priority",
        choices=["low", "medium", "high"],
        help="Filter by priority",
    )

    # update
    update_p = sub.add_parser("update", help="Update a task's status")
    update_p.add_argument("id", type=int, help="Task ID")
    update_p.add_argument(
        "status",
        choices=["in_progress", "done"],
        help="New status",
    )

    # delete
    delete_p = sub.add_parser("delete", help="Delete a task")
    delete_p.add_argument("id", type=int, help="Task ID to delete")

    # clear
    sub.add_parser("clear", help="Delete ALL tasks")

    return parser


def run(argv=None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    service = TaskService()

    if args.command == "add":
        task = service.add(args.title, args.description, args.priority)
        print_success(f"Task #{task.id} '{task.title}' created.")

    elif args.command == "list":
        if args.status:
            tasks = service.filter_by_status(args.status)
            print_info(f"Tasks with status '{args.status}':")
        elif args.priority:
            tasks = service.filter_by_priority(args.priority)
            print_info(f"Tasks with priority '{args.priority}':")
        else:
            tasks = service.list_all()
            print_info("All tasks:")
        print_task_list(tasks)

    elif args.command == "update":
        task = service.update_status(args.id, args.status)
        if task:
            print_success(f"Task #{task.id} updated to '{args.status}'.")
        else:
            print_error(f"Task #{args.id} not found.")
            sys.exit(1)

    elif args.command == "delete":
        if service.delete(args.id):
            print_success(f"Task #{args.id} deleted.")
        else:
            print_error(f"Task #{args.id} not found.")
            sys.exit(1)

    elif args.command == "clear":
        service.clear_all()
        print_success("All tasks cleared.")


if __name__ == "__main__":
    run()
