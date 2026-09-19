import pytest
from datetime import datetime

from app.company import Company
from app.dollar import Dollar
from app.portfolio import Portfolio
from app.price_provider import HardcodedPriceProvider
from app.text_formatter import TextFormatter


class FakePriceProvider:
    def __init__(self, prices: dict):
        self._prices = prices

    def get_current_price(self, company: Company) -> Dollar:
        return self._prices[company.name]


# =============================================================================
# ACCEPTANCE TEST
# Весь сценарий из README целиком. Этот тест — «северная звезда»:
# он падает первым и должен пройти последним, когда всё реализовано.
# =============================================================================


def test_portfolio_full_scenario(price_provider):
    portfolio = Portfolio()
    portfolio.add(Company("Old School Waterfall Software LTD"),
                  1000, datetime(1990, 2, 14))
    portfolio.add(Company("Crafter Masters Limited"),
                  400, datetime(2016, 6, 9))
    portfolio.add(Company("XP Practitioners Incorporated"),
                  700, datetime(2018, 12, 10))
    portfolio.remove(
        Company("Old School Waterfall Software LTD"), 500, datetime(2018, 12, 11))

    output = portfolio.print(price_provider, TextFormatter())

    expected = (
        "company | shares | current price | current value | last operation\n"
        "Old School Waterfall Software LTD | 500 | $5.75 | $2,875.00 | sold 500 on 11/12/2018\n"
        "Crafter Masters Limited | 400 | $17.25 | $6,900.00 | bought 400 on 09/06/2016\n"
        "XP Practitioners Incorporated | 700 | $25.55 | $17,885.00 | bought 700 on 10/12/2018"
    )
    assert output == expected
