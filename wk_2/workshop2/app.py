"""
Nucamp
Week 2 workshop Assignment: ATM application
Creator: Jin Jessica Yang
"""

from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


def register():
    print("          === Automated Teller Machine ===          ")
    while True:
        name = input("Enter name to register: ")
        if name_is_invalid(name):
            print("Max name length is 10 characters and min is 1 character.")
            print("User name must contain only characters.")
            continue
        else:
            break

    pin = input("Enter PIN: ")
    while pin_is_invalid(pin):
        print("PIN must contain 4 numbers")
        pin = input("Enter PIN: ")

    balance = 0
    print(f"{name} has been registered with a starting balance of ${balance}\n")
    login_validate(name, pin, balance)


def name_is_invalid(user_name):
    if len(user_name) < 1 or len(user_name) > 10:
        return True
    if not user_name.isalpha():
        return True
    return False


def pin_is_invalid(user_pin):
    if not user_pin.isdigit():
        return True
    if len(user_pin) != 4:
        return True
    return False


def login_validate(name, pin, bal):
    while True:
        print("          === Automated Teller Machine ===          ")
        print("LOGIN")
        name_to_validate = input("Enter name: ")
        pin_to_validate = input("Enter PIN: ")
        if name_to_validate == name and pin_to_validate == pin:
            print("Login successful!")
            break
        else:
            print("Invalid credentials!\n")
            continue
    option = 0
    while option != "4":
        user = name_to_validate
        atm_menu(user)
        option = input("Choose an option: ")
        if option == "1":
            account.show_balance(bal)
        elif option == "2":
            bal = account.deposit(bal)
            account.show_balance(bal)
        elif option == "3":
            bal = account.withdraw(bal)
            account.show_balance(bal)
        elif option == "4":
            account.logout(user)
        else:
            print("Error: You must enter a valid option.")


if __name__ == "__main__":
    register()
