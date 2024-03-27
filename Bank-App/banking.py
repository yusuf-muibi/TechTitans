import json

techtitans_database = ".database"


def deposit(username):
    try:
        with open(techtitans_database, "r") as td:
            cus_data = json.load(td)
        if username in cus_data:
            try:
                amount = float(input("Enter the amount to deposit: "))
                if amount > 0:
                    cus_data[username]["balance"] += amount
                    print(
                        f"Deposit successful. Your new balance is: {format(cus_data[username]['balance'], ',.2f')}"
                    )
                    with open(techtitans_database, "w") as td:
                        json.dump(cus_data, td, indent=2)
                else:
                    print("Invalid amount. Please enter a positive value.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Username not found. Please sign up or sign in first.")
    except FileNotFoundError:
        print("Database file not found.")


def withdraw(username):
    try:
        with open(techtitans_database, "r") as td:
            cus_data = json.load(td)
        if username in cus_data:
            try:
                amount = float(input("Enter the amount to withdraw: "))
                if amount > 0 and amount <= cus_data[username]["balance"]:
                    cus_data[username]["balance"] -= amount
                    print(
                        f"Withdrawal successful. Your new balance is: {format(cus_data[username]['balance'], ',.2f')}"
                    )
                    with open(techtitans_database, "w") as td:
                        json.dump(cus_data, td, indent=2)
                elif amount > cus_data[username]["balance"]:
                    print("Insufficient balance.")
                else:
                    print("Invalid amount. Please enter a positive value.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Username not found. Please sign up or sign in first.")
    except FileNotFoundError:
        print("Database file not found.")


def check_balance(username):
    try:
        with open(techtitans_database, "r") as td:
            cus_data = json.load(td)
        if username in cus_data:
            print(
                f"Your current balance is: {format(cus_data[username]['balance'], ',.2f')}"
            )
        else:
            print("Username not found. Please sign up or sign in first.")
    except FileNotFoundError:
        print("Database file not found.")


def invest(username):
    try:
        with open(techtitans_database, "r") as td:
            cus_data = json.load(td)
        if username in cus_data:
            try:
                amount = float(input("Enter the amount to invest: "))
                if amount > 0 and amount <= cus_data[username]["balance"]:
                    cus_data[username]["balance"] -= amount
                    print(
                        f"Investment successful. Your new balance is: {format(cus_data[username]['balance'], ',.2f')}"
                    )
                    with open(techtitans_database, "w") as td:
                        json.dump(cus_data, td, indent=2)
                elif amount > cus_data[username]["balance"]:
                    print("Insufficient balance.")
                else:
                    print("Invalid amount. Please enter a positive value.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Username not found. Please sign up or sign in first.")
    except FileNotFoundError:
        print("Database file not found.")
