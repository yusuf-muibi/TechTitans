print("Welcome to Toby's leap year checker")

what_year = int(input("Input the year: "))

if what_year % 4 == 0:
    print(f"{what_year} is a leap year")
elif what_year % 100 == 0:
    print(f"{what_year} is not a leap year")
elif what_year % 400 == 0:
    print(f"{what_year} is a leap year")
else:
    print(f"{what_year} is not a leap year")
