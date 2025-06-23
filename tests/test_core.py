from app.core import (
    add,
    subtract,
    multiply,
    divide,
    square_root,
    remainder_from_division,
    power,
)


def test_add():
    assert add(1, 2) == 3, "1 + 2 = 3"
    assert add(10, 15) == 25, "10 + 15 = 25"
    assert add(3.5, 6.8) == 10.3, "3.5 + 6.8 = 10.3"
    assert add(-2, 2) == 0, "-2 + 2 = 0"


def test_subtract():
    assert subtract(1, 0) == 1, "1 - 0 = 1"
    assert subtract(10, 15) == -5, "10 - 15 = -5"
    assert subtract(5.9, 8.2) == -2.3, "5.9 - 8.2 = -2.3"
    assert subtract(-2, 2) == -4, "-2 - 2 = -4"


def test_multiply():
    assert multiply(1, 0) == 0, "1 * 0 = 0"
    assert multiply(10, 15) == 150, "10 * 150 = 150"
    assert multiply(5.9, 8.2) == 48.38, "5.9 * 8.2 = 48.38"
    assert multiply(-2, 2) == -4, "-2 * 2 = -4"


def test_divide():
    assert divide(1, 0) == "Division by zero is not possible"
    assert divide(10, 15) == 0.6667, "10 / 15 = 0.6667"
    assert divide(5.9, 8.2) == 0.7195, "5.9 / 8.2 = 0.7195"
    assert divide(-2, 2) == -1, "-2 / 2 = -1"
    assert divide(0, 5) == 0, "0 / 5 = 0"


def test_square_root():
    assert square_root(1) == 1, "sqrt(1) == 1"
    assert square_root(81) == 9, "sqrt(81) == 9"
    assert square_root(5.9) == 2.429, "sqrt(5.9) == 2.429"
    assert square_root(-2) == "This is an impossible operation"
    assert square_root(0) == 0, "sqrt(0) == 0"


def test_remainder_from_division():
    assert remainder_from_division(1, 0) == "Division by zero is not possible"
    assert remainder_from_division(10, 15) == 10, "10 % 15 = 10"
    assert remainder_from_division(5.9, 8.2) == 5.9, "5.9 % 8.2 = 5.9"
    assert remainder_from_division(-2, 2) == 0, "-2 % 2 = 0"


def test_power():
    assert power(1, 1) == 1, "1 ^ 1 = 1"
    assert power(10, 15) == 1_000_000_000_000_000, "10 ^ 15 = 1_000_000_000_000_000"
    assert power(5.9, 8.2) == 2_094_047.3397, "5.9 ^ 8.2 = 2_094_047.3397"
    assert power(-2, 2) == 4, "-2 ^ 2 = 4"
    assert power(0, 0) == 1, "0 ^ 0 = 1"
