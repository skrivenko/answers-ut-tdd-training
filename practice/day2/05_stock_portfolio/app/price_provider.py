from app.company import Company
from app.dollar import Dollar


class IPriceProvider:
    def get_current_price(self, company: Company) -> Dollar:
        raise NotImplementedError


class HardcodedPriceProvider(IPriceProvider):
    def __init__(self, prices_dict) -> None:
        self._prices_dict = prices_dict
        super().__init__()

    def get_current_price(self, company: Company) -> Dollar:
        return self._prices_dict[company]
