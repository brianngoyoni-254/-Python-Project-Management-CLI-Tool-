from storage.json_db import load, save
from models.task import Task
from schemas.task_schema import TaskSchema
from rich import print
from rich.table import Table
from datetime import datetime, date, timezone


class TaskService:
    FILE = "tasks.json"
    PROJECT_FILE = "projects.json"
    USER_FILE = "users.json"

    #  HELPERS 

    def _find_project(self, project_name):
        projects = load(self.PROJECT_FILE) or []

        for p in projects:
            if p.get("title", "").strip().lower() == project_name.strip().lower():
                return p
        return None

    def _find_user(self, name):
        users = load(self.USER_FILE) or []

        for u in users:
            if u.get("name", "").strip().lower() == name.strip().lower():
                return u
        return None

    def _find_user_by_id(self, user_id):
        users = load(self.USER_FILE) or []

        for u in users:
            if u.get("id") == user_id:
                return u
        return None

    def _user_map(self):
        users = load(self.USER_FILE) or []
        return {u.get("id"): u.get("name") for u in users}

    def _parse_date(self, d):
        if not d:
            return None

        try:
            return datetime.strptime(d, "%Y-%m-%d").date()
        except ValueError:
            return None

    def _urgency(self, due):
        if not due:
            return "normal", "green"

        try:
            d = datetime.strptime(due, "%Y-%m-%d").date()
        except Exception:
            return "normal", "green"

        diff = (d - date.today()).days

        if diff < 0:
            return "overdue", "red"
        if diff <= 3:
            return "due soon", "yellow"
        return "normal", "green"

    #  CREATE TASK 

    def add_task_by_name(self, project_name, title, due_date=None):
        tasks = load(self.FILE) or []

        project = self._find_project(project_name)
        if not project:
            print(f"[red]Project not found:[/red] {project_name}")
            return False

        project_id = project["id"]
        parsed_due = self._parse_date(due_date)

        try:
            validated = TaskSchema(
                title=title,
                project_id=project_id,
                due_date=parsed_due
            )
        except Exception as e:
            print(f"[red]Invalid task input:[/red] {e}")
            return False

        assigned_user_ids = []

        if project.get("user_id"):
            assigned_user_ids.append(project["user_id"])

        task = Task(
            validated.title,
            validated.project_id,
            assigned_user_ids=assigned_user_ids,
            due_date=validated.due_date
        )

        tasks.append(task.to_dict())
        save(self.FILE, tasks)

        user_map = self._user_map()

        assignees = ", ".join(
            user_map.get(uid, "Unknown") for uid in assigned_user_ids
        ) if assigned_user_ids else "Unassigned"

        print("\n[green]Task created successfully[/green]")
        print(f"[cyan]Title:[/cyan] {task.title}")
        print(f"[magenta]Project:[/magenta] {project_name}")
        print(f"[blue]Assigned To:[/blue] {assignees}")
        print(f"[yellow]Status:[/yellow] {task.status}")

        if task.due_date:
            print(f"[blue]Due Date:[/blue] {task.due_date}")

        return True

    # LIST TASKS 

    def list_tasks(
        self,
        project=None,
        overdue=False,
        due_soon=False,
        completed=False,
        pending=False,
        assigned=None
    ):
        tasks = load(self.FILE) or []
        projects = load(self.PROJECT_FILE) or []

        project_map = {p["id"]: p["title"] for p in projects}
        user_map = self._user_map()

        table = Table(title="Tasks (Smart View)")
        table.add_column("Title", style="green")
        table.add_column("Project", style="magenta")
        table.add_column("Assigned To", style="cyan")
        table.add_column("Status", style="yellow")
        table.add_column("Created At", style="cyan")
        table.add_column("Due Date", style="cyan")
        table.add_column("Urgency", style="bold")

        filtered = []

        for t in tasks:
            project_title = project_map.get(t.get("project_id"), "Unknown")

            # SAFE NORMALIZATION 
            assigned_ids = t.get("assigned_user_ids") or []
            if not isinstance(assigned_ids, list):
                assigned_ids = [assigned_ids]

            assignees = ", ".join(
                user_map.get(uid, "Unknown") for uid in assigned_ids
            ) if assigned_ids else "Unassigned"

            status = t.get("status", "Pending")
            urgency, color = self._urgency(t.get("due_date"))

            if project and project_title.lower() != project.lower():
                continue

            if assigned and assigned.lower() not in assignees.lower():
                continue

            if completed and status != "Done":
                continue

            if pending and status == "Done":
                continue

            if overdue and urgency != "overdue":
                continue

            if due_soon and urgency != "due soon":
                continue

            filtered.append(t)

            table.add_row(
                t.get("title", ""),
                project_title,
                assignees,
                status,
                t.get("created_at", "-"),
                str(t.get("due_date", "-")),
                f"[{color}]{urgency}[/{color}]"
            )

        if not filtered:
            print("[red]No tasks found[/red]")
            return []

        print(table)
        return filtered

    #SEARCH 

    def search_task(self, keyword):
        tasks = load(self.FILE) or []
        projects = load(self.PROJECT_FILE) or []

        project_map = {p["id"]: p["title"] for p in projects}  # FIXED NAME BUG
        user_map = self._user_map()

        matches = []

        for t in tasks:
            if keyword.lower() in t.get("title", "").lower():
                matches.append(t)

        if not matches:
            print(f"[red]No tasks found matching '{keyword}'[/red]")
            return []

        table = Table(title=f"Task Search Results: {keyword}")

        table.add_column("Title", style="green")
        table.add_column("Project", style="magenta")
        table.add_column("Assigned To", style="cyan")
        table.add_column("Status", style="yellow")
        table.add_column("Due Date", style="blue")

        for t in matches:
            assigned_ids = t.get("assigned_user_ids") or []
            if not isinstance(assigned_ids, list):
                assigned_ids = [assigned_ids]

            assignees = ", ".join(
                user_map.get(uid, "Unknown") for uid in assigned_ids
            ) if assigned_ids else "Unassigned"

            table.add_row(
                t.get("title", ""),
                project_map.get(t.get("project_id"), "Unknown"),
                assignees,
                t.get("status", "Pending"),
                str(t.get("due_date", "-"))
            )

        print(table)
        return matches

    # COMPLETE 

    def complete_task(self, task_title):
        tasks = load(self.FILE) or []

        for t in tasks:
            if t.get("title", "").strip().lower() == task_title.strip().lower():
                t["status"] = "Done"
                t["updated_at"] = datetime.now(timezone.utc).isoformat()

                save(self.FILE, tasks)
                print(f"[green]Task completed:[/green] {task_title}")
                return True

        print("[red]Task not found[/red]")
        return False

    # DELETE 

    def delete_task(self, title):
        tasks = load(self.FILE) or []

        new_tasks = [
            t for t in tasks
            if t.get("title", "").lower() != title.lower()
        ]

        if len(new_tasks) == len(tasks):
            print("[red]Task not found[/red]")
            return False

        save(self.FILE, new_tasks)
        print(f"[green]Task deleted:[/green] {title}")
        return True

    # EDIT 

    def edit_task(self, title, new_title=None, due=None, assign=None):
        tasks = load(self.FILE) or []

        for t in tasks:
            if t.get("title", "").lower() == title.lower():

                if new_title:
                    t["title"] = new_title

                if due:
                    t["due_date"] = due

                if assign:
                    user = self._find_user(assign)
                    if not user:
                        print(f"[red]User not found:[/red] {assign}")
                        return False

                    uid = user["id"]

                    t.setdefault("assigned_user_ids", [])

                    if uid not in t["assigned_user_ids"]:
                        t["assigned_user_ids"].append(uid)

                t["updated_at"] = datetime.now(timezone.utc).isoformat()

                save(self.FILE, tasks)
                print(f"[green]Task updated:[/green] {title}")
                return True

        print("[red]Task not found[/red]")
        return False

    #  ADD CONTRIBUTOR 

    def add_contributor(self, task_title, user_name):
        tasks = load(self.FILE) or []
        user = self._find_user(user_name)

        if not user:
            print(f"[red]User not found:[/red] {user_name}")
            return False

        uid = user["id"]

        for t in tasks:
            if t.get("title", "").lower() == task_title.lower():

                t.setdefault("assigned_user_ids", [])

                if uid not in t["assigned_user_ids"]:
                    t["assigned_user_ids"].append(uid)

                t["updated_at"] = datetime.now(timezone.utc).isoformat()

                save(self.FILE, tasks)
                print(f"[green]Contributor added:[/green] {user_name} → {task_title}")
                return True

        print("[red]Task not found[/red]")
        return False