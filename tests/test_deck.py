from bj.deck import Deck
import unittest


class TestDeck(unittest.TestCase):

    def test_init_deck_state(self):
        """デッキには52枚のカードがありカードの重複が無い
        重複は、コンストラクタでハードコードしている以上自明なので、テストしない"""
        deck = Deck()
        self.assertEqual(52, len(deck.cards))
