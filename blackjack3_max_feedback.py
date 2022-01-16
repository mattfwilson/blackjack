# make check for natural blackjack a reusable function
# figure out why the check for blackjack isn't working
# use .pop to get and remove card from deck
# create function to deal with A funkiness
# try creating a class for the card draws


import random
import time
import itertools

values = [2, 3, 4, 5, 6, 7, 8, 9, "10", "J", "Q", "K", "A"]

# ace_high = 11
# ace_low = 1
# face = {"J": 10, "Q": 10, "K": 10}

suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
deck = list(itertools.product(values, suits)) * 6

playerTotal = 0
playerDeal1 = 0
playerDeal2 = 0

# intro
print("Welcome to Blackjack!")
start = input("Would you like to begin? [y/n] ")

if start != "y":
    quit()

# dealing anticipation
print("\n...Dealer shuffling...")
time.sleep(.7)
print("...Cutting the deck...")
time.sleep(.7)
print("...And dealing your cards...")
time.sleep(.7)

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
def hit(hand, total):
    playerHit = random.choice(deck)
    print(f"Your were dealt a: {playerHit}")
    hand.append(playerHit)
    if playerHit[0] == "A": # know it's an ace
        if total + 11 > 21:
            total = total + 1
            hand.append(total)
            #print("DEBUG check if A is worth 1") # debug
            #print(type(playerHit[0])) # debug
            return hand
        else:
            total = total + 11
            hand.append(total)
            #print("DEBUG check if A is worth 11") # debug
            #print(type(playerHit[0])) # debug
            return hand
    elif type(playerHit[0]) == str and playerHit[0] != "A":
        #print("DEBUG check for 10 or face card") # debug
        #print(type(playerHit[0])) # debug
        total = total + 10
        hand.append(total)
        return hand
    else:
        #print("DEBUG check for in card") # debug
        #print(type(playerHit[0])) # debug
        total = total + playerHit[0]
        hand.append(total)
        return hand

# validate card results
def results(total):
    if total == 21:
        print(f"\nYour hand: {playerHand}")
        print(f"{total}, BLACKJACK!")
        quit()
    elif total > 21:
        print(f"Your hand: {playerHand}")
        print(f"Your total: {total}, You BUSTED!\n")
        quit()
    else:
        print(f"\nYour hand: {playerHand}")
        print(f"Your total: {total}")

# display your current hand
playerHand = dealPlayer()
playerHandTotal = checkHand(playerHand[0][0], playerHand[1][0])

# display current house hand
houseHand = dealHouse()
houseHandTotal = checkHand(houseHand[0][0], houseHand[1][0])
print(f"\nDealer's hand: [{houseHand[0]}, ('???')]")

# # check if natural blackjack
# if playerHandTotal == 21:
#     print(f"Your hand: {playerHand}")
#     print(f"Your total: {playerHandTotal}, BLACKJACK!\n")
#     quit()

# ask to hit or stand
while playerHandTotal < 21:
    results(playerHandTotal)
    hitStand = input("\n>>> Do you want to hit or stand? [h/s] ")
    if hitStand == "h":
        print("\n...Dealing your hit...")
        time.sleep(.7)
        hasHit = hit(playerHand, playerHandTotal)
        playerHandTotal = hasHit[-1]
        #print(f"DEBUG player hand: {playerHand}")
        #print(f"DEBUG while loop player total: {playerHandTotal}")
        hasHit.pop()
        #print(hasHit[-1])
    elif hitStand == "s":
        print("You stand.")
        quit()
    else:
        hitStand = input(">>> Do you want to hit or stand? [h/s] ")
        print("\n...Dealing your hit...")
        time.sleep(.7)

print(f"\nYour hand: {playerHand}")
print(f"Your total: {playerHandTotal}, You BUSTED!\n")
quit()
