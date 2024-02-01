#!/usr/bin/python3
#This code checks plp who takes up the csfree challenge performing the necessary task for 89days, will be entitled
#to 5000 virtual bobo.
print("You are welcome to CSFree tutorial class. To paticipate in the challange, Fill in your details")

Fname = input("Enter your fname: ")
Surname = input("Enter your Surname: ")
Challange_days = input("Enter days you took the challange: ")

days = int(Challange_days)

if days >= 89:
    print(f"Conratulations {Fname} {Surname} because you performed the required task, you are entitled to CSFree virtual bobo ")
    print("Congratulations %s %s, because you performed the required task, you are entitled to CSFree virtual bobo" % (Fname, Surname))
else:  
    print(f"{Fname}{Surname} you are not entitled to CSFree virtual Bobo")
    print("%s %s, you are not entitled to CSFree virtual Bobo" % (Fname, Surname))