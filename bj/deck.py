

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

class Card:
    def __init__(self, val, suit, name):
        self.val, self.suit, self.name = val, suit, name
