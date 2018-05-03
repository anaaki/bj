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

    def display(self, final_judge=False):
        """プレイ用のカードの表示を返す"""
        template = "".join([card.display(final_judge=final_judge) for card in self.stock])
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
    
    def draw_card_by_17(self, deck):
        """手札が17以上になるまでカードを引き続ける"""
        while True:
            if sum([card.val for card in self.stock]) < 17:
                card = deck.draw_card()
                self.stock.append(card)
            else:
                break
            