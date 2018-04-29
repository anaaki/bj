class Judge:
    def __init__(self):
        self.judge_msg = ""
        self.BASE = 21

    def __sum_cards(self, player):
        s =  sum([card.val
            for card in player.stock
        ])
        return s

    def is_bust(self, player):
        if self.__sum_cards(player) > 21:
            return True
        return False

    def final_judge(self):
        player_score = abs(self.__sum_cards(self.player) - self.BASE)
        dealer_score = abs(self.__sum_cards(self.dealer) - self.BASE)
        if player_score < dealer_score:
            self.judge_msg = "player win"
        elif player_score == dealer_score:
            self.judge_msg = "player push"
        else:
            self.judge_msg = "player lose"
            