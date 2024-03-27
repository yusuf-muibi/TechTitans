from acctcreation import signin, signup
from banking import deposit, withdraw, check_balance, invest
import time

print("Welcome to Tech-titans portal")


def mainlayout():
    while True:
        cus_signup = input(
            "Do you want to sign up or sign in (or type 'exit' to quit): "
        )

        if cus_signup.lower() == "sign up":
            signup()
        elif cus_signup.lower() == "sign in":
            username = signin()

            while True:
                cus_banking = input("Would you like to access banking services? y/n: ")
                if cus_banking.lower() == "y":
                    while True:
                        options = input(
                            "\nBanking Services:\n1. Check Balance\n2. Withdraw Money\n3. Deposit money\n4. Invest\nEnter: "
                        )
                        if options.lower() == "1":
                            check_balance(username)
                        elif options.lower() == "2":
                            withdraw(username)
                        elif options.lower() == "3":
                            deposit(username)
                        elif options.lower() == "4":
                            invest(username)
                        else:
                            print("Error! Please enter a valid option.")
                            continue

                        another_services = input("Do you want to perform another banking operation? (y/n): ")
                        if another_services.lower() != "y":
                            break

                elif cus_banking.lower() == "n":
                    time.sleep(3)
                    print("Goodbye")
                    exit(1)
                else:
                    print("Invalid input please enter y/n")
                    continue

                signout = input("Do you want to sign out? (y/n): ")
                if signout.lower() == "y":
                    break

        elif cus_signup.lower() == "exit":
            print("Goodbye!")
            exit(1)
        else:
            print("Invalid Option Please enter 'sign up' or 'sign in'")



try:
    mainlayout()
except ValueError as ve:
    print(f"Error! {ve}")
