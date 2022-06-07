from typing import List
from database.connection import Database
from models.currency import Currency
from constants.transaction_constants import TransactionConstants
from models.user import User
import datetime


class Transaction(Database, TransactionConstants):
    user_name: str = None
    description: str = None
    amount: int = None
    type: bool = None
    currency: Currency = None
    timestamp: datetime.datetime = None

    def __init__(self):
        super().__init__(type(self).__name__)
        
    def getByUser(self, user: User) -> list:
        transactions = []
        
        for transaction in self.getAll():
            if transaction.user_name == user.name:
                transactions.append(transaction)
        
        return transactions
    
    def getBalanceByUser(self, user: User) -> list:
        balances = {}
        
        for transaction in self.getByUser(user):
            if transaction.currency.name not in balances:
                balances[transaction.currency.name] = 0
            
            if transaction.type == self.CREDIT:
                balances[transaction.currency.name] += transaction.amount
            elif transaction.type == self.DEBIT:
                balances[transaction.currency.name] -= transaction.amount
            
        return balances

    def save(self):
        super().create(self)
