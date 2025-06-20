from math import sqrt

DIVISION_ERROR = "Division by zero is not possible"


def type_definition(result: int | float) -> int | float:
    if isinstance(result, int):
        return int(result)
    return round(result, 4)


def add(a: int | float, b: int | float) -> int | float:
    result = a + b
    return type_definition(result)


def subtract(a: int | float, b: int | float) -> int | float:
    result = a - b
    return type_definition(result)


def multiply(a: int | float, b: int | float) -> int | float:
    result = a * b
    return type_definition(result)


def divide(a: int | float, b: int | float) -> int | float | str:
    if b == 0:
        return DIVISION_ERROR
    result = a / b
    return type_definition(result)


def remainder_from_division(a: int | float, b: int | float) -> int | float | str:
    if b == 0:
        return DIVISION_ERROR
    return a % b


def power(a: int | float, b: int | float) -> int | float:
    result = a**b
    return type_definition(result)


def square_root(a: int | float) -> int | float | str:
    if a < 0:
        return "This is an impossible operation"
    result = sqrt(a)
    return type_definition(result)
