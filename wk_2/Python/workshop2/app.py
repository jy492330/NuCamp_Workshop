# ATM application

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
    while True:      # Input-Validation Loop: Variation 1
        name = input("Enter name to register: ")
        if name_is_invalid(name):
            print("Max name length is 10 characters and min is 1 character.")
            continue
        else:
            break

    pin = input("Enter PIN: ")  # Priming Read
    while pin_is_invalid(pin):  # Input-Validation Loop: Variation 2 (Better Version)
        print("PIN must contain 4 numbers")
        pin = input("Enter PIN: ")

    balance = 0
    print(f"{name} has been registered with a starting balance of ${balance}\n")
    login_validate(name, pin, balance)


# Bonus Task 1
def name_is_invalid(user_name):
    if len(user_name) < 1 or len(user_name) > 10:  # must use OR not AND
        return True
    if not user_name.isalpha():
        return True
    return False   # don't use else statement and then return False.


# Bonus Task 2
def pin_is_invalid(user_pin):
    if not user_pin.isdigit():
        return True
    if len(user_pin) != 4:
        return True
    return False   # don't use else statement and then return False.


def login_validate(name, pin, balance):
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
            account.show_balance(balance)  # show current balance prior to deposit
        elif option == "2":
            updated_bal = account.deposit(balance)
            account.show_balance(updated_bal)
        elif option == "3":
            updated_bal = account.withdraw(updated_bal)
            account.show_balance(updated_bal)
        elif option == "4":
            account.logout(user)
        else:
            print("Error: You must enter a valid option.")


def main():
    register()


if __name__ == "__main__":
    main()
