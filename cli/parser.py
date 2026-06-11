import argparse


def build_parser():
    parser = argparse.ArgumentParser(
        description="Project Management CLI Tool"
    )

    subparsers = parser.add_subparsers(dest="group")

    #  USER GROUP 
    user_parser = subparsers.add_parser("user")
    user_sub = user_parser.add_subparsers(dest="command")

    user_add = user_sub.add_parser("add")
    user_add.add_argument("--name", required=True)
    user_add.add_argument("--email", required=True)

    user_sub.add_parser("list")

    #  PROJECT GROUP 
    project_parser = subparsers.add_parser("project")
    project_sub = project_parser.add_subparsers(dest="command")

    project_add = project_sub.add_parser("add")
    project_add.add_argument("--user", required=True)
    project_add.add_argument("--title", required=True)

    project_list = project_sub.add_parser("list")
    project_list.add_argument("--user", required=False)

    project_search = project_sub.add_parser("search")
    project_search.add_argument("--keyword", required=True)

    # TASK GROUP 
    task_parser = subparsers.add_parser("task")
    task_sub = task_parser.add_subparsers(dest="command")

    task_add = task_sub.add_parser("add")
    task_add.add_argument("--project", required=True)
    task_add.add_argument("--title", required=True)

    task_sub.add_parser("list")

    task_complete = task_sub.add_parser("complete")
    task_complete.add_argument("--task", required=True)

    task_search = task_sub.add_parser("search")
    task_search.add_argument("--keyword", required=True)

    # DASHBOARD 
    dashboard_parser = subparsers.add_parser("dashboard")
    dashboard_parser.add_argument("--show", action="store_true")

    return parser