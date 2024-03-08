# Create a signin, signup as functions
# Add an option to deposit, withdraw , invest and check balance
import json
techtitan_database = '.database'
print('Welcome to Techtitans "Our bank your bank"')
cus_data = {}
def signin():
    try:
        cus_username = input("Enter username: ")
        signin_pword = input("Enter password: ")
        with open(techtitan_database, 'r') as td:
            cus_data = json.load(td) 
            if cus_username in cus_data:
                if cus_data[cus_username]["password"] == signin_pword:
                    print(f"Welcome back {cus_username}")
                else:
                    print("Incorrect password")
            else:
                print("User not found")

    except(EOFError):
        print("Exit")
def signup():
    try:
        cus_signup = input("Do you want to signup or signin: ")
        if cus_signup.lower() == "signup":
            cus_info = {}
            cus_signup = ["Fullname", "Username", "Email", "Phone number"]
            
            for i in cus_signup:
                cus_info[i] = input(f"Enter your {i}: ")
            
            while True:
                cus_pword = input("""Create a password, password must have characters equal to or 
greater than 8 and must include  upper and lower case letter: """)
                if len(cus_pword) < 8 or not any(char.isupper() for char in cus_pword) or not any(char.islower() for char in cus_pword):
                    print("Password must contain character greater or equal to 8 and must include upper and lower case letter")
                    print("Please try again")
                    continue
                con_pword = input("Confirm password: ")
                
                if con_pword == cus_pword:
                    print("Valid password")
                    break
                else:
                    print("Invalid password")
                cus_info["password"] = cus_pword
                
                cus_data[cus_info["username"]] = cus_info 
                
            with open(techtitan_database, "a") as td:
                json.dump(cus_info, td, indent=2) 
        elif cus_signup.lower() == "signin":
            signin()
        else:
            print("Invalid input, signin or signup")
                
    except(EOFError):
        print("Exiting program")
try:
    signup()
except ValueError as ve:
    print("Error")