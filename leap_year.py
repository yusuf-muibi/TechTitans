print("Welcome to the leap year calculator")
while True:
    user_input = input("Kindly provide the year you'd like to know if it's a leap year:\n")
    if len(user_input) == 4:
        break
    else:
        print("Invalid input, kindly type a valid year")
year = int(user_input)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("%s is a leap year" % (year))
else:
    print("%s is not a leap year" % (year))
