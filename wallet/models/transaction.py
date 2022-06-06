from database.connection import Database


class Transaction(Database):
    description = None
    amount = None
    currency = None

    def __init__(self):
        super().__init__(type(self).__name__)

