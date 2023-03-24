import random

from card import suits
from card import ranks
from card import Card


class Deck:

    def __init__(self):
        self.all_cards_in_deck = []

        for suit in suits:
            for rank in ranks:
                self.all_cards_in_deck.append(Card(suit, rank))

    def shuffle_cards(self):
        random.shuffle(self.all_cards_in_deck)

    def deal(self):
        return self.all_cards_in_deck.pop()
