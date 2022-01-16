import random 

cards = [
    "A Spades",
    "2 Spades",
    "3 Spades",
    "4 Spades",
    "5 Spades",
    "6 Spades",
    "7 Spades",
    "8 Spades",
    "9 Spades",
    "10 Spades",
    "J Spades",
    "Q Spades",
    "K Spades",
    "A Diamonds",
    "2 Diamonds",
    "3 Diamonds",
    "4 Diamonds",
    "5 Diamonds",
    "6 Diamonds",
    "7 Diamonds",
    "8 Diamonds",
    "9 Diamonds",
    "10 Diamonds",
    "J Diamonds",
    "Q Diamonds",
    "K Diamonds",
    "A Clubs",
    "2 Clubs",
    "3 Clubs",
    "4 Clubs",
    "5 Clubs",
    "6 Clubs",
    "7 Clubs",
    "8 Clubs",
    "9 Clubs",
    "10 Clubs",
    "J Clubs",
    "Q Clubs",
    "K Clubs",
    "A Hearts",
    "2 Hearts",
    "3 Hearts",
    "4 Hearts",
    "5 Hearts",
    "6 Hearts",
    "7 Hearts",
    "8 Hearts",
    "9 Hearts",
    "10 Hearts",
    "J Hearts",
    "Q Hearts",
    "K Hearts",
]

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return self.suit

suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
    
deck = [Card(value, suit) for value in range(1, 14) for suit in suits]

print(deck)



def dealHand():
    # Deal your hand
    yourHand = []
    yourDeal1 = random.choice(cards)
    yourHand.append(yourDeal1)
    yourDeal2 = random.choice(cards)
    yourHand.append(yourDeal2)
    updatedDeck = [dealt for dealt in cards if dealt not in yourHand]
    print(f"Your hand: {yourDeal1}, {yourDeal2}")

    # Deal dealer's hand
    houseHand = []
    houseDeal1 = random.choice(updatedDeck)
    houseHand.append(houseDeal1)
    updatedDeck = [dealt for dealt in updatedDeck if dealt not in houseHand]
    print(f"Dealer's hand: {houseDeal1}, ???")
    print(updatedDeck)

dealHand()
