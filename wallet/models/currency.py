from database.connection import Database


class Currency(Database):
    name = None
    overdraft_limit = None

    def __init__(self):
        super().__init__(type(self).__name__)
        
    def save(self):
        super().create(self)