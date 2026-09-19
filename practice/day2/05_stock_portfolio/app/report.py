from app.company import Company
from app.dollar import Dollar
from app.price_provider import IPriceProvider
from app.shares import Shares
from app.text_formatter import TextFormatter


class _ReportLine:
    def __init__(self, company: Company, shares: Shares, price: Dollar) -> None:
        self.company = company.__str__()
        self.shares = shares.count()
        self.current_price = price.__str__()
        self.current_value = (price * shares.count()).__str__()
        self.last_operation = shares.last_operation().__str__()

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, _ReportLine):
            raise NotImplementedError
        return (
            self.company == other.company and
            self.shares == other.shares and
            self.current_price == other.current_price and
            self.current_value == other.current_value and
            self.last_operation == other.last_operation
        )


class Report:
    def __init__(self, shares, price_provider: IPriceProvider) -> None:
        self._shares = shares
        self._price_provider = price_provider

    def _get_report_line(self, company: Company):
        return _ReportLine(
            company,
            self._shares[company],
            self._price_provider.get_current_price(company),
        )

    def _get_lines(self) -> list[_ReportLine]:
        result = []

        for key in self._shares:
            result.append(self._get_report_line(key))

        return result

    def print(self, formatter: TextFormatter):
        values = []
        for line in self._get_lines():
            values.append([line.company, line.shares.__str__(), line.current_price,
                           line.current_value, line.last_operation])

        formatter.set_headers(["company", "shares", "current price",
                               "current value", "last operation"])
        formatter.set_values(values)

        return formatter.print()
