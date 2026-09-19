class StringCalculator:

    
    def add(self, input):
        if input == "":
            return "0"
        self._validate_input(input)
        numbers = self._parse_numbers(input)
        total_sum = sum(float(n) for n in numbers)
        return self._format_result(total_sum)

    
    def _validate_input(self, input):
        for i, char in enumerate(input):
            if i > 0 and self._is_delimiter(input[i-1]) and self._is_delimiter(char):
                raise ValueError(f"Ожидается число, но в позиции {i} найдено '{repr(char)[1:-1]}'")
        if input and self._is_delimiter(input[-1]):
            raise ValueError("Ожидается число, но найдено EOF")

    
    def _is_delimiter(self, char):
        return char == ',' or char == '\n'

    
    def _parse_numbers(self, input):
        input = input.replace("\n", ",")
        return input.split(",")

    
    def _format_result(self, value):
        return f"{value:g}"