import random
from bj.judge import Judge
from bj.show import Show

class Deck(Judge, Show):
    """トランプを引くデッキ"""

    def __init__(self):
        super().__init__()
        card_props = [
            (1, "A"), (2, "2"), (3, "3"),
            (4, "4"), (5, "5"), (6, "6"),
            (7, "7"), (8, "8"), (9, "9"),
            (10, "10"), (10, "J"), (10, "Q"),
            (10, "K")
        ]
        card_suits = ("ダイヤ", "スペード", "クラブ", "ハート")
        self.cards = []
        for s in card_suits:
            for p in card_props:
                self.cards.append(Card(suit=s, val=p[0], name=p[1]))
        # カードをシャッフル
        random.shuffle(self.cards)

    def add_player(self, player, dealer):
        """プレイヤを追加、審判の対象"""
        self.player = player
        self.dealer = dealer

    def draw_card(self):
        if len(self.cards)> 0:
            return self.cards.pop()
        else:
            return None

class Card:
    def __init__(self, val, suit, name):
        self.val, self.suit, self.name = val, suit, name
        self.visible = True

    def display(self):
        """プレイ用のカードの表示を返す
        通常は ダイヤA:
        非表示は *****:
        になる。
        """
        if self.visible:
            template = "{suit}{name}:".format(suit=self.suit,name=self.name)
            return template.rjust(7)
        else:
            return "*****:".rjust(7)
            

class PlayerBase:
    """ユーザーの基底クラス"""
    def __init__(self):
        self.stock =[]

    @property
    def role(self):
        raise NotImplementedError("サブクラスで実装して下さい。")
    
    def draw_card(self, deck):
        """カードを引く
        """
        card = deck.draw_card()
        self.stock.append(card)

    def display(self):
        """プレイ用のカードの表示を返す"""
        template = "".join([card.display() for card in self.stock])
        return self.role + "=>{}".format(template)

class Player(PlayerBase):
    """プレイヤー"""
    role = "player"
    def __init__(self):
        super().__init__()
   
class Dealer(PlayerBase):
    """ディーラー"""
    role = "dealer"
    def __init__(self):
        super().__init__()

    def draw_card(self, deck):
        """カードを引く
        2枚目は見えない
        """
        card = deck.draw_card()
        if len(self.stock) == 1:
            card.visible = False
        self.stock.append(card)
