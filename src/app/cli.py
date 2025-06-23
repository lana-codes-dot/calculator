from app.core import (
    add,
    subtract,
    multiply,
    divide,
    square_root,
    remainder_from_division,
    power,
)
import click


def type_definition(value: str) -> int | float:
    if "." in value:
        return float(value)
    return int(value)

@click.command()
def run_cli():
    while True:
        possible_operations = ["+", "-", "/", "^", "%", "sqrt", "exit"]

        print("Please, choose an operation: +, -, /, ^, %, sqrt or exit to finish")
        operation = input("Your choice: ").strip()

        if operation not in possible_operations:
            print("Invalid operation. Please try again")
        elif operation == "exit":
            print("Goodbye!")
            break

        try:
            if operation == "sqrt":
                num = input("Please enter a number: ")
                result = square_root(float(num))
            else:
                num1 = input("Please enter a number: ")
                num2 = input("Please enter one more number: ")

                num1 = type_definition(num1)
                num2 = type_definition(num2)

            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            elif operation == "/":
                result = divide(num1, num2)
            elif operation == "%":
                result = remainder_from_division(num1, num2)
            elif operation == "^":
                result = power(num1, num2)

            print(f"Result: {result}")

        except ValueError:
            print("Error. You entered an invalid number.")
