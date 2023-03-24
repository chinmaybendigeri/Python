from card import values


class Hand:

    def __init__(self, name):
        self.name = name
        self.value = 0
        self.current_cards = []
        self.ace = 0

    def add_card(self, card):
        self.current_cards.append(card)
        self.value = self.value + values[card.rank]
        if card.rank == "Ace":
            self.ace += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1
