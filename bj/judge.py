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
        player_is_bust = self.is_bust(self.player)
        dealer_is_bust = self.is_bust(self.dealer)
        player_score = abs(self.__sum_cards(self.player) - self.BASE)
        dealer_score = abs(self.__sum_cards(self.dealer) - self.BASE)
        if player_is_bust:
            # ディーラーと共にバーストしてもプレイヤーの負け
            return "player lose"
        if dealer_is_bust:
            return "player win"

        if player_score < dealer_score:
            return "player win"
        elif player_score == dealer_score:
            return "player push"
        else:
            return "player lose"
            