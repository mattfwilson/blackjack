# add initial deal and hit cards to a list/tuple and then display list/tuple as a ongoing summary

import random
import time
import itertools

vals = [2, 3, 4, 5, 6, 7, 8, 9, "10", "J", "Q", "K", "A"]
suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
deck = list(itertools.product(vals, suits))
playerTotal = 0
playerDeal1 = 0
playerDeal2 = 0

print(deck)
# # intro
# print("Welcome to Blackjack!")
# start = input("Would you like to begin? [y/n] ")

# if start != "y":
#     quit()

# dealing anticipation
print("\nDealer shuffling...")
time.sleep(.5)
print("Cutting the deck...")
time.sleep(.5)
print("And dealing your cards...")
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
def checkHand(card1, card2):
    # check for natural blackjack
    if type(card1) != int and type(card2) != int:
        if card1 == "A" and card2 == "A":
            total = 2
            return total
        # check for double aces
        elif card1 == "A" or card2 == "A":
            total = 21
            return total
        # check if BOTH cards are 10 or face cards
        else:
            total = 20
            return total
        
    # check if first card is 10 or face card
    elif type(card1) != int and type(card2) == int:
        if card1 == "A":
            total = card2 + 11
            return total
        else:
            total = card2 + 10
            return total
    
    # check if second card is 10 or face card
    elif type(card2) != int and type(card1) == int:
        if card2[0] == "A":
            total = card1 + 11
            return total
        else:
            total = card1 + 10
            return total

    # total normal int numbered cards
    else:
        total = int(card1) + int(card2)
        return total

# player hits
def hit(cards, total):
    playerHit = random.choice(deck)
    cards.append(playerHit)
    print(type(playerHit[0]))
    print(cards)
    print(f"Total before validation: {total}")
    if playerHit[0] == "A": # know it's an ace
        if total + 11 > 21:
            total = total + 1
            cards.append(total)
            print(f"Total after validation: {total}")
            return cards
        else:
            total = total + 11
            cards.append(total)
            print(f"Total after validation: {total}")
            return cards
    elif playerHit[0] == str:
        total = total + 10
        cards.append(total)
        print(f"Total after validation: {total}")
        return cards
    else:
        total = total + int(playerHit[0])
        cards.append(total)
        print(f"Total after validation: {total}")
        return cards

# check results of hit
def results():
    if playerHandTotal == 21:
        print(f"\nYour new hand: {playerHand}")
        print(f"BLACKJACK! Your new total: {playerHandTotal}")
        quit()
    else:
        print(f"\nYour new hand: {playerHand}")
        print(f"Your new total: {playerHandTotal}")

# display your current hand
playerHand = dealPlayer()
playerHandTotal = checkHand(playerHand[0][0], playerHand[1][0])
print(f"\nYour hand: {playerHand}")
print(f"Your total: {playerHandTotal}")

# display current house hand
houseHand = dealHouse()
houseHandTotal = checkHand(houseHand[0][0], houseHand[1][0])
print(f"\nDealer's hand: [{houseHand[0]}, ('???')]\n")

# ask to hit or stand
while playerHandTotal < 21:
    hitStand = input("Do you want to hit or stand? [h/s]")
    print("\nDealing your hit...")
    time.sleep(1)

    if hitStand == "h":
        hasHit = hit(playerHand, playerHandTotal)
    elif hitStand == "s":
        print("You stand.")
        quit()
    else:
        hitStand = input("Do you want to hit or stand? [h/s]")
        print("\nDealing your hit...")
        time.sleep(1)

