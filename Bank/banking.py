class BankAccount:
    def __init__(self, name, balance=0):
        self.account_holder = name
        self.bal = balance

    def deposit(self, amount):
        self.bal = self.bal + amount
        print(f"Deposited {amount} to your account")

    def withdrawal(self, amount):
        if amount > self.bal:
            print(f"Insufficient fund, your available balance is {self.bal}")

        else:
            self.bal = self.bal - amount

    def __str__(self):
        return f"Account Holder Name: {self.account_holder} \nBalance: {self.bal}"


obj = BankAccount("Tobi", 2000)
print(obj)
obj.deposit(200)
obj.withdrawal(500)
print(obj)
