from game_functionality import start_game


def welcome():
    choice = input("Welcome to the blackjack table, have a seat! "
                   "Press 's' to start the game, or 'q' to leave the table: ").lower()
    while choice not in ['s', 'q']:
        choice = (input("Please, press 's' to start the game, or 'q' to leave: ")).lower()

    if choice == 's':
        print("Alright, let's begin...")
        start_game()
    else:
        print("Okay, goodbye!")
        return


if __name__ == '__main__':
    welcome()
