# how would I calculate the total of the single first card for dealer before they hit (and show their second)
# says I beat the house even though my total is lower than house
# aces on house hit are being calculated as 11
# Test after conflict merge

import time
import random
import itertools

VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
SUITS = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
DECK = list(itertools.product(VALUES, SUITS))
PLAYER_TOTAL = 0
HOUSE_TOTAL = 0
PLAYER_STAND = 0
HOUSE_STAND = 0

ACE = 'A'
ACE_HIGH = 11
ACE_LOW = 1

FACES = {
    'J': 10,
    'Q': 10,
    'K': 10,
}

def dealPlayer(): 
    yourCards = []
    playerDeal1 = random.choice(DECK)
    yourCards.append(playerDeal1)
    DECK.remove(playerDeal1)
    playerDeal2 = random.choice(DECK)
    yourCards.append(playerDeal2)
    DECK.remove(playerDeal2)
    return yourCards

def dealHouse():
    houseCards = []
    houseDeal1 = random.choice(DECK)
    houseCards.append(houseDeal1)
    DECK.remove(houseDeal1)
    houseDeal2 = random.choice(DECK)
    houseCards.append(houseDeal2)
    DECK.remove(houseDeal2)
    return houseCards

def summary(hand, total, houseHand, houseTotal):
    print(f'\nYour hand: {hand}')
    print(f'Your total: {total}\n')
    print(f'House hand:: {houseHand[0]}, (???)')
    print(f'House total: {houseHand[0][0]}')
    print('------------------------------------------------------')

def summaryStand(hand, total, houseHand, houseTotal):
    print(f'\nYour hand: {hand}')
    print(f'Your total: {total}\n')
    print(f'House hand:: {houseHand}')
    print(f'House total: {houseTotal}')
    print('------------------------------------------------------')

def checkHand(hand, total):
    for card in hand:
        total += checkCardValue(card[0], total)
    return total

def checkCardValue(card, total):
    if card == ACE:
        return checkAceValue(total)
    return FACES.get(card, card)

def checkAceValue(total):
    if total + ACE_HIGH > 21:
        return ACE_LOW
    else:
        return ACE_HIGH

def hit(hand, total):
    playerHit = random.choice(DECK)
    print(f'\n>>> Your were dealt a: {playerHit}')
    hand.append(playerHit)
    return total

def houseHit(player_hand, player_total, house_hand, house_total):
    print('DEBUG: start of houseHit func')
    while house_total < 16:
        if house_total == 21:
            print('>>> House got BLACKJACK! You lost.')
            print('DEBUG: house wins')
            summaryStand(player_hand, player_total, house_hand, house_total)
            quit()
        elif house_total >= 16 and house_total < 21:
            print('DEBUG: in between 16-21')
            print(f'House stands at {house_total}')
            print('DEBUG: house > 16 but < 21 so stands')
            house_total = 0
            house_total = checkHand(house_hand, house_total)
            summaryStand(player_hand, player_total, house_hand, house_total)
            if PLAYER_TOTAL > HOUSE_TOTAL:
                print('You beat the house! You win!')
            elif PLAYER_TOTAL < HOUSE_TOTAL:
                print('The house beat you! Game over.')
            elif PLAYER_TOTAL == HOUSE_TOTAL:
                print('It was a tie!')
            quit()
        elif house_total < 16:
            print('DEBUG: house still hitting to 16')
            print('\n>>> Dealing the house\'s hit...')
            time.sleep(1)
            houseHitting = random.choice(DECK)
            house_hand.append(houseHitting)
            house_total = 0
            house_total = checkHand(house_hand, house_total)
            print(house_total)
            summaryStand(player_hand, player_total, house_hand, house_total)
    if house_total > 21:
        print('DEBUG: house > 21 and loses')
        print('>>> House BUSTED. You win!\n')
        quit()

PLAYER_DEAL = dealPlayer()
HOUSE_DEAL = dealHouse()
PLAYER_TOTAL = checkHand(PLAYER_DEAL, PLAYER_TOTAL)


while PLAYER_STAND == 0:
    summary(PLAYER_DEAL, PLAYER_TOTAL, HOUSE_DEAL, HOUSE_TOTAL)
    while PLAYER_TOTAL <= 21:
        if PLAYER_TOTAL == 21:
            print('\n>>> You got BLACKJACK! You win!')
            summaryStand(PLAYER_DEAL, PLAYER_TOTAL, HOUSE_DEAL, HOUSE_TOTAL)
            quit()
    
        hitStand = input('\n>>> Do you want to hit or stand? [h/s] ')
        if hitStand == 'h' or hitStand == 'hit':
            print('\n>>> Dealing your hit...')
            time.sleep(1)
            has_hit = hit(PLAYER_DEAL, PLAYER_TOTAL) 
            PLAYER_TOTAL = 0
            PLAYER_TOTAL = checkHand(PLAYER_DEAL, PLAYER_TOTAL)
            summary(PLAYER_DEAL, PLAYER_TOTAL, HOUSE_DEAL, HOUSE_TOTAL)
        elif hitStand == 's' or hitStand == 'stand':
            print('DEBUG: in if for stand')
            print(f'\n>>> You stand. Houses turn...')
            time.sleep(.7)
            STAND = 1
            HOUSE_TOTAL = checkHand(HOUSE_DEAL, HOUSE_TOTAL)
            summaryStand(PLAYER_DEAL, PLAYER_TOTAL, HOUSE_DEAL, HOUSE_TOTAL)
            houseHit(PLAYER_DEAL, PLAYER_TOTAL, HOUSE_DEAL, HOUSE_TOTAL)
        else:
            hitStand = input('>>> Do you want to hit or stand? [h/s] ')
            print("\nDealing your hit...")
            time.sleep(.7)

    print(f'\n>>> You BUSTED! Game')
    summary(PLAYER_DEAL, PLAYER_TOTAL, HOUSE_DEAL, HOUSE_TOTAL)
    print('\nDEBUG: end of > 21 while')
    quit()

print('DEBUG: end of STAND while / program')