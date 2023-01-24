import itertools
import random

def buildDeck():
    suit = ["Spades", "Hearts", "Clubs", "Diamonds"]
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    cards = list(itertools.product(value, suit))
    return cards

deck = buildDeck()
for i in deck:
    print(i)