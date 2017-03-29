from nose.tools import assert_true, assert_is_instance

from Memnarch.Strategy.Bomb import Bomb
from Memnarch.Strategy.Strategy import Strategy


class TestBomb(object):
    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""
        cls.strategy = Bomb()
        cls.cards = [
            {'text': 'Flying'},
            {'text': 'Trample'},
        ]

    @classmethod
    def teardown_class(cls):
        """This method is run once for each class _after_ all tests are run"""

    def test_analyze_content(self):
        for card in self.cards:
            yield self.is_true, card

    def test_is_instance_of(self):
        assert_is_instance(self.strategy, Strategy)

    def test_check_init(self):
        assert_true(type(self.strategy.abilities) is tuple)

    def is_true(self, card):
        assert_true(self.strategy.check(card))
