print("Welcome to Tech-titans portal")
user_data = {}  # Dictionary to store user dat
print("type ctrl d or ctrl c to quit the program")

storage = '.database'
import json

def signup():
    try:
        choice = input("Do you want to Sign Up or Sign In: ")

        if choice.lower() == 'sign up':
            user_info = {}  # Dictionary to store individual user's information
            choices = ["fullname", "username", "email"]

            # this senior boy is meant to only execute when choice is equal to sign up
            for usr_input in choices:
                user_info[usr_input] = input(f"Please Enter {usr_input}: ").strip()

            password = input("Create a password: ")
            user_info['password'] = password

            # Use the username as the key in the user_data dictionary
            user_data[user_info['username']] = user_info

            # open a file and write

            with open(storage, 'a') as db:
                # db.write(str(user_data))
                json.dump(user_data, db, indent=2)

            print(f"Successfully signed up {user_info['username']}")
        elif choice.lower() == 'sign in':
            print('signed in')
        else:
            print('Invalid Input! Try Again')
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")

def signin():
    try:
        signin_choice = input("Your username: ")
        pass_choice = input("Your password: ")

            with open(storage, 'b') as db:
                        user_data = json.load(db)
                        if signin_choice in user_data:
                            


try:
    signup()
except ValueError as ve:
    print(f'Error! ve')

#create a sign in button in the elif choice and use the
    #dictionary not the choices
    #create a big dictionary as key and the data as value

   
# choices = {
#     'fullname': input("Input Fullname: "),
#     'username': input("input username: "),
#     'email': input('input email')
# }
#
# print(choices)