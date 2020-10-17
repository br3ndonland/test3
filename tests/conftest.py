from types import SimpleNamespace

import pytest

import portfolio


class FakeRequests:
    # A simple fake for requests that is only good for one request.
    def get(self, url):
        return SimpleNamespace(text="\nDELL,,,140\nORCL,,,32\nMSFT,,,51\n")


@pytest.fixture
def fake_requests():
    old_requests = portfolio.portfolio3.requests
    portfolio.portfolio3.requests = FakeRequests()
    yield
    portfolio.portfolio3.requests = old_requests


@pytest.fixture
def simple_portfolio_1():
    p = portfolio.portfolio1.Portfolio()
    p.buy("MSFT", 100, 27.0)
    p.buy("DELL", 100, 17.0)
    p.buy("ORCL", 100, 34.0)
    return p


@pytest.fixture
def simple_portfolio_2():
    p = portfolio.portfolio2.Portfolio()
    p.buy("MSFT", 100, 27.0)
    p.buy("DELL", 100, 17.0)
    p.buy("ORCL", 100, 34.0)
    return p


@pytest.fixture
def simple_portfolio_3():
    p = portfolio.portfolio3.Portfolio()
    p.buy("MSFT", 100, 27.0)
    p.buy("DELL", 100, 17.0)
    p.buy("ORCL", 100, 34.0)
    return p


@pytest.fixture
def simple_portfolio_4():
    p = portfolio.portfolio4.Portfolio()
    p.buy("MSFT", 100, 27.0)
    p.buy("DELL", 100, 17.0)
    p.buy("ORCL", 100, 34.0)
    return p
