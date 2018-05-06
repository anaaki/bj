from bj.player import Player, Dealer
from bj.deck import Deck
class Game:
    
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        self.deck.add_player(player=self.player, dealer=self.dealer)

    def start(self):
        print("---------ゲーム開始---------")
        # 初期はまず2枚ずつ引く
        for i in range(2):
            self.player.draw_card(self.deck)
            self.dealer.draw_card(self.deck)
        print(self.deck.display_deck())
        self.play()

    def play(self):
        while True:
            draw = input("追加でカードを引きますか? yes/no: ")
            if "n" in draw:
                break
            self.player.draw_card(self.deck)
            if self.deck.is_bust(self.player):
                print("\n")
                print("player bust!!")
                break
            else:
                print("\n")
                print("---------デッキ状況---------")
                print(self.deck.display_deck())
        self.final_judge()

    def final_judge(self):
        self.dealer.draw_card_by_17(self.deck)
        msg = self.deck.final_judge()
        self.end(msg)
 
    def end(self, msg):
        print("=========ゲーム結果=========")
        print("###", msg, "###")
        print(self.deck.display_deck(final_judge=True))


