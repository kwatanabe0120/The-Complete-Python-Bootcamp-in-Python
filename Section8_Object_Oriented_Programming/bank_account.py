class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,value):
        print('Deposite is accepted')
        self.balance += value

    def withdraw(self,value):
        if self.balance < value:
            print("You don't have enoght money!")
        else:
            print('Withdrow is accepted')
            self.balance -= value

    def __str__(self):
        return f'Account Owner: {self.owner}\nAccount balance: {self.balance}'

acct1 = Account('Jose',300)

print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(100)
print(acct1.balance)
acct1.withdraw(100)
print(acct1.balance)
acct1.withdraw(100000000000)