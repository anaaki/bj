from bj.deck import Deck
import unittest


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_init_deck_state(self):
        """デッキには52枚のカードがありカードの重複が無い
        重複は、コンストラクタでハードコードしている以上自明なので、テストしない"""
        self.assertEqual(52, len(self.deck.cards))
