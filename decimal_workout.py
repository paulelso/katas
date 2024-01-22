# Description: Function that takes two decimal numbers as input and outputs their sum.
from decimal import Decimal


def decimal_sum():
    s = input("Enter two decimal numbers separated by a space: ")
    a, b = s.split()
    return Decimal(a) + Decimal(b)


if __name__ == "__main__":
    print(decimal_sum())
