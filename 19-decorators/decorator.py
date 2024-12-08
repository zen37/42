import datetime

class LogFile:
    def __init__(self, log_file_name):
        self.log_file_name = log_file_name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            try:
                result = func(*args, **kwargs)
                exc_type, exc_value = None, None  # No error occurred
            except Exception as e:
                result = None
                exc_type, exc_value = type(e), str(e)
            
            end_time = datetime.datetime.now()
            execution_time = end_time - start_time
            error_info = exc_value if exc_value else "None"
            log_entry = (
                f"Start: {start_time} | Run: {execution_time} | "
                f"An error occurred: {error_info}\n"
            )
            
            with open(self.log_file_name, 'a') as log_file:
                log_file.write(log_entry)
            
            if exc_type:
                raise exc_type(exc_value)  # Reraise the exception if one occurred
            
            return result
        
        return wrapper

@LogFile('log.txt')
def some_function():
    print("Inside function")
    1 / 0  # Simulate an error

try:
    some_function()
except ZeroDivisionError:
    print("Caught ZeroDivisionError")
