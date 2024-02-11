# We are creating a sign up or sign in form for our website.
# Create a prompt to either sign in or sign up
# if the user choosesto sign up collect the user's information.
# If they choose to sign in, only ask for their username and password

print("Welcome to Tech-titans portal")

users = []

isuser_loggedin = False

while True:
    choice = input("Do you want to Sign Up or Sign In: ")
    if choice.lower() == "sign up":
        name = input("Please enter your Fullname: ")
        username = input("Enter your desired Username: ")
        email = input("Enter your email: ")
        password = input("Create a Password: ")
        users.append(
            {"Name": name, "Username": username, "Email": email, "Password": password}
        )
        print(f"Hello {name}, Your account has been created!")

        while True:
            choice_sign = input("Do you want to proceed with Signing In? Y/N: ")

            if choice_sign.lower() == "y":
                isuser_loggedin = True
                break
            elif choice_sign.lower() == "n":
                continue
            else:
                print("Invalid Input! Please Enter a Valid input Again.")

        if choice_sign.lower() == "y":
            while True:
                log_username = input("Enter your Username: ")

                if any(user["Username"] == log_username for user in users):
                    logged_in_user = next(
                        user for user in users if user["Username"] == log_username
                    )
                    print("Proceed")
                    break
                else:
                    print("User not found! Try again.")

            while True:
                log_password = input("Enter your Password: ")

                if any(user["Password"] == log_password for user in users):
                    logged_in_user = next(
                        user for user in users if user["Password"] == log_password
                    )
                    print(f"Successfully Logged in")
                    break
                else:
                    print("Wrong password. Try again.")

    elif choice.lower() == "sign in":
        username = input("Enter your Username: ")
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")
        print(f"You have successfully logged in as {username}")
        break
    else:
        print(f"{choice} is not a valid option.")

    if isuser_loggedin:
        break
