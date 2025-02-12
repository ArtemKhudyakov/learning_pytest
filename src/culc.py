import math

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return x / y


def calculate_logarithm(x, base):
    return math.log(x, base)
