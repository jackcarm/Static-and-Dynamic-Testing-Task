import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game1 = CardGame()
        self.card1 = Card("Spades", 5)
        self.card2 = Card("Hearts", 4)
        self.cards = [self.card1, self.card2]

    def test_card_is_ace(self):
        self.assertEqual(False, self.game1.check_for_ace(self.card1))

    def test_highest_card(self):
        self.hightest_card = self.game1.highest_card(self.card1, self.card2)
        self.assertEqual(self.hightest_card.value, 5)

    def test_cards_total(self):
        self.assertEqual("You have a total of 9", self.game1.cards_total(self.cards))
