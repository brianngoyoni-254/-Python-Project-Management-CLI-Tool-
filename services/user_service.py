from storage.json_db import load, save
from models.user import User
from schemas.user_schema import UserSchema
from rich import print
from rich.table import Table


class UserService:
    FILE = "users.json"

    def add_user(self, name, email):
        users = load(self.FILE)

        #  Pydantic validation layer
        try:
            validated = UserSchema(name=name, email=email)
        except Exception as e:
            print(f"[red]Invalid user input:[/red] {e}")
            return False

        user = User(validated.name, str(validated.email))

        users.append(user.to_dict())
        save(self.FILE, users)

        print("\n[green]User created successfully[/green]")
        print(f"[cyan]Name:[/cyan] {user.name}")
        print(f"[magenta]Email:[/magenta] {user.email}")

        return True

    def list_users(self):
        users = load(self.FILE)

        table = Table(title="Users")
        table.add_column("Name", style="green")
        table.add_column("Email", style="magenta")

        for u in users:
            table.add_row(u["name"], u["email"])

        print(table)