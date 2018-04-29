import random
from bj.judge import Judge

class Deck(Judge):
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

class PlayerBase:

    def __init__(self):
        self.stock =[]
    
    def draw_card(self, deck):
        """カードを引く
        """
        card = deck.draw_card()
        self.stock.append(card)

class Player(PlayerBase):

    def __init__(self):
        super().__init__()
    
class Dealer(PlayerBase):
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
