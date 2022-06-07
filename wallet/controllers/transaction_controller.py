from models.user import User
from models.transaction import Transaction
from models.currency import Currency
from constants.transaction_constants import TransactionConstants
import datetime


class TransactionController(TransactionConstants):
    def __init__(self):
        self.users = User()
        self.transactions = Transaction()
    
    
    def create_transaction(self, user_name: str, description: str, amount: int, type: bool, currency: str) -> bool:
        user = self.users.findByName(user_name);
        
        if (user == None):
            raise Exception('Invalid user')
        
        currency_object = Currency().findByName(currency)
        
        if (currency_object == None):
            raise Exception('Invalid currency')
        
        balances = Transaction().getBalanceByUser(user)
        
        if currency in balances:
            user_balance = balances[currency]
        else:
            user_balance = 0
            
        if type == self.DEBIT and amount > user_balance + currency_object.overdraft_limit:
            raise Exception('Amount exceeds account balance and overdraft limit')
        
        transaction = Transaction()
        
        transaction.user_name = user_name
        transaction.timestamp = datetime.datetime.now()
        transaction.description = description
        transaction.amount = amount
        transaction.type = type
        transaction.currency = currency_object
        
        transaction.save()

        return True