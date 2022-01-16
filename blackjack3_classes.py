# remove hit card from deck
# hit() still not catching normal face cards, strs hitting else

import random
import time
import itertools

values = [2, 3, 4, 5, 6, 7, 8, 9, "10", "J", "Q", "K", "A"]
suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
deck = list(itertools.product(values, suits))
playerTotal = 0
playerDeal1 = 0
playerDeal2 = 0

# # intro
# print("Welcome to Blackjack!")
# start = input("Would you like to begin? [y/n] ")

# if start != "y":
#     quit()

# dealing anticipation
print("\n...Dealer shuffling...")
time.sleep(.5)
print("...Cutting the deck...")
time.sleep(.5)
print("...And dealing your cards...")
time.sleep(.5)

# deal/display your intial hand
def dealPlayer(): 
    yourCards = []
    playerDeal1 = random.choice(deck)
    yourCards.append(playerDeal1)
    deck.remove(playerDeal1)
    playerDeal2 = random.choice(deck)
    yourCards.append(playerDeal2)
    deck.remove(playerDeal2)
    return yourCards

# draw/display dealer's hand
def dealHouse():
    houseCards = []
    houseDeal1 = random.choice(deck)
    houseCards.append(houseDeal1)
    deck.remove(houseDeal1)
    houseDeal2 = random.choice(deck)
    houseCards.append(houseDeal2)
    deck.remove(houseDeal2)
    return houseCards

# check initial hand results
class Check:

    def __init__(self, card1, card2, total):
        self.card1 = card1
        self.card2 = card2
        self.total = total

    def checkHand(self, card1, card2):
        # check for natural blackjack
        if type(self.card1) != int and type(self.card2) != int:
            if self.card1 == "A" and self.card2 == "A":
                self.total = 2
                return self.total
            # check for double aces
            elif self.card1 == "A" or self.card2 == "A":
                self.total = 21
                return self.total
            # check if BOTH cards are 10 or face cards
            else:
                self.total = 20
                return self.total
            
        # check if first card is 10 or face card
        elif type(self.card1) != int and type(self.card2) == int:
            if self.card1 == "A":
                self.total = self.card2 + 11
                return self.total
            else:
                self.total = self.card2 + 10
                return self.total
        
        # check if second card is 10 or face card
        elif type(self.card2) != int and type(self.card1) == int:
            if self.card2[0] == "A":
                total = self.card1 + 11
                return self.total
            else:
                total = self.card1 + 10
                return self.total

        # total normal int numbered cards
        else:
            total = int(card1) + int(card2)
            return total

# player hits
def hit(cards, total):
    playerHit = random.choice(deck)
    print(f"Your were dealt a: {playerHit}")
    print("before valid " + type(playerHit[0]))
    cards.append(playerHit)
    if playerHit[0] == "A": # know it's an ace
        if total + 11 > 21:
            total = total + 1
            cards.append(total)
            print("if A equal 1 " + type(playerHit[0]))
            return cards
        else:
            total = total + 11
            cards.append(total)
            print("if A equals 11 " + type(playerHit[0]))
            return cards
    elif playerHit[0] != int and playerHit[0] != "A":
        print("if 10 or face card " + type(playerHit[0]))
        total = total + 10
        cards.append(total)
        return cards
    else:
        print(f"if int " + type(playerHit[0]))
        total = total + playerHit[0]
        cards.append(total)
        return cards

# check results of hit
def results():
    if playerHandTotal == 21:
        print(f"\nYour hand: {playerHand}")
        print(f"{playerHandTotal}, BLACKJACK!")
        quit()
    else:
        print(f"\nYour hand: {playerHand}")
        print(f"Your total: {playerHandTotal}")

# display your current hand
playerHand = dealPlayer()
playerHandTotal = checkHand(playerHand[0][0], playerHand[1][0])

# display current house hand
houseHand = dealHouse()
houseHandTotal = checkHand(houseHand[0][0], houseHand[1][0])
print(f"\nDealer's hand: [{houseHand[0]}, ('???')]")

# check if natural blackjack
if playerHandTotal == 21:
    print(f"{playerHand}")
    print(f"{playerHandTotal}, BLACKJACK!\n")
    quit()

results()

# ask to hit or stand
while playerHandTotal < 21:
    hitStand = input("\n>>> Do you want to hit or stand? [h/s] ")
    if hitStand == "h":
        print("\n### Dealing your hit...")
        time.sleep(1)
        hasHit = hit(playerHand, playerHandTotal)
        hasHit.pop()
        print(hasHit)
        results()
    elif hitStand == "s":
        print("You stand.")
        quit()
    else:
        hitStand = input(">>> Do you want to hit or stand? [h/s] ")
        print("\n### Dealing your hit...")
        time.sleep(1)

