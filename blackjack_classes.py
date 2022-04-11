class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def get_color(self):
        return self.color

    def get_value(self):
        card_values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        return self.value, card_values.index(self.value) + 1


class Player:
    def __init__(self):
        self.balance = 500
        self.score = 0
        self.folded = False

    def hit_card(self, card):
        card_suit, card_score = card.get_color(), card.get_value()
        print("Got card", card_suit, card_score[0])
        self.score += card_score[1]

        if self.score > 21:
            print("OVER 21! Score: {}".format(self.get_score()))
            self.fold()
        elif self.score == 21:
            print("21!")
            self.fold()
        else:
            print("Score is {}...".format(self.get_score()))

    def fold(self):
        self.folded = True

    def keeps_playing(self):
        return not self.folded

    def get_score(self):
        return self.score

    def set_score(self, amount):
        self.score = amount

    def get_balance(self):
        return self.balance

    def modify_balance(self, amount, result):
        if result == 'win':
            self.balance += amount
        else:
            self.balance -= amount


class Dealer(Player):
    def __init__(self):
        super().__init__()

    def keeps_playing(self):
        return self.score < 17
