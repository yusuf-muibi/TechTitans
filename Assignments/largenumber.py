# Write a Python function called find_largest_to_smallest_number that takes three numbers as parameters from the user
# and returns an output from largest to the smallest number.
# Don't use any built-in Python functions like max().


def find_largest_to_smallest_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        largest_num = num1
        if num2 >= num3:
            middle_num = num2
            smallest_num = num3
        else:
            middle_num = num3
            smallest_num = num2
    elif num2 > num1 and num2 > num3:
        largest_num = num2
        if num1 >= num3:
            middle_num = num1
            smallest_num = num3
        else:
            middle_num = num3
            smallest_num = num1
    else:
        largest_num = num3
        if num1 >= num2:
            middle_num = num1
            smallest_num = num2
        else:
            middle_num = num2
            smallest_num = num1

    return  largest_num, middle_num, smallest_num

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


varying_num = find_largest_to_smallest_number(num1, num2, num3)

print(f"largest - smallest {varying_num}")
