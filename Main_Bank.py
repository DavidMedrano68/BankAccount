from bank import *
oBank = Bank()
# loop until False
while True:
    print()
    print('to pay off an existing loan press "p"')
    print('to check your balance press "b"')
    print('to create an account press "c"')
    print('to make a deposit press "d"')
    print('to make a withdraw press "w"')
    print('to quit press "x"')
    print('to get a loan press "l" ')
    print()
# Prompt user then Grab user's first letter and lower cases it
    response = input('what would you like to do?')
    response = response.lower()
    response = response[0]
# with User's response do appropriate Action
    try:
        if response == 'c':
            oBank.open_acc()
        elif response == 'd':
            oBank.deposit()
        elif response == 'x':
            break
        elif response == 'w':
            oBank.withdraw()
        elif response == 'b':
            oBank.get_balance()
        elif response == 'l':
            oBank.get_loan()
        elif response == 'p':
            oBank.pay_loan()

    except Error:
        print(Error)
print('done')







