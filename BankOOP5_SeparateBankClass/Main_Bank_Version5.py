# Основная программа, контролирующая банк, состоящий из счетов

# Берем весь код класса банка
from Bank import *

# Создаем экземпляр банка
oBank = Bank('9 to 5', '123 Main Street, Anytown, USA', '(650) 555-1212')

# Основной код
while True:
    print()
    print('To get an account balance, press b')
    print('To close account, press c')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    try:
        if action == 'b':
            oBank.balance()
        elif action == 'c':
            oBank.closeAccount()
        elif action == 'd':
            oBank.deposit()
        elif action == 'i':
            oBank.getInfo()
        elif action == 'o':
            oBank.openAccount()
        elif action == 's':
            oBank.show()
        elif action == 'q':
            break
        elif action == 'w':
            oBank.withdraw()
    except AboutTransaction as error:
        print(error)

print('Done')