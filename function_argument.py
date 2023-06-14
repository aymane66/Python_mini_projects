import math


def calculate(x):
    y = 4 * math.pow(x, 3) - 13 * pow(x, 2) + x - 60
    return y


x = input("Value of f(x): ")

try:
    x = int(x)

    print(f"f({x}) = {int(calculate(x))}")


except ValueError:
    print("Invalid input! ")