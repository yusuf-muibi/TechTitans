user_name = input("Hey there! Kindly provide your name: ")
user_score = input("Thank you, now, please provide your score: ")

name = str(user_name)
score = float(user_score)


if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

"""F-string
print(f"The grade for the score {score} is {grade}.")


Modulus Operator
print("The grade for %s for the score %s is: %s" % (name, score, grade))
"""

"""F-string"""
print(f"The grade for {name} for the score {score} is {grade}")