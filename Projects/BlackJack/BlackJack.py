# -----------------------------------------------------
# BlackJack
#
# A text based blackjack game in which the user can play
# against the computer with the traditional blackjack
# rules.
#
#
# Made by Garrett Burroughs
# 3/14/17
# -----------------------------------------------------
import Projects.BlackJack.Card as Cards
from Projects.BlackJack.Suit import Suit
import random
import math


def blackJack():
    deck = [] # creating the deck

    # ---adding all of the cards to the deck--- #
    for i in range(1, 15):
        deck.append(Cards.card(Suit.SPADES, i))
    for i in range(1, 15):
        deck.append(Cards.card(Suit.CLUBS, i))
    for i in range(1, 15):
        deck.append(Cards.card(Suit.HEARTS, i))
    for i in range(1, 15):
        deck.append(Cards.card(Suit.DIAMONDS, i))

    random.shuffle(deck) # Randomly shuffle the deck
    
blackJack()