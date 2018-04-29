class Judge:
    def __init__(self):
        self.judge_msg = ""
        self.BASE = 21

    def final_judge(self):
        player_score = sum([card.val
            for card in self.player.stock
        ]) - self.BASE

        dealer_score = sum([card.val
            for card in self.dealer.stock
        ]) - self.BASE

        if abs(player_score) < abs(dealer_score):
            self.judge_msg = "player win"
        else:
            self.judge_msg = "player lose"
            