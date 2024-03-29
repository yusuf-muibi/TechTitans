cus_data = {}

techtitans_database = ".database"
import json
import re
from os import path

default_balance = 0.00


def signin():
    try:
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")

        with open(techtitans_database, "r") as td:
            cus_data = json.load(td)

            if username_input in cus_data:
                if cus_data[username_input]["password"] == password_input:
                    print(f"Welcome back, {username_input}")
                    return username_input
                else:
                    print("Incorrect password. Please try again.")
            else:
                print("Username not found. Please sign up if you haven't already.")

    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
    return None


def signup():
    try:
        cus_info = {}
        cus_signups = ["Fullname", "Username", "Email", "Phone number"]

        for i in cus_signups:
            if i == "Email":
                while True:
                    email = input(f"Enter your {i}: ")
                    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                        cus_info[i] = email
                        break
                    else:
                        print("Invalid email format! Please enter a valid email.")
            else:
                cus_info[i] = input(f"Enter your {i}: ")

        while True:
            cus_pword = input("Create Password: ")

            if len(cus_pword) >= 8 and cus_pword[0].isupper():
                con_pword = input("Confirm password: ")

                if con_pword == cus_pword:
                    print("Password match")
                    break
                else:
                    print("Passwords do not match. Try again.")
            else:
                print(
                    "Invalid password! Make sure it's at least 8 characters long and starts with an uppercase letter."
                )

        cus_info["password"] = cus_pword

        """To first of all load the existing database"""
        if not path.exists(techtitans_database) or path.getsize(techtitans_database) == 0:
            cus_data = {}
        else:
            with open(techtitans_database, "r") as td:
                    cus_data = json.load(td)

        """To add the user information to the database"""
        cus_data[cus_info["Username"]] = cus_info

        """To write the updated data back into the file"""
        with open(techtitans_database, "w") as td:
            json.dump(cus_data, td, indent=2)

        print(f"Successfully signed up {cus_info['Username']}")

        signin_option = input("Do you want to sign in now ? (yes/no): ")

        if signin_option.lower() == 'yes':
            signin()
        elif signin_option.lower() =="no":
            print("Goodbye!")
            exit(1)
        else:
            print("Invalid Option! Please enter a valid option.")

    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
