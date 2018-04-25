import random

class Deck:
    """トランプを引くデッキ"""

    def __init__(self):
        card_props = [
            (1, "A"),
            (2, "2"),
            (3, "3"),
            (4, "4"),
            (5, "5"),
            (6, "6"),
            (7, "7"),
            (8, "8"),
            (9, "9"),
            (10, "10"),
            (10, "J"),
            (10, "Q"),
            (10, "K")
        ]
        card_suits = (
            "ダイヤ",
            "スペード",
            "クラブ",
            "ハート"
        )
        self.cards = []
        for s in card_suits:
            for p in card_props:
                self.cards.append(Card(suit=s, val=p[0], name=p[1]))
        # カードをシャッフル
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards)> 0:
            return self.cards.pop()
        else:
            return None

class Card:
    def __init__(self, val, suit, name):
        self.val, self.suit, self.name = val, suit, name

class Player:

    def __init__(self):
        pass
    
    def draw_card(self, deck):
        """カードを引く
        return Card()
        """
        return deck.draw_card()
