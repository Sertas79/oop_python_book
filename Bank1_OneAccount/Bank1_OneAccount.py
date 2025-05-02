# Без ООП
# Банк. Версия 1
# Единственный счет

accountName = 'Jot'
accountBalance = 100
accountPassword ='soup'

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
        if userPassword != accountPassword:
            print('Incorrect password')
        else:
            print('Your balance is:', accountBalance)
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        if userDepositAmount < 0:
            print('You cannot deposit a negative amount!')

        elif userPassword != accountPassword:
            print('Incorrect password')
        else: # Ok
            accountBalance = accountBalance + userDepositAmount
            print('Your new balance is:', accountBalance)
    elif action == 's': # отображаем
        print('Show:')
        print('         Name', accountName)
        print('         Balance:', accountBalance)
        print('         Password:', accountPassword)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw')

        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)

        if userWithdrawAmount < 0:
            print('You cannot withdraw a nagative amount')

        elif userPassword != accountPassword:
            print('Incorrect password for this account')

        elif userWithdrawAmount > accountBalance:
            print('You cannot withdraw more than you have in your '
                  'account')
        else:
            accountBalance = accountBalance - userWithdrawAmount
            print('Your new balance is:', accountBalance)
print('Done')