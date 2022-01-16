import random
import itertools

vals = [2, 3, 4, 5, 6, 7, 8, 9, "10", "J", "Q", "K", "A"]
suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
deck = list(itertools.product(vals, suits))
bet = ""


def dealHand(): 
    # Deal your hand
    playerTotal = ""
    playerDeal1 = random.choice(deck)
    deck.remove(playerDeal1)
    playerDeal2 = random.choice(deck)
    deck.remove(playerDeal2)

    if type(playerDeal1[0]) != int and playerDeal2[0] != int:
        playerTotal = 20
        if playerDeal1[0] == "A" and playerDeal2[0] == "A":
            playerTotal = 2
            print(f"Player total: {playerTotal}")
        elif playerDeal1[0] == "A" or playerDeal2[0] == "A":
            playerTotal = 21
            print(f"{playerTotal}, Blackjack!")
    print(f"Your hand: {playerDeal1}, {playerDeal2}")

    # Deal dealer's hand
    houseDeal1 = random.choice(deck)
    deck.remove(houseDeal1)
    houseDeal2 = random.choice(deck)
    deck.remove(houseDeal2)
    print(f"Dealer's hand: {houseDeal1}, ('??', '??') \n")

def hit():
    playerHit = ""
    playerHit = random.choice(deck) 

dealHand()

# instead of removing from deck, if dealer hand == your hand, draw again