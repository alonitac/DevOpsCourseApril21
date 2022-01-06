"""
Create a bank account class that has two attributes:

* owner
* balance

and two methods:

* deposit
* withdraw

As an added requirement, withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""


class Account:
    def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print('Deposit Accepted')
        else:
            print('Deposit Rejected')

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')

    def __str__(self):
        return f'Account owner:   {self.owner} \nAccount balance: ${self.balance}'


class StudentAccount(Account):
    pass


if __name__ == '__main__':
    acct1 = Account('Jose', 100)
    print(acct1.owner)
    print(acct1.balance)
    print(acct1)
    acct1.deposit(50)
    print(acct1.balance)
    acct1.withdraw(75)
    acct1.withdraw(500)
