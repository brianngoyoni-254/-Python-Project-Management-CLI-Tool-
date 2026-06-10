from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, name, email):
        super().__init__()
        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "name": self._name,
            "email": self._email
        })
        return data