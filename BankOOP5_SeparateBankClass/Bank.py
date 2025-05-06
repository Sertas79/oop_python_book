# Банк, управляющий словарем объектов Account
from Account import *


class Bank:
    def __init__(self, hours, address, phone):
        self.accountDict = {}
        self.nextAccountNext = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def askForValidAccountNumber(self):
        accountNumber = input('What is your account number? ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AboutTransaction('The account number must be an integer')
        if accountNumber not in self.accountDict:
            raise AboutTransaction('There is no account ' +
                                   str(accountNumber))
        return accountNumber

    def getUsersAccount(self):
        accountNumber = self.askForValidAccountNumber()
        oAccount = self.accountDict[accountNumber]
        self.askForValidAccountNumber(oAccount)
        return oAccount

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNext
        self.accountDict[newAccountNumber] = oAccount
        # увеличиваем н единицу для подготовки к созданию следующей
        # учетной записи
        self.nextAccountNext += 1
        return newAccountNumber

    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is the name for the new user account? ')
        userStartingAmount = int(input('What is the staring balance for '
                                       'this account? '))
        userPassword = input('What is the password you want to use for '
                             'this account? ')

        userAccountNumber = self.createAccount(userName,
                                               userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)
        print()

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = int(input('What is your account number? '))
        userPassword = input('What is your password? ')
        oAccount = self.accountDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print('You had', theBalance, 'in your account, which is '
                                         'begin returned to you.')
            # удаляем учетную запись пользователя из словаря учетных
            # записей
            del self.accountDict[userAccountNumber]
            print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        userAccountNumber = int(input('Please enter your account number: '))
        userAccountPassword = input('What is your password? ')
        oAccount = self.accountDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        oAccount = self.getUsersAccount()
        depositAmount = int(input('Please enter amount to deposit: '))
        theBalance = oAccount.deposit(depositAmount)
        print('Deposited:', depositAmount)
        print('Your new balance is:', theBalance)

    def show(self):
        print('*** Show ***')
        print('(This would typically require an admin password)')
        for userAccountNumber in self.accountDict:
            oAccount = self.accountDict[userAccountNumber]
            print('Account:', userAccountNumber)
            oAccount.show()
            print()

    def withdraw(self):
        print('*** Withdraw ***')
        oAccount = self.getUsersAccount()
        userAccountNumber = int(input('Please enter your account number'))
        userAmount = int(input('Please enter your account number: '))
        userAccountPassword = input('What is your password? ')
        oAccount = self.accountDict[userAccountNumber]
        theBalance = oAccount.withdraw(userAmount, userAccountPassword)
        if theBalance is not None:
            print('Withdrew:', userAmount)
            print('Your new balance is:', theBalance)

    def getInfo(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print('We currently have', len(self.accountDict), 'account(s) '
                                                          'open.')
