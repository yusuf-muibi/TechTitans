print("Welcome to Toby's coffee shop")

size_coffee = input("Enter the size of your coffee (Small, Medium, Large): ")
extra_coffee = input("Do you want an extra? (Yes/No): ")

"""Prices"""

smallcoffee_price = 2.00
mediumcoffee_price = 3.00
largecoffee_price = 4.00
extracoffee_price = 1.00

"""Calculating the total price"""
total_price = 0

if size_coffee == "Small":
    total_price += smallcoffee_price
elif size_coffee == "Medium":
    total_price += mediumcoffee_price
elif size_coffee == "Large":
    total_price += largecoffee_price
else:
    print("Invalid coffee size. Please choose Small, Medium, or Large.")


if extra_coffee == "Yes":
    total_price += extracoffee_price
elif extra_coffee == "No":
    print("Ok")


"""Display the total price"""
if total_price > 0:
    print(f"Your total price is: ${total_price:.2f}")

print("Order Completed")