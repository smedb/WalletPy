from database.connection import Database


class AlertTrigger(Database):
    name = None
    amount = None
    action = None

    def __init__(self):
        super().__init__(type(self).__name__)
