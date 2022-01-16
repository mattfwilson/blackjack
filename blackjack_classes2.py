import time
import random
import itertools

VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
SUITS = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
DECK = list(itertools.product(VALUES, SUITS))
HAND_TOTAL = 0
HAS_HIT = 0

ACE = 'A'
ACE_HIGH = 11
ACE_LOW = 1

FACES = {
    'J': 10,
    'Q': 10,
    'K': 10,
}

# class Card:
#     def __init__(self, value, suit):
#         self.value = value
#         self.suit = suit

#     def __str__(self):
#         return f'{self.value} of {self.suit}'


# firstCard = Card(playerDeal[0][0], playerDeal[0][1])
# secondCard = Card(playerDeal[1][0], playerDeal[1][1])

def dealPlayer(): 
    yourCards = []
    playerDeal1 = random.choice(DECK)
    yourCards.append(playerDeal1)
    DECK.remove(playerDeal1)
    playerDeal2 = random.choice(DECK)
    yourCards.append(playerDeal2)
    DECK.remove(playerDeal2)
    return yourCards

def summary(hand, total):
    print(f'Your hand: {hand}')
    print(f'Your total: {total}')

def checkHand(hand, total):
    print(f"Total in checkHand {total}")
    for card in hand:
        total += checkCardValue(card[0], total)
    return total

# def checkHit(card, total):
#     print(f"Check hit card tota: {total}")
#     if card == ACE:
#         return checkAceValue(total)
#     return FACES.get(card, card)

def checkCardValue(card, total):
    print(f"Total in check for ace {total}")
    if card == ACE:
        return checkAceValue(total)
    return FACES.get(card, card)

def checkAceValue(total):
    print(f"Total in ace high/low {total}")
    if total + ACE_HIGH > 21:
        return ACE_LOW
    else:
        return ACE_HIGH

def hit(hand, total):
    print(f"Total in hit {total}")
    playerHit = random.choice(DECK)
    print(f"\nYour were dealt a: {playerHit}")
    checkCardValue(hand[0], total)
    hand.append(playerHit)
    return total

playerDeal = dealPlayer()
HAND_TOTAL = checkHand(playerDeal, HAND_TOTAL)

# ask to hit or stand
while HAND_TOTAL < 21:
    summary(playerDeal, HAND_TOTAL)
    hitStand = input("\n>>> Do you want to hit or stand? [h/s] ")
    if hitStand == "h":
        print("\n...Dealing your hit...")
        time.sleep(.7)
        HAND_TOTAL = 0
        HAS_HIT = hit(playerDeal, HAND_TOTAL) 
        checkHand(playerDeal, HAND_TOTAL)
    elif hitStand == "s":
        print("You stood bro!")
        quit()
    else:
        hitStand = input(">>> Do you want to hit or stand? [h/s] ")
        print("\n...Dealing your hit...")
        time.sleep(.7)

print(f'\nYou BUSTED bro!')
quit()