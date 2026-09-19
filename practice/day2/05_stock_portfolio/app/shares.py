from app.transaction import ITransaction


class Shares:
    def __init__(self, count: int) -> None:
        self._count = count

    def do(self, transaction: ITransaction):
        self._last_operation = transaction
        self._count = transaction.apply_operation_to_count(self._count)

    def last_operation(self):
        return self._last_operation

    def count(self):
        return self._count

    def __eq__(self, other) -> bool:
        if not isinstance(other, Shares):
            raise NotImplementedError
        return self._count == other._count
