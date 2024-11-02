# JG
# November 1, 2024
# The program is a class for a bank account, and contains code to test the class

class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):

        self.name = name

        self.account_number = account_number

        self.amount = amount

        self.interest_rate = interest_rate

    def set_interest_rate(self,interest_rate ):

        self.interest_rate = interest_rate

    def deposit(self, amount):

        if amount > 0:

            self.amount += amount

    def withdraw(self, amount):

        if amount > 0 and amount <= self.amount:

            self.amount -= amount

    def calculate_interest(self, days):

        interest = (self.amount * self.interest_rate / 100) * (days / 365)

        return interest


def test_bank_acct():

    # Create a bank account
    account = BankAcct("Bat Man", "123456789", 500, 4)

    # Display account summary before making any changes
    print('Before: ' + str(account.name) + ' : ' + str(account.amount))

    # Test withdrawing money
    account.withdraw(75)

    # Test depositing money
    account.deposit(25)

    # Test calculating the interest
    interest = account.calculate_interest(90)

    print("Interest for 30 days: " + str(interest))

    # Change the interest rate
    account.set_interest_rate(6.5)

    print("New interest rate: " + str(account.interest_rate))

    # Display account summary after making changes
    print('After: ' + str(account.name) + ' : ' + str(account.amount))


# Run the test function
test_bank_acct()

