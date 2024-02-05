correct_password = "python123"

while True:
    user_password = input("Enter the password: ")

    if user_password == correct_password:
        print("Login successful. Welcome!")
        break
    else:
        print("Incorrect password. Please try again.")
