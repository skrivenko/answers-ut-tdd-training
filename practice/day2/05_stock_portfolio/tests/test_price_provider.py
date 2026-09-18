from app.dollar import Dollar
from app.price_provider import HardcodedPriceProvider


def test_hardcoded_price_provider(waterfall_inc):
    provider = HardcodedPriceProvider(
        {
            waterfall_inc: Dollar(5),
        }
    )

    price = provider.get_current_price(waterfall_inc)

    assert Dollar(5) == price
