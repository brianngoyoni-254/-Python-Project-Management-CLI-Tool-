from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, name, email):
        super().__init__()
        self._name = name
        self._email = email

    # getters
    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    # optional setters
    def update_name(self, name):
        self._name = name
        self.touch()

    def update_email(self, email):
        self._email = email
        self.touch()

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "name": self._name,
            "email": self._email
        })
        return data