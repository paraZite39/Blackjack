import random
import time
from blackjack_classes import Card, Player, Dealer

card_suits = ['HEARTS', 'DIAMOND', 'SPADES', 'CLUBS']
card_values = ['A'] + list(range(2, 11)) + ['J', 'Q', 'K']
full_deck = [Card(suit, value) for suit in card_suits for value in card_values]


def draw_card(deck):
    return deck.pop()


def dealer_score(dealer, remaining_deck):
    print("----------------\n"
          "Dealer's turn...")
    while dealer.keeps_playing():
        dealer.hit_card(draw_card(remaining_deck))
        time.sleep(1)

    return dealer.get_score()


def start_game(bet: int):
    current_deck = random.sample(full_deck, len(full_deck))

    you = Player()
    dealer = Player()

    print("Dealing first two cards...")

    for _ in range(2):
        you.hit_card(draw_card(current_deck))
        time.sleep(1)

    if you.get_score() == 21:
        print("Natural! You win {} chips!".format(int(bet * 1.5)))
        return

    while you.keeps_playing():
        choice = input("Press 'h' to hit and 'f' to fold: ").lower()

        while choice not in ['h', 'f']:
            choice = input("Only 'h' or 'f', please: ").lower()

        if choice == 'h':
            random_card = draw_card(current_deck)
            you.hit_card(random_card)
        else:
            you.fold()

    y_score = you.get_score()
    time.sleep(1)
    d_score = dealer_score(dealer, current_deck)

    print("--------------")
    print("Your score:", y_score)
    print("Dealer score:", d_score)

    if y_score <= 21:
        if d_score > 21:
            print("You won {} chips!".format(bet * 2))
        elif d_score == y_score:
            print("It's a tie! No chips won or lost.")
        elif d_score < y_score:
            print("You won {} chips!".format(bet * 2))
        else:
            print("You lost {} chips!".format(bet))
    else:
        print("You lost {} chips!".format(bet))
