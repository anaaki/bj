class Judge:
    def __init__(self):
        self.judge_msg = ""
        self.BASE = 21

    def __sum_cards(self, player):
        s =  sum([card.val
            for card in player.stock
        ]) - self.BASE
        return abs(s)

    def final_judge(self):
        player_score = self.__sum_cards(self.player)
        dealer_score = self.__sum_cards(self.dealer)
        if player_score < dealer_score:
            self.judge_msg = "player win"
        elif player_score == dealer_score:
            self.judge_msg = "player push"
        else:
            self.judge_msg = "player lose"
            