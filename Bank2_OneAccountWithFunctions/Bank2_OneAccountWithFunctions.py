# Без ООП
# Банк 2
# Единственный счет

accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def show():
    global  accountName, accountBalance, accountPassword
    print('     Name', accountName)
    print('     Balance', accountBalance)
    print('     Name', accountPassword)
    print()

def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect password')
        return None
    return accountBalance

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != accountPassword:
        print('Incorrect password')
        return None

    accountBalance = accountBalance + amountToDeposit
    return accountBalance

def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword

    if amountToWithdraw < 0:
        print('Tou cannot withdraw a negative amount')
        return None

    if password != accountBalance:
        print('You cannot withdraw more than you have in your account')
        return None

    if amountToWithdraw > accountBalance:
        print('You cannot  withdraw more than you have in your account')
        return None

    accountBalance = accountBalance - amountToWithdraw
    return accountBalance

newAccount('Joe', 100, 'soup')

while True:
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower() # переводим в нижний регистр
    action = action[0] # используем первую букву
    print()

    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        newBalance = deposit(userDepositAmount,userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
    elif action == 's':
        print('Show: ')
        show()
    elif action == 'w':
        print('Withdrawal: ')
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')
        newBalance = withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
    elif action == 'q':
        break
print('Done')
