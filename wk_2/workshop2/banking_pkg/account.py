"""
Implement this module from the banking package with 4 functions
to view the balance, to withdraw and deposit from a bank account.
"""


def show_balance(balance):
    print("Current Balance: $", balance, sep="")


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return balance + amount


def withdraw(balance):
    amount = int(input("Enter amount to withdraw: "))
    if balance >= amount:
        return balance - amount
    else:
        print("Insufficient funds for withdrawal !")
        return balance


def logout(name):
    print("Goodbye", name)
