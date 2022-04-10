import random
from blackjack_classes import Card, Player, Dealer

card_suits = ['HEARTS', 'DIAMOND', 'SPADES', 'CLUBS']
card_values = ['A'] + list(range(2, 11)) + ['J', 'Q', 'K']
full_deck = [Card(suit, value) for suit in card_suits for value in card_values]


def dealer_score(dealer):
    while(Dealer.keeps_playing()):
        pass


def start_game():
    current_deck = full_deck[:]

    you = Player()
    dealer = Player()

    while you.keeps_playing():
        choice = input("Press 'h' to hit and 'f' to fold: ").lower()

        while choice not in ['h', 'f']:
            choice = input("Only 'h' or 'f', please: ").lower()

        if choice == 'h':
            random_card = random.choice(current_deck)

