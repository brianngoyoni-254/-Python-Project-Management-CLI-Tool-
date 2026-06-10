from models.user import User
from models.base_model import BaseModel


def test_create_user():
    user = User("Alex", "alex@mail.com")

    assert user.name == "Alex"
    assert user.email == "alex@mail.com"
    assert user.id is not None


def test_user_inherits_base_model():
    user = User("Alex", "alex@mail.com")

    assert isinstance(user, BaseModel)


def test_user_to_dict():
    user = User("Alex", "alex@mail.com")

    data = user.to_dict()

    assert isinstance(data, dict)
    assert data["name"] == "Alex"
    assert data["email"] == "alex@mail.com"
    assert "id" in data