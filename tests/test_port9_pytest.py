# test_port9_pytest.py
from types import SimpleNamespace

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


def test_value(simple_portfolio_3, mocker):
    req_get = mocker.patch(
        "portfolio.portfolio3.requests.get",
        return_value=SimpleNamespace(text="\nDELL,,,140\nORCL,,,32\nMSFT,,,51\n"),
    )
    assert simple_portfolio_3.value() == 22300
    assert len(req_get.call_args_list) == 1
    opened_url = req_get.call_args_list[0][0][0]
    assert "api.worldtradingdata.com/api/v1/stock" in opened_url
    assert "symbol=DELL,MSFT,ORCL" in opened_url
