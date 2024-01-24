voter_name = input("Hey there! Kindly state your name for record purpose: ")
print("Hello", voter_name)
voter_age = input("Kindly provide your age for verification: ")

name = str(voter_name)
age = int(voter_age)

if age < 18:
    print("Sorry, %s, You are not eligible to vote" % (voter_name))
else:
    print("Congratulations %s, You are eligible to vote, kindly proceed to place your vote" % (voter_name))
