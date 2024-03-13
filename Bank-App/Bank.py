print("Welcome to Tech-titans portal")
cus_data = {}

techtitans_database = ".database"
import json
import re


def mainlayout():
    cus_signup = input("Do you want to sign Up or sign In: ")

    if cus_signup.lower() == "sign up":
        signup()
    elif cus_signup.lower() == "sign in":
        signin()
    else:
        print("Invalid Option Please enter 'sign Up' or 'sign In'")


def signin():
    try:
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")

        with open(techtitans_database, "r") as td:
            cus_data = json.load(td)

            if username_input in cus_data:
                if cus_data[username_input]["password"] == password_input:
                    print(f"Welcome back, {username_input}")
                else:
                    print("Incorrect password. Please try again.")
            else:
                print("Username not found. Please sign up if you haven't already.")

    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")


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

        with open(techtitans_database, "r") as td:
            cus_data = json.load(td)

        cus_data[cus_info["Username"]] = cus_info

        with open(techtitans_database, "w") as td:
            json.dump(cus_data, td, indent=2)

        print(f"Successfully signed up {cus_info['Username']}")

    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")


try:
    mainlayout()
except ValueError as ve:
    print(f"Error! {ve}")
