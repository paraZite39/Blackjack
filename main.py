from game_functionality import start_game
from blackjack_classes import Player


def welcome():
    """
    Main menu. From here, the player can start or quit the game.
    :return: None
    """
    choice = input("Welcome to the blackjack table, have a seat! You've got 500 credits on the house. "
                   "Press 's' to start the game, or 'q' to leave the table: ").lower()

    while choice not in ['s', 'q']:
        choice = (input("Please, press 's' to start the game, or 'q' to leave: ")).lower()

    if choice == 's':
        player = Player()

        quit_game = False

        while not quit_game:
            if player.get_balance() <= 0:
                choice = input("Sorry, your balance is empty. Fill up with 200 credits? (y/n): ").lower()
                while choice not in ['y', 'n']:
                    choice = input("Enter 'y' or 'n', please: ").lower()

                if choice == 'y':
                    print("Here you go!")
                    player.modify_balance(200, 'win')
                else:
                    print("Well, if you don't want any more money... goodbye then!")
                    return

            bet = int(input("How many chips would you like to bet? (Available balance: {})".format(player.get_balance())))
            while not 0 < bet <= player.get_balance():
                bet = int(input("Invalid input. How many chips would you like to bet? (Available balance: {})".format(player.get_balance())))

            quit_game = start_game(player, bet)

        print("It was nice playing with you, goodbye!")
        return
    else:
        print("Okay, goodbye!")
        return


if __name__ == '__main__':
    welcome()
