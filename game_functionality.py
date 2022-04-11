import random
import time
from blackjack_classes import Card, Player, Dealer

card_suits = ['HEARTS', 'DIAMOND', 'SPADES', 'CLUBS']
card_values = ['A'] + list(range(2, 11)) + ['J', 'Q', 'K']
full_deck = [Card(suit, value) for suit in card_suits for value in card_values]


def draw_card(deck):
    """
    :param deck: a list of Card instances (preferably shuffled);
    :returns card: the last Card instance in the deck;
    """
    return deck.pop()


def finish_game():
    """
    Finishes current game.
    :return: True if player wants to end the game for good, False if the player wants to restart.
    """
    choice = input("Press 'r' to play again or 'q' to quit: ")
    while choice not in ['r', 'q']:
        choice = input("Press 'r' to play again or 'q' to quit: ")

    if choice == 'r':
        return False
    else:
        return True


def dealer_score(dealer, remaining_deck):
    """
    :param dealer: a Dealer instance;
    :param remaining_deck: the cards that remain in the deck after the player finished his hand;
    :returns: The dealer's final score;

    Note: The dealer draws until his score is at least 17.
    """
    print("----------------\n"
          "Dealer's turn...")
    while dealer.keeps_playing():
        dealer.hit_card(draw_card(remaining_deck))
        time.sleep(1)

    return dealer.get_score()


def start_game(player: Player, bet: int):
    """
    :param player: the Player
    :param bet: the amount of chips waged
    :return: True if the player wants to quit, False if the player wants to restart
    """
    # shuffling deck
    current_deck = random.sample(full_deck, len(full_deck))

    player.set_score(0)
    player.folded = False

    dealer = Dealer()

    print("Dealing first two cards...")

    for _ in range(2):
        player.hit_card(draw_card(current_deck))
        time.sleep(1)

    # player's first two cards sum up to 21 = natural (winnings = half the bet)
    if player.get_score() == 21:
        win_amount = int(bet * 0.5)
        print("Natural! You win {} chips!".format(win_amount))
        player.modify_balance(win_amount, 'win')
        return finish_game()

    while player.keeps_playing():
        choice = input("Press 'h' to hit and 'f' to fold: ").lower()

        while choice not in ['h', 'f']:
            choice = input("Only 'h' or 'f', please: ").lower()

        if choice == 'h':
            random_card = draw_card(current_deck)
            player.hit_card(random_card)
        else:
            player.fold()

    player_score = player.get_score()
    d_score = dealer_score(dealer, current_deck)

    print("--------------")
    print("Your score:", player_score)
    print("Dealer score:", d_score)

    if player_score <= 21:
        if d_score > 21 or d_score < player_score:
            win_amount = bet * 2
            print("You won {} chips!".format(win_amount))
            player.modify_balance(win_amount, 'win')
        elif d_score == player_score:
            print("It's a tie! No chips won or lost.")
        else:  # dealer has a hand under 21, higher than the player's hand
            print("You lost {} chips!".format(bet))
            player.modify_balance(bet, 'lose')
    else:  # player has a hand over 21 = loss
        print("You lost {} chips!".format(bet))
        player.modify_balance(bet, 'lose')

    # prompt user for another game or
    return finish_game()
