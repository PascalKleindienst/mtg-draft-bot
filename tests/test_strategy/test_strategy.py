from nose.tools import assert_equal, raises

from Memnarch.Strategy.Strategy import Strategy


class TestStrategy(object):
    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""
        cls.strategy = Strategy()

    @classmethod
    def teardown_class(cls):
        """This method is run once for each class _after_ all tests are run"""

    def test_analyze_content(self):
        assert_equal(4, self.strategy.analyze_content('Lorem ipsum dolor sit amet. Lorem ipsum', ('lorem', 'ipsum')))

    @raises(NotImplementedError)
    def test_check(self):
        self.strategy.check(None)
