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

    
    # USER COMMANDS
    
    if args.command == "add-user":
        user_service.add_user(args.name, args.email)

    elif args.command == "list-users":
        user_service.list_users()

    
    # PROJECT COMMANDS
    
    elif args.command == "add-project":
        project_service.add_project(args.user, args.title)

    elif args.command == "list-projects":
        project_service.list_projects(args.user)

    elif args.command == "search-project":
        project_service.search_project(args.keyword)

    
    # TASK COMMANDS
    
    elif args.command == "add-task":
        task_service.add_task_by_name(args.project, args.title)

    elif args.command == "list-tasks":
        task_service.list_tasks(args.project)

    elif args.command == "complete-task":
        task_service.complete_task(args.task)

    elif args.command == "search-task":
        task_service.search_task(args.keyword)

    
    # DASHBOARD
    
    elif args.command == "dashboard":
        dashboard_service.show_dashboard()

    else:
        print("[red]Unknown command[/red]")