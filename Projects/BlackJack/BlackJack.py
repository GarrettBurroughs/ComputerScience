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

wins = 0
losses = 0
def blackJack():
    deck = []  # creating the deck
    hand = []  # create the hand
    oppHand = []  # create the opponents hand

    # Adding cards to the deck
    for i in range(2, 15):
        deck.append(Cards.card(Suit.SPADES, i))
    for i in range(2, 15):
        deck.append(Cards.card(Suit.CLUBS, i))
    for i in range(2, 15):
        deck.append(Cards.card(Suit.HEARTS, i))
    for i in range(2, 15):
        deck.append(Cards.card(Suit.DIAMONDS, i))

    random.shuffle(deck)  # Randomly shuffle the deck

    # GamePlay

    print("----------------------------------")
    print("Welcome to BlackJack version 1.0.0")
    input("press ENTER to start")
    playing = True
    while playing:
        won = False
        hand = []
        oppHand = []
        # give the player the top two cards of the deck
        if len(deck) > 4:
            hand.append(deck[len(deck) - 1])
            deck.__delitem__(len(deck) - 1)
            hand.append(deck[len(deck) - 1])
            deck.__delitem__(len(deck) - 1)

            oppHand.append(deck[len(deck) - 1])
            deck.__delitem__(len(deck) - 1)
            oppHand.append(deck[len(deck) - 1])
            deck.__delitem__(len(deck) - 1)
        else:
            print("Re-Shuffling Deck")
            deck.clear()
            for i in range(2, 15):
                deck.append(Cards.card(Suit.SPADES, i))
            for i in range(2, 15):
                deck.append(Cards.card(Suit.CLUBS, i))
            for i in range(2, 15):
                deck.append(Cards.card(Suit.HEARTS, i))
            for i in range(2, 15):
                deck.append(Cards.card(Suit.DIAMONDS, i))

            random.shuffle(deck)  # Randomly shuffle the deck

            hand.append(deck[len(deck) - 1])
            deck.__delitem__(len(deck) - 1)
            hand.append(deck[len(deck) - 1])
            deck.__delitem__(len(deck) - 1)

            oppHand.append(deck[len(deck) - 1])
            deck.__delitem__(len(deck) - 1)
            oppHand.append(deck[len(deck) - 1])
            deck.__delitem__(len(deck) - 1)

        print()
        print("You have a", hand[0], "and a", hand[1])
        if hand[0].getId() == 14:
            print("ACE")
            hand[0].prompt()
        if hand[1].getId() == 14:
            print("ACE")
            hand[0].prompt()
        print("You can see that the dealer has a", oppHand[0])
        if hand[0].getValue() + hand[1].getValue() == 21:
            print("BLACKJACK, you win")
        else:
            sum = 0
            for card in hand:
                sum += card.getValue()
            while sum < 21:
                print("Your total is", sum)
                hit = input("Do you want to hit (Y/N) ")
                if hit.upper() == "Y":
                    try:
                        hand.append(deck[len(deck) - 1])
                        deck.__delitem__(len(deck) - 1)
                        print("You got a", hand[len(hand) - 1])
                        if hand[len(hand) - 1].getId() == 14:
                            hand[len(hand) - 1].prompt()
                    except:
                        print("ERROR")
                        for i in range(2, 15):
                            deck.append(Cards.card(Suit.SPADES, i))
                        for i in range(2, 15):
                            deck.append(Cards.card(Suit.CLUBS, i))
                        for i in range(2, 15):
                            deck.append(Cards.card(Suit.HEARTS, i))
                        for i in range(2, 15):
                            deck.append(Cards.card(Suit.DIAMONDS, i))

                        random.shuffle(deck)  # Randomly shuffle the deck
                elif hit.upper() == "N":
                    break
                else:
                    print("Please enter a 'Y' or a 'N' ")
                sum = 0
                for card in hand:
                    sum += card.getValue()
            if sum > 21:
                print("BUSTED")
                continue
            oppSum = 0
            for card in oppHand:
                oppSum += card.getValue()
            while oppSum < 21:
                if oppSum <= 16:
                    oppHand.append(deck[len(deck) - 1])
                    deck.__delitem__(len(deck) - 1)
                else:
                    break
                oppSum = 0
                for card in oppHand:
                    oppSum += card.getValue()
            if oppSum > 21:
                print("The dealer has busted with a", oppSum, "YOU WIN!")
                continue
            if (sum > oppSum):
                print("The dealer got {}, but you got {}. YOU WIN!".format(oppSum, sum))
            elif sum < oppSum:
                print("You got {}, but the dealer got {}. YOU LOSE!".format(sum, oppSum))
            cont = input("Continue Playing? (Y/N) ")
            if cont.upper() == "N":
                print("Thank you for playing!")
                break

blackJack()
