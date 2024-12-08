import datetime
import time
from contextlib import ContextDecorator


class LogFile(ContextDecorator):
    def __init__(self, log_file_name):
        self.log_file_name = log_file_name

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = datetime.datetime.now()
        execution_time = end_time - self.start_time

        # Determine error information
        error_info = None
        if exc_type:
            error_info = str(exc_value)

        # Log the entry
        log_entry = (
            f"Start: {self.start_time} | "
            f"Run: {execution_time} | "
            f"An error occurred: {error_info}\n"
        )

        # Write to the log file
        with open(self.log_file_name, 'a') as log_file:
            log_file.write(log_entry)

        # Reraise the exception if it occurred
        return False  # False ensures the exception propagates


# Usage example as a decorator
@LogFile('log.txt')
def some_func():
    print("This is some function.")
    # Simulate an error
    # raise ZeroDivisionError("division by zero")


# Usage example as a context manager
try:
    with LogFile('log.txt'):
        print("Inside context")
        1 / 0  # Simulate a ZeroDivisionError
except ZeroDivisionError:
    print("Caught ZeroDivisionError.")
