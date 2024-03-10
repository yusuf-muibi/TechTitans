# # create the signin, signup as function
# # add an option for invest, deposit, withdraw and check balance

# import json
# techtitans_database = '.database' # we are assigning a variable to takein our customers data 
# print('Welcome to Techtitans "Credit is what we do"')
# customer_data = {}
# def signin():
#     try:
#         customer_username = input("Enter username: ")
#         signin_password = input("Enter password: ")  
#         with open(techtitans_database, 'r') as td:
#             customer_data = json.load(td)
#             # if customer_username in customer_data:
#             #     if cus_data[cus]
#     except(EOFError):
#         print("Exit")
# def signup():
#     try:
#         customer_signup = input("Do you want to signup or signin: ")
#         if customer_signup.lower() == "signup":
#             customer_info = {}
#             customer_signup = ["fullname", "Username", "Email", "Phone number"]

#             for i in customer_signup: # the i is the input thta goes into customer signup and the 
#                 customer_info [i] = input(f"Enter your{i}: ") #here the i prompths all thats in the customer_signup and its kept in the customer_info

#             while True:

#                 customer_pasword = input("Create a password: ")
#                 correct_pasword = input("Confirm password")
#                 if customer_pasword == correct_pasword: 
#                     print("Valid Password") 
#                     break
#                 else:
#                     print("Invalid password")
#                 customer_info["password"] = customer_pasword

#                 customer_data[customer_info["ussername"]] == customer_info

#             with open(techtitans_database, "w") as td:
#                 json.dump(customer_info, td, indent=2)
#         elif customer_signup.lower() == "signin":
#             signin()
#         else:
#             print("Invalid input, Signin or Signup")

#     except(EOFError):
#         print("Exiting program")

# try: 
#     signup()
# except ValueError as ve:
#     print("Error")


print("This is a very long line that I want to \
      write in a more readable way.")