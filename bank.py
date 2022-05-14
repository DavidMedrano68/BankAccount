from account import *

# Bank Class to Store every account's separate data in a dictionary
class Bank():
    def __init__(self):
        self.AccountDict = {}
        self.NextAccountNumber = 0
# Ask user for Account number
    def ask_for_acct_num(self):
        acc_num = input('put in your account num: ')
        try:
           acc_num = int(acc_num)
        except ValueError:
            raise Error('account number must be an integer')
        if acc_num not in self.AccountDict:
            raise Error('your account number is not associated with any account')
        return acc_num
# get Accounts info
    def get_account(self):
        acc_num = self.ask_for_acct_num()
        o_account = self.AccountDict[acc_num]
        self.ask_for_pin(o_account)
        return o_account
# ask user to enter correct pin
    def ask_for_pin(self, o_account):
        pin = input('please enter in your pin')
        o_account.check_pass(pin)
# Function that works with the Open account function to create an account within the Bank Class
    def create_account(self, the_name, the_balance, the_pin):
        print('***create an account***')
        o_account = Account(the_name, the_balance, the_pin)
        new_account_number = self.NextAccountNumber
        self.AccountDict[new_account_number] = o_account
        self.NextAccountNumber = self.NextAccountNumber + 1
        return new_account_number

    def deposit(self):
        print('**deposit**')
        o_account = self.get_account()
        deposit_amount = input('please enter how much you would like to deposit')
        the_balance = o_account.deposit(deposit_amount)
        print('you have deposited: ', deposit_amount)


    def withdraw(self):
        print('**withdraw**')
        o_account = self.get_account()
        amount_to_withdraw = input('how much would you like to withdraw? ')
        the_balance = o_account.withdraw(amount_to_withdraw)
        print('you currently have: ', the_balance)
# Create an account and associate Account number to it
    def open_acc(self):
        print('**open account**')
        the_name = input('what is your name? ')
        the_balance = input('what would be your beginning balance? ')
        the_pin = input('what would you want your security pin to be? ')
        user_acc_num = self.create_account(the_name, the_balance, the_pin)
        print('you have successfully made an account ')
        print('your account number is: ', user_acc_num)

    def get_balance(self):
        print('**getting balance**')
        o_account = self.get_account()
        the_balance = o_account.check_balance()
        print('your balance is: ', the_balance)

    def get_loan(self):
        o_account = self.get_account()
        print('to get a loan you would have to have an account with us ')
        loan_amount = input('how much would you like to borrow? ')
        debt = o_account.o_loan(loan_amount)
        the_balance = o_account.check_balance()
        print('you currently owe: ', debt)
        print('your balance is: ', the_balance)

    def pay_loan(self):
        o_account = self.get_account()
        debt = o_account.get_amount_owed()
        if debt <= 0:
            return False
        pay_off = input('how much would you like to pay off your loan? ')
        remainder = o_account.pay_debt(pay_off)
        print('you owe the bank : ', remainder)

    def show_debt(self):
        o_account = self.get_account()
        debt = o_account.get_amount_owed
        print('your currently owe the bank: ', debt)





