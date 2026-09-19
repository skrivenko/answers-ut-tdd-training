import pytest
from app.string_calculator import StringCalculator


@pytest.mark.parametrize("description,input,expected", [
    ("empty string returns zero", "", "0"),
    ("single number returns itself", "1", "1"),
    ("two numbers return sum", "1,2", "3"),
    ("three float numbers return sum", "1.1,2.2,3.3", "6.6"),
    ("newline and comma delimiters", "1\n2,3", "6"),
])
def test_string_calculator_add(description, input, expected):
    calculator = StringCalculator()
    result = calculator.add(input)
    assert result == expected, description


@pytest.mark.parametrize("description,input,expected_error", [
    ("newline right after comma", "175.2,\n35", r"Ожидается число, но в позиции 6 найдено '\n'"),
    ("comma right after newline", "1,2\n,3", r"Ожидается число, но в позиции 4 найдено ','"),
    ("trailing delimiter at end", "1,3,", r"Ожидается число, но найдено EOF"),
])
def test_string_calculator_add_raises_error(description, input, expected_error):
    calculator = StringCalculator()
    with pytest.raises(ValueError) as exc_info:
        calculator.add(input)
    assert str(exc_info.value) == expected_error, description
