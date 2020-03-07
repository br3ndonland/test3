# test_port2_pytest_broken.py
import pytest
from portfolio.portfolio1 import Portfolio


def test_empty():
    p = Portfolio()
    assert p.cost() == 0.0


@pytest.mark.xfail(reason="Demonstration of failed test")
def test_buy_one_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176)  # this is wrong, to make the test fail!
    assert p.cost() == 17648.0


def test_buy_two_stocks():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    p.buy("HPQ", 100, 36.15)
    assert p.cost() == 21263.0
