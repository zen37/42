
from enum import Enum

from constants import *


# Using an enumeration
class EvenOdd(Enum):
    EVEN = "even" #0
    ODD = "odd" #1


def odd_or_even1(number):
    """Check if a number is odd or even."""
    if number % 2 == 0:
        return EvenOdd.EVEN
    else:
        return EvenOdd.ODD

def odd_or_even2(number):
    """Check if a number is odd or even."""
    return EvenOdd.EVEN if number % 2 == 0 else EvenOdd.ODD

def check(n):
        print(f"number to check: {n}")

        result = odd_or_even1(n)
        result = odd_or_even2(n)

        print(f"result: {result}")
        print(f"result.name: {result.name}")
        print(f"result.value: {result.value}")
        print()


def tuple():
    for n in numbers_tuple:
         check(n)


def main():
    tuple()
    set()


if __name__ == "__main__":
    main()

