from acctcreation import signin, signup

print("Welcome to Tech-titans portal")
def mainlayout():
    while True:
        cus_signup = input(
            "Do you want to sign up or sign in (or type 'exit' to quit): "
        )

        if cus_signup.lower() == "sign up":
            signup()
        elif cus_signup.lower() == "sign in":
            signin()
        elif cus_signup.lower() == "exit":
            print("Goodbye!")
            exit(1)
        else:
            print("Invalid Option Please enter 'sign up' or 'sign in'")


try:
    mainlayout()
except ValueError as ve:
    print(f"Error! {ve}")
