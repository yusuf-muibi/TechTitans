print("This is the prime number generator")
while True:
    try:
        number = int(input("Kindly input the number to check if its prime\n"))
        if (number > 0):
            break
        else:
            print("Invalid input, kindly type in a positive integer")
    except ValueError:
        print("Invalid input, kindly type in a positive integer")
prime = True
for i in range(2, int(number**0.5) + 1):
    if (number % i) == 0:
        prime = False
if prime:
    print("%s is a prime number" % (number))
else:
    print("%s is not a prime number" % (number))
