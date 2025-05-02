# HigherOrLower

import random

# Константы карт
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5','6', '7','8', '9','10',
              'Jack', 'Queen', 'King')

NCARDS = 8

# Проходим по колоде, и эта функция возвращает случайную карту из колоды
def getCard(deckListIn):
    thisCard = deckListIn.pop() # Снимаем одну карту с верхней части
    return thisCard             # колоды и возвращаем


# Проходим по колоде, и эта функция возвращает перемещенную копию колоды
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # создаем копию стартовой колоды
    random.shuffle(deckListOut)
    return deckListOut

# Основной код
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be '
      'higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()
startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True: # несколько игр
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Staring card is:', currentCardRank + ' of ' +
          currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS): # играем в одну игру из этого
                                        # количества карт
        answer = input('Will the next card be higher or lower than'
                       'the ' +
                       currentCardRank + ' of ' +
                       currentCardSuit + '? (enter h or l): ')
        answer = answer.casefold() # переводим в нижний регистр
        nextCardDict = getCard(gameDeckList)
        nextCardRang = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is', nextCardRang + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print('You got it right, it was lower')
                score = score + 20
            else:
                print('Sorry, it was not lower')
                score = score - 15
            print('Your score is:', score)
            print()
            currentCardRank = nextCardRang
            currentCardValue = nextCardValue # не нужна текущая масть

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('Ok bye')
