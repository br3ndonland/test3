# test_port7_pytest.py
import pytest

from portfolio.portfolio3 import Portfolio


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


def test_sell(simple_portfolio_3):
    simple_portfolio_3.sell("MSFT", 50)
    assert simple_portfolio_3.cost() == 6450


def test_not_enough(simple_portfolio_3):
    with pytest.raises(ValueError):
        simple_portfolio_3.sell("MSFT", 200)


def test_dont_own_it(simple_portfolio_3):
    with pytest.raises(ValueError):
        simple_portfolio_3.sell("IBM", 1)


@pytest.fixture
def fake_prices_portfolio(simple_portfolio_3):
    def fake_current_prices():
        return {"DELL": 140.0, "ORCL": 32.0, "MSFT": 51.0}

    simple_portfolio_3.current_prices = fake_current_prices
    return simple_portfolio_3


def test_value(fake_prices_portfolio):
    assert fake_prices_portfolio.value() == 22300
