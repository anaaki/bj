class Judge:
    def __init__(self):
        self.judge_msg = ""
        self.BASE = 21

    def __sum_cards(self, player):
        s =  sum([card.val
            for card in player.stock
        ]) - self.BASE
        return s

    def final_judge(self):
        player_score = self.__sum_cards(self.player)
        dealer_score = self.__sum_cards(self.dealer)

        if abs(player_score) < abs(dealer_score):
            self.judge_msg = "player win"
        else:
            self.judge_msg = "player lose"
            