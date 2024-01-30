# Setup the standard voting age
voting_age = 18

# prompt the  user to enter their name
user_name = str(input("Hello there! kindly enter your name: "))

# Prompt the user to enter their age
user_age = int(input("Hello there! kindly enter your age: "))

# Check if the user is eligible to vote
if user_age >= voting_age:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.")
