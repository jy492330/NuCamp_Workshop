"""
Nucamp
Week 3 workshop Assignment: Donation Website
Creator: Jin Jessica Yang
"""

from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register


database = {"admin": "password123"}
donations = list()


def main():
    authorized_user = ''
    while True:
        show_homepage()
        if authorized_user == '':
            print("You must be logged in to donate.")
        else:
            print(f"Logged in as: {authorized_user}")

        option = input("Choose an option: ")
        if option == "5":
            print()
            print("Exit DonateMe Homepage")
            break
        elif option == "1":  # Write Login Functionality
            print()
            username = input("Enter username: ")
            password = input("Enter password: ")
            print()
            authorized_user = login(database, username, password)
        elif option == "2":  # Write Register Functionality
            print()
            username = input("Enter username: ")
            password = input("Enter password: ")
            print()
            authorized_user = register(database, username)
            if authorized_user != '':
                database[username] = password
        elif option == "3":  # Write Donate Functionality
            print()
            if authorized_user != '':
                donation_str = donate(authorized_user)
                donations.append(donation_str)
            else:
                print("You are not logged in.")
        elif option == "4":  # Write Show Donations Functionality
            show_donations(donations)
        else:
            print("You must enter a valid option 1-5")


main()
