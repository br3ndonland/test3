# test_port6_pytest.py
import pytest

from portfolio.portfolio2 import Portfolio


def test_empty():
    p = Portfolio()
    assert p.cost() == 0.0


def test_buy_one_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    assert p.cost() == 17648.0


def test_buy_two_stocks():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    p.buy("HPQ", 100, 36.15)
    assert p.cost() == 21263.0


def test_bad_input():
    p = Portfolio()
    with pytest.raises(TypeError):
        p.buy("IBM")


def test_sell(simple_portfolio_2):
    simple_portfolio_2.sell("MSFT", 50)
    assert simple_portfolio_2.cost() == 6450


def test_not_enough(simple_portfolio_2):
    with pytest.raises(ValueError):
        simple_portfolio_2.sell("MSFT", 200)


def test_dont_own_it(simple_portfolio_2):
    with pytest.raises(ValueError):
        simple_portfolio_2.sell("IBM", 1)


# Tedious duplication:
def test_sell1(simple_portfolio_2):
    simple_portfolio_2.sell("MSFT", 50)
    assert simple_portfolio_2.cost() == 6450


def test_sell2(simple_portfolio_2):
    simple_portfolio_2.sell("MSFT", 10)
    assert simple_portfolio_2.cost() == 7530


def test_sell3(simple_portfolio_2):
    simple_portfolio_2.sell("ORCL", 90)
    assert simple_portfolio_2.cost() == 4740


# Nicely factored into parameters:
@pytest.mark.parametrize(
    "sym, num, cost", [("MSFT", 50, 6450), ("MSFT", 10, 7530), ("ORCL", 90, 4740)]
)
def test_selling(simple_portfolio_2, sym, num, cost):
    simple_portfolio_2.sell(sym, num)
    assert simple_portfolio_2.cost() == cost
