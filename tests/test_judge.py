from bj.deck import Deck, Card, Player, Dealer
import unittest


class TestJudge(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_judge_player_win(self):
        player = Player()
        dealer = Dealer()
        player.stock = [Card(2, "2", "ダイヤ"), Card(9, "9", "ダイヤ"), Card(10, "J", "ダイヤ")]
        dealer.stock = [Card(10, "J", "スペード"), Card(5, "5", "スペード")]
        self.deck.add_player(player=player, dealer=dealer)
        self.deck.final_judge()
        self.assertEqual("player win", self.deck.judge_msg)

    def test_judge_player_lose(self):
        player = Player()
        dealer = Dealer()
        dealer.stock = [Card(2, "2", "ダイヤ"), Card(9, "9", "ダイヤ"), Card(10, "J", "ダイヤ")]
        player.stock = [Card(10, "J", "スペード"), Card(5, "5", "スペード")]
        self.deck.add_player(player=player, dealer=dealer)
        self.deck.final_judge()
        self.assertEqual("player lose", self.deck.judge_msg)
