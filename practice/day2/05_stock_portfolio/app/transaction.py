from datetime import datetime
from enum import Enum


class ITransaction:
    def __init__(self, count: int, date: datetime) -> None:
        self.count = count
        self.date = date

    def apply_operation_to_count(self, current_amount: int) -> int:
        raise NotImplementedError


class BuyTransaction(ITransaction):
    def __init__(self, count: int, date: datetime) -> None:
        super().__init__(count, date)

    def apply_operation_to_count(self, current_amount: int) -> int:
        return current_amount + self.count

    def __str__(self) -> str:
        return f"bought {self.count} on {self.date.strftime('%d/%m/%Y')}"

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, BuyTransaction):
            raise NotImplementedError
        return (
            self.count == other.count and
            self.date == other.date
        )


class SellTransaction(ITransaction):
    def __init__(self, count: int, date: datetime) -> None:
        super().__init__(count, date)

    def apply_operation_to_count(self, current_amount: int) -> int:
        if current_amount < self.count:
            raise ArithmeticError(
                f"cannot sell more shares than exist in portfolio: have {current_amount}, selling {self.count}")
        return current_amount - self.count

    def __str__(self) -> str:
        return f"sold {self.count} on {self.date.strftime('%d/%m/%Y')}"

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, SellTransaction):
            raise NotImplementedError
        return (
            self.count == other.count and
            self.date == other.date
        )
