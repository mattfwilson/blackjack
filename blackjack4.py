from collections import deque
import itertools
import random

count = 0
deck = deque()
discard = deque()
player_hand = []

def buildDeck():
    suit = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    cards = list(itertools.product(value, suit))
    for i in cards:
        deck.append(i)
    random.shuffle(deck)
    return deck

def drawHand():
    hand_count = 2
    for num in range(hand_count):
        card = deck.popleft()
        player_hand.append(card)
    return player_hand

def discardHand(cards):
    for card in cards:
        discard.append(card)
        player_hand.remove(card)
    return discard

def showHand():
    return player_hand[0], player_hand[1]

def showPiles():
    print(f'Draw pile: {len(deck)}')
    print(f'Discard pile: {len(discard)}')

deck = buildDeck()

while True:
    draw = input('Draw? ')
    if draw == 'yes':
        discardHand(player_hand)
        drawHand()
        print(showHand())
    elif draw == 'piles':
        showPiles()
    elif draw == 'discard':
        print(discard)
    elif draw == 'deck':
        print(deck)
    else:
        quit()