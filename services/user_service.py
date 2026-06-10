from storage.json_db import load, save
from models.user import User
from utils.validators import validate_user
from rich import print
from rich.table import Table


class UserService:
    FILE = "users.json"

    def add_user(self, name, email):
        users = load(self.FILE)

        # Pydantic validation step
        validated = validate_user(name, email)

        if not validated:
            print("[red]User not created due to invalid input[/red]")
            return

        # Create user only after validation
        user = User(validated.name, validated.email)

        users.append(user.to_dict())
        save(self.FILE, users)

        print("\n[green]User created successfully[/green]")
        print(f"[cyan]Name:[/cyan] {user.name}")
        print(f"[magenta]Email:[/magenta] {user.email}")

    def list_users(self):
        users = load(self.FILE)

        table = Table(title="Users")
        table.add_column("Name", style="green")
        table.add_column("Email", style="magenta")

        for u in users:
            table.add_row(u["name"], u["email"])

        print(table)