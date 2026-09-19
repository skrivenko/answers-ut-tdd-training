from datetime import datetime

from app.company import Company
from app.price_provider import IPriceProvider
from app.report import Report
from app.shares import Shares
from app.transaction import BuyTransaction, SellTransaction, ITransaction


class Portfolio:
    def __init__(self) -> None:
        self._shares = {}

    def add(self, company, count: int, date: datetime) -> None:
        self._shares.setdefault(company, Shares(0))

        self._shares[company].do(BuyTransaction(
            count=count,
            date=date,
        ))

    def remove(self, company, count: int, date: datetime) -> None:
        self._shares.setdefault(company, Shares(0))

        self._shares[company].do(SellTransaction(
            count=count,
            date=date,
        ))

    def last_operation(self, company: Company) -> ITransaction:
        return self._shares[company].last_operation()

    def count(self, company: Company) -> int:
        return self._shares[company].count()

    def get_report(self, price_provider: IPriceProvider) -> Report:
        return Report(self._shares, price_provider)

    def print(self, price_provider, formatter) -> str:
        return self.get_report(price_provider).print(formatter)
