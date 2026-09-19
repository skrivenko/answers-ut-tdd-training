from datetime import datetime

from pytest import fixture

from app.company import Company
from app.dollar import Dollar
from app.portfolio import Portfolio
from app.price_provider import HardcodedPriceProvider


@fixture
def waterfall_inc():
    return Company("Old School Waterfall Software LTD")


@fixture
def crafter_ltd():
    return Company("Crafter Masters Limited")


@fixture
def xp_inc():
    return Company("XP Practitioners Incorporated")


@fixture
def portfolio_with_200_shares_of_waterfall_inc_bought_today(waterfall_inc):
    portfolio = Portfolio()
    portfolio.add(
        waterfall_inc,
        200,
        datetime.today(),
    )
    return portfolio


@fixture
def price_provider(waterfall_inc, crafter_ltd, xp_inc):
    return HardcodedPriceProvider({
        waterfall_inc: Dollar(5.75),
        crafter_ltd: Dollar(17.25),
        xp_inc: Dollar(25.55),
    })
