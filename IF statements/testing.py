username_str = input("Good day sir/ma, Please state your name: ")

print(f"Hey {username_str}! Let's check if you're eligible to vote.")

user_age = input("Please enter your age: ")

age = int(user_age)

votingAge_range = 18

if age >= votingAge_range:
    print(f"Hi {username_str}, You are eligible to vote!")
else:
    print(f"Hi {username_str} Sorry, you are not eligible to vote yet.")
