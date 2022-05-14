# Create an Exception
class Error(Exception):
    pass


# Create an Account Class to speak to the Bank class
class Account():

    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = self.check_amount(balance)
        self.pin = pin
        self.loan = 0

    # Function to convert amount to a Integer
    def check_amount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise Error('must be an integer')
        if amount < 0:
            raise Error('you can not take out a negative amount')
        return amount

    # Check if the pin of the Account is correct
    def check_pass(self, pin):
        if pin != self.pin:
            raise Error('wrong pin try again')

    # Take off money from Balance
    def withdraw(self, withdraw_amount):
        withdraw_amount = self.check_amount(withdraw_amount)
        if withdraw_amount > self.balance:
            raise Error('you do not have enough money to withdraw that')
        self.balance = self.balance - withdraw_amount
        return self.balance
    # Add money to the Balance
    def deposit(self, deposit_amount):
        deposit_amount = self.check_amount(deposit_amount)
        self.balance = deposit_amount + self.balance
        return self.balance

    def check_balance(self):
        return self.balance
    # Be able to take out a Loan
    def o_loan(self, loan_amount):
        loan_amount = self.check_amount(loan_amount)
        self.balance = loan_amount + self.balance
        self.loan = loan_amount
        return self.loan
    # pay off a Loan
    def pay_debt(self, pay_off):
        pay_off = self.check_amount(pay_off)
        if pay_off > self.balance:
            raise Error('insufficient funds. please deposit more money or change amount')
        self.loan = (pay_off - self.loan)
        self.balance = (self.balance - pay_off)
        print('your current balance is: ', self.balance)
        return self.loan
    # Show the Debt
    def get_amount_owed(self):
        return self.loan
