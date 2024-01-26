small = 2.00
medium = 3.00
large = 4.00

#Introduction
print("Welcome to TechTitans Coffee Shop")

while True:
    print("Would you like a small, medium, or large?")
    #takes in coffee size
    size = input("Kindly place your order, s for small, m for medium or l for large:\n")
    if size == "s":
        size = small
        break
    elif size == "m":
        size = medium
        break
    elif size == "l":
        size = large
        break
    else:
        print("Invalid input, Please enter 's', 'm' or 'l'")
while True:
    print("Would you like any extras?")
        #requests for extra
    extra = input("Kindly enter yes or no:\n")
            #checks if correct extra is inputted
    if extra == "yes":
        has_extra = 1.00
        break
    elif extra == "no":
        has_extra = 0.00
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'")

total_price = size + has_extra
print("The total cost of your order is: $", total_price)

