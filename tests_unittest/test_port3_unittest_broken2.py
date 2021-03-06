# test_port3_broken2.py

import unittest

from portfolio.portfolio1 import Portfolio


class PortfolioTest(unittest.TestCase):
    def test_empty(self):
        p = Portfolio()
        self.assertEqual(p.cost(), 0.0)

    @unittest.expectedFailure
    def test_buy_one_stock(self):
        p = Portfolio()
        p.buyXX("IBM", 100, 176.48)
        self.assertEqual(p.cost(), 17648.0)

    def test_buy_two_stocks(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        p.buy("HPQ", 100, 36.15)
        self.assertEqual(p.cost(), 21263.0)
