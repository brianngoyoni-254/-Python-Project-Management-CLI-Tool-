from models.base_model import BaseModel

class Project(BaseModel):

    def __init__(self, title, user_id):
        super().__init__()

        self.title = title
        self.user_id = user_id