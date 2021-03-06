from database.connection import Database


class User(Database):
    name: str = None

    def __init__(self):
        super().__init__(type(self).__name__)

    def findByName(self, name: str):
        return super().search('name', name)

    def save(self):
        user_search = self.findByName(self.name)

        if (user_search == None):
            super().create(self)
