from models.base_model import BaseModel

class User(BaseModel):

    def __init__(self, name, email):
        super().__init__()

        self.name = name
        self.email = email