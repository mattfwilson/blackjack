from collections import deque
import itertools
import random

count = 0
deck = deque()
discard = deque()

def buildDeck():
    suit = ["Spades", "Hearts", "Clubs", "Diamonds"]
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    cards = list(itertools.product(value, suit))
    for i in cards:
        deck.append(i)
    random.shuffle(deck)
    return deck

deck = buildDeck()

for card in deck:
    print(card)
    count += 1

while True:
    draw = input('Draw? ')
    if draw == 'y':
        card = deck.popleft()
        discard.append(card)
        print(f'You drew a {card}')
        print(f'Draw pile: {len(deck)}')
        print(f'Discard pile: {len(discard)}')
    
    else:
        print(f'Draw pile: {len(deck)}')
        print(f'Discard pile: {len(discard)}')
        quit()