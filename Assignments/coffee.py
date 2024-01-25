print("Welcome to Toby's coffee shop")

while True:
    size_coffee = input("Enter the size of your coffee (Small, Medium, Large): ")

    """Prices"""

    smallcoffee_price = 2.00
    mediumcoffee_price = 3.00
    largecoffee_price = 4.00
    extracoffee_price = 1.00
    noextracoffee_price = 0.00

    """Calculating the total price"""
    total_price = 0

    if size_coffee == "Small":
        total_price += smallcoffee_price
        break
    elif size_coffee == "Medium":
        total_price += mediumcoffee_price
        break
    elif size_coffee == "Large":
        total_price += largecoffee_price
        break
    else:
        print("Invalid coffee size. Please choose Small, Medium, or Large.")

while True:
    extra_coffee = input("Do you want an extra? (Yes/No): ")

    if extra_coffee == "Yes":
        total_price += extracoffee_price
        break
    elif extra_coffee == "No":
        total_price += noextracoffee_price
        break
    else:
        print("Invalid input!, Please enter Yes or No.")


"""Display the total price"""
if total_price > 0:
    print(f"Your total price is: ${total_price:.2f}")

print("Order Completed")
