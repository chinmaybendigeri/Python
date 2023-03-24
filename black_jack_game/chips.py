class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
        if self.total < self.bet:
            print("Insufficient Chips To Bet!")
        else:
            self.total = self.total - self.bet
            print("Amount Deducted!")
