# JG
# November 17, 2024
# The program simulates a hand of Poker

import Deck

def main():

    # Create a deck weith 52 cards
    deck = Deck.Deck(52)

    # Create an empty hand for the player
    hand = []

    # Deal 5 cards from the deck into the hand
    hand.append(deck.deal())

    hand.append(deck.deal())

    hand.append(deck.deal())

    hand.append(deck.deal())

    hand.append(deck.deal())

    # Print the hand
    print(hand)

    # Ask the user which cards to replace
    userChoice = input('Enter the card numbers you would like to replace')

    # For each card that the user wants to replace
    for index in userChoice.split():

        # Deal a new card to replace the card in the hand
        hand[int(index) - 1] = deck.deal()

    # Print the hand
    print(hand)


# Call the main function
main()