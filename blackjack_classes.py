class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def get_color(self):
        return self.color

    def get_value(self):
        return self.value


class Player:
    def __init__(self):
        self.score = 0
        self.folded = False

    def hit_card(self, card):
        card_suit, card_score = card.get_color(), card.get_value()
        print("Got card", card_suit, card_score)
        self.score += card_score

        if self.score > 21:
            print("OVER 21, LOST!")
        elif self.score == 21:
            print("21!")
        else:
            print("Alright for now...")

    def fold(self):
        self.folded = True

    def keeps_playing(self):
        return not self.folded


class Dealer(Player):
    def __init__(self):
        super().__init__()

