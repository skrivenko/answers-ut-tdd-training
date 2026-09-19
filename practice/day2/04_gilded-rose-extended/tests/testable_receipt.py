
from gilded_rose import Receipt


class TestableReceipt(Receipt):
    def __init__(self, now_override, item, customer_name, purchase_datetime):
        self.now_override = now_override
        super().__init__(item, customer_name, purchase_datetime)

    def now(self):
        if self.now_override is not None:
            return self.now_override
        return super().now()
