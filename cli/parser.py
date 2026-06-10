import argparse


def build_parser():
    parser = argparse.ArgumentParser(
        description="Project Management CLI Tool"
    )

    subparsers = parser.add_subparsers(dest="command")

    
    # USER COMMANDS
    
    add_user = subparsers.add_parser("add-user")
    add_user.add_argument("--name", required=True)
    add_user.add_argument("--email", required=True)

    subparsers.add_parser("list-users")

    
    # PROJECT COMMANDS
    
    add_project = subparsers.add_parser("add-project")
    add_project.add_argument("--user", required=True)
    add_project.add_argument("--title", required=True)

    list_projects = subparsers.add_parser("list-projects")
    list_projects.add_argument("--user", required=False)

    search_project = subparsers.add_parser("search-project")
    search_project.add_argument("--keyword", required=True)

    
    # TASK COMMANDS
    
    add_task = subparsers.add_parser("add-task")
    add_task.add_argument("--project", required=True)
    add_task.add_argument("--title", required=True)

    list_tasks = subparsers.add_parser("list-tasks")
    list_tasks.add_argument("--project", required=False)

    complete_task = subparsers.add_parser("complete-task")
    complete_task.add_argument("--task", required=True)

    search_task = subparsers.add_parser("search-task")
    search_task.add_argument("--keyword", required=True)

    
    # DASHBOARD
    
    subparsers.add_parser("dashboard")

    return parser