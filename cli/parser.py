import argparse

def build_parser():
    parser = argparse.ArgumentParser(
        description="Project Management CLI Tool"
    )

    subparsers = parser.add_subparsers(dest="group")

    
    # USER GROUP
    
    user_parser = subparsers.add_parser("user")
    user_sub = user_parser.add_subparsers(dest="command")

    user_add = user_sub.add_parser("add")
    user_add.add_argument("--name", required=True)
    user_add.add_argument("--email", required=True)

    user_sub.add_parser("list")

    # NEW
    user_delete = user_sub.add_parser("delete")
    user_delete.add_argument("--name", required=True)

    user_edit = user_sub.add_parser("edit")
    user_edit.add_argument("--name", required=True)
    user_edit.add_argument("--new-name", required=False)
    user_edit.add_argument("--new-email", required=False)

    
    # PROJECT GROUP
    
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
    project_edit.add_argument("--new-title", required=False)

    
    # TASK GROUP
    
    task_parser = subparsers.add_parser("task")
    task_sub = task_parser.add_subparsers(dest="command")

    # CREATE
    task_add = task_sub.add_parser("add")
    task_add.add_argument("--project", required=True)
    task_add.add_argument("--title", required=True)
    task_add.add_argument("--due", required=False)

    # LIST + FILTERS
    task_list = task_sub.add_parser("list")
    task_list.add_argument("--project", required=False)
    task_list.add_argument("--overdue", action="store_true")
    task_list.add_argument("--due-soon", action="store_true")
    task_list.add_argument("--completed", action="store_true")
    task_list.add_argument("--pending", action="store_true")
    task_list.add_argument("--assigned", required=False)

    # COMPLETE
    task_complete = task_sub.add_parser("complete")
    task_complete.add_argument("--title", required=True)

    # SEARCH
    task_search = task_sub.add_parser("search")
    task_search.add_argument("--keyword", required=True)

    # NEW CRUD
    task_delete = task_sub.add_parser("delete")
    task_delete.add_argument("--title", required=True)

    task_edit = task_sub.add_parser("edit")
    task_edit.add_argument("--title", required=True)
    task_edit.add_argument("--new-title", required=False)
    task_edit.add_argument("--due", required=False)
    task_edit.add_argument("--assign", required=False)


    # DASHBOARD
    
    subparsers.add_parser("dashboard")

    return parser