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

def draw():
    hand_count = 2
    for num in range(hand_count):
        card = deck.popleft()
        player_hand.append(card)
    return player_hand

def showHand():
    print(f'Draw pile: {len(deck)}')
    print(f'Discard pile: {len(discard)}')

def showPiles():
    print(f'Draw pile: {len(deck)}')
    print(f'Discard pile: {len(discard)}')

deck = buildDeck()

while True:
    draw = input('Draw? ')
    if draw == 'y':
        draw()
        showHand()
    elif draw == 'piles':
        showPiles()
    else:
        quit()