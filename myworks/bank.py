"""Create a signin, signup as functions
Add an option to deposit, withdraw and invest
invest, and check balance.
For password (it sld not be less than 8, it must contain letters(upper and lower case), numbers)
To make the email a real email, we might use regex
"""
import json #a way of saving our string value in a way the computer can understand and it is easier for our computer to access it as a dictionary
import re
Techtitan_database = '.database'
print("Welcome to techtitans 'Our bank your bank'")
cus_data = {}

def validate_email(email):
    # Define a regex pattern for email validation
    pattern = r"[\w\.-]+@[\w\.-]+(\.[\w]+)+"
    # Use re.match() to find matches
    if re.match(pattern, email):
        return True
    else:
        return False

def signin():
    try:
        cus_username = input("Enter username: ")
        signin_pword = input("Enter password: ")
        with open(Techtitan_database, "r") as td:
            cus_data = json.load(td)
            if cus_username in cus_data:
                if cus_data[cus_username]["password"] == signin_pword:
                    print(f"Welcome back {cus_username}")
                else:
                    print("Incorrect password")
            else:
                print("User not found")
    except (EOFError):
        print("Exit")
def signup():
    try:
        cus_signup = input("Do you want to signup or signin: ")
        if cus_signup.lower() == "signup":
            cus_info = {}
            cus_signup = ['Fullname', 'Username', 'Email', 'Address','Phone number']
            for cus in cus_signup:
                cus_info[cus] = input(f"Enter your {cus}: ")

                if cus == 'Email' and not validate_email(cus_info['Email']):
                    print("Invalid Email combination")
                    return 
            while True:

                cus_pword = input("Create your password, password must contain upper, lower and special characters and >= 8: ")
                if not len(cus_pword) >= 8 or not any(char.isupper() for char in cus_pword) or not any(char.islower() for char in cus_pword):
                    print("password must contain characters greater than 8 and must include upper,lower and special characters")
                    print("pls try again")
                    continue
                
    
                con_pword = input("Confirm your password: ") 
                
                if con_pword == cus_pword:
                    print("Valid password")
                    break
                else:
                    print("Invalid password")
                cus_info["password"] = cus_pword
                    

                cus_data[cus_info['Username']] = cus_info 
            
            with open(Techtitan_database, "a") as td:
                json.dump(cus_info, td, indent=2)
        elif cus_signup.lower() == "signin":
            signin()
        else:
            print("Invalid input, signin or signup")
    except(EOFError):
        print("Exiting Program")
try:
    signup()
except ValueError as ve:
    print("Error")