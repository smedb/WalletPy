from controllers.user_controller import UserController
from controllers.transaction_controller import TransactionController
from controllers.currency_controller import CurrencyController
from constants.transaction_constants import TransactionConstants

user_controller = UserController()
transaction_controller = TransactionController()
currency_controller = CurrencyController()


def set_currencies():
    print("Please enter currencies by name and overdraft limit. Leave the field empty to finish.")

    name = None

    while (name != ""):
        try:
            name = str(input("Currency name (USD): "))
            overdraft_limit = int(input("Currency overdraft limit (5000): "))
        except ValueError:
            return

        currency_controller.create_currency(name, overdraft_limit)

        print(
            f'Currency created: {name} with overdraft limit {overdraft_limit}')


def option_new_user():
    new_user_name = input("Username: ")

    user_search = user_controller.user_exists(new_user_name)

    if (user_search):
        print("User already exists.")
        return

    currencies = currency_controller.list_currencies()

    initial_investment = {}

    for currency in currencies:
        try:
            amount = int(input(f'Initial investment on {currency}: '))

            if (amount > 0):
                initial_investment[currency] = amount
        except ValueError:
            print("The amount must be a number")

    new_user = user_controller.create_user(new_user_name)

    print(f'User created: {new_user}')

    for investment_currency in initial_investment:
        transaction_controller.create_transaction(new_user_name,
                                                  'Initial investment',
                                                  initial_investment[investment_currency],
                                                  transaction_controller.CREDIT,
                                                  investment_currency)

        print(
            f'{investment_currency} ${initial_investment[investment_currency]}')


def option_user_historic():
    new_user_name = input("Username: ")

    historic = user_controller.get_user_historic(new_user_name)

    if (historic == None):
        print("User doesn't exists.")
        return

    for currency in historic:
        print(f'*** {currency} ***')
        for transaction in historic[currency]:
            print(transaction)
        print("")


def option_user_movement():
    user_name = input("Username: ")

    user_search = user_controller.user_exists(user_name)

    if (user_search == False):
        print("User doesn't exists.")
        return

    currencies = currency_controller.list_currencies()

    for currency in currencies:
        print(f'[{currency}]')

    transaction_currency = input('Choose currency: ')
    
    print('Choose debit or credit:')
    print('1: CREDIT')
    print('2: DEBIT')
    
    try:
        transaction_type = int(input('Type 1 or 2: '))
    except ValueError:
        print("The amount must be a number")
        return
    
    if transaction_type == 1:
        transaction_type = TransactionConstants.CREDIT
    elif transaction_type == 2:
        transaction_type = TransactionConstants.DEBIT
    else:
        print("Invalid type")
        return

    transaction_description = input("Description: ")

    try:
        amount = int(input('Amount: '))
    except ValueError:
        print("The amount must be a number")
        return
    try:
        TransactionController().create_transaction(user_name, transaction_description,
                                               amount, transaction_type, transaction_currency)
    except Exception as e:
        print(e)


def option_list_users():
    users = UserController().list_users()

    for user in users:
        print(user)
