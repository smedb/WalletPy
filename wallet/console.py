import os
from console_options import *


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def wait_for_enter_key():
    input("Press Enter to continue...")


def menu():
    clear_console()

    print("*** Wallet Kata ***")
    print("")
    print("Press 0 to exit.")
    print("Press 1 to create a new user.")
    print("Press 2 to list users.")


def option_action(option: int):
    if (option == 1):
        option_new_user()
    elif (option == 2):
        option_list_users()


def prompt():
    set_currencies()
    
    option_selected = None

    while option_selected != 0:
        try:
            menu()
            option_selected = int(input("Choose an option: "))
        except ValueError:
            continue

        if (option_selected > 0):
            clear_console()

            option_action(option_selected)

            wait_for_enter_key()

    print("Bye")
