from typing import List


class ArithmeticOperations:
    @staticmethod
    def add(x: float, y: float) -> float:
        return x + y

    @staticmethod
    def subtract(x: float, y: float) -> float:
        return x - y

    @staticmethod
    def multiply(x: float, y: float) -> float:
        return x * y

    @staticmethod
    def divide(x: float, y: float) -> float:
        return x / y


def simple_calculator() -> None:
    print("Welcome to the simple calculator!")
    operators: List[str] = ["+", "-", "*", "/"]

    while True:
        try:
            num1: float = float(input("Enter the first number: "))
            num2: float = float(input("Enter the second number: "))
            operator: str = input(
                "Enter the operator, this calculator supports one of the following(+, -, *, /): "
            )

            if operator not in operators:
                print("Invalid operator, please try again!")
                continue

            if operator == "+":
                result = ArithmeticOperations.add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif operator == "-":
                result = ArithmeticOperations.subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif operator == "*":
                result = ArithmeticOperations.multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            else:
                result = ArithmeticOperations.divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

        except ValueError:
            print("Invalid input, please try again!")
            continue

        choice: str = input("Do you want to continue? (y/n): ")
        if choice != "y":
            break

    print("Thank you for using the simple calculator!")


simple_calculator()
