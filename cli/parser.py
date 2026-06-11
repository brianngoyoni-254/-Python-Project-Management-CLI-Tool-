import argparse


def build_parser():
    parser = argparse.ArgumentParser(
        description="Project Management CLI Tool"
    )

    subparsers = parser.add_subparsers(dest="group")

    # USER 
    user_parser = subparsers.add_parser("user")
    user_sub = user_parser.add_subparsers(dest="command")

    user_sub.add_parser("list")

    user_add = user_sub.add_parser("add")
    user_add.add_argument("--name", required=True)
    user_add.add_argument("--email", required=True)

    user_delete = user_sub.add_parser("delete")
    user_delete.add_argument("--name", required=True)

    user_edit = user_sub.add_parser("edit")
    user_edit.add_argument("--name", required=True)
    user_edit.add_argument("--new-name")
    user_edit.add_argument("--new-email")

    # PROJECT 
    project_parser = subparsers.add_parser("project")
    project_sub = project_parser.add_subparsers(dest="command")

    project_add = project_sub.add_parser("add")
    project_add.add_argument("--user", required=True)
    project_add.add_argument("--title", required=True)

    project_sub.add_parser("list")

    project_search = project_sub.add_parser("search")
    project_search.add_argument("--keyword", required=True)

    project_delete = project_sub.add_parser("delete")
    project_delete.add_argument("--title", required=True)

    project_edit = project_sub.add_parser("edit")
    project_edit.add_argument("--title", required=True)
    project_edit.add_argument("--new-title")

    # TASK
    task_parser = subparsers.add_parser("task")
    task_sub = task_parser.add_subparsers(dest="command")

    task_add = task_sub.add_parser("add")
    task_add.add_argument("--project", required=True)
    task_add.add_argument("--title", required=True)
    task_add.add_argument("--due")

    task_sub.add_parser("list")

    task_complete = task_sub.add_parser("complete")
    task_complete.add_argument("--title", required=True)

    task_search = task_sub.add_parser("search")
    task_search.add_argument("--keyword", required=True)

    task_delete = task_sub.add_parser("delete")
    task_delete.add_argument("--title", required=True)

    task_edit = task_sub.add_parser("edit")
    task_edit.add_argument("--title", required=True)
    task_edit.add_argument("--new-title")
    task_edit.add_argument("--due")
    task_edit.add_argument("--assign")

    task_contrib = task_sub.add_parser("add-contributor")
    task_contrib.add_argument("--title", required=True)
    task_contrib.add_argument("--user", required=True)

    # DASHBOARD 
    subparsers.add_parser("dashboard")

    return parser