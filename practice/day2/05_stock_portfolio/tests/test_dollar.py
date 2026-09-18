from app.dollar import Dollar


def test_dollar_multiply():
    five_dollar = Dollar(5)
    ten_dollar = five_dollar * 2
    assert ten_dollar == Dollar(10)


def test_dollar_str_musst_always_show_2_digits_for_cents():
    assert Dollar(125).__str__() == "$125.00"


def test_dollar_str_musst_separate_thousands():
    assert Dollar(6000500400300).__str__() == "$6,000,500,400,300.00"
