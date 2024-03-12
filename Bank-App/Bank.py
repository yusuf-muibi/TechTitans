# Create a signin, signup as functions
# Add an option to deposit, withdraw , invest and check balance
import json
import re

techtitan_database = ".database"
print('Welcome to Techtitans "Our bank your bank"')
cus_data = {}


def signin():
    try:
        cus_username = input("Enter username: ")
        signin_pword = input("Enter password: ")
        with open(techtitan_database, "r") as td:
            cus_data = json.load(td)
            if cus_username in cus_data:
                if cus_data[cus_username]["password"] == signin_pword:
                    print(f"Welcome back {cus_username}")
                else:
                    print("Incorrect password")
            else:
                print("User not found")

    except EOFError:
        print("Exit")


def signup():
    try:
        cus_signup = input("Do you want to sign up or sign in: ")
        if cus_signup.lower() == "sign up":
            cus_info = {}
            cus_signup = ["Fullname", "Username", "Email", "Phone number"]

            for i in cus_signup:
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

            """ this is where the changes started"""

            while True:
                cus_pword = input("Create Password: ")

                if len(cus_pword) >= 8 and cus_pword[0].isupper():
                    con_pword = input("Confirm password: ")

                    if con_pword == cus_pword:
                        print("Valid password")
                        break
                    else:
                        print("Passwords do not match. Try again.")
                else:
                    print(
                        "Invalid password! Make sure it's at least 8 characters long and starts with an uppercase letter."
                    )

            cus_info["password"] = cus_pword
            cus_data[cus_info["Username"]] = cus_info

            """And it ended here"""

            with open(techtitan_database, "a") as td:
                json.dump(cus_info, td, indent=2)

            print(f"Successfully signed up {cus_info['Username']}")

        elif cus_signup.lower() == "sign in":
            signin()
        else:
            print("Invalid input, sign in or sign up")

    except EOFError:
        print("Exiting program")


try:
    signup()
except ValueError as ve:
    print("Error")
