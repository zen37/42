import time

from constants import *

"""
ChatGPT
Yes, in Python, it is more idiomatic to use snake_case for function and variable names, following the PEP 8 style guide. So, is_even is considered more Pythonic than isEven.

Python's naming conventions recommend using lowercase letters with underscores for function and variable names. This helps maintain consistency across the Python community and makes the code more readable for others who may be familiar with these conventions.

Therefore, it's a good practice to use is_even instead of isEven in Python.
"""
#def isEven
def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def is_odd(number):
    """Check if a number is odd."""
    return number % 2 != 0

def check(n):
        print(f"number: {n}")

        #start_time = time.time()
        # Record the start time in nanoseconds
        start_time = time.time_ns()

        even = is_even(n)
        odd = is_odd(n)

        #end_time = time.time()
        end_time = time.time_ns()

        #elapsed_time_seconds = end_time - start_time
        # Convert elapsed time to milliseconds
        #elapsed_time_milliseconds = elapsed_time_seconds * 1000
        elapsed_time_nanoseconds = end_time - start_time

        print(f"Elapsed Time: {elapsed_time_nanoseconds} nanoseconds")

        print(f"even: {even}")
        print(f"odd: {odd}")

def set():
    for n in numbers_set:
        check(n)

def tuple():
    for n in numbers_tuple:
         check(n)


def main():
    tuple()
    set()


if __name__ == "__main__":
    main()

