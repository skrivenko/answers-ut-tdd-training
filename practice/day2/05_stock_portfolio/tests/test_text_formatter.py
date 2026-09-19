import pytest

from app.text_formatter import TextFormatter


def test_formatter_prints_values():
    fmt = TextFormatter()
    fmt.set_headers(["name", "phone"])
    fmt.set_values([
        ["John", "123"],
        ["Jane", "321"],
    ])

    assert fmt.print() == (
        "name | phone\n"
        "John | 123\n"
        "Jane | 321"
    )


def test_formatter_raises_error_when_length_mismatch():
    fmt = TextFormatter()
    fmt.set_headers(["name"])

    with pytest.raises(RuntimeError):
        fmt.set_values([
            ["John", "123"],
        ])
