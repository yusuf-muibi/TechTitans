from acctcreation import techtitans_database
import json


def deposit(username, amount):
    try:
        with open(techtitans_database, "r") as td:
            cus_data = json.load(td)
            if username in cus_data:
                cus_data[username]["balance"] += amount
                print(
                    f"Deposit successful. New balance: {cus_data[username]['balance']}"
                )
                with open(techtitans_database, "w") as td:
                    json.dump(cus_data, td, indent=2)
            else:
                print("User not found")
    except Exception as e:
        print(f'An error occurred:" ,{e}')


def withdraw(username, amount):
    try:
        with open(techtitans_database, "r") as td:
            cus_data = json.load(td)
            if username in cus_data:
                if cus_data[username]["balance"] >= amount:
                    cus_data[username]["balance"] -= amount
                    print(
                        f"Withdrawal successful. New balance: {cus_data[username]['balance']}"
                    )
                    with open(techtitans_database, "w") as td:
                        json.dump(cus_data, td, indent=2)
                else:
                    print("Insufficient balance")
            else:
                print("User not found")
    except Exception as e:
        print(f'An error occurred:", {e}')


def invest(username, amount):
    try:
        with open(techtitans_database, "r") as td:
            cus_data = json.load(td)
            if username in cus_data:
                if cus_data[username]["balance"] >= amount:
                    cus_data[username]["balance"] -= amount
                    cus_data[username]["investments"] += amount
                    print(
                        f"Investment successful. New balance: {cus_data[username]['balance']}"
                    )
                    with open(techtitans_database, "w") as td:
                        json.dump(cus_data, td, indent=2)
                else:
                    print("Insufficient balance")
            else:
                print("User not found")
    except Exception as e:
        print('An error occurred:", {e}')


def check_balance(username):
    try:
        with open(techtitans_database, "r") as td:
            cus_data = json.load(td)
            if username in cus_data:
                print(f"Current balance: {cus_data[username]['balance']}")
            else:
                print("User not found")
    except Exception as e:
        print(f'An error occurred:", {e}')
