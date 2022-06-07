from models.user import User
from models.transaction import Transaction
from constants.transaction_constants import TransactionConstants


class UserController:
    def __init__(self):
        self.users = User()

    def create_user(self, name: str) -> str:
        user = User()
        user.name = name
        user.save()

        return user.name

    def list_users(self) -> list[str]:
        user_list = []

        for user in self.users.getAll():
            balances = self.get_user_balances(user.name)
            balances_string = ' ('

            for currency in balances:
                balances_string += currency + ' $' + \
                    str(balances[currency]) + ') ('

            user_list.append(user.name + balances_string[:-2])

        return user_list

    def get_user_balances(self, name: str):
        user = self.users.findByName(name)

        if (user == None):
            return None

        return Transaction().getBalanceByUser(user)

    def get_user_historic(self, name: str):
        user = self.users.findByName(name)

        if (user == None):
            return None

        historic = {}

        for transaction in Transaction().getByUser(user):
            if transaction.currency.name not in historic:
                historic[transaction.currency.name] = []

            if transaction.type == TransactionConstants.CREDIT:
                historic[transaction.currency.name].append(
                    f'{transaction.timestamp} | CREDIT | $ {transaction.amount}')
            elif transaction.type == TransactionConstants.DEBIT:
                historic[transaction.currency.name].append(
                    f'{transaction.timestamp} | DEBIT  | $ {transaction.amount}')

        return historic

    def user_exists(self, name: str) -> bool:
        user = self.users.findByName(name)

        return (user != None)
