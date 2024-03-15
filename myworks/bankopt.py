"""start
check if the user has signed in
prompt the banking options
check balance
invest
deposit
withdraw"""
import bank
def check_balance():
    balance = 0.00
    if bank.signin == True:
        print(balance)

check_balance()





def deposit():
    amount = int(input("input the amount you want to deposit: "))
