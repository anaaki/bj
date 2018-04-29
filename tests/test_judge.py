from bj.deck import Deck, Card, Player, Dealer
import unittest


class TestJudge(unittest.TestCase):

    def test_judge_player_win(self):
        """プレイヤーがかつパターン"""
        deck = Deck()
        player = Player()
        dealer = Dealer()
        player.stock = [Card(2, "2", "ダイヤ"), Card(9, "9", "ダイヤ"), Card(10, "J", "ダイヤ")]
        dealer.stock = [Card(10, "J", "スペード"), Card(5, "5", "スペード")]
        deck.add_player(player=player, dealer=dealer)
        self.assertEqual("player win", deck.final_judge())

    def test_judge_player_lose(self):
        """プレイヤー負けるパターン"""
        deck = Deck()
        player = Player()
        dealer = Dealer()
        dealer.stock = [Card(2, "2", "ダイヤ"), Card(9, "9", "ダイヤ"), Card(10, "J", "ダイヤ")]
        player.stock = [Card(10, "J", "スペード"), Card(5, "5", "スペード")]
        deck.add_player(player=player, dealer=dealer)
        self.assertEqual("player lose", deck.final_judge())

    def test_judge_player_push(self):
        """引き分けの場合"""
        deck = Deck()
        player = Player()
        dealer = Dealer()
        player.stock = [Card(2, "2", "ダイヤ"), Card(8, "8", "ダイヤ"), Card(10, "J", "ダイヤ")]
        dealer.stock = [Card(2, "2", "ダイヤ"), Card(8, "8", "ダイヤ"), Card(10, "J", "ダイヤ")]
        deck.add_player(player=player, dealer=dealer)
        self.assertEqual("player push", deck.final_judge())

    def test_bust(self):
        """バーストする場合"""
        deck = Deck()
        player = Player()
        player.stock = [Card(10, "10", "ダイヤ"), Card(9, "9", "ダイヤ"), Card(3, "3", "ダイヤ")]
        deck.is_bust(player=player)
        self.assertTrue(deck.is_bust(player=player))
    
    def test_bust_both(self):
        """両方バーストすると、ディーラーが勝つ"""
        deck = Deck()
        player = Player()
        dealer = Dealer()
        player.stock = [Card(10, "Q", "ダイヤ"), Card(8, "8", "ダイヤ"), Card(10, "J", "ダイヤ")]
        dealer.stock = [Card(10, "Q", "クラブ"), Card(8, "8", "クラブ"), Card(10, "J", "クラブ")]
        deck.add_player(player=player, dealer=dealer)
        self.assertEqual("player lose", deck.final_judge())
