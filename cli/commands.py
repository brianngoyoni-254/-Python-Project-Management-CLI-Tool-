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

    # USER 
    if args.group == "user":

        if args.command == "add":
            user_service.add_user(args.name, args.email)

        elif args.command == "list":
            user_service.list_users()

        else:
            print("[red]Unknown user command[/red]")

    # PROJECT 
    elif args.group == "project":

        if args.command == "add":
            project_service.add_project(args.user, args.title)

        elif args.command == "list":
            project_service.list_projects(args.user)

        elif args.command == "search":
            project_service.search_project(args.keyword)

        else:
            print("[red]Unknown project command[/red]")

    #  TASK
    elif args.group == "task":

        if args.command == "add":
            task_service.add_task_by_name(args.project, args.title)

        elif args.command == "list":
            task_service.list_tasks()

        elif args.command == "complete":
            task_service.complete_task(args.task)

        elif args.command == "search":
            task_service.search_task(args.keyword)

        else:
            print("[red]Unknown task command[/red]")

    # DASHBOARD 
    elif args.group == "dashboard":
        dashboard_service.show_dashboard()

    else:
        print("[red]Unknown command group[/red]")