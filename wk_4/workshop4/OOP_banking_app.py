"""
Nucamp
Week 4 workshop Assignment: OOP Banking App
Creator: Jin Jessica Yang
"""


class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name
        return self.name

    def change_pin(self, pin):
        self.pin = pin
        return self.pin

    def change_password(self, password):
        self.password = password
        return self.password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.amount = 0
        self.balance = 0

    def show_balance(self):
        print(f"{self.name} has an account balance of: {float(self.balance)}")

    def withdraw(self, amount):
        if amount != 0:
            self.amount = float(amount)
            self.balance -= self.amount
            return self.balance

    def deposit(self, amount):
        if amount != 0:
            self.amount = float(amount)
            self.balance += self.amount
            return self.balance

    def transfer_money(self, amount, other_user):
        if amount != 0 and not self.balance <= 0:
            self.amount = amount
            print(f"You are transferring ${self.amount} to {other_user.name}")
            print("Authentication is required......")
            PIN = input("Enter your PIN: ")
            if self.pin == PIN:
                print("Transfer authorized")
                print(f"Transferring ${self.amount} to {other_user.name}")
                self.balance -= self.amount
                other_user.balance += self.amount
                return True

            print("Invalid PIN. Transaction cancelled.")
            return False
        print(f"Your account balance is insufficient to transfer ${amount} to {other_user.name}.")

    def request_money(self, amount, other_user):
        if amount != 0 and not other_user.balance <= 0:
            self.amount = amount
            print(f"You are requesting ${self.amount} from {other_user.name}")
            print("Authentication is required......")
            sender_pin = input(f"Enter {other_user.name}'s PIN: ")
            requester_password = input("Enter your password: ")
            if other_user.pin == sender_pin and self.password == requester_password:
                print("Request authorized")
                print(f"{other_user.name} sent ${self.amount}")
                self.balance += self.amount
                other_user.balance -= self.amount
                return True
            else:
                if other_user.pin != sender_pin:
                    print("Invalid PIN. Transaction cancelled.")
                    return False
                elif self.password != requester_password:
                    print("Invalid password. Transaction cancelled.")
                    return False
        print(f"{other_user.name}'s account balance is insufficient to send the request ${amount} to you.")


""" Driver Code for Task 1 """
# user = User("Jessica", "5678", "password")
# print(user.name, user.pin, user.password)


""" Driver Code for Task 2 """
# user = User("Jessica", "5678", "password")
# print(user.name, user.pin, user.password)
# print(user.change_name("Julie"), user.change_pin("1234"), user.change_password("newpassword"))


""" Driver Code for Task 3 """
# bank_user1 = BankUser("John", "1234", "password")
# print(bank_user1.name, bank_user1.pin, bank_user1.password, bank_user1.balance)


""" Driver Code for Task 4 """
# bank_user2 = BankUser("Joe", "4321", "password")
# bank_user2.show_balance()
# bank_user2.deposit(1000)
# bank_user2.show_balance()
# bank_user2.withdraw(500)
# bank_user2.show_balance()


""" Driver Code for Task 5 """
# first_user = BankUser("Bob", "7849", "bobpassword")
# second_user = BankUser("Alice", "0238", "alicepassword")
# second_user.deposit(5000)
# second_user.show_balance()
# first_user.show_balance()
# print()
# second_user.transfer_money(500, first_user)
# second_user.show_balance()
# first_user.show_balance()
# print()
# second_user.request_money(250, first_user)
# second_user.show_balance()
# first_user.show_balance()
