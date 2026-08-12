# Instance Methods Practice

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    # Instance method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Updated Balance:", self.balance)

    # Instance method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Updated Balance:", self.balance)
        else:
            print("Insufficient funds.")

    # Instance method to get current balance
    def get_balance(self):
        return self.balance


# Creating a BankAccount object
account = BankAccount(100000000)

print("Initial Balance:", account.get_balance())

account.deposit(5000000)

account.withdraw(300000)

print("Final Balance:", account.get_balance())