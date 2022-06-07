from database.connection import Database


class Trigger(Database):
    name: str = None
    amount: int = None
    action: int = None

    def __init__(self):
        super().__init__(type(self).__name__)
        
    def save(self):
        super().create(self)