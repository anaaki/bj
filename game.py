from bj.deck import Deck
from bj.player import Player, Dealer

def bj_start():
    """ゲームを開始する
    """
    print("---------ゲーム開始---------")
    deck = Deck()
    player, dealer = Player(), Dealer()
    deck.add_player(player, dealer)
    # 初期はまず2枚ずつ引く
    for i in range(2):
        player.draw_card(deck)
        dealer.draw_card(deck)
    print(deck.display_deck())

    # プレイヤーがカードを引く意思を確認
    while True:
        draw = input("追加でカードを引きますか? yes/no: ")
        if "n" in draw:
            break
        else:
            player.draw_card(deck)
            print("---------デッキ状況---------", "\n")
            print(deck.display_deck())
    # 最終ジャッジへ
    dealer.draw_card_by_17(deck)
    msg = deck.final_judge()
    print("---------ゲーム結果---------", "\n")
    print("###", msg, "###")
    print(deck.display_deck(final_judge=True))

if __name__ == '__main__':
    bj_start()

