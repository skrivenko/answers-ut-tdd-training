class TextFormatter:
    def set_headers(self, headers: list[str]):
        self._header = headers

    def set_values(self, values: list[list[str]]):
        for row in values:
            if not row.__len__() == self._header.__len__():
                raise RuntimeError("mismatch header length")
        self._values = values

    def print(self) -> str:
        result = " | ".join(self._header)
        for row in self._values:
            result += "\n" + " | ".join(row)
        return result
