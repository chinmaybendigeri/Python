class Bank:

    def __init__(self, owner, balance=100):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"{amount} Deposit Successful!")
        return self.balance


    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient Funds!")
        else:
            self.balance = self.balance - amount
            print(f"{amount} Withdraw Successful!")
        return self.balance

    def __str__(self):
        return f"Available Balance is {self.balance}"


myaccount = Bank("chinmay")

print(myaccount.owner)
print(myaccount.balance)
print(myaccount)
print(myaccount.deposit(100))
print(myaccount.withdraw(150))
print(myaccount.withdraw(500))
