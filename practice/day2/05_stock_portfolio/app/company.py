class Company:
    def __init__(self, name: str) -> None:
        self.name = name

    def __hash__(self) -> int:
        return abs(hash(self.name))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Company):
            return False
        return self.name == other.name

    def __str__(self) -> str:
        return self.name
