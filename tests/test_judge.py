from bj.deck import Deck, Card, Player, Dealer
import unittest


class TestJudge(unittest.TestCase):

    def test_judge_player_win(self):
        deck = Deck()
        player = Player()
        dealer = Dealer()
        player.stock = [Card(2, "2", "ダイヤ"), Card(9, "9", "ダイヤ"), Card(10, "J", "ダイヤ")]
        dealer.stock = [Card(10, "J", "スペード"), Card(5, "5", "スペード")]
        deck.add_player(player=player, dealer=dealer)
        deck.final_judge()
        self.assertEqual("player win", deck.judge_msg)

    def test_judge_player_lose(self):
        deck = Deck()
        player = Player()
        dealer = Dealer()
        dealer.stock = [Card(2, "2", "ダイヤ"), Card(9, "9", "ダイヤ"), Card(10, "J", "ダイヤ")]
        player.stock = [Card(10, "J", "スペード"), Card(5, "5", "スペード")]
        deck.add_player(player=player, dealer=dealer)
        deck.final_judge()
        self.assertEqual("player lose", deck.judge_msg)

    def test_judge_player_push(self):
        deck = Deck()
        player = Player()
        dealer = Dealer()
        player.stock = [Card(2, "2", "ダイヤ"), Card(8, "8", "ダイヤ"), Card(10, "J", "ダイヤ")]
        dealer.stock = [Card(2, "2", "ダイヤ"), Card(8, "8", "ダイヤ"), Card(10, "J", "ダイヤ")]
        deck.add_player(player=player, dealer=dealer)
        deck.final_judge()
        self.assertEqual("player push", deck.judge_msg)
