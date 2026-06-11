from services.user_service import UserService
from services.project_service import ProjectService
from services.task_service import TaskService
from services.dashboard_service import DashboardService
from rich import print

user_service = UserService()
project_service = ProjectService()
task_service = TaskService()
dashboard_service = DashboardService()


def handle_command(args):

    if not hasattr(args, "group") or not args.group:
        print("[red]No command group provided[/red]")
        return

    #  USER COMMANDS 
    if args.group == "user":

        if args.command == "add":
            user_service.add_user(args.name, args.email)

        elif args.command == "list":
            user_service.list_users()

        elif args.command == "delete":
            user_service.delete_user(args.name)

        elif args.command == "edit":
            user_service.edit_user(
                args.name,
                getattr(args, "new_name", None),
                getattr(args, "new_email", None)
            )

        else:
            print("[red]Unknown user command[/red]")


    # PROJECT COMMANDS 
    elif args.group == "project":

        if args.command == "add":
            project_service.add_project(args.user, args.title)

        elif args.command == "list":
            # FIXED: no args.user anymore
            project_service.list_projects()

        elif args.command == "search":
            project_service.search_project(args.keyword)

        elif args.command == "delete":
            project_service.delete_project(args.title)

        elif args.command == "edit":
            project_service.edit_project(
                args.title,
                getattr(args, "new_title", None)
            )

        else:
            print("[red]Unknown project command[/red]")


    # TASK COMMANDS 
    elif args.group == "task":

        if args.command == "add":
            task_service.add_task_by_name(
                args.project,
                args.title,
                getattr(args, "due", None)
            )

        elif args.command == "list":
            task_service.list_tasks(
                project=getattr(args, "project", None),
                overdue=getattr(args, "overdue", False),
                due_soon=getattr(args, "due_soon", False),
                completed=getattr(args, "completed", False),
                pending=getattr(args, "pending", False),
                assigned=getattr(args, "assigned", None)
            )

        elif args.command == "add-contributor":
            task_service.add_contributor(args.title, args.user)

        elif args.command == "complete":
            task_service.complete_task(args.title)

        elif args.command == "search":
            task_service.search_task(args.keyword)

        elif args.command == "delete":
            task_service.delete_task(args.title)

        elif args.command == "edit":
            task_service.edit_task(
                args.title,
                new_title=getattr(args, "new_title", None),
                due=getattr(args, "due", None),
                assign=getattr(args, "assign", None)
            )

        else:
            print("[red]Unknown task command[/red]")


    # DASHBOARD 
    elif args.group == "dashboard":
        dashboard_service.show_dashboard()

    else:
        print("[red]Unknown command group[/red]")