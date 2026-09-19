import pytest

from app.portfolio import Portfolio
from datetime import datetime
from app.transaction import BuyTransaction


def test_portfolio_can_add_1000_shares_of_waterfall_inc(waterfall_inc):
    portfolio = Portfolio()

    portfolio.add(
        waterfall_inc,
        1000,
        datetime.today(),
    )

    assert portfolio.count(waterfall_inc) == 1000


def test_if_portfolio_added_1000_watefall_inc_last_operation_shows_it(waterfall_inc):
    portfolio = Portfolio()
    operation_date = datetime.today()

    portfolio.add(
        waterfall_inc,
        1000,
        operation_date,
    )

    assert portfolio.last_operation(waterfall_inc) == BuyTransaction(
        count=1000,
        date=operation_date,
    )


def test_portfolio_can_add_100_shares_of_waterfall_inc_to_existing_200(
        waterfall_inc,
        portfolio_with_200_shares_of_waterfall_inc_bought_today
):
    portfolio = portfolio_with_200_shares_of_waterfall_inc_bought_today

    portfolio.add(
        waterfall_inc,
        100,
        datetime.today(),
    )

    assert portfolio.count(waterfall_inc) == 300


def test_portfolio_can_remove_100_shares_of_waterfall_inc_from_existing_200(
        waterfall_inc,
        portfolio_with_200_shares_of_waterfall_inc_bought_today
):
    portfolio = portfolio_with_200_shares_of_waterfall_inc_bought_today

    portfolio.remove(
        waterfall_inc,
        100,
        datetime.today(),
    )

    assert portfolio.count(waterfall_inc) == 100


def test_portfolio_cannot_remove_300_shares_of_waterfall_inc_from_existing_200(
        waterfall_inc,
        portfolio_with_200_shares_of_waterfall_inc_bought_today
):
    portfolio = portfolio_with_200_shares_of_waterfall_inc_bought_today

    with pytest.raises(ArithmeticError) as cannot_retract_error:
        portfolio.remove(
            waterfall_inc,
            300,
            datetime.today(),
        )

    assert ("cannot sell more shares than exist in portfolio"
            in cannot_retract_error.value.args[0])
    assert portfolio.count(waterfall_inc) == 200
