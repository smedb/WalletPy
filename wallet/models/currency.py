from database.connection import Database


class Currency(Database):
    name: str = None
    overdraft_limit: int = None

    def __init__(self):
        super().__init__(type(self).__name__)
        
    def findByName(self, name: str):
        return super().search('name', name)

    def save(self):
        super().create(self)
