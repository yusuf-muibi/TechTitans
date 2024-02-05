def positive_int(prime_num):
    if prime_num <= 1:
        return False
    for i in range(2, int(prime_num**0.5) + 1):
        if prime_num % i == 0:
            return False
    return True


while True:
    user_int = input("Enter a positive integer: \n")

    if user_int.isdigit():
        prime_num = int(user_int)

        if prime_num > 0:
            if positive_int(prime_num):
                print(f"{prime_num} is a prime number")
                break
            else:
                print(f"{prime_num} is not a prime number, please enter a prime number")
        else:
            print("Make sure it is a positive integer")
    else:
        print("Invalid input. Please enter a valid positive integer.")
