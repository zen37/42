import time

log_filename = "log.txt"
sep = ";"

def log(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        arg_names = fn.__code__.co_varnames[:fn.__code__.co_argcount]
        a = ', '.join([f"{name}={value}" for name, value in zip(arg_names, args)])
        k = ', '.join([f"{key}={value}" for key, value in kwargs.items()])
        end_time = time.time()
        duration = end_time - start_time
        line = f"{fn.__name__}{sep} args: {a}{sep} kwargs: {k}{sep} execution time: {duration}"
        with open(log_filename, 'a') as log:
            log.write(f"{line}\n")

    return wrapper

@log
def foo(a, b, c):
    pass

if __name__ == "__main__":
    foo(1, 2, c=3)
