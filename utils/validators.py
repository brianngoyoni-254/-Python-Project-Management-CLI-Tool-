from pydantic import BaseModel, EmailStr, ValidationError


class UserValidator(BaseModel):
    name: str
    email: EmailStr


def validate_user(name: str, email: str):
    """
    Validates user input using Pydantic.
    Raises error if invalid.
    """
    try:
        validated = UserValidator(name=name, email=email)
        return validated
    except ValidationError as e:
        print("[red]Invalid user data:[/red]")
        print(e)
        return None