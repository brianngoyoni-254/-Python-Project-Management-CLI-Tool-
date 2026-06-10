from utils.id_generator import generate_id

class BaseModel:
    def __init__(self):
        self.id = generate_id()

    def to_dict(self):
        return self.__dict__