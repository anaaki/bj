from bj.deck import Deck
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

    def test_ace_is_10(self):
        """ Aはとりあえず「1」としてだけ扱う。「11」にはしない"""
        ace_cards = [
            c for c in self.deck.cards if c.name in ["A"]]

        self.assertTrue(
            all([True if c.val == 1 else False for c in ace_cards])
        )
