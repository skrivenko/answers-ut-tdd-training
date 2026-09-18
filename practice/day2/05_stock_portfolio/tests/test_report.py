from datetime import datetime

from app.company import Company
from app.portfolio import Portfolio
from app.shares import Shares
from app.text_formatter import TextFormatter


def get_test_shares(company: Company, portfolio: Portfolio) -> Shares:
    shares = Shares(0)
    shares.do(portfolio.last_operation(company))
    return shares


def test_report_print(
        waterfall_inc,
        price_provider):
    portfolio = Portfolio()
    portfolio.add(waterfall_inc,
                  1000, datetime(1990, 2, 14))

    report = portfolio.get_report(price_provider).print(TextFormatter())

    assert report == (
        "company | shares | current price | current value | last operation\n"
        f"{waterfall_inc.name} | 1000 | {price_provider.get_current_price(waterfall_inc)} | {price_provider.get_current_price(waterfall_inc) * 1000} | bought 1000 on 14/02/1990"
    )
