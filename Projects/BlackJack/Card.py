# -----------------------------------------------------
# Card
#
# This file contains all the information to create a
# card object for the BlackJack game
#
# Made by Garrett Burroughs
# 3/14/17
# -----------------------------------------------------
from Projects.BlackJack.Suit import Suit

class card:
    cardSuit = Suit.NULL
    cardId = 0
    cardValue = 0
    isEleven = False

    def __init__(self, suit, Id):
        self.cardSuit = suit
        self.cardId = Id
        if self.cardId <= 10:
            self.cardValue = self.cardId
        elif self.cardId < 14:
            self.cardValue = 10
        elif self.isEleven:
            self.cardValue = 11
        else:
            self.cardValue = 1

    def getSuit(self):
        return self.cardSuit
    def setSuit(self, suit):
        self.cardSuit = suit
    def getId(self):
        return self.cardId
    def setId(self, Id):
        self.cardId = Id
    def getValue(self):
        return self.cardValue
    def updateValue(self):
        if self.cardId <= 10:
            self.cardValue = self.cardId
        elif self.cardId < 14:
            self.cardValue = 10
        elif self.isEleven:
            self.cardValue = 11
        else:
            self.cardValue = 1
    def setAceValue(self, isEleven):
        self.isEleven = isEleven
    def __str__(self):
        if self.cardSuit == Suit.SPADES:
            suit = "Spades"
        elif self.cardSuit == Suit.CLUBS:
            suit = "Clubs"
        elif self.cardSuit == Suit.HEARTS:
            suit = "Hearts"
        elif self.cardSuit == Suit.DIAMONDS:
            suit = "Diamonds"
        if self.cardId <= 10:
            name = str(self.cardId)
        elif self.cardId == 11:
            name = "Jack"
        elif self.cardId == 12:
            name = "Queen"
        elif self.cardId == 13:
            name = "King"
        elif self.cardId == 14:
            name = "Ace"
        return "{} of {}".format(name, suit)