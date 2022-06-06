from controllers.user_controller import UserController
from controllers.currency_controller import CurrencyController

def set_currencies():
    print("Please enter currencies by name and overdraft limit. Leave the field empty to finish.")
    
    name = None
    
    while (name != ""):
        try:
            name = str(input("Currency name (USD): "))
            overdraft_limit = int(input("Currency overdraft limit (5000): "))
        except ValueError:
            return
        
        CurrencyController().create_currency(name, overdraft_limit)
        
        

def option_new_user():
    new_user_name = input("Username: ")

    user_search = UserController().user_exists(new_user_name)

    if (user_search):
        print("User already exists.")
        return
    
    currencies = CurrencyController().list_currencies()
    
    initial_investment = {}
    
    for currency in currencies:
        try:
            initial_investment[currency] = int(input(f'Initial investment on {currency}: '))
        except ValueError:
            print("The amount must be a number")        
        
    new_user = UserController().create_user(new_user_name)

    print(f'User created: {new_user}')
    


def option_list_users():
    users = UserController().list_users()

    for user in users:
        print(user)

