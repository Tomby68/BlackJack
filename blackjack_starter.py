# Global constant for the winning number of cards
MAX = 21
import random

# main function
def main():
    # Local variables
    hand1 = 0
    hand2 = 0
    deck = create_deck()


    while hand1 < 21 and hand2 < 21:

        card, value = deck.popitem()
        print('Player 1 was dealt ' + card)
       
        card2, value2 = deck.popitem()
        print('Player 2 was dealt ' + card2 + '\n')

        hand1 = update_hand_value(hand1, value, card)
        hand2 = update_hand_value(hand2, value2, card2)





    #Print 'There is no winner' or
    #'Player 1 wins' or
    #'Player 2 wins'

    if hand1 > 21 and hand2 > 21:
        print('There is no winner')

    else:
        print('Player 1 wins') if hand1 <= 21 else print('Player 2 wins')


# The create_deck function creates a deck of cards and
# returns the deck.
def create_deck():
    # Set up local variables
    suits = ['Spades','Hearts','Clubs','Diamonds']
    special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}

    # Create list of all the card values
    numbers = ['Ace', 'King', 'Queen', 'Jack']
    for i in range(2,11):
        numbers.append(str(i))

    
    # Initialize deck
    deck = {}
    for suit in suits:



        for num in numbers:

            randSuit = suits[random.randint(0, 3)]
            randCard = random.randint(2, 14)

            if randCard >= 11 and randCard <= 14:
                randCard = numbers[randCard - 11]

            if str(randCard).isnumeric():
                deck[str(randCard) + ' of ' + randSuit] = int(randCard)
            else:
                deck[randCard + ' of ' + randSuit] = special_values[randCard]

    return deck

def update_hand_value(hand, value, card):
    if 'Ace' in card:
        if (hand + 11) > 21:
            hand += 1
        else:
            hand += 11
    else:
        hand += value

    return hand

# Call the main function
main()
