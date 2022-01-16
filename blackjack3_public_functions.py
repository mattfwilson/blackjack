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
    playerDeal1 = random.choice(deck)
    deck.remove(playerDeal1)
    playerDeal2 = random.choice(deck)
    deck.remove(playerDeal2)

    return playerDeal1, playerDeal2

def checkHand(card1, card2):
    # check for natural blackjack

    if type(card1[0]) != int and type(card2[0]) != int:
        if card1[0] == "A" and card2[0] == "A":
            total = 2
            return total

        # check for double aces
        elif card1[0] == "A" or card2[0] == "A":
            total = 21
            return total

        # check if BOTH cards are 10 or face cards
        else:
            total = 20
            return total
        
    # check if first card is 10 or face card
    elif type(card1[0]) != int and type(card2[0]) == int:
        if card1[0] == "A":
            total = card2[0] + 11
            return total
        else:
            total = card2[0] + 10
            return total
    
    # check if second card is 10 or face card
    elif type(card2[0]) != int and type(card1[0]) == int:
        if card2[0] == "A":
            total = card1[0] + 11
            return total
        else:
            total = card1[0] + 10
            return total

    # total normal int numbered cards
    else:
        total = int(card1[0]) + int(card2[0])
        return total

# draw/display dealer's hand
def dealHouseHand():
    houseDeal1 = random.choice(deck)
    deck.remove(houseDeal1)
    houseDeal2 = random.choice(deck)
    deck.remove(houseDeal2)
    return houseDeal1, houseDeal2

# display your current hand
playerHand = dealPlayer()
playerCard1 = playerHand[0]
playerCard2 = playerHand[1]
playerHandTotal = checkHand(playerCard1, playerCard2)
print(playerHand)

# check for natural blackjack
if playerHandTotal == 21:
    print(f"\nYour hand: {playerHand}")
    print(f"BLACKJACK! Your total: {playerHandTotal}")
else:
    print(f"\nYour hand: {playerHand}")
    print(f"Your total: {playerHandTotal}")

# display current house hand
houseHand = dealHouseHand()
houseCard1 = houseHand[0]
houseCard2 = houseHand[1]
houseHandTotal = checkHand(houseCard1, houseCard2)
print(f"\nDealer's hand: ({playerCard1}, ('???'))\n")

# # player chooses to hit
# def hit(total):
#     playerHit = random.choice(deck)
#     print(playerHit)
#     if playerHit[0] != int and playerHit[0] == "A": # know it's an ace
#         if total + 11 > 21:
#             total = total + 1
#             return total, playerHit
#         else:
#             total = total + 11
#             return total, playerHit
#     elif playerHit[0] != int and playerHit[0] != "A":
#         total = total + 10
#         return total, playerHit
#     else:
#         total = total + playerHit[0]
#         return total, playerHit

# hitStand = input("Do you want to hit or stand? [h/s] ")
# if hitStand == "h":
#     hitting = hit(playerHandTotal)
# elif hitStand == "s":
#     print("You stand.")
# else:
#     hitStand = input("Do you want to hit or stand? [h/s] ")

# print(hitting)

# if playerHandTotal == 21:
#     print(f"\nYour hand: {playerCard1}, {playerCard2}")
#     print(f"BLACKJACK! Your total: {playerHandTotal}")
# else:
#     print(f"\nYour hand: {playerCard1}, {playerCard2}, {playerHit}")
#     print(f"Your new total: {playerHandTotal}")

