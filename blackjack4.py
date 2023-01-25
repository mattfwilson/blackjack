import itertools
import random

count = 0

def buildDeck():
    suit = ["Spades", "Hearts", "Clubs", "Diamonds"]
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    cards = list(itertools.product(value, suit))
    deck = []
    for i in cards:
        deck.append(i)
    random.shuffle(deck)
    return deck

deck = buildDeck()


for card in deck:
    print(card)
    count += 1

print(f'Deck count: {count}')