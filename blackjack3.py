# make validation classes of what things are public  to both player and dealer

import random
import time
import itertools

vals = [2, 3, 4, 5, 6, 7, 8, 9, "10", "J", "Q", "K", "A"]
suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
deck = list(itertools.product(vals, suits))
playerTotal = 0

# # intro
# print("Welcome to Blackjack!")
# start = input("Would you like to begin? [y/n] ")

# if start != "y":
#     quit()

# dealing
print("\nDealer shuffling...")
time.sleep(.5)
print("Cutting the deck...")
time.sleep(.5)
print("And dealing your cards...")
time.sleep(.5)

# deal/display your intial hand
def dealPlayerHand(total): 
    playerDeal1 = random.choice(deck)
    deck.remove(playerDeal1)
    playerDeal2 = random.choice(deck)
    deck.remove(playerDeal2)

    # check for natural blackjack
    if type(playerDeal1[0]) != int and type(playerDeal2[0]) != int:
        if playerDeal1[0] == "A" and playerDeal2[0] == "A":
            total = 2
            print(f"\nYour hand: {playerDeal1}, {playerDeal2}")
            print(f"Your current total: {total}")
            return total

        # check for double aces
        elif playerDeal1[0] == "A" or playerDeal2[0] == "A":
            total = 21
            print(f"\nYour hand: {playerDeal1}, {playerDeal2}")
            print(f"Your current total: {total}")
            print(f"\n{total}, Blackjack!")
            return total

        # check if BOTH cards are 10 or face cards
        else:
            total = 20
            print(f"\nYour hand: {playerDeal1}, {playerDeal2}")
            print(f"Your current total: {total}")
            return total
        
    # check if first card is 10 or face card
    elif type(playerDeal1[0]) != int and type(playerDeal2[0]) == int:
        total = playerDeal2[0] + 10
        print(f"\nYour hand: {playerDeal1}, {playerDeal2}")
        print(f"Your current total: {total}")
        return total
    
    # check if second card is 10 or face card
    elif type(playerDeal2[0]) != int and type(playerDeal1[0]) == int:
        total = playerDeal1[0] + 10
        print(f"\nYour hand: {playerDeal1}, {playerDeal2}")
        print(f"Your current total: {total}")
        return total

    # total normal int numbered cards
    else:
        total = int(playerDeal1[0]) + int(playerDeal2[0])
        print(f"\nYour hand: {playerDeal1}, {playerDeal2}")
        print(f"Your current total: {total}")
        return total

# draw/display dealer's hand
def dealHouseHand():
    houseDeal1 = random.choice(deck)
    deck.remove(houseDeal1)
    houseDeal2 = random.choice(deck)
    deck.remove(houseDeal2)
    print(f"\nDealer's hand: {houseDeal1}, ('???')")
    print(f"Dealer's current total: {houseDeal1}\n")

dealPlayerHand(playerTotal)
dealHouseHand()

# # player chooses to hit
# def playerHit(total):
#     playerHit = random.choice(deck)
#     if playerHit[0] != int and playerHit[0] != "A":
#         total = total + 10
#         print(f"You were dealt a: {playerHit}")
#         print(f"Your new total is {total}")
#     # gauge whether an hit ace is 1 or 11
#     elif playerHit[0] == "A":
#         if total + 11 > 21:
#             playerHit = 1
#             total  = total + playerHit
#             print(f"You were dealt a: {playerHit}")
#             print(f"Your new total is {total}")
#         else:
#             playerHit = 11
#             if total + playerHit[0] == 21:
#                 print("21, Blackjack!")
#             elif total + playerHit[0] > 21:
#                 print(f"Your total is {total}. You busted!")
#             else:
#                 total = total + playerHit[0]
#                 print(f"You were dealt a: {playerHit}")
#                 print(f"Your new total is {total}")


# # all players stand, house reveals
# def stand(firstCard, secondCard):
#     print(f"Dealer's hand: {firstCard}, {secondCard}")

# hitStand = input("Do you want to hit or stand? [h/s] ")

# if hitStand == "h":
#     playerHit(playerTotal)
# elif hitStand == "s":
#     stand()
# else:
#     hitStand = input("Do you want to hit or stand? [h/s] ")