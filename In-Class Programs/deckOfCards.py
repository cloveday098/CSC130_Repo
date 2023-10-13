deck = [x for x in range(0,52)]
import random
random.shuffle(deck)
# Randomly shuffles cards

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]   # Assign the four different suits
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]   # Assign the 13 ranks

cards = deck[0:4] # First four cards

for card_index in cards:
    suit = suits[card_index // 13]
    rank = ranks[card_index % 13]
    print(rank, "of", suit)