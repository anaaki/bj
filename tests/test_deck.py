from bj.deck import Deck, Card
from bj.player import  Player, Dealer
import unittest


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_init_deck_state(self):
        """デッキには52枚のカードがありカードの重複が無い
        重複は、コンストラクタでハードコードしている以上自明なので、テストしない"""
        self.assertEqual(52, len(self.deck.cards))

    def test_jqk_is_10(self):
        """JとQとKは10として扱う"""
        jqk_cards = [
            c for c in self.deck.cards if c.name in ["J", "Q", "K"]]

        self.assertTrue(
            all([True if c.val == 10 else False for c in jqk_cards])
        )

    def test_ace_is_1(self):
        """ Aはとりあえず「1」としてだけ扱う。「11」にはしない"""
        ace_cards = [
            c for c in self.deck.cards if c.name in ["A"]]

        self.assertTrue(
            all([True if c.val == 1 else False for c in ace_cards])
        )


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_draw_card(self):
        """カードを引く"""
        player = Player()
        player.draw_card(self.deck)
        player.draw_card(self.deck)
        self.assertEqual(Card, type(player.stock[0]))
        self.assertEqual(50, len(self.deck.cards))


class TestDealer(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_draw_card(self):
        """カードを引けるが、2枚めは非表示になっている"""
        dealer = Dealer()
        dealer.draw_card(self.deck)
        dealer.draw_card(self.deck)
        self.assertTrue(dealer.stock[0].visible)
        self.assertFalse(dealer.stock[1].visible)
        dealer.draw_card(self.deck)
        self.assertTrue(dealer.stock[2].visible)


class TestDesplay(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_show_stock(self):
        """カードをディスプレイに表示する時、2枚めは非表示としてアスタリスク5個設定されている。
        dealer=> ダイヤA: *****: ダイヤJ:
        player=> クラブA: クラブ1: ダイヤK:
        """
        dealer=Dealer()
        player=Player()
        self.deck.add_player(player=player, dealer=dealer)
        for i in range(2):
            player.draw_card(self.deck)
            dealer.draw_card(self.deck)            
        current_deck = self.deck.display_deck()                
        self.assertEqual("*****", current_deck[16:21])
        self.assertTrue(current_deck.startswith("dealer=>"))
        self.assertTrue(current_deck.split("\n")[1].startswith("player=>"))